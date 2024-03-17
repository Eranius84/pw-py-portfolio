from typing import Any

from playwright.sync_api import APIRequestContext, APIResponse


class HttpClient:
    def __init__(self, api_context: APIRequestContext):
        self.__context = api_context

    def fire_post_req(self, end_point: str, data: Any) -> APIResponse:
        return self.__context.post(url=end_point, data=data)

    def close_connection(self) -> None:
        self.__context.dispose()
