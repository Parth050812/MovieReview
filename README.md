# Movie Recommendation and Review System (Tkinter GUI)
This project is a Movie Recommendation and Review System developed using Python and Tkinter.<br>
It allows users to search for movies, filter by genre, maintain watchlists, mark movies as completed, add reviews, and explore random movie recommendations.
## Features
- Search movies by Title, Actor/Actress, Director, Year, or Rating.
- Display movie details, including Poster, Summary, Genre, and Cast.
- Filter movies based on selected genres (max 2 at a time).
- Manage Watchlist:
  - Add movies to Watchlist.
  - Mark movies as Completed.
  - Add your personal Review and Rating after watching.
- Manage Not Interested List:
  - Add movies you don't want to watch.
  - Remove movies from the list if you change your mind.
- Show random movies on application start.
- Full-screen immersive UI using Tkinter Canvas, Frames, and Scrollbars.

## Clone
Do the git clone of the repo 
```bash
git clone https://github.com/Parth050812/MovieReview.git
cd MovieReview
```
## Dependencies
Before running the project, install the following Python libraries:
```bash
pip install pillow
```
### Note:
- **tkinter** is included by default with standard Python installations (especially with Python 3.x).
- **sqlite3** is a built-in Python module — no installation required.
- **io** is also a standard Python library — no installation needed.

### Imported Modules:
- **tkinter** – for GUI interface
- **tkinter.messagebox** – for pop-up dialogs and alerts
- **sqlite3** – for handling the movie database
- **PIL (pillow)** – for displaying movie posters
- **io** – for working with image byte streams
  
## Database
SQLite database file: **moviep.db**
- The database stores:
- Title, Year, Rating, Summary
- Director, Actors, Musician
- Genres (up to 4 per movie)
- Poster image
- Review and Review Rating
- Flags for Watchlist, Not Interested, and Completed movies

## Run the File:
Make sure you have Python installed (version 3.6 or later recommended).
Install required dependency (pillow) using pip.
Keep the main.py file and the moviep.db database file in the same directory.
Run the app:
```bash
python main.py
```

## Important Notes
- At startup, random movies are displayed.
- Search and filter results are dynamically shown.
- The system automatically updates the database based on user actions (like marking completed, adding reviews, etc.).
- All movie posters are retrieved from the database (BLOB format).
