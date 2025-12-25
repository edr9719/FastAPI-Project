from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        list_of_posts = list(text_posts.values())[:limit]
        print(f'This is the list of posts :{list_of_posts}. The end.')
        return list_of_posts
    return text_posts

@app.get("/posts/{post_id}")
def get_single_post(post_id: int) -> PostResponse:
    post = text_posts.get(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
