import os

GRAFANA_URL = os.getenv('GRAFANA_URL', 'http://localhost:3000')
TOKEN = os.getenv('GRAFANA_TOKEN', None)
if TOKEN is None:
    with open("/secrets/api_key", "r") as file:
        TOKEN = file.read()
print(TOKEN)
HTTP_GET_HEADERS = {'Authorization': 'Bearer ' + TOKEN}
HTTP_POST_HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'}
SEARCH_API_LIMIT = 5000
DEBUG = True
VERIFY_SSL = False
