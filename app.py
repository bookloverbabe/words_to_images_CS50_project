# This pages is where any configuration, registration, and other setup the application needs will happen. 
from flask import Flask, render_template, request, flash
import secrets
# Creates a flask application object in the current python module
app = Flask(__name__)

# Generate a secure random secret key of 16 bytes
app.secret_key = secrets.token_hex(16)
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", total_sum=None)

def get_letter_value(letter):
    vowel = 'aeiou'
    consonant = 'bjkqvxyz'
    remainder = 'cdfghlmnprstw'
    
    if letter.isalpha():
        if letter.lower() in vowel:
            return 2
        elif letter.lower() in consonant:
            return 4
        elif letter.lower() in remainder:
            return 1
    elif letter == " ":
        return 0
    else:
        return 0

@app.route('/', methods=['GET', 'POST'])
def calculate_letter_sum():
    if request.method == 'POST':
        text = request.form.get('text')
        total_sum = 0

        for letter in text:
            total_sum += get_letter_value(letter)
        
        if total_sum == 0:
          flash('Please enter a word')

    return render_template("index.html", total_sum=total_sum)

if __name__ == "__main__":
    app.run()