import requests
import time
import os
import uuid

if __name__ == "__main__":
    grafana_url = os.getenv("GRAFANA_URL", None)
    if not grafana_url:
        exit("GRAFANA_URL env variable must be set")
    

    grafana_username = os.getenv("GRAFANA_USERNAME", None)
    if not grafana_username:
        exit("GRAFANA_USERNAME env variable must be set")

    grafana_password = os.getenv("GRAFANA_PASSWORD", None)
    if not grafana_password:
        exit("GRAFANA_PASSWORD env variable must be set")
    
    grafana_ready = False
    while(not grafana_ready):
        time.sleep(1)
        response = requests.get(f"{grafana_url}/api/health")
        if response.status_code != 200:
            continue
            
        response_data = response.json()
        grafana_ready = response_data.get("database") == "ok"
    
    print("Grafana Ready!")
    response = requests.post(
        url=f'{grafana_url}/api/auth/keys', 
        auth=(grafana_username, grafana_password), 
        headers={'Content-Type': 'application/json'}, 
        json={
            "role": "Editor",
            "name": f"backup-and-restore-{uuid.uuid4()}"
        }
    )

    print(response.status_code)
    if response.status_code == 200:
        print("Writing key to file")
        file = open("/secrets/api_key", "w")
        file.write(response.json().get("key"))
        file.flush()
        file.close()


