"""Test basic access to the API."""

import pytest

from offchain.api import ApiError
from offchain.tests.utils import init_tests

# ---------------------------------------------------------------------

def test_me( api ):
    """Test calling the "me" endpoint."""

    # initialize
    init_tests( api, fixtures="basic" )

    # call the "me" endpoint and check the response
    resp = api.me()
    assert resp.code == 200
    assert isinstance( resp.headers, dict )
    assert isinstance( resp.raw, bytes )
    assert resp.json["status"] == "success"

    assert resp.json["email"] and resp.json["name"]

# ---------------------------------------------------------------------

def test_date( api ):
    """Test calling the "date" endpoint."""

    # initialize
    init_tests( api, fixtures="basic" )

    # call the "date" endpoint and check the response
    resp = api.date( "AU", date="2019-01-01", subdivision="NSW" )
    assert resp.code == 200
    assert isinstance( resp.headers, dict )
    assert isinstance( resp.raw, bytes )
    assert resp.json["status"] == "success"
    assert isinstance( resp.json["data"], dict )

# ---------------------------------------------------------------------

def test_business_days( api ):
    """Test calling the "business-days" endpoint."""

    # initialize
    init_tests( api, fixtures="basic" )

    # call the "holidays" endpoint and check the response
    resp = api.business_days( "2020-01-01","2020-02-01", country="AU" )
    assert resp.code == 200
    assert isinstance( resp.headers, dict )
    assert isinstance( resp.raw, bytes )
    assert resp.json["status"] == "success"
    assert resp.json["data"]["business_days"] and resp.json["data"]["total_days"]

# ---------------------------------------------------------------------

def test_holidays( api ):
    """Test calling the "holidays" endpoint."""

    # initialize
    init_tests( api, fixtures="basic" )

    # call the "holidays" endpoint and check the response
    resp = api.holidays( year=2020, country="AU" )
    assert resp.code == 200
    assert isinstance( resp.headers, dict )
    assert isinstance( resp.raw, bytes )
    assert resp.json["status"] == "success"
    assert isinstance( resp.json["data"], list )

# ---------------------------------------------------------------------

def test_locations( api ):
    """Test calling the "locations" endpoint."""

    # initialize
    init_tests( api, fixtures="basic" )

    # call the "locations" endpoint and check the response
    resp = api.locations()
    assert resp.code == 200
    assert isinstance( resp.headers, dict )
    assert isinstance( resp.raw, bytes )
    assert resp.json["status"] == "success"

    assert isinstance( resp.json["data"], list )

# ---------------------------------------------------------------------

def test_bad_token( api, options, monkeypatch ):
    """Test using a bad API token."""

    if not options.live:
        return

    # call the "me" endpoint with an invalid token
    monkeypatch.setattr( api, "token", "<bad-token>" )
    with pytest.raises( ApiError ) as ex_info:
        resp = api.me()
    assert ex_info.value.message == "401 Unauthorized"
