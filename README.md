# Dark Sensor using Arduino and Python

A simple data acquisition project that uses an Arduino Uno and a Light-Dependent Resistor (LDR) to measure ambient light intensity. The sensor readings are transmitted to Python via serial communication, visualized in real time with Matplotlib, and logged to a CSV file for further analysis. 

---

## Project Overview

### Hardware Setup

![Hardware Setup](set-up.jpeg)

### Live Sensor Graph

![Live Graph](dark_sensor.png)

---

## Features

- 📡 Reads real-time light intensity using an LDR and Arduino Uno
- 🔄 Transfers sensor data to Python via serial communication
- 📈 Displays a live graph using Matplotlib
- 💾 Saves sensor readings to a CSV file
- 📊 Exports the graph as a PNG image

---

## Components Used

### Hardware
- Arduino Uno
- LDR (Light Dependent Resistor)
- LED
- 220 Ω resistor
- 10 kΩ resistor
- Breadboard
- Jumper wires

### Software
- Arduino IDE
- Python 3
- PySerial
- Matplotlib
- CSV module

---

## How It Works

1. The Arduino continuously reads the analog value from the LDR.
2. The sensor readings are transmitted to the computer through serial communication.
3. A Python script reads the incoming data.
4. The data is plotted in real time using Matplotlib.
5. The readings are stored in a CSV file for future analysis.
6. When the program stops, the graph is saved as an image.

---

## Repository Structure

```
dark-sensor-arduino-python/
│
├── dark_sensor.ino      # Arduino code
├── dark_sensor.py       # Python script
├── dark_sensor.csv      # Sample logged data
├── dark_sensor.png      # Output graph
├── setup.jpg            # Hardware setup
├── demo.mp4             # Project demonstration
└── README.md
```

---

## Getting Started

### Hardware

- Connect the LDR and LED to the Arduino Uno as shown in the hardware setup image.
- Upload `dark_sensor.ino` using the Arduino IDE.

### Software

Install the required Python library:

```bash
pip install pyserial matplotlib
```

Run the Python script:

```bash
python dark_sensor.py
```

---

## Debugging Experience

- Incorrect resistor values led to LED failures, highlighting the importance of current limiting in circuits
- Initial wiring mistakes caused unstable readings in the LDR circuit
- Serial output required debugging due to inconsistent data formatting
- Learned to verify connections step-by-step before powering the circuit
  
---

## Challenges Faced
Managing noise in analog sensor readings from LDR
Selecting an appropriate threshold for light/dark detection
Ensuring stable serial communication between Arduino and Python
Handling inconsistent or delayed serial input during initial setup
Preventing graph flickering in real-time visualization

---

## What I Learned
Working of voltage divider circuits in analog sensing
Interfacing Arduino with Python using serial communication
Real-time data visualization techniques
Basics of data logging using CSV files
Debugging hardware-software integration issues

---

## Future Improvements

- Add a moving average filter for smoother visualization
- Save data with timestamps
- Build a real-time dashboard
- Extend the project to physiological sensors such as PPG

---

## Author

**Aadyaa Mehrotra**
