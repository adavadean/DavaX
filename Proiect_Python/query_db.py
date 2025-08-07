import sqlite3

def show_all_operations():
    conn = sqlite3.connect("math.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM operations")
    rows = cur.fetchall()
    conn.close()

    print("\n=== Istoric Operatii ===")
    for row in rows:
        print(f"[ID {row[0]}] {row[1]}({row[2]}{', ' + str(row[3]) if row[3] is not None else ''}) = {row[4]}")

if __name__ == "__main__":
    show_all_operations()
