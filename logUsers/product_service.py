import logging
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from nameko.dependency_providers import Config

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))
    price = Column(Float)

class ProductService:
    name = 'product_service'
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

    config = Config()


    db = DatabaseSession(Base)

    @classmethod
    def from_config(cls, config):
        db_uri = config['database']['uri']
        print(db_uri)
        engine = create_engine(db_uri)
        Base.metadata.create_all(engine)
        return cls(engine)
    def setup(self):
        self.db = self.__class__.from_config(self.config)

    @rpc
    def create_product(self, name, description, price):
        product = Product(name=name, description=description, price=price)
        self.db.add(product)
        self.db.commit()
        return {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price}

    @rpc
    def get_product(self, id):
        product = self.db.query(Product).filter(Product.id == id).first()
        if not product:
            return None
        return {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price}

    @rpc
    def delete_product(self, id):
        product = self.db.query(Product).filter(Product.id == id).first()
        if not product:
            return None
        self.db.delete(product)
        self.db.commit()
        return {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price}
