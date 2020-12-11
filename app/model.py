from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'Renato Lelis',
                'email': 'renatojlelis@gmail.com',
                'password': 'weakpassword'
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'email': 'renatojlelis@gmail.com',
                'password': 'weakpassword',
            }
        }


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'title': 'Securing FastAPI applications with JWT',
                'content': 'In this tutorial, you will learn how to secure your application by enabling authentication using JWT. We will be using PyJWT so sign, encode and decode JWT tokens...'
            }
        }
