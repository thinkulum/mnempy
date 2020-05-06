import pytest
from context import mnempy


class TestCLI(object):
    """
    Class for testing the command interface.
    """

    def test_onecmd_with_wrapper_script(self):
        # Fixture setup
        import sys
        app_dir = '../..'
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        import app
        sys.argv = ['test.py', app.__file__, 'q']

        # Exercise system
        result = app.main()

        # Verify outcome
        assert result

        # Fixture teardown

    def test_onecmd_with_hyphen_c_script(self):
        # Fixture setup
        import sys
        app_dir = '../..'
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        import app
        sys.argv = ['-c', 'q']

        # Exercise system
        result = app.main()

        # Verify outcome
        assert result

        # Fixture teardown

    def test_onecmd_with_empty_script(self):
        # Fixture setup
        import sys
        app_dir = '../..'
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        import app
        sys.argv = ['', 'q']

        # Exercise system
        result = app.main()

        # Verify outcome
        assert result

        # Fixture teardown

    def test_quit(self):
        cli = mnempy.cli.CLI()
        assert cli.onecmd('q') == 1


class TestMetadata(object):
    """
    Class for testing the app's metadata.
    """

    def test_version_number(self):
        assert mnempy.__version__ == '0.0.1'


if __name__ == '__main__':
    pytest.main([__file__])
