. 📝 Django Blog Project with Unit Tests

This is a simple Django blog application with unit testing setup. It allows users to create and list blog posts. The project also includes model, view, and form tests using Django's built-in test framework.

---
 .🛠 Features

- Create and manage blog posts
- Form handling using Django forms
- Unit testing with Django's built-in test framework
- Organized app structure
- Lightweight and easy to extend


. 📁 Project Structure


myblog/
├── blog/ # Main app
│ ├── migrations/
│ ├── templates/
│ ├── tests/ # Contains test files
│ │ ├── init.py
│ │ ├── test_models.py
│ │ ├── test_views.py
│ │ └── test_forms.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── manage.py
└── myblog/ # Project settings
├── settings.py
├── urls.py
└── wsgi.py


. Clone the Repository


git clone https://github.com/Testcases/myblog
cd myblog
