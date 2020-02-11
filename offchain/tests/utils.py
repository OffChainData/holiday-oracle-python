""" Miscellaneous helper stuff for the test suite. """

import os

# ---------------------------------------------------------------------

def init_tests( api, fixtures=None ):
    """Prepare to run tests."""

    # check if we should run the tests against the live server
    if api._fixtures_dir:
        assert api._fixtures_dir == "..." # nb: this was set by the api() fixtures setup function
        fixtures = os.path.join( "fixtures", fixtures )
        fixtures = os.path.join( os.path.split(__file__)[0], fixtures )
        assert os.path.isdir( fixtures )
        api._fixtures_dir = fixtures
