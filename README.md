# Gift Sharing Application

A Flask-based web application for creating and sharing gift wishlists.

## Features

- User registration and authentication
- Create and manage multiple wishlists
- Add items with URLs and descriptions
- Track item purchase status
- Easy wishlist sharing
- Responsive design with CSS styling

## Setup

1. Install dependencies:
```bash
pip install flask flask-sqlalchemy werkzeug
```

2. Initialize the database:
```bash
flask shell
>>> from app import db
>>> db.create_all()
```

3. Create a secure secret key in app.py

4. Run the application:
```bash
flask run
```

## Project Structure

- `/models` - Database models
- `/routes` - Application routes
- `/templates` - HTML templates
- `/static` - CSS and images

## Usage

1. Register an account or login
2. Create a new wishlist
3. Add items to your wishlist
4. Share the wishlist URL with friends and family
5. Track which items have been purchased