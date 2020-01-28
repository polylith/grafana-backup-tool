#!/bin/bash

set -e

trap 'echo -ne "\n:::\n:::\tCaught signal, exiting at line $LINENO, while running :${BASH_COMMAND}:\n:::\n"; exit' SIGINT SIGQUIT

current_path=$(pwd)

python src/restore_from_s3.py

tmp_dir="/tmp/restore_grafana.$$"
mkdir -p "$tmp_dir"
tar -xzf archive-latest.tar.gz -C $tmp_dir

for j in folder datasource dashboard alert_channel
do
	find ${tmp_dir} -type f -name "*.${j}" | while read f
	do
		python "${current_path}/src/create_${j}.py" "${f}"
	done
done

rm -rf $tmp_dir
