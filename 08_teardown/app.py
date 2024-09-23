# your heading here

'''
DISCO:
<note any discoveries you made here... no m-atter how small!>

QCC:
0. without activating the virtual environment, the code will not run because flask is not a built in python3 module
1. c is an @ suppresor
2. when it is just run, there is an error: "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead."
3. when link is clicked, empty web[page with "no hablo queso"
4. must be run in virtual environment
5. how to include user input in such a program?
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? c has the @ symbol that suppresses prints

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'? directory navigation
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print? "No hablo queso!" to the terminal
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


