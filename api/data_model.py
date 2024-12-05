from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from typing import List, Optional

class CharacterInput(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    strengths: List[str] = Field(default=None, primary_key=False)
    weaknesses: List[str] = Field(default=None, primary_key=False)
    goals: List[str] = Field(default=None, primary_key=False)
    fears: List[str] = Field(default=None, primary_key=False)
    hobbies: List[str] = Field(default=None, primary_key=False)
    vices: List[str] = Field(default=None, primary_key=False)
    virtues: List[str] = Field(default=None, primary_key=False)
    name: List[str] | None = Field(default=None, primary_key=False) 
class CharacterProfile(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    character_input: List[CharacterInput] = Field(default=None, primary_key=False)
    overview: str = Field(default=None, primary_key=False)
    abilities: List[str] = Field(default=None, primary_key=False)
    stats: List[str] = Field(default=None, primary_key=False)
    traits: List[str] = Field(default=None, primary_key=False)
    created_at: str = Field(default=None, primary_key=False)
    user: "User" = Relationship(back_populates="profiles")

class User(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(default=None, primary_key=True, unique=True, index=True)
    email: str = Field(default=None, primary_key=False)
    profiles: List["CharacterProfile"] = Relationship(back_populates="user")
