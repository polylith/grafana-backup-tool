#!/bin/bash

python src/wait_for_grafana_to_be_started.py

echo "Resotring grafana"
./restore_grafana.sh

while :
do
  echo "Backing up grafana"
  ./backup_grafana.sh
  sleep 300
done
