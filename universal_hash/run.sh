#!/bin/bash

timestamp(){
        date "+%s"
}
for i in {1..10}
do

	 : > time_$i.txt
	timestamp >> time_$i.txt
	python3 main.py -n $i
	timestamp >> time_$i.txt
done
