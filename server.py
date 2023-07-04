from flask import Flask, render_template, request, redirect, session

# The session is the interval at which the client logs on to the server and logs out the server. The data that is required to be saved in the session is stored in a temporary directory on the server.

app = Flask(__name__)

app.secret_key = "Keep this phrase private" # set a secret key for security purposes


@app.route('/')
def index():
    if "click" not in session:
        session['click'] = 0
    else:
        session['click'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def increment_by_two():
    if "click" not in session:
        session['click'] = 0
    else:
        session['click'] += 1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

