import sqlite3

def list_all_movies():
    # Connect to database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    # Get all movies
    cursor.execute('SELECT id, title FROM movies ORDER BY title')
    movies = cursor.fetchall()
    
    print("All movies in database:")
    print("-" * 50)
    for movie_id, title in movies:
        print(f"ID: {movie_id}, Title: {title}")
        if ':' in title:
            print("  ^ Contains colon")
    
    conn.close()

if __name__ == "__main__":
    list_all_movies()
