from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pathlib import Path

class Base(DeclarativeBase):
    pass

class Atendimentos(Base):
    __tablename__ = 'atendimentos'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    motivo: Mapped[str] = mapped_column(String(200))
    canal: Mapped[str] = mapped_column(String(50))
    origem: Mapped[str] = mapped_column(String(50))
    gravidade: Mapped[int] = mapped_column(Integer())

    def __repr__(self):
        return f'Id: {self.id} | motivo: {self.motivo} | canal: {self.canal} | origem: {self.origem} | gravidade: {self.gravidade}'
    
class Database_config():
    def __init__(self):
        self.engine = self._get_engine()

    def _database_path(self):
        return str(Path(__file__).parent / 'bd_atendimentos.sqlite')

    def _database_url(self):
        return 'sqlite:///' + self._database_path()
    
    def _get_engine(self):
        return create_engine(self._database_url())


        