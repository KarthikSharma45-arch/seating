# Exam Seating Arrangement Manager

A web application for managing exam seating arrangements with a clean, responsive interface.

## Features

- Interactive seating arrangement display
- Group-based color coding
- Student information management
- Search functionality
- Export/Import options
- Admin authentication
- Printing functionality

## Project Structure

```
seat-2/
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
├── backend/
│   ├── app.py
│   ├── models.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python backend/app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Requirements

- Python 3.8+
- Flask
- SQLAlchemy
- Other dependencies listed in requirements.txt

## Usage

1. Initialize the seating arrangement
2. Generate new arrangements as needed
3. Search for students by name or group
4. Export/Import arrangements
5. Print seating charts

## License

MIT License 