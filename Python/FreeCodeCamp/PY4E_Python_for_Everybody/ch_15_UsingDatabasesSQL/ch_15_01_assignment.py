# See README.md for assignment briefs.

# Used python to create the .sqlite file instead of using the Execute SQL tab
# found in the UI of DB Browser for SQLite.

# Remainder of assigment instructions and brief executed using input to the
# Execute SQL tab.

import sqlite3

conn = sqlite3.connect('ch_15_01_assigment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

conn.close()
