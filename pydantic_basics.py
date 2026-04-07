"""
{
  "courses": [
    {
      "id": "string",
      "title": "string",
      "maxScore": 0,
      "minScore": 0,
      "description": "string",
      "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
      },
      "estimatedTime": "string",
      "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
  ]
}
"""
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel
import uuid

class FileSchema(BaseModel):
    id: str
    url: str
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CoursesSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel,populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "HTTPX"
    max_score: int  = Field(default=1000)
    min_score: int  = Field(default=0)
    preview_file: FileSchema = Field(default_factory=lambda: FileSchema(
        id="default_file_id",
        url="http://localhost:8000/api/v1/files",
        filename="default.txt",
        directory="courses"
    ))
    description: str = "API Course"
    created_by_user: UserSchema = Field(default_factory=lambda: UserSchema(
        id="default_user_id",
        email="default@mail.com",
        lastName="Default",
        firstName="User",
        middleName="Test"
    ))
    estimated_time: str  = Field(default="8 Weeks")

course_default_model = CoursesSchema(
    id="course_uuid",
    title="HTTPX",
    maxScore=100,
    minScore=0,
    previewFile=FileSchema(
        id="file_id",
        url="http://localhost:8000/api/v1/files",
        filename="file.txt",
        directory="Courses"
    ),
    description="API Course",
    createdByUser=UserSchema(
        id="userId",
        email="test@mail.com",
        lastName="Engineer",
        firstName="Mike",
        middleName="QA"
    ),
    estimatedTime="10 weeks"
)
print("Course default model:", course_default_model)

course_dict = {
    "id":"course_uuid",
    "title":"HTTPX",
    "maxScore":100,
    "minScore":0,
    "previewFile": {
        "id": "file_id",
        "url": "http://localhost:8000/api/v1/files",
        "filename": "file.txt",
        "directory": "Courses"
    },
    "description":"API Course",
    "createdByUser": {
        "id":"userId",
        "email":"test@mail.com",
        "lastName":"Engineer",
        "firstName":"Mike",
        "middleName":"QA"
    },
    "estimatedTime":"10 weeks"
}

course_dict_model = CoursesSchema(**course_dict)
print("Course dict model:", course_dict_model)

course_json = """
{
    "id":"course_uuid",
    "title":"HTTPX",
    "maxScore":100,
    "minScore":0,
    "previewFile": {
        "id": "file_id",
        "url": "http://localhost:8000/api/v1/files",
        "filename": "file.txt",
        "directory": "Courses"
    },
    "description":"API Course",
    "createdByUser": {
        "id":"userId",
        "email":"test@mail.com",
        "lastName":"Engineer",
        "firstName":"Mike",
        "middleName":"QA"
    },
    "estimatedTime":"10 weeks"
}
"""
course_json_model = CoursesSchema.model_validate_json(course_json)
print("Course JSON model:", course_json_model)
print(course_json_model.model_dump_json(by_alias=True))
print(course_json_model.model_dump(by_alias=True))

course_1 = CoursesSchema()
course_2 = CoursesSchema()
print(course_1.id)
print(course_2.id)