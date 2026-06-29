import serial
import matplotlib.pyplot as plt
import time
import csv

# CHANGE THIS to your Arduino port
arduino = serial.Serial('/dev/cu.usbserial-1420', 9600)

time.sleep(2)  # let connection settle

values = []

plt.ion()  # interactive mode ON
fig, ax = plt.subplots()

file = open("dark_sensor.csv","w", newline="")
writer = csv.writer(file)
writer.writerow(["sample","value"])
i=0

while True:
    try:
        line = arduino.readline().decode().strip()

        if line.strip().isdigit():
            value = int(line)
            values.append(value)

            writer.writerow([i,value])
            i+=1

            # keep last 50 values only
            if len(values) > 50:
                values.pop(0)

            ax.clear()
            ax.plot(values)

            ax.set_title("LDR Live Graph")
            ax.set_xlabel("Time")
            ax.set_ylabel("Sensor Value (0–1023)")
            ax.set_ylim(0, 1023)

            plt.pause(0.1)

    except KeyboardInterrupt:
        print("Stopped by user")
        break


arduino.close()
file.close()
plt.savefig("dark_sensor.png")