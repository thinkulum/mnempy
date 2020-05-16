import os
import cmd
from . import config
from . import controller
from docopt import docopt, DocoptExit


# From https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class CLI(cmd.Cmd):
    """
    Class for defining the command interface.
    """

    def __init__(self, config_dir):
        super(CLI, self).__init__()

        # TODO: Get config_paths instead of config_dir from arguments?
        config_filenames = ['app.ini']
        config_paths = [os.path.join(config_dir, filename)
                        for filename in config_filenames]
        # TODO: Allow config to treat different config sources differently?
        self.config = config.Config(config_paths)

    @docopt_cmd
    def do_generate(self, arg):
        """Perform all the steps needed to create a dictionary from scratch.

        Usage: generate [overwrite]"""
        c = controller.GenerateCommandController(self.config, arg)
        c.run()

    @docopt_cmd
    def do_import(self, arg):
        """Import a dataset into the app's database.

        Usage: import (wn)"""
        c = controller.ImportCommandController(self.config, arg)
        c.run()

    @docopt_cmd
    def do_query(self, arg):
        """Import a dataset into the app's database.

        Usage: query (tp)"""
        c = controller.QueryCommandController(self.config, arg)
        c.run()

    @docopt_cmd
    def do_build(self, arg):
        """Create the dictionary file(s) from the collected data.

        Usage: build"""
        c = controller.BuildCommandController(self.config, arg)
        c.run()

    def do_q(self, arg):
        """Quit the application."""
        print('Bye!')
        return True
