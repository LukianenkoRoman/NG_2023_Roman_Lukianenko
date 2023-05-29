from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key"  
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

chat_messages = [] 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
      
        action = request.form.get("action")
        if action == "login":
            return redirect("/login")
        elif action == "register":
            return redirect("/register")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session["username"] = user.username
            return redirect("/chat")
        else:
            error_message = "Invalid username or password"
            return render_template("login.html", error_message=error_message)
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error_message = "Username already exists"
            return render_template("register.html", error_message=error_message)
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            session["username"] = new_user.username
            return redirect("/chat")
    return render_template("register.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "username" in session:
        if request.method == "POST":
            message = request.form.get("message")
            if message:
                sender = session["username"]
                chat_messages.append({"sender": sender, "message": message})
        return render_template("chat.html", username=session["username"], chat_messages=chat_messages)
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', port=80)

