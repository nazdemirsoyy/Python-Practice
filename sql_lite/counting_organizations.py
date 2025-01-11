import sqlite3
import re

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("orgs.sqlite")
cur = conn.cursor()

# Create the 'Counts' table
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("""
CREATE TABLE Counts (org TEXT, count INTEGER)
""")

# Open the mbox file
filename = "mbox.txt"
try:
    fh = open(filename)
except FileNotFoundError:
    print(f"File {filename} not found.")
    exit()

# Process the file
for line in fh:
    if not line.startswith("From: "): 
        continue
    # Extract the email address
    email = line.split()[1]
    # Extract the domain name
    domain = email.split("@")[1]
    
    # Update the count in the database
    cur.execute("SELECT count FROM Counts WHERE org = ?", (domain,))
    row = cur.fetchone()
    if row is None:
        # Insert new record
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (domain,))
    else:
        # Update existing record
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain,))
    
# Commit changes and close the file
conn.commit()
fh.close()

# Display the results
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(sqlstr):
    print(f"{row[0]}: {row[1]}")

# Close the connection
cur.close()
conn.close()
