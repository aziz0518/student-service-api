# Student Service API 🚀

Production-grade Online Education / Student Service backend API built with Django REST Framework, Docker, Redis, Celery, and MinIO.

## 🛠 Tech Stack

- **Framework:** Django 4.2+, DRF
- **Database:** PostgreSQL (via Docker)
- **Cache & Message Broker:** Redis
- **Task Queue:** Celery (Asynchronous Notifications)
- **Object Storage:** MinIO (S3 Compatible Storage for media files)
- **Authentication:** JWT (SimpleJWT) with Custom User Roles
- **Documentation:** OpenAPI 3 / Swagger UI (`drf-spectacular`)
- **Testing:** Pytest, pytest-django, Factory-Boy

## 📦 Features

- **Authentication:** Register, Login, Refresh Token with Student and Admin roles.
- **Service Management:** CRUD for Categories and Services with response caching.
- **Order System:** Submit academic requests/orders with file uploads stored directly in MinIO S3.
- **Async Tasks:** Automatic task triggers via Celery when orders are placed.
- **Optimization:** Fixed N+1 queries using `select_related`.
- **Unit & Integration Tests:** High test coverage using Pytest.

## 🚦 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/student-service-api.git](https://github.com/your-username/student-service-api.git)
cd student-service-api
