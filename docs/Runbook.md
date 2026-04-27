## Runbook

### Prerequisites
- Docker Desktop installed and running
- Python 3.10+
- `make` installed

### Fresh Clone & Run
1. Clone the repository
```bash
   git clone <https://github.com/miaalvv/Log-Intrusion-Detection.git>
   cd Log-Intrusion-Detection
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Build and run the full system
```bash
   make up && make demo
```
   On Windows, run separately:
```bash
   make up
   make demo
```
the container will automatically exit after processing.
4. The system will automatically:
   - Parse logs from `data/logs.txt`
   - Detect suspicious login activity
   - Generate alerts
   - Output `artifacts/release/results.csv` and `artifacts/release/summary.json`

### Tear Down
```bash
make down
```
