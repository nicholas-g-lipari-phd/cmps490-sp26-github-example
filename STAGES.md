# STAGES.md — Implementation Progression

This project is designed to be built in small, testable steps. Each stage leaves the app in a working state. Move forward only after you can run the app and verify the stage’s outcomes.

## Conventions Used Here

- **Frontend**: what runs in the browser (HTML/CSS/JS).
- **Backend**: Flask server code that receives requests and returns responses.
- **API / REST endpoint**: a URL your frontend calls to get data (usually JSON).
- **Route**: a Flask function mapped to a URL path (for example, `/ping` or `/api/ping`).
- **JSON**: a common format for structured data (`{...}` and `[...]`).
- **GET request**: a request used to retrieve data (no data is changed).
- **Query parameter**: key-value data after `?` in a URL (for example, `?title=term`).
- **Path parameter**: a value embedded in the URL path (for example, `/api/books/<id>`).
- **User-Agent**: a request header identifying the browser or client making the request.
- **Client IP**: the network address of the requester (often `request.remote_addr` in Flask).
- **Viewer page**: an HTML page that fetches data from an API endpoint and displays it (for example, `/ping` displays `/api/ping`).

---

## Stage 0 — Project Setup and “Hello Flask”
**Goal:** You can run a Flask server locally and see a page in the browser.

**Tasks**
- Create a Python virtual environment (venv) and install dependencies.
- Add a minimal `app.py` with one route:
  - `GET /` returns a simple HTML page or text.
- Add a `requirements.txt` (or `pyproject.toml`) for dependencies.

**Progress**
- [x] Create a Python virtual environment (venv) and install dependencies
- [x] Add a minimal `app.py` with one route: `GET /` returns a simple HTML page or text
- [x] Add a `requirements.txt` (or `pyproject.toml`) for dependencies

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

**Progress**
- [x] Create `templates/` for HTML
- [x] Create `static/` for CSS and JS
- [x] Make `/` render an HTML template (not just a string)
- [x] Add a simple CSS file and confirm it loads

**Definition of Done**
- The home page is rendered from `templates/index.html`.
- Styling changes in `static/style.css` affect the page.

---

## Stage 2 — First API Endpoint Returning JSON
**Goal:** Learn the idea of an API endpoint by returning JSON from Flask, observing request/response information, and displaying it in a readable page.

**Tasks**

1. **Return basic status**
   - Add a route:
     - `GET /api/ping` returns JSON like:
       ```json
       {"status": "ok"}
       ```
   - In the browser, open `/api/ping` and observe JSON output.

2. **Add diagnostic information**
   After confirming the status works, extend the response to include:

   - a message (for example, `"API reachable"`)
   - server time
   - browser user agent
   - client IP address
   - request method

   Example response:

   ```json
   {
     "status": "ok",
     "message": "API reachable",
     "server_time": "...",
     "user_agent": "...",
     "client_ip": "...",
     "method": "GET"
   }
   ```

3. **Add a readable “Ping Viewer” page**
   Create a simple HTML page that fetches `/api/ping` and displays the JSON in a formatted block.

   - Add a new route:
     - `GET /ping` returns an HTML page (template is fine)
   - On the page, use JavaScript to fetch `/api/ping`
   - Display the JSON using `JSON.stringify(data, null, 2)` inside a `<pre>` element

4. **Add CSS styling for the JSON block**
   Add a CSS file (or extend your existing one) to make the JSON output easy to read.

   Suggested CSS (example):

   ```css
   body {
     font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
     margin: 2rem;
     line-height: 1.4;
   }

   .card {
     max-width: 900px;
     padding: 1rem 1.25rem;
     border: 1px solid #ddd;
     border-radius: 10px;
   }

   pre.json {
     margin: 0;
     padding: 1rem;
     background: #f6f8fa;
     border: 1px solid #e5e7eb;
     border-radius: 8px;
     overflow: auto;
     font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
     font-size: 0.95rem;
     white-space: pre;
   }
   ```

