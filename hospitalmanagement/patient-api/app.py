from flask import Flask, request, jsonify
from flask_cors import CORS
import MySQLdb
import MySQLdb.cursors
import time

app = Flask(__name__)
CORS(app)

# MySQL configuration
DB_CONFIG = {
    'host': 'mysql',  # Docker container name / network alias
    'user': 'user',
    'passwd': 'pass123',
    'db': 'hospital',
    'cursorclass': MySQLdb.cursors.DictCursor
}

# Helper function to get DB connection
def get_db_connection():
    return MySQLdb.connect(**DB_CONFIG)

# Create patients table if not exists, retrying until MySQL is reachable
def init_db(retries=30, delay=2):
    for attempt in range(1, retries + 1):
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS patients (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255),
                        age INT
                    )
                """)
                conn.commit()
            return
        except MySQLdb.OperationalError as e:
            print(f"DB not ready (attempt {attempt}/{retries}): {e}", flush=True)
            time.sleep(delay)
    raise RuntimeError("Could not connect to MySQL after multiple attempts")

init_db()

# Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
    return jsonify(patients)

# Add a patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        patient_id = cursor.lastrowid
    return jsonify({'id': patient_id, 'name': name, 'age': age})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
