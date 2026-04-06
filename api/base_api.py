"""
Base API
(Requests)
"""
import requests
from data.data import Base

#=======================================================================================================================
class BaseAPI:
    base_url = Base.URL

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        return requests.request(
            method=method,
            url=f'{self.base_url}{endpoint}',
            **kwargs
        )

    # 🟩GET
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request('GET', endpoint, **kwargs)

    # 🟨POST
    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request('POST', endpoint, **kwargs)

    # 🟦PUT
    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request('PUT', endpoint, **kwargs)

    # 🟪PATCH
    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request('PATCH', endpoint, **kwargs)

    # 🟥DELETE
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request('DELETE', endpoint, **kwargs)

#-----------------------------------------------------------------------------------------------------------------------