import os
from typing import Generator
import json
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext

from infra.clients.http_client import HttpClient

load_dotenv()

userEmail = os.getenv("EMAIL")
assert userEmail, "userEmail is not set"

testUrl = os.getenv("TESTENV_LOGIN")
assert testUrl, "testUrl is not set"

password = os.getenv("PW1")
assert password, "password is not set"


@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url=f"{testUrl}")
    client = HttpClient(api_context=request_context)
    yield client
    client.close_connection()
