import sqlite3

# Step 1: Connect to SQLite (creates a database file if it doesn't exist)
connection = sqlite3.connect("example.sqlite")
cursor = connection.cursor()

# Step 2: Create the 'Ages' table
cursor.execute("DROP TABLE IF EXISTS Ages")  # Ensure the table is empty
cursor.execute("""
CREATE TABLE Ages (
    name VARCHAR(128),
    age INTEGER
)
""")

# Step 3: Insert data into the table
data = [
    ('Maria', 37),
    ('Benoit', 40),
    ('Girls', 13),
    ('Shawn', 23),
    ('Cejay', 29),
    ('Zijie', 16)
]
cursor.executemany("INSERT INTO Ages (name, age) VALUES (?, ?)", data)

# Step 4: Run the SQL query
cursor.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
result = cursor.fetchone()[0]

# Step 5: Print the result
print("Result:", result)

# Step 6: Close the connection
connection.commit()
connection.close()
