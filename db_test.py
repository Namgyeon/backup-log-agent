import sqlite3

conn = sqlite3.connect("app.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS pcs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    disk TEXT,
    last_backup TEXT
)
""")

cur.execute(
    "INSERT INTO pcs (name, disk, last_backup) VALUES (?,?,?)",
    ("mac", "80%", "2026-10-24"),
)

conn.commit()

cur.execute("SELECT * FROM pcs")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM pcs WHERE id = ?", (99,))
row = cur.fetchone()
print(row)

conn.close()
