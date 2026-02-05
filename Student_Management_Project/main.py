import sqlite3

class StudentDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS students 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, branch TEXT, cgpa REAL)'''
        self.cursor.execute(query)
        self.conn.commit()

    def add_student(self, name, branch, cgpa):
        query = "INSERT INTO students (name, branch, cgpa) VALUES (?, ?, ?)"
        self.cursor.execute(query, (name, branch, cgpa))
        self.conn.commit()
        print(f"Successfully added: {name}")

    def show_all(self):
        self.cursor.execute("SELECT * FROM students")
        records = self.cursor.fetchall()
        print("\n--- Current Student Records ---")
        for r in records:
            print(f"ID: {r[0]} | Name: {r[1]} | Branch: {r[2]} | CGPA: {r[3]}")

    def close(self):
        self.conn.close()

# --- Running the Project ---
if __name__ == "__main__":
    db = StudentDB("college.db")
    db.add_student("Muddam Karthik", "CSE", 7.6)
    db.show_all()
    db.close()