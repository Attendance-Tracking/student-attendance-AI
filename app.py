from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Route handler for the home page.
    """
    return 'Hello, Flask!'



if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
