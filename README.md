# 🌀 RIMES Django Web Application

This is a Django-based web application developed as a mini project for:

- 🧑 User Registration & Login
- 📝 Posting Articles/News with optional image upload (JPEG/PNG up to 5MB)
- 📊 Visualizing letter frequency (`r`, `i`, `m`, `e`, `s`) with Bar & Pie Charts
- 🛠 Admin Panel and Custom Management for Messages and Blogs
- 🐳 Fully containerized with Docker, PostgreSQL, Gunicorn, and NGINX

---

## 🚀 Features

### ✅ Frontend

- `/` — Home with message form and letter-frequency charts (filter by registered/anonymous users)
- `/blogs/` — Create, edit, delete your own articles
- `/accounts/login/` — Sign in
- `/accounts/register/` — Sign up

### 🔐 Admin Panel (`/admin`)

- View and manage users, blogs, and messages
- Staff users can delete all blog posts

---

## ⚙️ Technologies Used

- Python 3.11
- Django 5.x
- PostgreSQL 14
- Gunicorn
- NGINX (as reverse proxy)
- Docker & Docker Compose
- Chart.js (via CDN)
- Pillow (image upload)
- psycopg (PostgreSQL adapter)

---

## 🛠 Project Structure

```text
.
├── rimesproject/           # Django project
├── blogs/                  # Blog app
├── accounts/               # Auth app
├── messagesapp/            # Message + chart app
├── staticfiles/            # Collected static assets
├── media/                  # Uploaded media files
├── entrypoint.sh           # Runs migrate, collectstatic, createsuperuser
├── wait-for-postgres.sh    # Waits for DB to be ready
├── create_superuser.py     # Script to auto-create default admin
├── Dockerfile              # Web app Dockerfile
├── docker-compose.yml      # All services: web, db, nginx
├── nginx/nginx.conf        # NGINX config for serving static & reverse proxy
├── requirements.txt
└── README.md
```

---

## 🐳 Getting Started with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rimesproject.git
cd rimesproject
```

### 2. Build and Run the Containers

```bash
docker-compose up --build
```

> On first run, this will:
> - Wait for PostgreSQL to be ready
> - Run migrations
> - Collect static files
> - Auto-create a default superuser

---

## 🔑 Default Admin Credentials

```
Username: admin
Email:    admin@gmail.com
Password: P@ssw0rd
```

Access via: http://localhost/admin

---

## 🔎 Access URLs

| URL | Description |
|-----|-------------|
| `/` | Home with message form & charts |
| `/blogs/` | Create/Edit/Delete articles |
| `/accounts/login/` | Login |
| `/admin/` | Django admin dashboard |
| `/admin/blogs/` | Custom admin view (if any) |

---

## 📁 Static & Media Files

- `STATIC_ROOT` is `/app/staticfiles`
- Served by NGINX via volume
- Run `collectstatic` automatically during container startup

---

## 🧪 Development Notes

To reinitialize everything:
```bash
docker-compose down -v
docker-compose up --build
```

To access container shell:
```bash
docker exec -it django-app sh
```

To create a new app:
```bash
docker-compose exec web python manage.py startapp newapp
```

---

## 📦 Requirements

Install Docker & Docker Compose:
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## ✅ Author

Developed by: **Santichai Saksoong**

---

## 📜 License

MIT License
