# We no longer need 'io' or 'contextlib'
from flask import Flask, jsonify, render_template, request
from password_generator import passworder  # Make sure filename is correct

# Create the Flask app
app = Flask(__name__)

# This route still serves your HTML frontend
@app.route('/')
def index():
    return render_template('index.html')

# This route (API endpoint) will generate the password
@app.route('/generate_password')
def get_password():
    # Get the 'length' from the URL (e.g., /generate_password?length=16)
    # Default to 12 if not provided.
    try:
        length = int(request.args.get('length', 12))
    except ValueError:
        length = 12
    
    # Clamp length between a safe range
    if length < 8: length = 8
    if length > 100: length = 100

    # Call your modified function with the specific length
    password = passworder(length)
    
    # Send the password back to the frontend
    return jsonify({'password': password})

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)