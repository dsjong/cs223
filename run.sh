set -e
help="./run.sh lecture_number"
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
