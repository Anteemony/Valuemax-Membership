from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, UserLoginForm, AdminLoginForm

#i added a comment
app = Flask(__name__)
app.config['SECRET_KEY'] = "0f3c34f7789f6917e12593945aa86bdb"

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def user_login():
  form = UserLoginForm()
  if form.validate_on_submit():
    if form.phone.data == "08012345678" and form.password.data == "1234":
      flash('You have been logged in!', 'success')
      return(redirect(url_for("home")))
    else:
      flash('Invalid credentials. Try again.', 'danger')

    
  return render_template("user_login.html", title="Login", form=form)

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
  form = AdminLoginForm()
  if form.validate_on_submit():
    if form.email.data == "admin@admin.com" and form.password.data == "admin1234":
      flash('You have been logged in!', 'success')
      return(redirect(url_for("admin")))
    else:
      flash('Invalid credentials. Try again.', 'danger')
  return render_template("admin_login.html", title="Admin Login", form=form)

#admin must be logged in for this route later on
@app.route("/admin/home")
def admin():
  return render_template("admin.html", title="Admin")

#admin must be logged in for this route later on
@app.route("/admin/register-member", methods=["GET", "POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f"Account created for {form.username.data} successfully", "success")
    return(redirect(url_for("admin/home")))
    
  return render_template("register.html", title="Register New Member", form=form)
  

if __name__ == "__main__":
  app.run(port='8080', host='0.0.0.0', debug=True)