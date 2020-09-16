from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

DATABASE = "sqlite:///DB.sqlite"

ENGINE = create_engine(
    DATABASE,
    encoding = "utf8",
    echo=True
)

session = scoped_session(
  # ORM実行時の設定。自動コミットするか、自動反映するなど。
        sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = ENGINE
        )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()