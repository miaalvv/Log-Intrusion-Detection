## Setup Instructions

### Using Make
```bash
make bootstrap
```
### Manual Setup
```bash
pip install -r requirements.txt
```

## Run the System
### Mac/Linux
```bash
make up && make demo
```
the container will automatically exit after processing.

### Windows (PowerShell)
```bash
make up
make demo
```
the container will automatically exit after processing.

## Runbook
1. Clone the repository  
2. Run: make demo  
3. The system will:
   - Parse logs
   - Detect suspicious activity
   - Generate alerts
   - Output results to artifacts/release/

All outputs are saved automatically.
