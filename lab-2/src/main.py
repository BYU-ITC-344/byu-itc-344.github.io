import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Initialize the flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET")


# ------------------------ BEGIN ROUTES ------------------------ #

@app.route("/", methods=["GET"])
def root():
    return render_template("index.html") # Return the page to be rendered

# Browse page
@app.route("/browse", methods=["GET"])
def browse():
    """
    This function renders the browse page.
    This page should display all of the recipes.
    """
        
    # Get all the recipes from the database
    
    # Add the recipes to the session


    # Render the front end
    return render_template('browse.html')
    
# ------------------------ END ROUTES ------------------------ #

# listen on port 8080
if __name__ == "__main__":
    #Debug code

    app.config['SESSION_TYPE'] = 'filesystem'

    app.run( port=8080, debug=True) # TODO: Students PLEASE remove debug=True when you deploy this for production!!!!!