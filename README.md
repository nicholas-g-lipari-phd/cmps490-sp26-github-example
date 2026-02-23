# cmps-357-sp26-book-search (Flask + AI-Assisted Development)

This project is a simple full-stack web application for searching and viewing book information. The application is built with **Flask** and developed incrementally with AI assistance, demonstrating how to design a frontend, implement REST endpoints, and process external data.

The project begins with static data for testing and later integrates the Google Books API, allowing students to explore data retrieval, transformation, and application structure.

---

## Overview

The application allows users to:

- Search for books by title  
- View a list of matching results  
- Select a book to see detailed information  

The system demonstrates a complete data flow from user input to backend processing and response rendering.

**Application Flow:**

```
User enters search term
    → Frontend sends request
        → Backend retrieves data
            → Backend transforms data
                → Results displayed to user
```

---

## Features

### Frontend
- Search bar for book titles
- Results list with clickable book entries
- Details section displaying selected book information
- Interface based on a provided wireframe

### Backend
- REST API built with Flask
- Two endpoints:
  - `GET /api/books?title=term` — search books
  - `GET /api/books/<id>` — retrieve book details
- Starts with a static JSON data source
- Later integrates the Google Books API:
  - https://www.googleapis.com/books/v1/volumes?q=<term>
- Includes multiple data manipulation steps such as:
  - filtering
  - sorting
  - formatting
  - simplifying results
- Data transformations work independently and when chained together

---

## Learning Goals

This project demonstrates:

- Basic Flask application structure
- REST API design
- Client–server data flow
- External API integration
- Data transformation pipelines
- Incremental development with AI assistance
- Separation of frontend and backend concerns

---

## Project Structure (Planned)

```
project-root/
├── app.py              # Flask application entry point
├── routes/             # API endpoints
├── services/           # Data retrieval and processing logic
├── static/             # Frontend assets (CSS, JS)
├── templates/          # HTML templates
├── data/               # Static JSON data for testing
├── README.md           # This file
└── STAGES.md           # Step-by-step guide for building the app incrementally
```

---

## Development Approach

The application is built in stages:

1. Basic Flask setup  
2. Static JSON data source  
3. Search endpoint implementation  
4. Data manipulation steps  
5. Frontend interface  
6. Google Books API integration  
7. Refinement and testing  

Each stage builds on the previous one and can be completed with guided AI assistance.

---

## Running the App (Typical Setup)

```bash
pip install flask requests
python app.py
```

Then open a browser to:

```
http://localhost:5000
```

---

## Notes

- The focus of this project is architecture and data flow rather than visual design.
- The code is intentionally structured to support experimentation, modification, and extension.
- AI tools may be used to assist with implementation, debugging, and design decisions.
