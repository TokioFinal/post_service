from sqlmodel import Field, SQLModel

class PostBase(SQLModel):
    title: str
    content: str 

class Post(PostBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author: str 


class PostCreate(PostBase):
    pass
