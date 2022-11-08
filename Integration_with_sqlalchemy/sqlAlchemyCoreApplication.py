from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy import Column, create_engine, func, inspect, select 
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData(schema='teste')
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40),nullable=False),
    Column('email_address',String(60)),
    Column('nickname', String(50), nullable=False)
)

user = Table(
    'user_prefs', metadata_obj,
    Column('prefs_id',Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('prefs_name', String(40),nullable=False),
    Column('prefs_value',String(100)),
)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_db_obj = MetaData(schema='bank')
financial_info = Table(
      'financial_info',
       metadata_db_obj,
       Column('id', Integer, primary_key=True),
       Column('value',String(100), nullable=False),
)
  
print(financial_info.primary_key)