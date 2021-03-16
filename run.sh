#!/bin/bash
FOLDER=$(dirname "$BASH_SOURCE")
cd "$FOLDER"
set -e
wget https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html --no-check-certificate --convert-links -O temp.html &> /dev/null
cp -f temp.html notes.html
help="./run.sh lecture-number"
if [ -z "$1" ]; then
	echo "error: No homework number supplied"
	echo $help
	exit 1
fi

re='^[0-9]+$'
if ! [[ $1 =~ $re ]] ; then
	echo "error: First argument not a number"
	echo $help
	exit 1
fi
echo $1 | python main.py
cmd.exe /C start output.html
