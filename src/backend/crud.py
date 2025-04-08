from backend.database import Database_config, Atendimentos, Base
from sqlalchemy.orm import Session
from sqlalchemy import select

class CRUD:
    def __init__(self):
        db_config = Database_config()
        self.engine = db_config.engine
        self.table = Atendimentos  
        Base.metadata.create_all(bind=self.engine)

    def create_service(self, **kwargs):
        with Session(bind=self.engine) as session:
            service = self.table(**kwargs)
            session.add(service)
            session.commit()

    def update_service(self,id,**kwargs):
        with Session(bind=self.engine) as session:
            query = select(self.table).filter_by(id=id)
            services = session.execute(query).fetchall()
            for service in services:
                for key, value in kwargs.items():
                    setattr(service[0],key,value)

            session.commit()

    def delete_service(self,id):
        with Session(bind=self.engine) as session:
            query = select(self.table).filter_by(id=id)
            services = session.execute(query).fetchall()
            for service in services:
                session.delete(service[0])
            session.commit()

    def read_a_service(self,id):
        with Session(bind=self.engine) as session:
            query = select(self.table).filter_by(id=id)
            services = session.execute(query).fetchall()
            service = services[0][0]
            return service
        
    def read_all_services(self):
        with Session(bind=self.engine) as session:
            query = select(self.table)
            services = session.execute(query).fetchall()
            service = [service[0] for service in services]
            return service
        
if __name__ == '__main__':
    #CRUD().create_service(
    #    motivo='não sei',
    #    canal='Teste',
    #    origem='disney',
    #    gravidade=1
    #)
    print(CRUD().read_all_services())
