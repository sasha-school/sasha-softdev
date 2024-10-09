from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission


app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
#     print("***DIAG: request.args['username']  ***")
#     print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
#     print("***DIAG: request.args['username']  ***")
#     print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    method1 = request.method
    if request.method == 'POST':
        username = request.form['username']
        requesttype = "POST"
    else:
        username = request.args.get('username')
        requesttype = "GET"
    
    return render_template( 'response.html', username=username, request = requesttype )  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()