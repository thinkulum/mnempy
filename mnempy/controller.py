from nltk.corpus import wordnet as wn
import sqlite3


class Command(object):
    """
    Superclass for commands.
    """

    def __init__(self, config, arg):
        super(Command, self).__init__()
        self.arg = arg

        self.config = config

    def set_name(self):
        name_keys = [name_key for name_key in self.arg.keys()
                     if self.arg[name_key] == True]
        if len(name_keys) > 0:
            name_key = names[0]
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

    def run(self):
        pass


class BuildCommandController(Command):
    """
    Controller for querying a dataset.
    """

    def __init__(self, config, arg):
        super(BuildCommandController, self).__init__(config, arg)

    def run(self):
        pass
