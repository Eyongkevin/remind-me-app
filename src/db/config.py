"""
Setup sqlite database with sqlalchemy.
'DATABASE_URL' is consumed from the environment variable.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL"), echo=os.getenv("DEBUG", "False") == "True"
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Model(DeclarativeBase):
    """
    SQLAlchemy based model
    """

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


if __name__ == "__main__":
    print("DATABASE_URL: ", os.environ["DATABASE_URL"])
