from flask import Flask, render_template, request
import random
app = Flask(__name__)

all_personalities = {'ESTJ' : ['BACK TO THE FUTURE', 'HARRY POTTER', 'THE SOCIAL NETWORK'], 'ENTJ' : ['test 1', 'test 2', 'test 3'], 'ESFJ' : ['test 1', 'test 2', 'test 3'], 
'ENFJ' : ['test 1', 'test 2', 'test 3'], 'ISTJ' : ['test 1', 'test 2', 'test 3'], 'ISFJ' : ['test 1', 'test 2', 'test 3'], 'INTJ' :  ['test 1', 'test 2', 'test 3'], 'INFJ' : ['test 1', 'test 2', 'test 3'], 
'ESTP' : ['test 1', 'test 2', 'test 3'], 'ESFP' : ['test 1', 'test 2', 'test 3'], 'ENTP' : ['test 1', 'test 2', 'test 3'], 'ENFP' : ['test 1', 'test 2', 'test 3'], 'ISTP' : ['test 1', 'test 2', 'test 3'], 
'ISFP' : ['test 1', 'test 2', 'test 3'], 'INTP' : ['test 1', 'test 2', 'test 3'], 'INFP' : ['test 1', 'test 2', 'test 3']}

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     movie = find_movie(processed_text, all_personalities)
#     return render_template('index.html', movie=movie)

# def find_movie(processed_text, all_personalities):
#     personality_type = processed_text
#     return random.choice(all_personalities[personality_type])
    text = request.form['text']
    processed_text = text.upper()

    # Debug: Print the processed input
    print(f"Processed Personality Type: {processed_text}")

    if processed_text in all_personalities:
        movie = random.choice(all_personalities[processed_text])
        print(f"Selected Movie: {movie}")  # Debug: Print the chosen movie
    else:
        movie = "Invalid personality type. Please try again."
        print("Invalid personality type provided.")  # Debug: Error message

    return render_template('index.html', movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
