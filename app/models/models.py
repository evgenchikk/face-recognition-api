from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, DeclarativeBase

from app.database.database import engine


class Base(DeclarativeBase): pass

class ImageModel(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)

class FppResponseModel(Base):
    __tablename__ = 'fpp_responses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fpp_response = Column(String, nullable=False)
    image_id = Column(Integer, ForeignKey('images.id'), nullable=False)

    image = relationship(ImageModel)

Base.metadata.create_all(engine)
