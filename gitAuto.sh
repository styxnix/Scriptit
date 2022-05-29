#!/bin/sh
echo "Hello World1"
commitComment=""
echo "Hello World2"
git add .
echo "Hello World3"
read commitComment=
git commit -m "$commitComment"
git push
