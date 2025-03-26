from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base


class GPTPost(Base):
    __tablename__ = 'gpt_post'

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    response = Column(JSONB)
