#!/bin/bash

# Usage: ./zero-gzip-timestamp.sh < filename.gz > filename-with-no-timestamp.gz
#    Replaces the timestamp field in filename.gz by 0000 so the gzip file
#    contents do not depend on compression date

head -c 4
head -c 4 > /dev/null
printf '\00\00\00\00'
cat
