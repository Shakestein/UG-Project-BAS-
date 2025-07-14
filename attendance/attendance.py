import datetime
from .scanner import scan_for_duration
from .csv_handler import read_students_csv, save_attendance_to_csv

def mark_attendance():
    print("\n=== Taking Attendance ===")
    print(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    students = read_students_csv()
    detected_devices = scan_for_duration()

    attendance = {name: False for name in students.values()}
    present_count = 0

    for mac_address in detected_devices.keys():
        mac_upper = mac_address.upper()
        if mac_upper in students:
            student_name = students[mac_upper]
            attendance[student_name] = True
            present_count += 1
            print(f"✓ Marked {student_name} as present (MAC: {mac_address})")

    print("\n=== Attendance Report ===")
    print(f"Total students: {len(students)}")
    print(f"Present: {present_count}")
    print(f"Absent: {len(students) - present_count}")
    
    print("\nPresent Students:")
    for name, present in attendance.items():
        if present:
            print(f"- {name}")

    save_attendance_to_csv(attendance)
    return attendance
