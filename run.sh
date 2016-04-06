#!/bin/bash
set -eu

if [ $# -ne 1 ]
then
    echo "Usage: $0 <images_directory>"
    exit 1
fi

cd $(dirname $0)

images_directory="$1"

if [ ! -d "$images_directory" ]
then
    echo "Directory does not exist: $images_directory"
    exit 2
fi

rm -rf app/static
ln -s "$1" app/static
./env/bin/python run.py
