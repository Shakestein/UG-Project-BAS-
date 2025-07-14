import csv
import os
import datetime

def read_students_csv(filepath='data/students.csv'):
    students = {}
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students[row['MAC'].strip().upper()] = row['Name'].strip()
    except Exception as e:
        print(f"Error reading student CSV: {e}")
    return students

def save_attendance_to_csv(attendance, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = os.path.join(output_dir, f"attendance_{date_str}.csv")

    try:
        file_exists = os.path.exists(filename)
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['Timestamp', 'Student', 'Present']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for student, present in attendance.items():
                writer.writerow({
                    'Timestamp': timestamp,
                    'Student': student,
                    'Present': 'Yes' if present else 'No'
                })
        print(f"\nAttendance saved to {filename}")
    except Exception as e:
        print(f"Error saving attendance to CSV: {e}")
