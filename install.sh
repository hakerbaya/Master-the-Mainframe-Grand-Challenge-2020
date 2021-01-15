#!/bin/bash
# Author: Mubashir Ahmad
# Github: hakerbaya

# Script Usage:
# ____________
# This script runs the basic set-up to ensure everything runs well and good
# Ensure you have ZOAU installed in USS: https://www.ibm.com/support/knowledgecenter/en/SSKFYE_1.0.1/install.html

echo "Checking required files"
file="requirements.txt"
script_dir="$( cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 ; pwd -P )"

# Check if requirements.txt exists
if [[ -e "$script_dir/$file" ]] && [[ -s "$script_dir/$file" ]]; then
  echo "Downloading pip modules"
  pip3 install -r "$script_dir/$file"
fi