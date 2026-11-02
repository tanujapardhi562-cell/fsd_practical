
from flask import Flask, render_template,flash,request
import psycopg2

app = Flask(__name__)
app.secret_key = "my_secret_key" 

def db_connect():
    conn = psycopg2.connect(
        dbname="fsd_project",
        user="postgres",
        password="Tanuja@1106",
        host="localhost",
        port="5432"
    )
    return conn


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        if not name or not email or not password:
            flash("Please fill all fields.")

        conn = db_connect()
        cur = conn.cursor()

        cur.execute(
            """create table if not exists users( 
                        Name VARCHAR(100),
                        email VARCHAR(100),
                        password varchar(100));
                """)
        

        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )

        conn.commit()
        cur.close()
        conn.close()

        return render_template("dashboard.html", name=name)
    return render_template("registration.html")       

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return render_template("dashboard.html")

    return render_template("login.html")

    return render_template("login.html")
@app.route("/dashboard")
def dashboard():
    

    return render_template(
        "dashboard.html",
        
    )
@app.route("/logout")
def logout():
    return render_template("login.html")

if  __name__ == "__main__":
    app.run(debug=True)
