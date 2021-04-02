# sre-hiring-test

## Objectif

L'objectif de ce test est d'évaluer ta capacité à provisionner à l'aide de code les ressources GCP nécessaires au fonctionnement d'une simple application.

Il s'agit d'une application permettant de convertir une image en fichier PDF. Le code est en Python. L'application offre une interface HTTP pour la convertion. L'application télécharge l'image sur un endpoint de type POST, la convertie en fichier PDF, stocke le résultat dans un bucket Cloud Storage et enfin renvoie une URL permettant à l'utilisateur de télécharger le PDF sur un appel HTTP de type GET.

Voici deux commandes illustrant l'usage de cette application:
```
curl --location --request POST 'http://<service-url>/img2pdf' \
--form 'file=@img.png'

curl http://<url-returned-by-the-previous-curl>/pdf/94ab2e9c-a803-4cdd-90d6-2c8e218b30c7.pdf --output=img.pdf
```

Le choix du service GCP (App Engine, Cloud Run, Function, ...) et de l'outil d'Infra As Code t'es libre. Afin d'exprimer au mieux tes compétences, nous te recommendons d'utiliser des technologies que tu maitrises.

## Livrables

Nous avons besoin à minima de l'URL sur lequel faire l'appel POST et de l'URL du repository GitHub privé contenant ton code. Merci de donner l'accès en administration à Thierry (GitHub id: ThierryAbalea). Ce dernier ajoutera par la suite les membres de l'équipe chargaient de revoir ton code.

## Hors scope

Bien que nécessaire pour être production-ready, il n'est pas nécessaire de travailler sur les problématiques suivantes:
- DNS. Des URLs avec des noms de domaine GCP suffisent.
- CI/CD
- tests automatisés
