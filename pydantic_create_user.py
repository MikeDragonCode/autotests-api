from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    """Модель данных пользователя."""
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """Модель запроса на создание пользователя."""
    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Модель ответа с данными созданного пользователя."""
    user: UserSchema

user_default_model = UserSchema(
    id="user_id",
    email="email@user.com",
    lastName="Engineer",
    firstName="Mike",
    middleName="QA",
)
print("User default model:", user_default_model)

create_user_request_model = CreateUserRequestSchema(
    email="test@mail.com",
    password="secret123",
    lastName="Иванов",
    firstName="Иван",
    middleName="Иванович",
)
print("Create user request model:", create_user_request_model)

create_user_response_model = CreateUserResponseSchema(
    user=user_default_model
)
print("Create user response model:", create_user_response_model)