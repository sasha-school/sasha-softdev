# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...") # print "about to print __name__..." to terminal
    print(__name__)               #where will this go? =-----prints "__main__"to terminal
    return "No hablo queso!"    #site looks the same etc

app.run()

