import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user:password@localhost:5432/cashbackdb"
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
