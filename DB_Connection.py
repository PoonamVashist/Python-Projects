import sqlite3
def create_table():
    conn=sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store ")
    conn.commit()
    conn.close()
def insert(item,quantity, price):
    conn=sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity, price))
    conn.commit()
    conn.close()
    
insert("Water", 6, 18.0)

def view(): 
    conn=sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item): 
    conn=sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()
    
def update(price,quantity,item): 
    conn=sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price=?, quantity=? where item = ?",(price, quantity,item))
    conn.commit()
    conn.close()
   
#delete("Car") 
update(10, 45, 'Water')
print(view())
