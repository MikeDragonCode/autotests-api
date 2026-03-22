from httpx import Response
from clients.api_client import ApiClient
from typing import TypedDict

class CreateUserRequestDict(TypedDict):
  """
        Описание структуры запроса для создания пользователя.
        """
  email: str
  password: str
  lastName: str
  firstName: str
  middleName: str

class PublicUsersClient(ApiClient):

    def create_user_api(self, request:CreateUserRequestDict) -> Response:
        """
                       Метод выполняет cоздание пользователя.
                       :param request: Словарь с email, password, lastName, firstName, middleName
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.post('/api/v1/users',json=request)

