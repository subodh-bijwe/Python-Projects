
import psycopg2 as psy

conn = psy.connect(host="localhost", dbname="postgres", user="postgres", password="root", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender CHAR
        );
""")
cur.execute("""INSERT INTO person (id, name, age, gender) VALUES 
            (1, 'Subodh', 27, 'm'),
            (2, 'Pooja', 21, 'f'),
            (3, 'Pumant', 25, 'm'),
            (4, 'Utk', 28, 'm'),
            (5, 'Prameya', 27, 'm');
            """)

cur.execute("""SELECT * FROM person WHERE age > 21;
            """)
for row in cur.fetchall():
    print(row)
    
    
print("-->>--<<--")

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s""", ("P", 26))
print(sql)
cur.execute(sql)
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()