from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle the request
@app.route('/')
def run():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
