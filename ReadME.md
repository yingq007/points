INTRODUCTION
---------------------
This project if for fetch rewards takehome assignment. It is used to track points in user's account. 
When spend points, following the two rules:
1. Spend the oldest points first
2.No payer's points to go negative
This project can add points to user's profile, spend points based on the two rules and show balance after spending points.

REQUIREMENTS
---------------------
To run the code, Python must be installed (Python 3.8.9).
Below are requiements in requiements.txt that need to be installed before running the code:
Flask==2.0.1
a virturl enviornment is also created 

RUNNING THE SCRIPT
---------------------
1. Create a virtual enviornment, in the terminal, run:
virtualenv env
source env/bin/activiate
2. Install this porject's dependencies from requirment.txt, in the terminal, run:
pip3 install-r requirements.txt
3. Start the Server:
Run track_points.py
open http://localhost:5000 in your browser
4.  Type in any payer, points and time to test the add points function
    Type in any points in spend points to test the spend points function
    Click on show balance button to test the show balance function
    They results will also be printed to the terminal
5. Run test.py to test the functions in track_points.py
