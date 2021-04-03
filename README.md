# SRE Hiring Test

## Objectif

L'objectif de ce test est d'évaluer ta capacité à provisionner à l'aide de code les ressources GCP nécessaires au fonctionnement d'une simple application.

Il s'agit d'une application permettant de convertir une image en fichier PDF. Le code est en Python. L'application offre une interface HTTP pour la conversion. L'application convertit une image dont l'URL est fournie en entrée en un fichier PDF, stocke le résultat dans un bucket Cloud Storage et enfin renvoie une URL permettant à l'utilisateur de télécharger le PDF sur un appel HTTP de type GET.

Voici deux commandes illustrant l'usage de cette application:

```bash
$ curl -X POST "https://image2pdf-e3dvrhlyrq-ew.a.run.app/image_to_pdf" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d '{"source_url":"https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"}'
{
    "source_url": "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png",
    "converted_url": "https://storage.googleapis.com/image2pdf-files/5b42006d-c733-493d-9032-a083bc870e19.pdf"
}

$ curl "https://storage.googleapis.com/image2pdf-files/5b42006d-c733-493d-9032-a083bc870e19.pdf" --output img.pdf
...
```

Le choix du service GCP (App Engine, Cloud Run, Function, ...) et de l'outil d'Infra As Code t'es libre. Afin d'exprimer au mieux tes compétences, nous te recommandons d'utiliser des techniques que tu maitrises.

## Livrables

Nous avons besoin a minima de l'URL sur lequel faire l'appel POST et de l'URL du repository GitHub privé contenant ton code. Merci de donner l'accès en administration à Thierry (GitHub id: ThierryAbalea). Ce dernier ajoutera par la suite les membres de l'équipe chargés de revoir ton code.

## Hors scope

Bien que nécessaire pour être production-ready, il n'est pas nécessaire de travailler sur les problématiques suivantes:

- DNS. Des URLs avec des noms de domaine GCP suffisent.
- CI/CD
- tests automatisés

## Informations complémentaires

* Le point d'entrée du service est le script shell `scripts/entrypoint.sh`.
  Ce script peut être exécuté avec le paramètre `dev` pour exécuter le serveur de développement:

  ```bash
  $ ./scripts/entrypoint.sh dev
  INFO:     Uvicorn running on http://0.0.0.0:4321 (Press CTRL+C to quit)
  INFO:     Started reloader process [7] using statreload
  ...
  ```

  Il peut également être exécuté avec le paramètre `prod` pour exécuter le serveur en production:

  ```bash
  $ ./scripts/entrypoint.sh prod
  [2021-04-03 14:49:54 +0000] [1] [INFO] Starting gunicorn 20.1.0
  [2021-04-03 14:49:54 +0000] [1] [INFO] Listening at: http://0.0.0.0:4321 (1)
  ...
  ```

* Le service nécessite de définir les variables d'environnement suivantes:

  - `PROJECT_ID`: Doit contenir les nom du projet GCP hébergeant le service.
  - `SENTRY_DSN`: Doit contenir le DSN Sentry, permettant de collecter les erreurs en production. Sa valeur doit être `https://8a3f1db0f57e44e382eef7276c7f74b2@o185731.ingest.sentry.io/5704178`.
  - `PDF_BUCKET`: Doit contenir le nom du Bucket Google Storage qui hébergera les fichiers PDFs convertis.
  - `PORT`: Doit contenir le numéro de port sur lequel s'exécute le service.

* Le service nécessite d'installer les packages décrits dans le fichier `config/requirements.txt`.
