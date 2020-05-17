import os
from nltk.corpus import wordnet as wn
from sqlalchemy import create_engine
import csv
import codecs
import requests
from lxml.html.soupparser import fromstring
from lxml import etree
import hashlib


class Command(object):
    """
    Superclass for commands.
    """

    def __init__(self, config, arg):
        super(Command, self).__init__()
        self.arg = arg

        self.config = config
        # self.db = create_engine('sqlite:///{}'.format(db_path))

    def set_name(self):
        name_keys = [name_key for name_key in self.arg.keys()
                     if self.arg[name_key] == True]
        if len(name_keys) > 0:
            name_key = name_keys[0]
            if hasattr(self, 'name_for'):
                self.name = self.name_for[name_key]
            else:
                self.name = name_key
        else:
            self.name = ''


class GenerateCommandController(Command):
    """
    Controller for creating a dictionary from scratch.
    """

    def __init__(self, config, arg):
        super(GenerateCommandController, self).__init__(config, arg)

    def run(self):
        # BuildCommandController(self.config, '').run()
        pass


class ImportCommandController(Command):
    """
    Controller for importing a dataset.
    """

    def __init__(self, config, arg):
        super(ImportCommandController, self).__init__(config, arg)

        self.name_for = {
            'wn': 'wordnet',
        }
        self.set_name()

    def run(self):
        self.explore_wordnet()
        # data = self.parse(self.name)
        # self.create_table(data)

    def parse(self, name):
        """Parse the named set of data."""

        fn_for = {
            'wordnet': '',
        }

        method = 'parse_' + name
        data = getattr(self, method)(fn_for[name])

        return data

    def parse_wordnet(self, in_fn):
        """Read the WordNet data."""

        # Get the database connection and cursor.
        # conn = sqlite3.connect(self.dir_data + '/data.db')
        # c = conn.cursor()

    def explore_wordnet(self):
        # print(len(list(wn.all_synsets())))
        # for synset in list(wn.all_synsets())[:10]:
        all_synsets = list(wn.all_synsets())
        # all_synsets = [wn.synset('dog.n.01')]
        root_hypernyms_set = {root.name() for synset in all_synsets
                              for root in synset.root_hypernyms()}
        root_hypernyms_list = list(root_hypernyms_set)
        root_hypernyms_sorted = sorted(root_hypernyms_list)
        print(root_hypernyms_sorted)
        print(len(root_hypernyms_sorted))
        # for synset in [wn.synset('dog.n.01')]:
        #     print('synset: {}'.format(synset))
        #     for hyper in synset.hypernyms():
        #         print('  hyper: {}'.format(hyper))

        # c.close()


class QueryCommandController(Command):
    """
    Controller for querying a dataset.
    """

    def __init__(self, config, arg):
        super(QueryCommandController, self).__init__(config, arg)

        self.name_for = {
            'tp': 'transphoner',
        }
        self.set_name()

        self.cache_dir = self.config['general']['cache_dir']

    def run(self):
        method = 'query_' + self.name
        data = getattr(self, method)()

    def query_transphoner(self):
        transphoner_url_keys = ['inputLang', 'outputLang', 'nrows',
                                'searchBeamSize', 'phoneApprox',
                                'orthographicSimilarityWeight',
                                'phoneticWeight', 'phoneSim',
                                'semanticSimilarityWeight',
                                'semanticSimilarity', 'imageabilityWeight',
                                'initialMatchWeight', 'languageModelWeight',
                                'syllabify', 'ignoreTones', 'wordPenalty',
                                'infreqPenalty', 'filterRareWordCount',
                                'filterRareWordRank',
                                'filterMaxSyllablesPerWord', 'filterSourceWord']
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        rows = [['word', 'substitute']]
        words = ['one']
        for word in words:
            print(word)
            doc = self.get_doc(transphoner_url_keys, word)
            if doc is not None:
                doc_data = self.get_doc_data(doc)
                for candidate in doc_data:
                    rows.append([word, candidate])
        self.insert_rows(rows)

    def insert_rows(self, rows):
        pass

    def get_doc_data(self, doc):
        root = fromstring(doc)
        result_cells = root.xpath("//tr[ @class = 'resultsRow' ]"
                                  "/td[ @class = 'resultCell' ][1]")
        candidates = [ self.normalize_space(self.elt_text(td))
                       for td in result_cells ]
        return candidates

    def normalize_space(self, string):
        return ' '.join(''.join(string).split())

    def elt_text(self, elt):
        return ''.join(elt.xpath(".//text()"))

    def get_doc(self, transphoner_url_keys, word):
        doc = None
        request_params = tuple((('input', word),)) + tuple(
            (key, self.config['transphoner'][key])
            for key in transphoner_url_keys)
        request = requests.PreparedRequest()
        request.prepare(method='GET',
                        url=self.config['transphoner']['base_url'],
                        params=request_params)
        cache_file_path = self.get_cache_file_path(request.path_url)
        if os.path.exists(cache_file_path):
            with codecs.open(
                cache_file_path, encoding='utf-8') as cache_file:
                doc = cache_file.read()
        else:
            response = requests.Session().send(request)
            if response.status_code == requests.codes.ok:
                doc = response.text
                self.cache_doc(request.path_url, doc)
            else:
                print('[WARNING] Response for word {} was {}. Skipping.'
                      .format(word, response.status_code))
        return doc

    def cache_doc(self, path_url, doc):
        cache_file_path = self.get_cache_file_path(path_url)
        with codecs.open(cache_file_path, 'w', encoding='utf-8') as cache_file:
            cache_file.write(doc)

    def get_cache_file_path(self, path_url):
        digest = hashlib.sha224(path_url.encode('utf-8')).hexdigest()
        cache_file_path = os.path.join(
            self.cache_dir, '{}.html'.format(digest))
        return cache_file_path


class BuildCommandController(Command):
    """
    Controller for querying a dataset.
    """

    def __init__(self, config, arg):
        super(BuildCommandController, self).__init__(config, arg)

        if '<build_path>' in self.arg:
            self.build_file_path = self.arg['<build_path>']
            self.build_dir = os.path.dirname(self.build_file_path)
        else:
            self.build_dir = self.config['general']['build_dir']
            self.build_file_path = os.path.join(self.build_dir, 'mnemdic.csv')

    def run(self):
        rows = [['word', 'substitutes']]
        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)
        with codecs.open(
                self.build_file_path, 'w', encoding='utf-8') as build_file:
            build_writer = csv.writer(build_file)
            for row in rows:
                build_writer.writerow(row)
