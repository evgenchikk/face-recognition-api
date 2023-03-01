from sqlalchemy import Column, ForeignKey, Integer, String, BINARY
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.db import engine


class Images(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    file_binary = Column(BINARY, nullable=False)
    fpp_response_id = Column(Integer, ForeignKey('fpp_responses.id'), nullable=False)

    fpp_response = relationship('FppResponses', back_populates='id')

class FppResponces(Base):
    __tablename__ = 'fpp_responses'

    id = Column(Integer, ForeignKey('images.fpp_response_id'), primary_key=True, index=True)
    fpp_response = Column(String, nullable=False)

    images = relationship('Images', back_populates='fpp_response_id')

# Base.metadata.create_all(bind=engine)
