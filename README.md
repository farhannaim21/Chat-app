# Chat-app
# Django Chat Application

A Django-based chat application where users can register, log in, and initiate one-on-one chats with other registered users. This project leverages Django's built-in authentication system and provides a real-time chatting experience.

---

## Features

- **User Authentication**: 
  - Register, login, and logout functionality.
  - Secure password handling using Django's authentication framework.

- **Chat Functionality**: 
  - Initiate one-on-one chats with any registered user.
  - Real-time messaging.

- **User Management**: 
  - List all registered users in a collapsible left menu.
  - Responsive user interface for easy navigation.

- **Database Integration**: 
  - User data and chat logs are stored in a MySQL database.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/django-chat-app.git
cd django-chat-app
2. Set Up a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure the Database
Open settings.py in the chatapp directory.
Update the DATABASES settings to connect to your MySQL database:
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
5. Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
6. Create a Superuser (Optional)
bash
Copy code
python manage.py createsuperuser
7. Run the Server
bash
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000.

Project Structure
csharp
Copy code
django-chat-app/
│
├── chatapp/                # Main project directory
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URLs
│   ├── wsgi.py             # WSGI application
│   └── ...
│
├── chat/                   # Chat app directory
│   ├── templates/          # HTML templates
│   │   ├── registration/   # Login and Signup templates
│   │   ├── base.html       # Base layout
│   │   └── chat.html       # Chat interface
│   ├── static/             # Static files (CSS, JS, images)
│   ├── views.py            # App views
│   ├── models.py           # Database models
│   ├── urls.py             # App URLs
│   └── ...
│
├── templates/              # Global templates
│   └── ...
│
├── static/                 # Global static files
│   └── ...
│
├── db.sqlite3              # SQLite database (if used)
└── manage.py               # Django's command-line utility
How to Use
Register and Login
Visit /accounts/signup/ to create a new account.
Log in at /accounts/login/.
Chat with Users
After logging in, you'll see a collapsible menu with a list of registered users.
Select a user to start a chat.
Dependencies
Django
MySQL
Python 3.10 or later
Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

Acknowledgments
Django Documentation
Special thanks to all contributors and testers.
Developed by Farhan Naim.

sql
Copy code

### **Steps to Use**
1. Replace `<your-username>` with your GitHub username.
2. Customize any project-specific details (e.g., database credentials, acknowledgments).
3. Add the file to your project directory and commit it to your repository:

```bash
git add README.md
git commit -m "Add README file"
git push
