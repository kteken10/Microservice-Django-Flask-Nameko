import logging
from nameko.rpc import rpc
from nameko.web.handlers import http
from flask import jsonify
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
    db_uri = "postgresql://postgres:kevin@localhost/microservice"
    db = DatabaseSession(Bd)
    def __init__(self):
            engine = create_engine(self.db_uri)
            Bd.metadata.create_all(engine)
            self.db.bind = engine
      # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s] %(message)s')
    handler = logging.FileHandler('logger.log')
    handler.setFormatter(formatter)
    logger.addHandler(handler)        
        
    # ...
##ALL THE METHOD RPC OFF THE USER_SERVICE
    @rpc
    def get_all_users(self):
        self.logger.info('Get all users')
        users = self.db.query(User).all()
        user_list = []
        for user in users:
            user_list.append({
                "id": user.id,
                "name": user.name,
                "email": user.email
            })
        return user_list
    
    @rpc
    def create_user(self, name, email, password):
        self.logger.info(f'Create user: {name}')
        new_user = User(name=name, email=email, password=password)
        self.db.add(new_user)
        self.db.commit()
        user_list={"id": new_user.id, "name": new_user.name, "email": new_user.email}
        return user_list
    
    @rpc
    def update_user(self, user_id, name=None, email=None, password=None):
        self.logger.info(f'Update user: {user_id}')
        user = self.db.query(User).filter_by(id=user_id).first()

        if not user:
            return {'error': 'User not found'}

        if name:
            user.name = name

        if email:
            user.email = email

        if password:
            user.password = password

        self.db.commit()

        return {'id': user.id, 'name': user.name, 'email': user.email}
    
    @rpc
    def delete_user(self, user_id):
        self.logger.info(f'Delete user: {user_id}')
        user = self.db.query(User).get(user_id)
        if user is None:
            return {"error": "User not found"}
        self.db.delete(user)
        self.db.commit()
        return {"message": "User deleted successfully"}
    
    @rpc
    def get_user_by_id(self, user_id):
        self.logger.info(f'Get user by id: {user_id}')
        user = self.db.query(User).get(user_id)
        if user is None:
            return {"error": "User not found"}
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
##API CAN BE EXPOSE DIRECTLY WITH NAMEKO     

    @http("GET", "/users")
    def http_get_all_users(self, request):
        user_list = self.get_all_users()
        return jsonify(user_list)
    
    @http('POST', '/users')
    def http_create_user(self, request):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return jsonify({'error': 'missing required fields'}), 400

        user = self.create_user(name, email, password)
        return jsonify(user), 201 
    
    @http('GET', '/users/<int:user_id>')
    def http_get_user_by_id(self, request, user_id):
        user = self.get_user_by_id(user_id)
        return jsonify(user)
    @http('PUT', '/users/<int:user_id>')
    def http_update_user(self, request, user_id):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not any([name, email, password]):
            return jsonify({'error': 'missing required fields'}), 400

        updated_user = self.update_user(user_id, name=name, email=email, password=password)

        if 'error' in updated_user:
            return jsonify(updated_user), 404

        return jsonify(updated_user), 200
    @http("DELETE", "/users/<int:user_id>")
    def delete_user(self, request, user_id):
        result = self.user_rpc.delete_user(user_id)
        return result
    