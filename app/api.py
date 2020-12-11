from fastapi import Body, Depends, FastAPI

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT

from .model import PostSchema, UserLoginSchema, UserSchema

app = FastAPI()

posts = [
    {
        'id': 1,
        'title': 'Pancake',
        'content': 'Lorem Ipsum',
    }
]

users = []


@app.get('/', tags=['roots'])
async def read_root() -> dict:
    return {'message': 'Welcome to your blog'}


@app.get('/posts', tags=['posts'])
async def get_posts() -> dict:
    return {'data': posts}


@app.get('/posts/{id}', tags=['posts'])
async def get_post(id: int) -> dict:
    if id > len(posts):
        return {
            'error': 'No such post with the supplied Id.'
        }
    for post in posts:
        if post['id'] == id:
            return {
                'data': post
            }


@app.post('/posts', dependencies=[Depends(JWTBearer())], tags=['posts'])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        'data': 'post added'
    }


@app.post('/users/signup', tags=['users'])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)
