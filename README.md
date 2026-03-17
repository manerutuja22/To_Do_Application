📝 Todo Application (Django)

A simple Todo web application built using Django. This project demonstrates core Django concepts like models, views, templates, CRUD operations, and basic UI styling.

---

🚀 Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as completed
* Display task creation time
* Clean and responsive UI using Bootstrap

---

🛠️ Tech Stack

* Python 3.12
* Django 6.x
* SQLite (default database)
* HTML, CSS, Bootstrap

---

📁 Project Structure

```
Todo-Application/
│
├── todo/                # Main project folder
│   ├── settings.py
│   ├── urls.py
│
├── tasks/               # App folder
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── list.html
│   │       └── update.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

⚙️ Setup Instructions

1. Clone the repository

```
git clone <your-repo-link>
cd Todo-Application
```

---

2. Create virtual environment

```
python -m venv .venv
```

Activate it:

**Windows:**

```
.venv\Scripts\activate
```

---

3. Install dependencies

```
pip install -r requirements.txt
```

---

4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

5. Start server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

🧠 How It Works

* **Model**: Defines the Task structure (title, completed, created_at)
* **Views**: Handle logic for displaying, adding, updating, deleting tasks
* **Templates**: Render UI using Django template engine
* **URLs**: Connect user requests to views

🔐 CSRF Protection

All forms use Django’s CSRF protection:

```
{% csrf_token %}
```

This prevents unauthorized form submissions and ensures secure requests.

📸 Screenshots

Home Page
![Home](screenshots/homepage.png)

Task States
![States](screenshots/task_states.png)

Update Task
![Update](screenshots/update.png)

Delete Task
![Delete](screenshots/delete.png)

📌 Future Improvements

* AJAX (no page reload)
* User authentication (login/register)
* Task categories
* Due dates & reminders
* REST API version

👨‍💻 Author

Rutuja Mane

📄 License

This project is for learning purposes.
