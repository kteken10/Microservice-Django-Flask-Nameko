from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': 'amqp://guest:guest@localhost',
}

with ClusterRpcProxy(config) as rpc:
    # Appel à la méthode "hello" du service
    result = rpc.user_service.hello("John")

    # Création d'un utilisateur
    
    name=input("name of your user :")
    email=input("email of your user :")
    password=input("password of your user :")

    user_id = rpc.user_service.create_user(name,email,password)
   
    # Récupération d'un utilisateur
    user_name = rpc.user_service.get_user(user_id)
   

    # Mise à jour du nom d'un utilisateur
    rpc.user_service.update_user(user_id, "Janet","Janet@yzhoo.com","123impose")
    response=input(" la suppression de l'utilisateur ? %s "%(user_id))
    if response=="Y" or response=="O":
        rpc.user_service.delete_user(user_id)
