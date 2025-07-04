# Contact Book Flask Application

A simple web-based contact book application built with Flask that allows users to add and view contact information.

## Features

- Add new contacts with name and email
- View all submitted contacts in a list below the form
- Simple and clean web interface
- Form validation for required fields
- Hungarian language interface

## File Structure

```
contact_book/
├── app.py          # Main Flask application
└── index.html      # HTML template for the web interface
```

## Requirements

- Python 3.x
- Flask

## Installation and Usage

1. Clone or download this repository
2. Navigate to the project directory
3. Install Flask:
   ```bash
   pip install flask
   ```
4. Navigate to the `contact_book` directory:
   ```bash
   cd contact_book
   ```
5. Run the Flask application:
   ```bash
   python app.py
   ```
6. Open your web browser and go to:
   ```
   http://localhost:5000
   ```
7. Use the form to add contacts:
   - Enter a name in the "Név" field
   - Enter an email address in the "Email" field
   - Click "Hozzáadás" (Add) to submit

## Application Details

### Backend (`app.py`)

The Flask application includes:
- A single route (`/`) that handles both GET and POST requests
- In-memory storage for contacts using a Python list
- Form data processing for name and email fields

### Frontend (`index.html`)

The HTML template features:
- Simple form with name and email input fields
- Form validation (required fields)
- Display of all submitted contacts in a list below the form
- Hungarian language labels and interface

### Data Flow

1. User visits the homepage (GET request)
2. Flask renders the `index.html` template
3. User fills out the form and submits (POST request)
4. Flask processes the form data and adds it to the contacts list
5. Flask rerenders the `index.html` template with the updated contacts list
