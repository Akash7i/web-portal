from flask import Flask, render_template, request, redirect, url_for, session 

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Student data
students_data = {
    "710123243004": {"name": "AKASHKUMAR P", "grades": {"BS3171": "O", "CY3151": "A", "GE3151": "B+", "GE3152": "B+", "GE3171": "A+", "GE3172": "A+", "HS3152": "B+", "MA3151": "A+", "PH3151": "A"}},
    "710123243002": {"name": "ABHISHEK DALLAS", "grades": {"BS3171": "O", "CY3151": "A", "GE3151": "B+", "GE3152": "B+", "GE3171": "A+", "GE3172": "A+", "HS3152": "A", "MA3151": "A+", "PH3151": "A"}},
    "710123243023": {"name": "HARIHARAN R", "grades": {"BS3171": "A+", "CY3151": "U", "GE3151": "U", "GE3152": "B+", "GE3171": "A+", "GE3172": "A+", "HS3152": "B+", "MA3151": "B+", "PH3151": "U"}},
    "710123243017": {"name": "GEORGE KIPSON", "grades": {"BS3171": "O", "CY3151": "B+", "GE3151": "B", "GE3152": "B+", "GE3171": "A+", "GE3172": "A+", "HS3152": "B", "MA3151": "B+", "PH3151": "B+"}},
    "710123243059": {"name": "SUNIL S", "grades": {"BS3171": "O", "CY3151": "A", "GE3151": "A+", "GE3152": "B+", "GE3171": "A+", "GE3172": "A+", "HS3152": "B+", "MA3151": "A", "PH3151": "A+"}},
    "710123243049": {"name": "RAGUL S", "grades": {"BS3171": "A+", "CY3151": "U", "GE3151": "B", "GE3152": "C", "GE3171": "A+", "GE3172": "A+", "HS3152": "U", "MA3151": "U", "PH3151": "U"}},
    "710123243048": {"name": "RAGUL S", "grades": {"BS3171": "A+", "CY3151": "A", "GE3151": "B+", "GE3152": "B", "GE3171": "A+", "GE3172": "A+", "HS3152": "U", "MA3151": "A", "PH3151": "B+"}},
    "71012324304": {"name": "PRAVEEN KS", "grades": {"BS3171": "A+", "CY3151": "B+", "GE3151": "B+", "GE3152": "B+", "GE3171": "A+", "GE3172": "A+", "HS3152": "B", "MA3151": "B+", "PH3151": "B+"}}
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        reg_no = request.form["reg_no"]
        if reg_no in students_data:
            session["reg_no"] = reg_no  # Store in session
            return redirect(url_for("result"))
        else:
            error = "Invalid Register Number!"
            return render_template("login.html", error=error)
    
    return render_template("login.html")

@app.route("/result")
def result():
    reg_no = session.get("reg_no")  
    if not reg_no or reg_no not in students_data:  
        return redirect(url_for("login"))  # Redirect if not logged in
    
    student = students_data[reg_no]
    return render_template("index.html", student=student)

@app.route("/logout")
def logout():
    session.pop("reg_no", None)  
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
