from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


# USER TABLE
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)

    password = Column(String)

    notes = relationship("Note", back_populates="owner")


# NOTES TABLE
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    content = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="notes"
    )
    is_pinned = Column(
    Integer,
    default=0
    )

# SHARED NOTES TABLE
class SharedNote(Base):
    __tablename__ = "shared_notes"

    id = Column(Integer, primary_key=True, index=True)

    note_id = Column(
        Integer,
        ForeignKey("notes.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )