# World Cup 2026 Countdown

This is a Python script that calculates the remaining time until the World Cup 2026 and returns the result in a JSON format.

## Prerequisites

To run this script, you need to have Python 3 and Flask installed in your system.

You can check if you have Python 3 installed by running the following command:

`python3 --version`

If you don't have Python 3 installed, you can install it by running:

`sudo apt-get update`
`sudo apt-get install python3`

To install Flask, you need to have pip (Python package manager) installed. If you don't have pip installed, you can install it by running:

`sudo apt-get update`
`sudo apt-get install python3-pip`

Once you have pip installed, you can install Flask by running:

`pip3 install flask`

## Installation

To install this script, follow these steps:

1. Clone this repository:

`git clone https://github.com/zingaya/worldcup2026countdown.git`

2. Navigate to the directory:

`cd worldcup2026countdown`

## Execution

To run this script, execute the following command:

`python3 worldcup2026countdown.py`

The script will start a local server at port 18080. To see the countdown, open your browser and go to http://localhost:18080/.

## In case of error

If you get an error saying that Python or pip are not recognized as commands, it means that they are not in your PATH.

To add Python to your PATH, add the following line to your .bashrc file (located in your home directory):

`export PATH=$PATH:/usr/local/bin`

To add pip to your PATH, add the following line to your .bashrc file:

`export PATH=$PATH:/usr/local/pip/bin`

Don't forget to source your .bashrc file after adding these lines:

`source ~/.bashrc`

#

Created with the help of OpenAI.

