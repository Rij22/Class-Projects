#! /bin/bash
myfile=/Users/rijayaturazak/Documents/GitHub/Class-Projects/cut7.txt 


while read line || [ -n "$line" ];
do
    echo "$line";
    done < $myfile | cut -d ' ' -f 3-5



# cut1.txt
