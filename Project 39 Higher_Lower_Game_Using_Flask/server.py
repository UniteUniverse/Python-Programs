from flask import Flask
import random

app = Flask(__name__)

def random_check_decorator(function):
    def wrapper_function(num):
        random_num = random.randint(0, 9)
        print(random_num)
        if num == random_num:
            return function(num, "correct")
        elif num > random_num:
            return function(num, "higher")
        else:
            return function(num, "lower")
    return wrapper_function

@app.route("/")
def home():
    return '''<h1 style="text-align:center">Guess a number between 0 to 9.</h1>
              <img style="display: block; margin: auto;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'''

@app.route("/<int:num>")
@random_check_decorator
def guess(num, result):
    if result == "correct":
        return '''<h1 style="text-align:center; color:green">You Found Me!</h1>
                  <img style="display: block; margin: auto;" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'''
    elif result == "higher":
        return '''<h1 style="text-align:center; color:purple">Too high! Try again.</h1>
                  <img style="display: block; margin: auto;" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'''
    else:
        return '''<h1 style="text-align:center; color:red">Too low! Try again.</h1>
                  <img style="display: block; margin: auto;" src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'''

if __name__ == '__main__':
    app.run(debug=True)
