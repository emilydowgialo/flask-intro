from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    #return "Hi! This is the home page."
    #<a href = "/hello">Click here to fill out a form</a>
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi this is the homepage</title>
      </head>
      <body>
        <h1>Hi this is the homepage!</h1>
        <a href="/hello">Click here to fill out a form</a>
      </body>
    </html>
    """


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
          <label>What's your name? <input type="text" name="person"></label>
          <p>Select a compliment: </p>
          <select name="compliment">
            <option value="cool">You're cool</option>
            <option value="rad">You be rad</option>
            <option value="best">You da best</option>
          </select>
          <input type="submit">
        </form>

        <p>OR: Select an insult: </p>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <select name="diss">
            <option value="terrible">You're terrible</option>
            <option value="aweful">You be aweful</option>
            <option value="the worst">You da the worst</option>
          </select>
          <input type="submit">
        </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    instult = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, instult)
    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
