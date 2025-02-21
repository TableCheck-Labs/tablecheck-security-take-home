
# Application

Test application for the take-home project.

## Setup Instructions

1. Create a virtual environment:
```python
python -m venv venv
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the application:
```
python app.py
```

The application will be available at http://localhost:5000

Available Endpoints
* POST /login - User authentication
* GET /users - List users
* POST /upload - File upload
* GET /files/ - File download
* GET /template - Custom template rendering
* GET /export - System information
* GET /logs - Application logs
* GET /init - Initialize database

Default admin credentials:
* Username: admin
* Password: admin123