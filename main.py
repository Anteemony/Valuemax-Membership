from flask import Flask, render_template

#i added a comment
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/login")
def login():
  return render_template("login.html", title="Login")

@app.route("/admin")
def admin():
  return render_template("admin.html", title="Admin")
  

if __name__ == "__main__":
  app.run(port='8080', host='0.0.0.0', debug=True)