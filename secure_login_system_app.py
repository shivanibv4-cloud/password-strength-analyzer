from flask import Flask, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"


def create_database():
    conn = sqlite3.connect("users.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    if "username" in session:
        return f"""
        <h2>Welcome, {session['username']}!</h2>
        <a href="/logout">Logout</a>
        """
    return """
    <h2>Secure Login System</h2>
    <a href="/register">Register</a><br><br>
    <a href="/login">Login</a>
    """


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or len(password) < 8:
            return "Enter a username and a password of at least 8 characters."

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect("users.db")
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
            conn.close()
            return redirect("/login")
        except sqlite3.IntegrityError:
            return "Username already exists."

    return """
    <h2>Register</h2>
    <form method="post">
        Username: <input name="username" required><br><br>
        Password: <input name="password" type="password"
        minlength="8" required><br><br>
        <button type="submit">Register</button>
    </form>
    """


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        user = conn.execute(
            "SELECT username, password FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            session.clear()
            session["username"] = user[0]
            return redirect("/")

        return "Invalid username or password."

    return """
    <h2>Login</h2>
    <form method="post">
        Username: <input name="username" required><br><br>
        Password: <input name="password" type="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    create_database()
    app.run(debug=False)