from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Attribute(Base):
    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("attributes.id"), nullable=True)