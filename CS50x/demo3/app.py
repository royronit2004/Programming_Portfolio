from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials for demonstration (in production, use a secure authentication system)
users = [{'username': 'user1', 'password': 'password1'}]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the provided credentials are valid (in production, use a secure authentication system)
    if any(user['username'] == username and user['password'] == password for user in users):
        return redirect(url_for('survey'))
    else:
        return "Login failed. Please try again."

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        # Check if the username is already taken (in production, use a secure database)
        if any(user['username'] == new_username for user in users):
            return "Username is already taken. Please choose another."

        # Add the new user to the user list (in production, store user data securely)
        users.append({'username': new_username, 'password': new_password})
        return redirect(url_for('login'))

    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)