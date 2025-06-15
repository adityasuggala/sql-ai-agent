# create_sample_data.py
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)
''', [
    ('Alice', 'Engineering', 120000),
    ('Bob', 'Sales', 90000),
    ('Charlie', 'HR', 70000),
    ('Diana', 'Engineering', 125000),
    ('Eve', 'Sales', 95000)
])

conn.commit()
conn.close()
print('Sample table and data created in test.db')
