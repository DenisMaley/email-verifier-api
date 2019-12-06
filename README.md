# Email Verifier API

 > This is an email validation service

## What is this project about?

This is the project to validate and verify an email with validators such as Regex, DNS

## Requirements

To build this project you will need [Docker][Docker Install] and [Docker Compose][Docker Compose Install].

## Deploy and Run

After cloning this repository, type the following commands to start the app:

```sh
docker-compose build
```
```sh
docker-compose up
```

To stop the app:

```sh
docker-compose down
```

Then visit [localhost:5000/status][App] to check the status.
If you see 
 
 ```json
{
    "status": "OK"
}
```
 
it means that everything went well

## Usage

To validate e-mail run 

```sh
curl -d '{"email":"abc@xyz.com"}' -H "Content-Type: application/json" -X POST http://localhost:5000/email/validate
```


[Docker Install]:  https://docs.docker.com/install/
[Docker Compose Install]: https://docs.docker.com/compose/install/
[App]: http://127.0.0.1:5000/status