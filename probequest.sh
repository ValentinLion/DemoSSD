#!/bin/bash

sudo airmon-ng start wlan0
sudo probequest -i wlan0mon -o result.csv
