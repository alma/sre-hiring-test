# SRE Hiring Test

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Objective](#objective)
- [Deliverables](#deliverables)
- [Out of scope](#out-of-scope)
- [Additional information](#additional-information)
- [Questions](#questions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Objective

The purpose of this test is to assess your ability to provision, using code, the GCP resources necessary for a simple application.

The application in this repository allows for converting an image into a PDF file.
The code is in Python. The application provides an HTTP interface for the conversion.
The application converts an image whose URL is provided as input as a PDF file, stores the result in a GCP Cloud Storage bucket and finally returns a URL allowing the user to download the PDF over an HTTP GET call.

Here are two commands illustrating the use of this application:

```bash
$ curl -X POST "http://116-203-255-68.nip.io/image_to_pdf" \
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

The choice of compute GCP service ([Compute Engine](https://cloud.google.com/compute), [AppEngine](https://cloud.google.com/appengine), [CloudRun](https://cloud.google.com/run), [GKE](https://cloud.google.com/kubernetes-engine), [Cloud Functions](https://cloud.google.com/functions), etc) and the tool of Infrastructure as Code (Terraform, Ansible, Pulumi, etc) is yours.

In order to best express your skills, we recommend that you use techniques and tools that you master.
In order to better understand your approach, you can justify your choices in the associated documentation.

## Deliverables

* We will need, at least, the URL on which to test your deployed application by issuing `POST` calls. We will also need the URL of the private GitHub repository containing your code.
* You must create a **private** repository, using the [Github project import](https://github.com/new/import), and the [URL](https://github.com/alma/sre-hiring-test) of this repository. The procedure is well [documented](https://docs.github.com/en/migrations/importing-source-code/using-github-importer/importing-a-repository-with-github-importer). Please, do **not** clone the public repository, as you will not be able to change its visibility afterwards.
  
  When you are ready to deliver your code for review, please, give administration access to Arnaud Rolland (whose GitHub Id is [arnaudrolland](https://github.com/arnaudrolland)). He will, then, add the team members responsible for reviewing your code.
* You should deploy the application and the associated resources in a GCP project, by taking advantage of the [Free Tier products](https://cloud.google.com/free) of GCP.
* The deployed application should be **only** reachable through an URL using the application [nip.io](https://nip.io/). For example, `app-116-203-255-68.nip.io`.
  Doing this will require creating a load balancer to route the traffic to your deployed application.
* You should consider the security of your deployed application, and implement some measures to ensure its secure use (VPC, if needed; service account; etc)
* Your repository should enable continuous delivery of the application. So, any change on the repository should trigger an automatic update of the deployed application. You are free to use the Continuous Integration service of your choice (Github Action, Travis CI, Circle CI, etc).

## Out of scope

Although necessary to be production-ready, it is not necessary to work on the following issues:

- Automated testing of the application.
- Continuous Integration nor tests for the application. Testing the correct behavior of your deployed application can be part of your answer, thought.

## Additional information

* The application's entrypoint is the `scripts/entrypoint.sh` shell script.
  After installing the requirements specified in the `config/requirements.txt` file, this script can be run with the `dev` parameter to run the development server:

  ```bash
  $ ./scripts/entrypoint.sh dev
  INFO:     Uvicorn running on http://0.0.0.0:4321 (Press CTRL+C to quit)
  INFO:     Started reloader process [7] using statreload
  ...
  ```

  It can also be run with the `prod` parameter to run the server in production:

  ```bash
  $ ./scripts/entrypoint.sh prod
  [2021-04-03 14:49:54 +0000] [1] [INFO] Starting gunicorn 20.1.0
  [2021-04-03 14:49:54 +0000] [1] [INFO] Listening at: http://0.0.0.0:4321 (1)
  ...
  ```

* The application requires setting the following environment variables:

  - `PROJECT_ID`: Must contain the name of the GCP project hosting the application.
  - `SENTRY_DSN`: Must contain the Sentry DSN, allowing errors to be collected in production. Its value must be `https://8a3f1db0f57e44e382eef7276c7f74b2@o185731.ingest.sentry.io/5704178`.
  - `PDF_BUCKET`: Must contain the name of the Google Storage Bucket which will host the converted PDF files.
  - `PORT`: Must contain the port number the application is running on.

* The service requires installing the packages described in the `config/requirements.txt` file.

## Questions

You are free to ask any question required for the implementation of your solution, by reaching out to [Arnaud Rolland](mailto:arnaud.rolland@getalma.eu).
