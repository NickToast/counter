from flask import Flask, render_template, redirect, session, request  # Import Flask to allow us to create our app, if u need render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'life' 	#key goes into here

@app.route('/')
def home():
    if 'counter' in session:        #if this key is in this session dictionary, add one to the counter
        session['counter'] += 1
    else:                           #if not, set a key in session dictionary to 'counter' and set the
        session['counter'] = 1      #value of that key to 1
    if 'visit value' in session:
        session['visit value'] += 1
    else:
        session['visit value'] = 1
    return render_template('index.html')

@app.route('/add2')
def add_two_visits():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/incrementby', methods=['POST'])
def increment():
    session['counter'] += int(request.form['incrementby'])
    session['counter'] -= 1
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.