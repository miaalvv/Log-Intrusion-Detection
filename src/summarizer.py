import json
import os

def save_summary(suspicious_users, output_path="artifacts/release/summary.json"):
    os.makedirs("artifacts/release", exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(suspicious_users, f, indent=4)

    print(f"[INFO] Summary saved to {output_path}")