**Progress**
- [x] Return basic status — `GET /api/ping` returns `{"status": "ok"}`
- [x] Add diagnostic information (message, server time, user agent, client IP, request method)
- [x] Add a readable "Ping Viewer" page at `GET /ping` that fetches `/api/ping` and displays the JSON
- [x] Add CSS styling for the JSON block

**Definition of Done**

- `/api/ping` returns valid JSON including:
  - status
  - message
  - server time
  - user agent
  - client IP
  - request method
- Visiting `/ping` shows a readable page with formatted JSON (not raw JSON in the browser).
- The JSON block is styled with CSS for readability (padding, monospace font, and scroll for long content).
- You can explain:
  - “`/api/ping` is an API endpoint (data). `/ping` is a web page (HTML) that displays the data.”

---

## Stage 3 — Load Static Book Data from a JSON File
**Goal:** Use a local JSON file as your “database” for testing.

**Tasks**
- Add `data/books.json` containing an array of book objects (see PR #1).
- Write a function to load and return the list of books.
- Add:
  - `GET /api/books` returns *all* books (temporary).

**Progress**
- [x] Add `data/books.json` containing an array of book objects
- [x] Write a function to load and return the list of books
- [x] Add `GET /api/books` returns all books

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

**Progress**
- [ ] Read the `title` query parameter from `/api/books?title=term`
- [ ] Filter the list of books by title (case-insensitive, partial match)
- [ ] Decide what to do when `title` is missing or empty

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

**Progress**
- [x] Add unique IDs in `books.json`
- [ ] Implement lookup by ID
- [ ] Return 404 with JSON `{"error": "Book not found"}` for missing IDs

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

**Progress**
- [ ] Add a text input, "Search" button, and results area to `index.html`
- [ ] Use `fetch()` in `static/app.js` to call `/api/books?title=...`
- [ ] Display results as a clickable list

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

**Progress**
- [ ] Call `/api/books/<id>` when a book is clicked
- [ ] Display details (title, author(s), description) in a "details" section

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

**Progress**
- [ ] Create `step1_filter_or_select_fields(books)` function
- [ ] Create `step2_sort_or_format(books)` function
- [ ] Apply both steps in sequence for the search endpoint response

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

**Progress**
- [ ] Create a service function that calls the Google Books API and extracts needed fields
- [ ] Keep `/api/books?title=term` and `/api/books/<id>` endpoints stable (frontend unchanged)

**Definition of Done**
- Searching uses live data from Google Books.
- Your frontend still works without changes to routes.

---

## Stage 10 — API Keys with `.env` + OMDb Movie Lookup (Books Adapted Into Movies)
**Goal:** Learn how to use API keys safely with environment variables and extend the app by enriching book results with movie adaptation data from OMDb.

### Concept
- Google Books (or your static JSON) provides **books**.
- OMDb provides **movies** and requires an **API key**.
- The frontend will offer a checkbox like **“Check for movie adaptation”**. When enabled, each book result triggers a follow-up OMDb search to see whether a movie with a matching title exists.

---

## Tasks

### 10.1 Add `.env` support
1. Install and add to `requirements.txt`:
   - `python-dotenv`
2. Create a `.env` file in the project root (do not commit it):
   ```env
   OMDB_API_KEY=your_key_here
   ```
3. Add `.env` to `.gitignore`.

**Progress**
- [ ] Install `python-dotenv` and add to `requirements.txt`
- [ ] Create a `.env` file in the project root (not committed)
- [ ] Add `.env` to `.gitignore`

**Definition of Done**
- You can start the Flask app and access `OMDB_API_KEY` via environment variables (not hard-coded in source).

---

### 10.2 Create an OMDb service module (backend)
Create a small backend “service” function that calls OMDb using the key from the environment.

**OMDb endpoint**
- `http://www.omdbapi.com/?apikey=<key>&t=<title>`

Recommended behavior:
- Use `t=` (title lookup) first for simplicity.
- If you want broader matching later, use `s=` (search) as an enhancement.

**Progress**
- [ ] Create an OMDb service module that calls the OMDb API using the key from the environment
- [ ] Handle missing key and OMDb errors with a clear JSON error response

**Definition of Done**
- You can call OMDb from the backend and get a parsed JSON response.
- If the key is missing or OMDb errors, you return a clear JSON error.

---

### 10.3 Add a new backend endpoint: movie lookup for a book title
Add an endpoint that accepts a title and returns a simplified movie payload.

Example:
- `GET /api/omdb?title=<book_title>`

Return a simplified response like:
```json
{
  "found": true,
  "title": "The Godfather",
  "year": "1972",
  "rated": "R",
  "runtime": "175 min",
  "imdb_id": "tt0068646",
  "imdb_rating": "9.2",
  "poster": "https://....jpg"
}
```

If not found:
```json
{
  "found": false
}
```

**Progress**
- [ ] Add `GET /api/omdb?title=<book_title>` endpoint
- [ ] Return simplified movie payload or `{"found": false}`
- [ ] Return 400 with a helpful error message for missing `title`

**Definition of Done**
- `/api/omdb?title=...` works in the browser and returns consistent JSON.
- Missing `title` returns a 400 with a helpful error message.

---

### 10.4 Add UI: “Check for movie adaptation” checkbox
On the frontend:
1. Add a checkbox:
   - Label: “Check for movie adaptation”
2. When searching books:
   - If the box is unchecked: display books normally.
   - If checked: for each displayed book, make a follow-up request to:
     - `/api/omdb?title=<book title>`

Suggested UI behavior:
- Show a placeholder under each result while loading:
  - “Checking OMDb…”
- When a movie is found, show:
  - “Movie found: <title> (<year>) ⭐ <imdb_rating>”
  - Optional: poster thumbnail
- When not found:
  - “No movie adaptation found.”

**Progress**
- [ ] Add “Check for movie adaptation” checkbox to the frontend
- [ ] Perform OMDb lookups for each book result when the checkbox is checked
- [ ] Display movie found / not found message for each book result

**Definition of Done**
- Checking the box causes the app to perform OMDb lookups after book results load.
- Each book result can display whether a movie adaptation was found.

---

### 10.5 Add caching or throttling (lightweight)
To avoid repeated lookups:
- Add a simple in-memory cache on the frontend keyed by title, or
- Add a backend cache keyed by title for the current run.

**Progress**
- [ ] Add a simple in-memory cache (frontend or backend) to avoid repeated OMDb requests for the same title

**Definition of Done**
- Repeating the same search does not spam OMDb with identical requests.

---

## Error Handling Requirements
- If `OMDB_API_KEY` is missing:
  - backend returns a 500 with a clear message like:
    - `"OMDB_API_KEY is not set. Add it to your .env file."`
- If OMDb returns not found:
  - return `{ "found": false }`
- If OMDb rate-limits or errors:
  - return `{ "found": false, "error": "..." }` (or a 502 with details)

---

## Learning Goals
By completing this stage, you can explain:
- Why API keys should not be committed to Git
- How environment variables and `.env` files work
- How to extend an app by composing multiple APIs
- How to handle many follow-up requests responsibly (caching/throttling)

---
## Stage 11 — Error Handling and “Polish”
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

**Progress**
- [ ] Handle missing query parameters gracefully (backend)
- [ ] Handle Google API failures: network errors, non-200 responses, empty results (backend)
- [ ] Return clear JSON errors with appropriate status codes (backend)
- [ ] Show a friendly message for no results and server errors (frontend)
- [ ] Disable the Search button while a request is in progress (optional)

**Definition of Done**
- App behaves predictably even when something goes wrong.
- Users get helpful messages instead of a broken screen.

---

## Stage 12 — Optional Enhancements
Pick one or two if you have time.

**Ideas**
- Add pagination or limit results.
- Add a “recent searches” list.
- Add a loading spinner.
- Add additional filters (author, published year).
- Add unit tests for transformation functions.

**Progress**
- [ ] Select and implement one or two optional enhancements

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
