from attendance.attendance import mark_attendance
import time

def main():
    print("=== Bluetooth Attendance Tracking System ===")
    print("Press Ctrl+C to exit\n")

    try:
        while True:
            mark_attendance()
            user_input = input("\nPress Enter to take attendance again or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Exiting program")
                break
    except KeyboardInterrupt:
        print("\nExiting program")


if __name__ == "__main__":
    main()
