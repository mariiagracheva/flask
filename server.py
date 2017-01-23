from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
import locale


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

JOBS = ['', 'Software Engineer', 'QA Engineer', 'Product Manager']

# YOUR ROUTES GO HERE
@app.route("/")
def start():
    """Home page, template index.html"""
    return render_template("index.html")


@app.route("/application-form")
def form():
    """Application form page"""
    return render_template("application-form.html", jobs=JOBS)


@app.route("/application-success", methods=["POST"])
def success():
    """Summary from submitted application form"""
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    salary = locale.currency(int(request.form.get('salary')), symbol=True, grouping=True)
    job = request.form.get('job')
    if firstname == "" or lastname == "" or salary == "" or job == "":
        return render_template("application-form.html", jobs=JOBS)
    else:
        return render_template("application-response.html",
                                firstname=firstname,
                                lastname=lastname,
                                salary=salary,
                                job=job)
    
        


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
