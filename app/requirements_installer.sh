#!/bin/sh

#script is used to install all of the requirements
#if you can't run this script because you are on windos, please reconsider your os decisions. 

echo "I work with pip3. If you work with another installer, you are on your own. \n\n"

echo "Installing uvicorn ############################"
pip3 install uvicorn

echo "Installing qunicorn ###########################"
pip3 install gunicorn

echo "Installing pandas #############################"
pip3 install pandas

echo "Installing request ############################"
pip3 install requests

echo "Installing pycountry ##########################"
pip3 install pycountry

echo "Installing pytest #############################"
pip3 install pytest

echo "\n\nThank you for choosing this script. Leben Sie wohl."

