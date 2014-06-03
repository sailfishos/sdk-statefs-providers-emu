#!/bin/bash

s="/run/state/namespaces/Battery/"

mkdir -p $s

echo "100" > $s"Capacity"
echo "100" > $s"ChargePercentage"
echo "0" > $s"IsCharging"
echo "0" > $s"LowBattery"
echo "1" > $s"OnBattery"
echo "0" > $s"TimeUntilFull"
echo "0" > $s"TimeUntilLow"

chown nemo:nemo $s*

