"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <a href="/hello">Welcome to the webpage</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <input type="radio" name="compliment" value="awesome">Awesome!<br>
          <input type="radio" name="compliment" value="terrific">Terrific!<br>
          <input type="radio" name="compliment" value="fantastic">Fantastic<br>
          <input type="radio" name="compliment" value="neato">Neato!<br>
          <input type="radio" name="compliment" value="fantabulous">Fantabulous!<br>
          <input type="radio" name="compliment" value="wowza">Wowza!<br>
          <input type="radio" name="compliment" value="oh-so-not-meh">Oh-So-Not-Meh!<br>
          <input type="radio" name="compliment" value="brilliant">Brilliant!<br>
          <input type="radio" name="compliment" value="ducky">Ducky!<br>
          <input type="radio" name="compliment" value="coolio">Coolio!<br>
          <input type="radio" name="compliment" value="incredible">Incredible!<br>
          <input type="radio" name="compliment" value="wonderful">Wonderful!<br>
          <input type="radio" name="compliment" value="smashing">Smashing!<br>
          <input type="radio" name="compliment" value="lovely">Lovely!<br>
          <input type="submit" value="Submit">
        </form>
        <br>
        <form action="/diss">
        For when your not feeling nice...<br>
        What's your name? <input type="text" name="person"><br>
        <select name="insults">
            <option value="slythrin">Slythrin!
            <option value="poopyhead">Poopyhead!
            <option value="buttfart">Buttfart!
            <option value="programmer">Bad Programmer!
            <br>
        <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name with compliment"""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment= request.args.get("compliment")
    return """ 
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route('/diss')
def insult_person():
    """Greet user by name with insult"""
    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    insult= request.args.get("insult")
    return """ 
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're a {}!
      </body>
    </html>
    """.format(player, insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
