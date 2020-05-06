from . import config


class Command(object):
    """
    Superclass for commands.
    """

    def __init__(self, arg):
        super(Command, self).__init__()
        self.arg = arg

        self.config = config.Config()
