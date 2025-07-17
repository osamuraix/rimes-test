from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

username = "admin"
email = "admin@gmail.com"
password = "P@ssw0rd"

if not User.objects.filter(username=username).exists():
    print("🛠️ Creating default superuser...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("✅ Default superuser already exists.")