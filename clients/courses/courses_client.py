from httpx import Response, Request, request
from clients.api_client import ApiClient
from typing import TypedDict

class GetCoursesCreateDict(TypedDict):
    userId : str

class CreateCoursesCreateDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime:str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesCreateDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(ApiClient):

    def get_course_api(self, course_id: str) -> Response:
        return self.get(f'/api/v1/courses/{course_id}')

    def get_courses_api(self, query: GetCoursesCreateDict) -> Response:
        return self.get('/api/v1/courses/', params=query)

    def create_course_api(self, request: CreateCoursesCreateDict)-> Response:
        return self.post('/api/v1/courses/', json=request)

    def update_file_api(self, course_id: str) -> Response:
        return self.patch(f'/api/v1/courses/{course_id}')

    def delete_file_api(self, course_id: str, request: UpdateCoursesCreateDict) -> Response:
        return self.delete(f'/api/v1/courses/{course_id}', json=request)