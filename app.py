from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its associated handler
@app.route('/')
def home():
    return "Hello, World!"

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)




