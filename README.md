Bienvenue dans votre application!

## Description

Cette application est composée de trois services principaux qui fonctionnent ensemble pour fournir une expérience utilisateur complète. Les services sont:

1. Gestion des produits en Django
2. Application principale pour gérer les likes de produits en Flask
3. Application pour gérer la journalisation en Nameko

Chacun de ces services est encapsulé dans un conteneur Docker pour une gestion facile de l'environnement d'exécution.

## Prérequis

Avant d'exécuter l'application, vous devez vous assurer que Docker est installé sur votre machine. Si vous n'avez pas encore installé Docker, veuillez consulter la documentation officielle pour votre système d'exploitation pour obtenir des instructions d'installation.
- installer postgres pour l'utilisation des services:

les paramètre de configuration de la base de donnée sont dans le fichier config.yaml

- installer ou utiliser une image de RabbitMq via docker

## Exécution de l'application

Pour exécuter l'application, vous devez suivre les étapes suivantes:

1. Clonez le repository git en utilisant la commande suivante:

 



Vous pouvez maintenant commencer à utiliser l'application!

## Service 1: Gestion des produits en Django

Ce service est responsable de la gestion des produits. Il fournit une API pour créer, modifier, supprimer et récupérer des produits. Cette API peut être utilisée par les autres services de l'application.
### ouvrire le dossier admin du projet et lancer la commande :
    - docker-compose up
    - ensuite taper la commande python manage.py runserver  pour lancer le serveur de Django

## Service 2: Application pour gérer la journalisation en Nameko (CERATION DES UTILISATEUR AVEC FLASK  ET NAMEKO)

Ce service est responsable de la journalisation des événements importants dans l'application. Il utilise le framework Nameko pour fournir une journalisation en temps réel à l'aide d'une file d'attente RabbitMQ.
, et il utilise le framework Flask pour l'api.

### ouvrire le dossier Users du projet et lancer la commande :
    -  nameko run User --config config.yaml
    -  ensuite taper la commande python client.py pour tester le service Nameko  , vous pouvez utiliser un outils comme postman pour vérifier les point de terminaison de l'application.
## Conclusion

C'est tout! Vous avez maintenant une application entièrement fonctionnelle avec trois services principaux travaillant ensemble pour fournir une expérience utilisateur complète. N'hésitez pas à explorer les différents services et à les personnaliser selon vos besoins.
