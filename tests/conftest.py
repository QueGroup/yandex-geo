import json
import typing
from urllib.parse import (
    urlencode,
)

import pytest
from pytest_httpx import (
    HTTPXMock,
)


def _encode(geocode: str, api_key: str = "well-known-key") -> str:
    params = {"format": "json", "apikey": api_key, "geocode": geocode}
    query = urlencode(params)
    return f"https://geocode-maps.yandex.ru/1.x/?{query}"


def _mock_setup(
    httpx_mock: HTTPXMock,
    resp: str,
    status_code: int,
    **encode_kw: typing.Any,
) -> typing.Any:
    httpx_mock.add_response(
        method="GET",
        url=_encode(**encode_kw),
        json=load_fixture(resp) if isinstance(resp, str) else resp,
        status_code=status_code,
    )


@pytest.fixture
def mock_api(httpx_mock: HTTPXMock) -> typing.Any:
    return lambda resp, status_code, **encode_kw: _mock_setup(
        httpx_mock, resp, status_code, **encode_kw
    )


def load_fixture(fixture_name: str) -> dict[str, typing.Any]:
    with open(f"./tests/fixtures/{fixture_name}.json") as fixture:
        return json.load(fixture)
