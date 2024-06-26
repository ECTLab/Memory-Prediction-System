# Memory Harvesting System for Linux Operating System

## Overview

The Memory Harvesting System is designed to monitor and predict memory usage in Linux environments. This system includes a Go-based agent for collecting and analyzing memory data from virtual machines managed by the KVM virtualizer, using the Libvirt library. Key functionalities include:

- Monitoring running virtual machines, allocated memory, and current memory consumption.
- Predicting memory usage based on recent consumption trends.
- Reporting memory harvesting data to system managers.
- Recording and managing memory usage violations.
- Visualizing data with Prometheus and Grafana.

The server side is implemented in Python with the Flask framework and uses an SQLite database for data storage. It manages agent registrations, boundary settings, and violation data.

## Features

- **Memory Monitoring:** Tracks number of running VMs, allocated memory, and momentary memory consumption (RSS).
- **Prediction:** Uses recent memory consumption to predict near-future usage.
- **Harvesting:** Calculates and reports differences between allocated and predicted memory.
- **Violation Management:** Logs instances where actual memory consumption exceeds predictions.
- **Visualization:** Integrates with Prometheus and Grafana for data visualization.
- **Server Management:** Flask-based server to manage agents, boundaries, and violations.

## Installation

### Agent (prometheus-libvirt-exporter.go)

To install and run the Go-based agent:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/memory-harvesting.git
   cd memory-harvesting
   ```

2. **Install Dependencies:**
   Ensure you have Go installed. Then, run:
   ```sh
   go mod tidy
   ```

3. **Run the Agent:**
   ```sh
   go run prometheus-libvirt-exporter.go
   ```

### Server (Flask Application)

To set up and run the Flask-based server:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/memory-harvesting-server.git
   cd memory-harvesting-server
   ```

2. **Set Up Virtual Environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Server:**
   ```sh
   flask run
   ```

## Directory Structure

### Agent

- `prometheus-libvirt-exporter.go`: Main agent code file.

### Server

- `./static`: Static files.
- `./static/back.jpg`: Background image.
- `./instance`: Instance-specific files.
- `./instance/vms.db`: SQLite database.
- `./app.py`: Main server application file.
- `./templates`: HTML templates.
- `./templates/index.html`: Main HTML template.

## Usage

Once the agent and server are running, memory data will be collected and sent to Prometheus. You can then visualize the data in Grafana and manage configurations via the Flask web interface.

## Contributing

Feel free to contribute by submitting issues or pull requests. Please ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

|A|B|C|
|-|-|-|
|Installation Issues|Usage Examples|Contribution Guidelines|
