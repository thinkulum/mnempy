import pytest
from context import mnempy


class TestController(object):
    """
    Class for testing the controller module.
    """

    def test_controller_includes_empty_config(self):
        # Fixture setup
        c = cookiefactory.controller.Command('')

        # Exercise system
        result = c.config

        # Verify outcome
        assert type(result) == cookiefactory.config.Config
        assert result == {}

        # Fixture teardown


if __name__ == '__main__':
    pytest.main([__file__])
