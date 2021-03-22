#!/bin/bash
FOLDER=$(dirname "$BASH_SOURCE")
cd "$FOLDER"
set -e
help="./run.sh lecture|hw <number>"

commands=("lecture" "hw")

if [ -z "$1" ]; then
	echo "error: No type supplied"
	echo $help
	exit 1
fi

if [ -z "$2" ]; then
	echo "error: No number supplied"
	echo $help
	exit 1
fi

if [[ ! " ${commands[@]} " =~ " $1 " ]]; then
	echo "error: Command not found"
	echo $help
	exit 1
fi

re='^[0-9]+$'
if ! [[ $2 =~ $re ]] ; then
	echo "error: Second argument not a number"
	echo $help
	exit 1
fi

wget https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html --no-check-certificate --convert-links -O temp.html &> /dev/null
cp -f temp.html notes.html

echo $2 | python $1.py
cmd.exe /C start output.html
