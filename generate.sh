#!/usr/bin/env bash
set -euo pipefail
name=$1
expected_result=$2
day=$(ls input | grep -v test | cut -c 4- | sort -rn | head -1 | cat  <(echo "1") - | paste -sd+ | bc)
day=$(printf "%02d" $day)

echo "Creating new files for day ${day} with name ${name} and expected test result ${expected_result}"
touch input/day${day}
touch input/test_day${day}

sed 's/day_n/'${name}'/g' <src/dayN.py >src/day${day}.py
sed 's/day_n/'${name}'/;s/dayN/day'${day}'/;s/TestDayN/TestDay'${day}'/;s/999/'${expected_result}'/' <src/test/test_dayN.py >src/test/test_day${day}.py
