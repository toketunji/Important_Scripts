#!/bin/bash

mkdir /tmp/dump/old
cd 
mkdir logging && cd logging
dd if=/dev/zero of=app.txt bs=1024 count=0 seek=$[1024*10]
dd if=/dev/zero of=bi_access.txt bs=1024 count=0 seek=$[1024*2]
dd if=/dev/zero of=bi_error.log bs=1024 count=0 seek=$[1024*3]
dd if=/dev/zero of=init.log bs=1024 count=0 seek=$[1024*20]
dd if=/dev/zero of=answer.log bs=1024 count=0 seek=$[1024*20]


touch -d 20170101 answer.log
touch -d 20170101 bi_access.txt
touch -d 20170513 init.log
