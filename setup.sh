#!/bin/bash
echo "Setting up the wordle project!"

function report_result() {
    # Gets the return value `$?` of the last command and reports success or not
    if [ $? -eq 0 ]; then
        echo -e "Success."
    else
        echo -e "\nSomething went wrong! Bailing..."
        exit 1
    fi
}


# create a venv
echo "Creating a virtual environment..."
python -m venv venv

# venv
echo -e "\n*** Activating the python virtual environment for this script..."
OS=$(uname -a | cut -c1-5)
report_result
if [[ $OS =~ "Linux" ]]; then
    source ./venv/bin/activate
else
    source ./venv/Scripts/activate
fi
report_result
echo -e "Using: $(which python)"

# upgrade pip
echo -e "\n*** Updating pip to latest version...\n"
python -m pip install --upgrade pip
report_result

# pip install
echo -e "\n*** Installing latest Python requirements...\n"
python -m pip install -r requirements.txt
report_result

# Run wordle
echo "Running wordle..."
python main.py

