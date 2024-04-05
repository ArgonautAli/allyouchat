from sqlalchemy import Boolean,Column,Integer, String, UUID, ARRAY, Table, ForeignKey
from sqlalchemy.orm import relationship
from db import Base;

association_table = Table('association', Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id')),
    Column('message_id', Integer, ForeignKey('messages.id'))
)

class User(Base):
    __tablename__ = 'users'

    id= Column(UUID, primary_key=True,index=True)
    user_name = Column(String(50))


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(UUID(as_uuid=True), nullable=False)
    participants = relationship("User", secondary=association_table, back_populates="messages")
    content = Column(String(256))