from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade= "all, delete-orphan"
    )

    def __repr__(self):
        return f"User (id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30),nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)


    user = relationship("User", back_populates="address")

    def __repr__(self):
        return  f"Address (id={self.id}, email={self.email_address})"

print(User.__tablename__)
print(Address.__table__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

#print(engine.table_names())
inspetor_engine = inspect(engine)
print(inspetor_engine.get_table_names())