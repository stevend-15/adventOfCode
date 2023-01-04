#!/bin/bash

#need to look at this line
pwd 
cd ~/coding_practice
pwd

today=$(date +%-d)
year=$(date +%y)
year4=$(date +%Y)

echo "today: $today, year: $year"
year_dir="aoc$year"
echo "year dir: $year_dir"

echo "four char year: $year4"

day_dir="day$today"
echo "day_dir: $day_dir"

py_file="day$today.py"
echo "py file:$py_file" 
pwd

#if the yearly folder doesn't exist, create it (ie on Dec 1 of each year)
if [ ! -d $year_dir ];then
    echo "creating dir $year_dir"
    mkdir $year_dir
else
    echo "$year_dir already exists"
fi 

#cd into yearly folder and create the daily folder
cd $year_dir
pwd
if [ ! -d $day_dir ];then
    mkdir $day_dir
    echo "created dir $day_dir"
else
    echo "$day_dir already exists"
fi 

#create the daily file
cd $day_dir
pwd
touch $py_file

#next, scrape the input file from the aoc website
#website="https://adventofcode.com/$year4/day/$today/input"
#echo -e "website: $website\n\n"

#wget --load-cookies aoc_cookies.txt -d -c $website -O input.txt

#next, push aoc code to github
