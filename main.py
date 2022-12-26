from flask import Flask, render_template, request
from datetime import datetime as dt
import random
import os

x = dt.now()

app = Flask(__name__)

lives = 10

random_number = random.randint(1, 100)

high_responses = ["While admirable, generosity isn't always warranted!", "Much too generous, much too generous!",
                  "A bit overboard, I'd say."]

low_responses = ["This is no time to be coy!", "Stinginess is not an attractive characteristic.",
                 "A stingy one."]

@app.route("/")
def home():
    # Footer #
    year = x.year
    answer = "Let's see how shrewd you are!"
    return render_template("index.html", num_lives=lives, year=year, comment=answer)


@app.route("/", methods=["POST"])
def receive_data():
    global lives, random_number
    guess = int(request.form["number"])
    while lives > 1:
        if guess == random_number:
            answer = f"You Got It. The correct answer was {random_number}\nEnter a new number to keep playing."
            lives = 10
            random_number = random.randint(1, 100)
        elif guess < random_number:
            lives -= 1
            answer = f"{random.choice(low_responses)} Go higher."
        else:
            lives -= 1
            answer = f"{random.choice(high_responses)} Go lower."

        return render_template("index.html", num_lives=lives, comment=answer)
    else:
        answer = f"You lose! The correct answer was {random_number}\nEnter a new number to keep playing."
        lives = 10
        random_number = random.randint(1, 100)
    return render_template("index.html", num_lives=lives, comment=answer)



if __name__ == "__main__":
    app.run(debug=True)
