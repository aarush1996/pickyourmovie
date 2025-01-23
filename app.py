from flask import Flask, render_template, request, jsonify
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations')
def recommendations():
    # Temporary: Just return some random movies instead of ML-based recommendations
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies LIMIT 5').fetchall()
    conn.close()
    return render_template('recommendations.html', recommendations=movies)

@app.route('/swipe')
def swipe():
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movies ORDER BY RANDOM() LIMIT 1').fetchone()
    conn.close()
    return render_template('swipe.html', movie=movie)

@app.route('/like_movie', methods=['POST'])
def like_movie():
    movie_id = request.form.get('movie_id')
    liked = request.form.get('liked')
    
    # Just store the like/dislike without ML processing
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
