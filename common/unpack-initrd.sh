#!/bin/bash

INITRD_PATH=$1
INITRD_TMP_DIR={$2:=/tmp/initrd}

if [ -z "$1" ]; then
  echo "`basename $0` /boot/initrd-2.6.32-100.24.1.el5.img [WORKING_TEMP_DIR]"
  exit 1
fi

INITRD_NAME=`basename $INITRD_PATH`

mkdir -p $INITRD_TMP_DIR
cp -f $INITRD_PATH $INITRD_TMP_DIR

cd $INITRD_TMP_DIR
mv ./$INITRD_NAME initrd.gz
gunzip initrd.gz

mkdir -p ./tmp
cd ./tmp
cpio -id < ../initrd

echo "Check under $INITRD_TMP_DIR"
