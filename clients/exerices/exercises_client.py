from httpx import Response
from clients.api_client import ApiClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class GetExerciseDict(TypedDict):
    """
             Описание структуры запроса на получние упражнений.
             """
    courseId: str

class CreateExerciseDict(TypedDict):
    """
          Описание структуры запроса на создание упражнений.
          """
    title: str
    courseId : str
    maxScore: int
    minScore: int
    orderIndex: str
    description: str
    estimatedTime: str

class UpdateExerciseDict(TypedDict):
    """
             Описание структуры запроса на обновление упражнений.
             """
    title: str | None
    courseId : str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: str | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(ApiClient):

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
                       Метод получения упражнения.

                       :param exercise_id: Идентификатор файла.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def get_exercises_api(self, query: GetExerciseDict) -> Response:
        """
                    Метод получения списка упрежнений конкретного курча.

                    :param query: Словарь с exercise_id.
                    :return: Ответ от сервера в виде объекта httpx.Response
                    """
        return self.get('/api/v1/exercises/', params=query)

    def create_exercises_api(self, request: CreateExerciseDict)-> Response:
        """
                      Метод создания уупрежнения.

                      :param request: Словарь с title, maxScore, minScore, description, estimatedTime, courseId, orderIndex
                      :return: Ответ от сервера в виде объекта httpx.Response
                      """
        return self.post('/api/v1/exercises/', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseDict) -> Response:
        """
                     Метод обновления курса.

                     :param exercise_id: Идентификатор упражнения.
                     :param request: Словарь с title, maxScore, minScore, description, estimatedTime, courseId, orderIndex
                     :return: Ответ от сервера в виде объекта httpx.Response
                     """
        return self.patch(f'/api/v1/exercises/{exercise_id}',json=request)

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
                       Метод удаления курса.

                       :param exercise_id: Идентификатор упражнения.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))