import logging
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Bd = declarative_base()


class User(Bd):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class UserService:
    name = "user_service"
   # Créer un logger nommé "my_logger"
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

        # Configurer un handler de fichier
    handler = logging.FileHandler("logfile.log")
    handler.setLevel(logging.DEBUG)

        # Configurer le format du message de journalisation
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

        # Ajouter le handler au logger
    logger.addHandler(handler)

    db_uri = "postgresql://postgres:kevin@localhost/microservice"
    db = DatabaseSession(Bd)

    def __init__(self):
        engine = create_engine(self.db_uri)
        Bd.metadata.create_all(engine)
        self.db.bind = engine
       
        
    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

    @rpc
    def create_user(self, name, email, password):
        self.logger.info("Received request: create_user %s", name)
        user = User(name=name, email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.logger.info("User %s created with id %s", name, user.id)
        return user.id

    @rpc
    def get_user(self, id):
        self.logger.info("Received request: get_user %s", id)
        user = self.db.query(User).filter_by(id=id).first()
        if user is not None:
            self.logger.info("User with id %s found: %s", id, user.name)
            return user.name
        else:
            self.logger.warning("User with id %s not found", id)
            return None

    @rpc
    def update_user(self, id, name, email, password):
        self.logger.info("Received request: update_user %s", name)
        user = self.db.query(User).filter_by(id=id).first()
        user.name = name
        user.email = email
        user.password = password
        self.db.commit()
        self.logger.info("User update sucessfuly with infos %s %s "%(user.name,user.email))


    @rpc
    def delete_user(self, id):
        user = self.db.query(User).filter_by(id=id).first()
        self.logger.warning("Delete sucessfuly user  with infos %s %s "%(user.name,user.email))
        self.db.delete(user)
        self.db.commit()
        self.logger.warning("User with id %s deleted", id)
