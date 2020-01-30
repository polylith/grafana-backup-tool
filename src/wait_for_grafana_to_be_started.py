import requests
import time
import os


if __name__ == "__main__":
    grafana_url = os.getenv("GRAFANA_URL", None)
    if not grafana_url:
        exit("GRAFANA_URL env variable must be set")
    
    grafana_ready = False
    while(not grafana_ready):
        time.sleep(1)
        response = requests.get(f"{grafana_url}/api/health")
        if response.status_code != 200:
            continue
            
        response_data = response.json()
        grafana_ready = response_data.get("database") == "ok"
    
    print("Grafana Ready!")