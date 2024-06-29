# Import necessary modules from the Flask framework
from flask import Flask, render_template, url_for, request
# Import functions from the database module
from database import store_post_data, get_posts_data

# Create an instance of the Flask class
app = Flask(__name__)

# Retrieve posts data from the database using the get_posts_data function
get_posts: dict = get_posts_data()

# Convert the dictionary keys to a list and reverse the order
posts_keys = list(get_posts.keys())
posts_keys.reverse()

# Define the route for the home page ("/")
@app.route("/")
def index():
    # Render the index.html template with the posts data and keys
    return render_template('index.html', posts=get_posts, keys=posts_keys)

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=9000)


#TODO  Function to store the post in a database (not implemented)
