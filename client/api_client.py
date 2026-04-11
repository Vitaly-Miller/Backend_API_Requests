"""
API Client
(Requests)
"""
import requests
from data.data import Base
from typing import Any

#=======================================================================================================================
class APIClient:
    def __init__(self, base_url: str = Base.URL):
        self.base_url = base_url
        self.client = requests.Session()


    # ➡️Внутренний _метод — сюда логи, авторизация, retry
    def _request(
            self,
            method: str,
            endpoint: str,
            **kwargs
    ) -> requests.Response:
        return self.client.request(method=method, url=f'{self.base_url}{endpoint}', **kwargs)


    # 🟩GET ------------------------------------------------------------------------------------------------------------
    def get(
            self,
            endpoint: str,
            params: dict | None = None,
            headers: dict[str, str] | None = None,
            timeout: float | None = None
    ) -> requests.Response:
        return self._request('GET', endpoint, params=params, headers=headers, timeout=timeout)


    # 🟨POST -----------------------------------------------------------------------------------------------------------
    def post(
            self,
            endpoint: str,
            params: dict | None = None,
            headers: dict[str, str] | None = None,
            json: Any | None = None,
            data: Any | None = None,
            files: Any | None = None,
            timeout: float | None = None
    ) -> requests.Response:
        return self._request('POST', endpoint, params=params, headers=headers, json=json, data=data, files=files, timeout=timeout)


    # 🟪PATCH ----------------------------------------------------------------------------------------------------------
    def patch(
            self,
            endpoint: str,
            params: dict | None = None,
            headers: dict[str, str] | None = None,
            json: Any | None = None,
            data: Any | None = None,
            files: Any | None = None,
            timeout: float | None = None
    ) -> requests.Response:
        return self._request('PATCH', endpoint, params=params, headers=headers, json=json, data=data, files=files, timeout=timeout)


    # 🟦PUT ------------------------------------------------------------------------------------------------------------
    def put(
            self,
            endpoint: str,
            params: dict | None = None,
            headers: dict[str, str] | None = None,
            json: Any | None = None,
            data: Any | None = None,
            files: Any | None = None,
            timeout: float | None = None
    ) -> requests.Response:
        return self._request('PUT', endpoint, params=params, headers=headers, json=json, data=data, files=files, timeout=timeout)


    # 🟥DELETE ---------------------------------------------------------------------------------------------------------
    def delete(
            self,
            endpoint: str,
            params: dict | None = None,
            headers: dict[str, str] | None = None,
            timeout: float | None = None
    ) -> requests.Response:
        return self._request('DELETE', endpoint, params=params, headers=headers, timeout=timeout)

    #-------------------------------------------------------------------------------------------------------------------

