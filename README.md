# Log-Intrusion-Detection

## Project Overview
This project is a log-based intrusion detection system that analyzes system logs to detect suspicious activity, such as repeated failed login attempts or unusual user behavior. The goal is to identify potential security threats early and provide alerts for further investigation.
## Features
- Analyzes system log data
- Detects suspicious patterns (e.g., multiple failed logins)
- Generates alerts for potential threats
- Modular design for easy updates and scalability
## System Architecture
The system follows a modular architecture with separate components for log reading, parsing, detection, and alert generation. This allows each part of the system to be developed and tested independently.
## Repository Structure
- `data/` – Contains sample log files
- `src/` – Core system modules (log reader, parser, detector, alert)
- `tests/` – Test files for validating system behavior
- `docker-compose.yml` – Container setup for reproducibility
- `Makefile` – Commands for setup and running the project
## Setup Instructions
To set up the project, run:
```
make bootstrap
```
## Run the System
To run the system, use:
```
make run
```
## Testing
To run tests, use:
```
make test
```

