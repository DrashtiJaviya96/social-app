# Social App (Microservices)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-Django%20REST-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-black)

A simple microservices-based social app built with Django, DRF, PostgreSQL, Docker, and JWT.

---

## Services

### User Service (Port 8000)
- User registration
- Authentication (JWT)
- Profile management

### Post Service (Port 8001)
- Create, update, delete posts
- Requires JWT authentication

---

## ▶️ Run Project

```bash id="run-final"
docker compose up --build
```

---

## Authentication Flow

1. Login via User Service
2. Receive JWT token
3. Send token in request header:

 ```
   Authorization: Bearer <token>
 ```

4. Post Service validates token and processes request

---

## Swagger Docs

* User Service → http://127.0.0.1:8000/api/docs/
* Post Service → http://127.0.0.1:8001/api/docs/

---
##  Design Patterns

- Microservices pattern → split app into small services, easier to scale, easier to manage
- Database per service → each service owns its data, avoids tight coupling, safer
- JWT authentication (stateless) → no session storage, works across services, simple and scalable
- Separation of concerns → each service does one job, cleaner code, easier to maintain
- Layered architecture → models, serializers, views, permissions, keeps code organized and readable



## ⚠️ Notes

- .env should not be committed
- JWT secret must be same across services
- Run using Docker

---


