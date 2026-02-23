# Frontend Wireframe Suggestions

Below are several layout options, increasing in complexity. Each keeps the focus on clarity and data flow rather than visual polish.

---

## Option 1 — Simple Vertical Layout (Beginner Friendly)

Good for early stages and minimal CSS.

```
+--------------------------------------------------+
|                  Book Search                     |
+--------------------------------------------------+

[ Search by Title: __________________ ] [ Search ]

[ ] Check for movie adaptation

----------------------------------------------------
Results:
----------------------------------------------------

- Book Title 1
  Author(s)
  [Details]

  (Movie status appears here if enabled)

- Book Title 2
  Author(s)
  [Details]
```

### Notes
- All content stacked vertically
- Results expand downward
- Movie adaptation status appears under each book (initially empty or giving `Feature Not Implemented` message)
- Easiest to implement

---

## Option 2 — Two-Column Layout (Results + Details)

Good for reinforcing separation of concerns.

```
+--------------------------------------------------+
|                  Book Search                     |
+--------------------------------------------------+

[ Search: __________________ ] [ Search ]   [ ] Movie?

+--------------------+----------------------+
| Results            | Details              |
|--------------------|----------------------|
| - Book 1           | Title:               |
| - Book 2           | Author:              |
| - Book 3           | Description:         |
|                    |                      |
|                    | Movie Info:          |
|                    | (if enabled)         |
+--------------------+----------------------+
```

### Notes
- Left side: clickable results list
- Right side: selected book details
- Movie lookup result shown inside details panel
- Teaches dynamic DOM updates

---

## Option 3 — Card-Based Results Layout

More modern, good mid-semester stretch goal.

```
+--------------------------------------------------+
|                  Book Search                     |
+--------------------------------------------------+

[ Search: __________________ ] [ Search ]
[ ] Check for movie adaptation

----------------------------------------------------

+------------------------------+
| Title                        |
| Author(s)                    |
| Short description            |
|                              |
| Movie: Checking...           |
| or                           |
| Movie found: Title (Year)    |
+------------------------------+

+--------------------------------+
| Another Book                   |
| ...                            |
+--------------------------------+
```

### Notes
- Each result is a “card”
- Movie info is embedded in the card
- Easy to style with border + padding
- Good for adding posters later

---

## Option 4 — Progressive Disclosure Layout

Keeps initial results clean.

```
[ Search: __________________ ] [ Search ]
[ ] Check for movie adaptation

Results:
----------------------------------------------------

- Book Title 1 (Author)
    ▼ View Details
        Description...
        Movie: Found (1972) ⭐ 9.2

- Book Title 2 (Author)
    ▼ View Details
```

### Notes
- Results are compact initially
- Clicking expands content inline
- Reduces page clutter
- Teaches toggling UI state

---

## Option 5 — Advanced Split with Movie Badge Indicator

Good for emphasizing API composition.

```
+--------------------------------------------------+
| Book Search                                      |
+--------------------------------------------------+

[ Search __________________ ] [ Search ] [ ] Movie?

----------------------------------------------------

Results:

[📘] The Godfather
      Author: Mario Puzo
      [🎬 Movie Found]

[📘] Some Book
      Author: ...
      [No Movie]

----------------------------------------------------
Details Panel (Right or Below):
----------------------------------------------------
Full Description
Movie Poster (if found)
IMDB Rating
Runtime
```

### Notes
- Shows movie status as a visual badge
- Keeps results compact
- Encourages thinking about state synchronization

---

# Recommendation for Your Course

If building step-by-step:

1. Start with Option 1 (vertical list).
2. Move to Option 2 when adding details.
3. Upgrade to Option 3 when adding OMDb integration.

This progression mirrors backend complexity growth and reinforces architectural separation.

If you would like, I can next provide:
- a minimal HTML skeleton for one of these layouts
- or a CSS starter sheet that supports all of them
```
