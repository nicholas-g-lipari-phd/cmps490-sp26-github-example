# STAGES.md — Implementation Progression

This project is designed to be built in small, testable steps. Each stage leaves the app in a working state. Move forward only after you can run the app and verify the stage’s outcomes.

## Conventions Used Here

- **Frontend**: what runs in the browser (HTML/CSS/JS).
- **Backend**: Flask server code that receives requests and returns responses.
- **API / REST endpoint**: a URL your frontend calls to get data (usually JSON).
- **JSON**: a common format for structured data (`{...}` and `[...]`).
- **GET request**: a request used to retrieve data (no data is changed).

---

## Stage 0 — Project Setup and “Hello Flask”
**Goal:** You can run a Flask server locally and see a page in the browser.

**Tasks**
- Create a Python virtual environment (venv) and install dependencies.
- Add a minimal `app.py` with one route:
  - `GET /` returns a simple HTML page or text.
- Add a `requirements.txt` (or `pyproject.toml`) for dependencies.

**Definition of Done**
- Running `python app.py` starts a server.
- Visiting `http://localhost:5000/` shows your page.

---

## Stage 1 — Basic Folder Structure + Templates + Static Files
**Goal:** Understand how Flask serves HTML templates and static assets.

**Tasks**
- Create:
  - `templates/` for HTML
  - `static/` for CSS and JS
- Make `/` render an HTML template (not just a string).
- Add a simple CSS file and confirm it loads.

**Definition of Done**
- The home page is rendered from `templates/index.html`.
- Styling changes in `static/style.css` affect the page.

---

## Stage 2 — First API Endpoint Returning JSON
**Goal:** Learn the idea of an API endpoint by returning JSON from Flask.

**Tasks**
- Add a route:
  - `GET /api/ping` returns JSON like `{"status": "ok"}`.
- In the browser, open `/api/ping` and observe JSON output.

**Definition of Done**
- `/api/ping` returns valid JSON and you can explain:
  - “This endpoint returns data, not a web page.”

---

## Stage 3 — Load Static Book Data from a JSON File
**Goal:** Use a local JSON file as your “database” for testing.

**Tasks**
- Add `data/books.json` containing an array of book objects.
- Write a function to load and return the list of books.
- Add:
  - `GET /api/books` returns *all* books (temporary).

**Definition of Done**
- `/api/books` returns the list from your JSON file.
- If you change the JSON file, the endpoint response changes.

---

## Stage 4 — Search Endpoint with Query Parameters
**Goal:** Learn how a frontend can send a search term to the backend.

**API**
- `GET /api/books?title=term`

**Tasks**
- Read the `title` query parameter (for example, `?title=potter`).
- Filter the list of books by title (case-insensitive, partial match).
- Decide what to do when `title` is missing or empty:
  - Option A: return all books
  - Option B: return an empty list

**Definition of Done**
- `/api/books?title=...` returns relevant matches.
- You can explain:
  - “Query parameters appear after `?` in the URL.”

---

## Stage 5 — Book Details Endpoint Using Path Parameters
**Goal:** Learn how to request one specific item by its ID.

**API**
- `GET /api/books/<id>`

**Tasks**
- Add unique IDs in your `books.json`.
- Implement lookup by ID.
- If the ID does not exist, return a 404 status code with JSON:
  - `{"error": "Book not found"}`

**Definition of Done**
- `/api/books/123` returns one book (if it exists).
- Nonexistent IDs return a helpful JSON error and a 404.

---

## Stage 6 — Minimal Frontend (No Fancy UI Yet)
**Goal:** Create the simplest possible UI that calls the API.

**Tasks**
- In `index.html`, add:
  - a text input
  - a “Search” button
  - a results area (an empty `<div>` or `<ul>`)
- In `static/app.js`, use `fetch()` to call:
  - `/api/books?title=...`
- Display results as a clickable list.

**Definition of Done**
- Searching from the page updates the results list.
- You can open DevTools (Network tab) and see requests being made.

---

## Stage 7 — Details Panel in the Frontend
**Goal:** Click a result and show detailed info.

**Tasks**
- When a user clicks a book in the list:
  - call `/api/books/<id>`
  - display details in a “details” section
- Include at least:
  - title
  - author(s)
  - description (if present)

**Definition of Done**
- Clicking a book fetches details and updates the details section.

---

## Stage 8 — Data Manipulation Pipelines (Two Independent Steps)
**Goal:** Practice transforming raw data into cleaner, consistent output.

**Requirement**
- Include **two distinct data manipulation steps** (examples below).
- Each step:
  - works **independently**
  - also works correctly when **chained**

**Suggested Approach**
- In backend code, create two functions like:
  - `step1_filter_or_select_fields(books)`
  - `step2_sort_or_format(books)`
- Apply them in sequence for the search endpoint response.

**Examples of Two-Step Pipelines**
- Step 1: filter books by title
- Step 2: sort results alphabetically by title

OR

- Step 1: simplify each book object (keep only id/title/authors)
- Step 2: format fields (join authors list into a single string)

**Definition of Done**
- You can run each step alone (turn the other off) and it still works.
- With both enabled, output is correct.

---

## Stage 9 — Introduce the Google Books API (Backend Only)
**Goal:** Replace static data with real API data, while keeping your endpoints the same.

**API to call**
- `https://www.googleapis.com/books/v1/volumes?q=<term>`

**Tasks**
- Create a service function that:
  - sends a request to Google Books
  - reads the JSON response
  - extracts only the fields your app needs
- Keep your own endpoints stable:
  - `/api/books?title=term` should still work
  - `/api/books/<id>` should still work (you may define what “id” means here)

**Definition of Done**
- Searching uses live data from Google Books.
- Your frontend still works without changes to routes.

---

## Stage 10 — Error Handling and “Polish”
**Goal:** Make the app resilient and user-friendly.

**Backend tasks**
- Handle missing query parameters gracefully.
- Handle Google API failures:
  - network errors
  - non-200 responses
  - empty results
- Return clear JSON errors with appropriate status codes.

**Frontend tasks**
- Show a friendly message for:
  - no results
  - server errors
- Disable the Search button while a request is in progress (optional).

**Definition of Done**
- App behaves predictably even when something goes wrong.
- Users get helpful messages instead of a broken screen.

---

## Stage 11 — Optional Enhancements
Pick one or two if you have time.

**Ideas**
- Add pagination or limit results.
- Add a “recent searches” list.
- Add a loading spinner.
- Add additional filters (author, published year).
- Add unit tests for transformation functions.

**Definition of Done**
- Enhancement works and does not break earlier stages.

---

## Recommended Checkpoints (When to Commit)
Use Git commits to mark progress.

- After Stage 0: “Setup Flask and hello route”
- After Stage 3: “Load books from JSON and return via API”
- After Stage 6: “Frontend search calls backend and renders results”
- After Stage 9: “Google Books integration in backend”

---
