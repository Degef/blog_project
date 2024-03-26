from django.contrib.auth.models import User

# Retrieve all users
users = User.objects.all()

# Print user IDs
for user in users:
    print(f"User: {user.username}, ID: {user.id}")
