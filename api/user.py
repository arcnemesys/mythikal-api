from os import walk
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from typing import List, Optional
from passlib.hash import bcrypt
from . data_model import CharacterProfile
class User(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(index=True, primary_key=True, unique=True, nullable=False) 
    email: str = Field(index=True, primary_key=False, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    hashed_password: str = Field()
    profiles: List["CharacterProfile"] = Relationship(back_populates="user")

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.hashed_password)

    @classmethod 
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)
