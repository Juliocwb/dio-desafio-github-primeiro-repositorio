from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, func, inspect, select 
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
        return  f"Address (id={self.id}, email_address={self.email_address})"

print(User.__tablename__)
print(Address.__table__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)
#print(inspetor_engine.__initi__())

with Session (engine) as session:
    julio = User(
        name='julio',
        fullname='Julio Carvalho',
        address=[Address(email_address='julio.cwb@gmail.com')]
    )

    carlos = User(
        name='carlos',
        fullname='Carlos andre',
        address=[Address(email_address='andre@gmail.com'),
                 Address(email_address='andre@hotmail.com')  ]
    )

    aron = User(name='aron',fullname='Aron carvalho')

    session.add_all([julio,carlos,aron])

    session.commit()

stmt = select(User).where(User.name.in_(['julio','aron']))
print("Recuperasndo usuarios a partir de condição de filtragem")

for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print("Recuperasndo os endreço de email de andre")
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperasndo info de maneira ordenada")

for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address,User )

for result in session.scalars(stmt_join):
    print(result)

#print(select(User.fullname, Address.email_address).join_from(Address,User ))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\n executeando statement a partir da connection")

for result in results:
    print(result)
stmt_count = select(func.count('*')).select_form(User)

for result in session.scalars(stmt_count):
    print(result)