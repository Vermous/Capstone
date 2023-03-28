
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('trash.db')

# Create the requests table if it doesn't exist
conn.execute("CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY, location TEXT, reason TEXT)")

# Insert some sample data into the table
conn.execute("INSERT INTO requests (location, reason) VALUES (?, ?)", ('Building A', 'There is no trash can nearby.'))
conn.execute("INSERT INTO requests (location, reason) VALUES (?, ?)", ('Building B', 'There is too much litter around.'))
conn.execute("INSERT INTO requests (location, reason) VALUES (?, ?)", ('Building C', 'It is a high-traffic area with no trash cans.'))
conn.commit()

# Close the database connection
conn.close()
