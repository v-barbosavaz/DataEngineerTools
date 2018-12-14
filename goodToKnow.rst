=============
Good to know
=============

Docker
------

`Docker compose <https://web.leikir.io/docker-compose-un-outil-desormais-indispensable/>`_

> docker-compose up -d

Détacher docker du terminal pour qu'il nous rende la main (ne pas avoir les logs qui s'affichent en continu)

> docker exec -it mongo mongo

executer le conteneur mongo et lancer mongo

> docker logs mongo

> docker ps


http://localhost:27017/
Ça ne fonctionnera pas, c'est un port http alors que docker génère un port TCP non utilisable sur le navigateur.
On pourra le faire avec Elastic Search.


Vim
------
> vim docker-compose.yml

Quitter vim : esc puis :wq (pour write and quit) ou :q (juste pour quitter)