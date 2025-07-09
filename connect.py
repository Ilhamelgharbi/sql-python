import os 
from dotenv import  load_dotenv
from  sqlalchemy import create_engine
load_dotenv()

DB_HOST = os.getenv(DB_HOST)
DB_USER =  os.getenv(DB_USER)
DB_PORT =  os.getenv(DB_PORT)
DB_PASSWORD =  os.getenv(DB_PASSWORD)
DB_DBNAME =  os.getenv(DB_DBNAME)

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}

engine= create_engine(DATABASE_URL)


try :
  with engine.connect() as connection :
    print("conection is successful")
except exception as e :
  print(e)
