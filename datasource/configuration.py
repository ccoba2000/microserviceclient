import os
from .secrets import get_secret

name_db=os.getenv("NAME_DB")
# user_db=os.getenv("USER_DB","root")
user_db=get_secret("db-user")
# password_db=os.getenv("PASSWORD_DB", "80Chicles#")
password_db=get_secret("db-password")
ip_db=os.getenv("IP_DB")
port_db=os.getenv("PORT_DB")

class Config:
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{user_db}:{password_db}@{ip_db}:{port_db}/{name_db}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
 
