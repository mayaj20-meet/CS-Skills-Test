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

def update_lab_status(name, finished_lab):

   users_object = session.query(
       Student).filter_by(
       name=name).first()
   user_object.finished_lab = finished_lab
   session.commit()


def delete_user(their_name):

   session.query(User).filter_by(
       username=their_username).delete()
   session.commit()
