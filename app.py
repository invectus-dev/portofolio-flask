from flask import Flask, render_template, request, redirect
from models import db, Feedback

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    feedbacks = Feedback.query.all()
    return render_template("index.html", feedbacks=feedbacks)

@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        rating = int(request.form["rating"])

        new_feedback = Feedback(name=name, message=message, rating=rating)
        db.session.add(new_feedback)
        db.session.commit()

        return redirect("/")
    
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)