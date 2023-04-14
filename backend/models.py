from sqlalchemy import Integer, String, SmallInteger, JSON, inspect
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column

from db import engine


class Base(DeclarativeBase):
    pass


class Goods(Base):
    __tablename__ = 'Goods'

    nm_id = mapped_column(Integer, nullable=False, primary_key=True)
    name = mapped_column(String, nullable=False)
    brand = mapped_column(String, nullable=False)
    brand_id = mapped_column(Integer, nullable=False)
    site_brand_id = mapped_column(Integer, nullable=False)
    supplier_id = mapped_column(Integer, nullable=False)
    sale = mapped_column(String, nullable=False)
    price = mapped_column(Integer, nullable=False)
    sale_price = mapped_column(Integer, nullable=False)
    rating = mapped_column(SmallInteger, nullable=False)
    feedbacks = mapped_column(Integer, nullable=False)
    colors = mapped_column(JSON, nullable=False)

    def __repr__(self) -> str:
        return f"Goods(nm_id={self.nm_id!r}, name={self.name!r})"


if not inspect(engine).has_table('Goods'):
    Base.metadata.create_all(engine)
