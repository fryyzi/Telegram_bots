import psutil

battery = psutil.sensors_battery()

if battery:
    percent = battery.percent
    plugged = battery.power_plugged
    print(f"Battery percentage: {percent}%")
    print("Plugged in: Yes" if plugged else "Plugged in: No")
else:
    print("Battery information not available")
