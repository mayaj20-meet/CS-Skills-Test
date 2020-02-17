@app.route('/login')
def login():
    Return render_template("hometest.html")

def add_user(username,email,password):
    user = User(
            username=username,
            email=email,
            password = password,
            )
    session.add(user)
    session.commit()

def signup():
		Username = request.form['Username']
		Email = request.form['Email']
		Password = request.form['Password']
		add_user(Username,Email,Password)
		return render_template ('hometest.html')

def delete_user_by():
    return session.query().delete()