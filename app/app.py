from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "First Post", "content": "Welcome to the blog. This is the first post."},
    2: {"title": "FastAPI Basics", "content": "An introduction to building APIs with FastAPI."},
    3: {"title": "Python Tips", "content": "A few useful Python tips for cleaner code."},
    4: {"title": "REST APIs", "content": "What REST is and why it still matters."},
    5: {"title": "Error Handling", "content": "How to handle errors properly in web APIs."},
    6: {"title": "Type Hints", "content": "Using type hints to improve code readability."},
    7: {"title": "Async in Python", "content": "Understanding async and await in modern Python."},
    8: {"title": "Testing APIs", "content": "Why automated tests save you from future pain."},
    9: {"title": "Clean Code", "content": "Small habits that make code easier to maintain."},
    10: {"title": "Scaling Up", "content": "What changes when your API starts to grow."}
}

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
