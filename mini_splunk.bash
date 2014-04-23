#!/bin/bash

# check if the user provided logfile
if [ -z $1 ]; then
    echo "No logfile provided. Usage: $0 logfile string"
        exit 2
    fi 

if [ -z $2 ]; then
    echo "No search string provided. Usage: $0 logfile string"
        exit 2
    fi 




grep $2 $1 | sort -r
