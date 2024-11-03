from flask import Flask, render_template, request
import random
app = Flask(__name__)

all_personalities = {
    'INTJ': [
        'Inception (2010)', 
        'The Imitation Game (2014)', 
        'Ex Machina (2014)', 
        'A Beautiful Mind (2001)', 
        'The Social Network (2010)'
    ],
    'INTP': [
        'The Imitation Game (2014)', 
        'Primer (2004)', 
        'Interstellar (2014)', 
        'Eternal Sunshine of the Spotless Mind (2004)', 
        'The Matrix (1999)'
    ],
    'ENTJ': [
        'The Social Network (2010)', 
        'Moneyball (2011)', 
        'The Devil Wears Prada (2006)', 
        'Glengarry Glen Ross (1992)', 
        'The Wolf of Wall Street (2013)'
    ],
    'ENTP': [
        'Iron Man (2008)', 
        'Thank You for Smoking (2005)', 
        'The Prestige (2006)', 
        'Deadpool (2016)', 
        'The Big Short (2015)'
    ],
    'INFJ': [
        'Amélie (2001)', 
        'The Pursuit of Happyness (2006)', 
        'Atonement (2007)', 
        'The Book Thief (2013)', 
        'Her (2013)'
    ],
    'INFP': [
        'The Secret Life of Walter Mitty (2013)', 
        'Eternal Sunshine of the Spotless Mind (2004)', 
        'The Perks of Being a Wallflower (2012)', 
        'The Fault in Our Stars (2014)', 
        'Big Fish (2003)'
    ],
    'ENFJ': [
        'Dead Poets Society (1989)', 
        'Freedom Writers (2007)', 
        'The Blind Side (2009)', 
        'The Help (2011)', 
        'Remember the Titans (2000)'
    ],
    'ENFP': [
        'Into the Wild (2007)', 
        'The Greatest Showman (2017)', 
        '500 Days of Summer (2009)', 
        'Little Miss Sunshine (2006)', 
        'About Time (2013)'
    ],
    'ISTJ': [
        'The Martian (2015)', 
        'Sully (2016)', 
        'The King\'s Speech (2010)', 
        'Saving Private Ryan (1998)', 
        'The Accountant (2016)'
    ],
    'ISFJ': [
        'Forrest Gump (1994)', 
        'The Blind Side (2009)', 
        'The Help (2011)', 
        'A Beautiful Day in the Neighborhood (2019)', 
        'Pride (2014)'
    ],
    'ESTJ': [
        'Moneyball (2011)', 
        'The Devil Wears Prada (2006)', 
        '12 Angry Men (1957)', 
        'The Intern (2015)', 
        'Erin Brockovich (2000)'
    ],
    'ESFJ': [
        'The Sound of Music (1965)', 
        'Mamma Mia! (2008)', 
        'Steel Magnolias (1989)', 
        'Fried Green Tomatoes (1991)', 
        'Julie & Julia (2009)'
    ],
    'ISTP': [
        'Mad Max: Fury Road (2015)', 
        'Die Hard (1988)', 
        'John Wick (2014)', 
        'The Bourne Identity (2002)', 
        'Fight Club (1999)'
    ],
    'ISFP': [
        'The Pursuit of Happyness (2006)', 
        'Into the Wild (2007)', 
        'Garden State (2004)', 
        'A Ghost Story (2017)', 
        'La La Land (2016)'
    ],
    'ESTP': [
        'The Wolf of Wall Street (2013)', 
        'Baby Driver (2017)', 
        'Rush (2013)', 
        'Casino Royale (2006)', 
        'Kingsman: The Secret Service (2014)'
    ],
    'ESFP': [
        'The Greatest Showman (2017)', 
        'Zoolander (2001)', 
        'The Hangover (2009)', 
        'Pitch Perfect (2012)', 
        'Mamma Mia! (2008)'
    ]
}

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    movie = find_movie(processed_text, all_personalities)
    return render_template('index.html', movie=movie, personality=processed_text)

def find_movie(processed_text, all_personalities):
    personality_type = processed_text
    if personality_type in all_personalities:
        return 'Your movie match is ' + random.choice(all_personalities[personality_type]) + '!'
    else:
        return "Personality type not found. Please enter a valid 4-letter type."

if __name__ == "__main__":
    app.run(debug=True)
