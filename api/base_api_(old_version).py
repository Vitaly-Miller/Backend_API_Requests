"""
Base API (Old version)
(Requests)
"""
import requests
from data.data import Base

#=======================================================================================================================
class BaseAPI:
    base_url = Base.URL

    # 🟩GET
    def get(
            self,
            endpoint: str,
            params: dict | None = None,    # query string: ?key=value
            headers: dict | None = None,   # заголовки
            timeout: float | None = None,  # секунды
            auth=None                      #
    ) -> requests.Response:

        return requests.get(
            url=f'{self.base_url}{endpoint}',
            params=params,
            headers=headers,
            timeout=timeout,
            auth=auth
        )

    #-------------------------------------------------------------------------------------------------------------------
    # 🟨POST
    def post(
            self,
            endpoint: str,
            json: dict | None = None,        # тело запроса как JSON
            data: dict | str | None = None,  # form-data или raw строка
            headers: dict | None = None,
            params: dict | None = None,
            timeout: float | None = None,
            auth=None,
            files: dict | None = None        # загрузка файлов
    ) -> requests.Response:

        return requests.post(
            url=f'{self.base_url}{endpoint}',
            json=json,
            data=data,
            headers=headers,
            params=params,
            timeout=timeout,
            auth=auth,
            files=files
        )

    #-------------------------------------------------------------------------------------------------------------------
    # 🟦PUT
    def put(
            self,
            endpoint: str,
            json: dict | None = None,        # полная замена объекта
            data: dict | str | None = None,
            headers: dict | None = None,
            params: dict | None = None,
            timeout: float | None = None,
            auth=None
    ) -> requests.Response:

        return requests.put(
            url=f'{self.base_url}{endpoint}',
            json=json,
            data=data,
            headers=headers,
            params=params,
            timeout=timeout,
            auth=auth
        )

    #-------------------------------------------------------------------------------------------------------------------
    # 🟪PATCH
    def patch(
            self,
            endpoint: str,
            json: dict | None = None,        # частичное обновление
            data: dict | str | None = None,
            headers: dict | None = None,
            params: dict | None = None,
            timeout: float | None = None,
            auth=None
    ) -> requests.Response:

        return requests.patch(
            url=f'{self.base_url}{endpoint}',
            json=json,
            data=data,
            headers=headers,
            params=params,
            timeout=timeout,
            auth=auth
        )

    #-------------------------------------------------------------------------------------------------------------------
    # 🟥DELETE
    def delete(
            self,
            endpoint: str,
            headers: dict | None = None,
            params: dict | None = None,      # иногда передают id через params
            json: dict | None = None,        # редко, но бывает тело
            timeout: float | None = None,
            auth=None
    ) -> requests.Response:

        return requests.delete(
            url=f'{self.base_url}{endpoint}',
            json=json,
            headers=headers,
            params=params,
            timeout=timeout,
            auth=auth
        )
#-----------------------------------------------------------------------------------------------------------------------