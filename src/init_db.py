
import sqlite3

conn = sqlite3.connect('data/parking.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS parking_slots (
    slot TEXT PRIMARY KEY,
    vehicle_type TEXT,
    occupied INTEGER,
    zone TEXT,
    distance INTEGER,
    priority_reserved INTEGER,
    charging INTEGER
)
''')

cursor.execute("DELETE FROM parking_slots")

slots = [

    ('A_B1', 'Bike', 0, 'Zone A', 5, 0, 0),
    ('A_C1', 'Car', 0, 'Zone A', 8, 0, 0),
    ('A_S1', 'SUV', 0, 'Zone A', 10, 1, 0),
    ('A_E1', 'EV', 0, 'Zone A', 4, 1, 1),

    ('B_B1', 'Bike', 0, 'Zone B', 7, 0, 0),
    ('B_C1', 'Car', 0, 'Zone B', 6, 0, 0),
    ('B_S1', 'SUV', 0, 'Zone B', 12, 1, 0),
    ('B_E1', 'EV', 0, 'Zone B', 3, 1, 1),

    ('C_B1', 'Bike', 0, 'Zone C', 5, 0, 0),
    ('C_C1', 'Car', 0, 'Zone C', 9, 0, 0),
    ('C_S1', 'SUV', 0, 'Zone C', 11, 1, 0),
    ('C_E1', 'EV', 0, 'Zone C', 2, 1, 1)
]

cursor.executemany(
    "INSERT INTO parking_slots VALUES (?, ?, ?, ?, ?, ?, ?)",
    slots
)

conn.commit()
conn.close()

print("AI Smart Parking Database Initialized")
