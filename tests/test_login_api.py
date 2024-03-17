import json
from playwright.sync_api import Playwright, APIRequestContext

from infra.clients.http_client import HttpClient
from tests.conftest import userEmail, password


def test_login_with_existing_user(api_request_context: HttpClient) -> None:
    data = {
        "user": {
            "email": f"{userEmail}",
            "password": f"{password}",
        }
    }
    jsondata = json.dumps(data)
    print(jsondata)
    response = api_request_context.fire_post_req("/api/users/login", data=data)

    assert response.ok, f"Request failed: {response.status}"
    login_response = response.json()
    assert login_response["user"]["email"] == userEmail, "Email does not match"
