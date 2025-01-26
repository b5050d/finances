import pandas as pd
import sqlite3

# Create a sample pandas DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Connect to an SQLite3 database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Write the DataFrame to the SQLite database
df.to_sql('users', conn, if_exists='replace', index=False)

# Verify by reading from the database
result = pd.read_sql('SELECT * FROM users', conn)

# Print the result
print(result)

# Close the connection
conn.close()
