from pydantic import BaseModel, validator
from pydantic import ValidationError
from errors import HttpError
import re
password_regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")


class CreateUser(BaseModel):

    username: str
    password: str

    @validator('password')
    def validate_password(cls, value: str):
        if not re.search(password_regex, value):
            raise ValueError('password is too easy')
        return value


def validate_create_user(json_data):

    try:
        user_schema = CreateUser(**json_data)
        return user_schema.dict()
    except ValidationError as er:
        raise HttpError(status_code=400, message=er.errors())
