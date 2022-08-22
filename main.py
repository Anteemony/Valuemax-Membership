from flask import Flask, render_template, url_for

#i added a comment
app = Flask(__name__)
app.config['SECRET_KEY'] = "0f3c34f7789f6917e12593945aa86bdb"

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/login")
def user_login():
  return render_template("user_login.html", title="Login")

@app.route("/admin")
def admin_login():
  return render_template("admin_login.html", title="Admin Login")

#admin must be logged in for this route later on
@app.route("/admin/home")
def admin():
  return render_template("admin.html", title="Admin")

#admin must be logged in for this route later on
@app.route("/admin/register-member")
def register():
  return render_template("register.html", title="Register New Member")
  

if __name__ == "__main__":
  app.run(port='8080', host='0.0.0.0', debug=True)