#!/usr/bin/env bash

python3 -m venv myenv
source myenv/bin/activate
pip3 install scrapegraphai==1.38.1
python3 -m playwright install
