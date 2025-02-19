#!/usr/bin/env bash

python3 -m venv myenv
source myenv/bin/activate
pip3 install scrapegraphai
python3 -m playwright install
