"""
Base API
(HTTP request methods)
"""
import requests
from data.data import Base

#=======================================================================================================================
class BaseAPI:
    base_url = Base.URL

    # 🟩GET
    def get(self, endpoint, headers=None, params=None):
        return requests.get(
            url=f'{self.base_url}{endpoint}',
            headers=headers,
            params=params
        )

    # 🟨POST
    def post(self, endpoint, headers=None, json=None, params=None):
        return requests.post(
            url=f'{self.base_url}{endpoint}',
            headers=headers,
            params=params,
            json=json
        )

    # 🟦PUT
    def put(self, endpoint, headers=None, json=None, params=None):
        return requests.put(
            url=f'{self.base_url}{endpoint}',
            headers=headers,
            params=params,
            json=json
        )

    # 🟪PATCH
    def patch(self, endpoint, headers=None, json=None, params=None):
        return requests.patch(
            url=f'{self.base_url}{endpoint}',
            headers=headers,
            params=params,
            json=json
        )

    # 🟥DELETE
    def delete(self, endpoint, headers=None, params=None, json=None):
        return requests.delete(
            url=f'{self.base_url}{endpoint}',
            headers=headers,
            params=params,
            json=json
        )
#-----------------------------------------------------------------------------------------------------------------------