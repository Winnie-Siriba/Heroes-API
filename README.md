# Flask Superheroes API

A simple REST API for tracking superheroes and their powers, built with Flask and SQLAlchemy.

## Author
Winnie Siriba - Software Engineering Student

## Description
This API allows you to manage superheroes and their superpowers through a many-to-many relationship. Heroes can have multiple powers, and powers can belong to multiple heroes. The API provides full CRUD operations with proper validation and error handling.

## Features
- ✅ Complete REST API with 6 endpoints
- ✅ Many-to-many relationships between Heroes and Powers
- ✅ Input validation with descriptive error messages
- ✅ Proper HTTP status codes (200, 201, 400, 404)
- ✅ JSON responses in specified format
- ✅ Database seeding with sample data
- ✅ SQLAlchemy ORM with migrations

## Technology Stack
- **Backend**: Flask 2.3.3
- **Database**: SQLite (development) 
- **ORM**: SQLAlchemy with Flask-SQLAlchemy
- **Migrations**: Flask-Migrate
- **Language**: Python 3.8+

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd heroes-api
Create and activate virtual environment:
bash# Create virtual environment
python -m venv venv

2. # Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

Install dependencies:
bashpip install -r requirements.txt

Set up the database:
bash# Initialize migrations
flask db init

3. # Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade

# Seed the database with sample data:
bashpython seed.py

# Run the application:
bashpython app.py


The API will be available at http://localhost:5000
# API Endpoints
Heroes

GET /heroes - Retrieve all heroes
GET /heroes/:id - Retrieve specific hero with their powers

Powers

GET /powers - Retrieve all powers
GET /powers/:id - Retrieve specific power
PATCH /powers/:id - Update power description

Hero Powers

POST /hero_powers - Create new hero-power relationship

Usage Examples
Get all heroes
bashcurl http://localhost:5000/heroes
Get specific hero with powers
bashcurl http://localhost:5000/heroes/1
Create new hero-power relationship
bashcurl -X POST http://localhost:5000/hero_powers \
  -H "Content-Type: application/json" \
  -d '{
    "strength": "Strong",
    "power_id": 1,
    "hero_id": 2
  }'
Update power description
bashcurl -X PATCH http://localhost:5000/powers/1 \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Updated description with at least 20 characters"
  }'
# Data Models
Hero

id: Integer (Primary Key)
name: String (Real name)
super_name: String (Superhero name)

Power

id: Integer (Primary Key)
name: String (Power name)
description: String (Must be at least 20 characters)

HeroPower

id: Integer (Primary Key)
strength: String (Must be 'Strong', 'Weak', or 'Average')
hero_id: Integer (Foreign Key)
power_id: Integer (Foreign Key)

# Validation Rules

Power description: Must be present and at least 20 characters long
HeroPower strength: Must be exactly one of: 'Strong', 'Weak', 'Average'

# Error Handling
The API returns appropriate HTTP status codes:

200: Success
201: Created successfully
400: Bad request / Validation error
404: Resource not found

Error responses include descriptive messages:
json{
  "error": "Hero not found"
}
json{
  "errors": ["Description must be at least 20 characters long"]
}
Testing
You can test the API using:

Postman (import the provided collection)
curl commands 
Thunder Client (VS Code extension)

Support
For questions or issues:

GitHub: Winnie-Siriba

Thank You.