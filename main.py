from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return "Welcome to Valuemax Communications. <a href='/login'>Click here</a> to login"

@app.route("/login")
def login():
  return "In progress"

@app.route("/admin")
def admin():
  return "In progress"
  

if __name__ == "__main__":
  app.run(port='8080', host='0.0.0.0', debug=True)