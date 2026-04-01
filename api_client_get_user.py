from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from clients.users.private_users_client import get_private_user_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from httpx_get_user import create_user_response_data, get_user_response_data
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName= "string",
    firstName= "string",
    middleName= "string",
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

authentification_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

private_users_client = get_private_user_client(authentification_user)

get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print('Get user data:', get_user_response)