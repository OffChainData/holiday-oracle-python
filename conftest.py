""" pytest support functions. """

import pytest

from offchain.api import OffChainApi

# ---------------------------------------------------------------------

def pytest_addoption( parser ):
    """Configure pytest options."""

    # NOTE: This file needs to be in the project root for this to work :-/
    #   https://docs.pytest.org/en/latest/reference.html#initialization-hooks

    # add test options
    parser.addoption(
        "--live", action="store_true", dest="live", default=False,
        help="Run the tests against the real API server."
    )
    parser.addoption(
        "--token", action="store", dest="token", default=None,
        help="API token (only needed if running live tests)."
    )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@pytest.fixture( scope="session" )
def options( request ):
    """Return the command-line options."""
    return request.config.option

# ---------------------------------------------------------------------

@pytest.fixture( scope="function" )
def api( request ):
    """Return a test OffChainApi object."""

    if request.config.getoption( "--live" ):
        fixtures_dir = None
    else:
        # NOTE: Since we are returning this OffChainApi object as a fixture, we can't set
        # the fixtures directory here; the caller will have to do it themselves (see init_tests()).
        fixtures_dir = "..."
    return OffChainApi(
        request.config.getoption( "--token" ),
        fixtures_dir
    )
