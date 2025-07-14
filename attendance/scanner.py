import bluetooth

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    try:
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
        devices = {addr: name for addr, name in nearby_devices}
        print(f"Found {len(devices)} devices")
        return devices
    except Exception as e:
        print(f"Error scanning for Bluetooth devices: {e}")
        return {}

def scan_for_duration(duration_seconds=60, interval_seconds=5):
    import time
    start_time = time.time()
    end_time = start_time + duration_seconds
    all_detected_devices = {}
    scan_count = 0

    while time.time() < end_time:
        scan_count += 1
        print(f"\nScan #{scan_count} (Remaining time: {int(end_time - time.time())} seconds)")
        devices = scan_bluetooth_devices()
        all_detected_devices.update(devices)

        if time.time() + interval_seconds < end_time:
            print(f"Waiting {interval_seconds} seconds before next scan...")
            time.sleep(interval_seconds)
        else:
            break

    print(f"\n=== Scan session completed ({scan_count} scans performed) ===")
    return all_detected_devices
