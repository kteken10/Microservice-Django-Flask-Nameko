Bienvenue dans votre application!

## Description

Cette application est composée de trois services principaux qui fonctionnent ensemble pour fournir une expérience utilisateur complète. Les services sont:

1. Gestion des produits en Django
2. Application principale pour gérer les likes de produits en Flask
3. Application pour gérer la journalisation en Nameko

Chacun de ces services est encapsulé dans un conteneur Docker pour une gestion facile de l'environnement d'exécution.

## Prérequis

Avant d'exécuter l'application, vous devez vous assurer que Docker est installé sur votre machine. Si vous n'avez pas encore installé Docker, veuillez consulter la documentation officielle pour votre système d'exploitation pour obtenir des instructions d'installation.

## Exécution de l'application

Pour exécuter l'application, vous devez suivre les étapes suivantes:

1. Clonez le repository git en utilisant la commande suivante:


2. Accédez au répertoire du projet à l'aide de la commande suivante:


3. Construisez les images Docker pour chaque service à l'aide de la commande suivante:


4. Lancez les services à l'aide de la commande suivante:


5. Accédez à l'application principale dans votre navigateur Web en entrant l'URL suivante:


Vous pouvez maintenant commencer à utiliser l'application!

## Service 1: Gestion des produits en Django

Ce service est responsable de la gestion des produits. Il fournit une API pour créer, modifier, supprimer et récupérer des produits. Cette API peut être utilisée par les autres services de l'application.

## Service 2: Application principale pour gérer les likes de produit en Flask

Ce service est responsable de la gestion des likes des produits. Il fournit une API pour ajouter des likes à des produits et récupérer le nombre total de likes pour chaque produit.

## Service 3: Application pour gérer la journalisation en Nameko

Ce service est responsable de la journalisation des événements importants dans l'application. Il utilise le framework Nameko pour fournir une journalisation en temps réel à l'aide d'une file d'attente RabbitMQ.

## Conclusion

C'est tout! Vous avez maintenant une application entièrement fonctionnelle avec trois services principaux travaillant ensemble pour fournir une expérience utilisateur complète. N'hésitez pas à explorer les différents services et à les personnaliser selon vos besoins.
