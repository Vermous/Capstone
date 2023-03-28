
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a connection to the database
conn = sqlite3.connect('trash.db')

# Define a route for handling trash can requests
@app.route('/request', methods=['POST'])
def submit_request():
    # Extract the location and reason from the request data
    location = request.form.get('location')
    reason = request.form.get('reason')
    
    # Insert the request into the database
    conn.execute("INSERT INTO requests (location, reason) VALUES (?, ?)", (location, reason))
    conn.commit()
    
    response = {'message': 'Request submitted successfully.'}
    
    return jsonify(response)

# Define a route for getting summary statistics
@app.route('/stats', methods=['GET'])
def get_stats():
    # Count the number of requests for each location
    cursor = conn.execute("SELECT location, COUNT(*) FROM requests GROUP BY location")
    results = cursor.fetchall()
    
    # Format the results as a dictionary
    stats = {location: count for location, count in results}
    
    return jsonify(stats)

# Create the requests table if it doesn't exist
conn.execute("CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY, location TEXT, reason TEXT)")
conn.commit()

# Run the app
if __name__ == '__main__':
    app.run()
