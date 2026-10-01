from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


# ==========================================
# ПОЛЬЗОВАТЕЛИ (USERS)
# ==========================================
class UserRead(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email: str
    password: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None
    username: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    is_verified: bool | None = None


# ==========================================
# КОММЕНТАРИИ (COMMENTS)
# ==========================================
class CommentRead(BaseModel):
    id: int
    text: str
    pub_date: datetime
    author: UserRead | None = None
    author_id: int
    model_config = ConfigDict(from_attributes=True)

class CommentCreate(BaseModel):
    text: str


# ==========================================
# ПОСТЫ (POSTS)
# ==========================================
class PostList(BaseModel):
    id: int
    text: str
    pub_date: datetime
    image: str | None = None
    author: UserRead
    author_id: int
    group_id: int | None = None
    comments: list[CommentRead] = []
    model_config = ConfigDict(from_attributes=True)

class PostCreate(BaseModel):
    text: str
    image: str | None = None
    group_id: int | None = None

class PostDetailResponse(BaseModel):
    post: PostList
    author_post_count: int


# ==========================================
# ПРОФИЛЬ (PROFILE)
# ==========================================
class ProfileResponse(BaseModel):
    author: UserRead
    posts: dict
    is_following: bool
    total_posts: int


# ==========================================
# СООБЩЕСТВА (GROUPS)
# ==========================================
class GroupRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    slug: str
    owner_id: int | None = None
    model_config = ConfigDict(from_attributes=True)

class GroupCreate(BaseModel):
    title: str
    description: str | None = None
    slug: str | None = None