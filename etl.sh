#!/bin/bash
#
#
export option=$1
export ftp_file=$2
export location_file=$3
export data_file=$4
#

usage(){
	echo "Usage: etl.sh [new|append] ftp_file location_file data_file"
}
if [ $# -ne 4 ]
then
	usage
	exit 1
fi

location=$(sed -n 1p $ftp_file)
lat_long_ele=$(sed -n 2p $ftp_file)
data=$(tail -n +3 $ftp_file)



if [ $option == "new" ]; then
	echo $ftp_file $location $lat_long_ele > $location_file
	echo $data > $data_file
elif [ $option == "append" ]; then
	echo $ftp_file $location $lat_long_ele >> $location_file
	echo $data >> $data_file
else
	usage
fi
	
