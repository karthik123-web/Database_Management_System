import sqlite3
import logging
import sys

# Setup Professional Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StudentSystem:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('enterprise_data.db')
            self.cursor = self.conn.cursor()
            self.migrate_tables()
            logging.info("Database Connection Established.")
        except sqlite3.Error as e:
            logging.error(f"Database Init Failed: {e}")
            sys.exit()

    def migrate_tables(self):
        """Creates the schema if it doesn't exist."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT NOT NULL, 
             branch TEXT, 
             cgpa REAL CHECK(cgpa <= 10.0))''')
        self.conn.commit()

    def add_record(self, name, branch, cgpa):
        """Adds a student with data validation."""
        try:
            if not name or cgpa < 0:
                raise ValueError("Invalid Data Input")
            self.cursor.execute("INSERT INTO students (name, branch, cgpa) VALUES (?, ?, ?)", (name, branch, cgpa))
            self.conn.commit()
            print(f"\n SUCCESS: Record created for {name}")
        except Exception as e:
            print(f"\n ERROR: Could not add record. {e}")

    def fetch_analytics(self):
        """Advanced query to show analytics instead of just a list."""
        print("\n" + "="*40)
        print("SYSTEM ANALYTICS & STUDENT RECORDS")
        print("="*40)
        self.cursor.execute("SELECT * FROM students ORDER BY cgpa DESC")
        rows = self.cursor.fetchall()
        
        print(f"{'ID':<5} | {'NAME':<20} | {'BRANCH':<10} | {'CGPA':<5}")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<10} | {row[3]:<5}")
        print("="*40)

# --- Simulation of Heavy Logic ---
if __name__ == "__main__":
    system = StudentSystem()
    
    # Adding your real profile data
    system.add_record("Muddam Karthik", "CSE", 7.6) #
    system.add_record("External User", "ECE", 8.2)
    
    # Show professional output
    system.fetch_analytics()
