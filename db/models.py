 
__all__ = [
  'User', 
  'Base'
]

import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DATE, Column, Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):
  """модель пользователя тг для регистрации"""
  
  __tablename__ = 'user_table'

  user_id = Column(Integer, nullable = False, unique = True, primary_key = True)
  
  username = Column(String, nullable = False, unique = False)
  
  reg_date = Column(DATE, default = datetime.datetime.now, nullable = False, unique = False)
  

