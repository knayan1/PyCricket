# PyCricket
Python program to fetch cricket score and display as windows notification

## Description
This is initial version of the program to fetch the match lists and the score of the selected match. It will notify scores every 30 seconds as windows notification.

## Requirements
1. win10toast
2. requests

## How to install
1. Clone this repository
```git clone git@github.com:knayan1/PyCricket.git```
2. Create virtual environment. You can skip this if don't want to work in virtual environment. ```mkvirtualenv cricket```
3. Install required modules ```pip install -r requirements.txt```
4. Execute script ```python cricket_score.py```

## Screenshot
![Screenshot of the program](https://raw.githubusercontent.com/knayan1/PyCricket/master/cricket_score.png)
## Things ahead
1. Make it generic to work on any platform
2. Make API call directly to the espn or cricinfo.

## Note:
Feel Free to fork and extend