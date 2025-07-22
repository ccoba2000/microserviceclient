from entities.model import Client
from datasource.db_session import local_session


def insert(client:Client)->bool:
    with local_session() as orm:
        if client:
            orm.add(client)
            orm.commit()
            return True
        

def update(client:Client)->bool:
    with local_session() as orm:
        result=orm.query(Client).filter(Client.id==client.id).update({
            Client.name:client.name,
            Client.email:client.email,
            Client.address:client.address,
        })
        orm. commit ( )
        return result>0
        
def delete(id:int)->bool:
    with local_session() as orm:
        result=orm.query(Client).filter(Client.id==id).delete()
        orm.commit()
        return result>0
    


def select_all():
    return