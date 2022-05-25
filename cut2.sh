#! /bin/bash

myfile=/Users/rijayaturazak/Documents/GitHub/Class-Projects/cut1.txt 
while read line || [ -n "$line" ];
do
    echo "$line";
done < $myfile | cut -c1-4 $myfile 