from flask import Flask, render_template
import json

app = Flask(__name__)
posts=[
    {
        "name": "mritunjay",
        "age": 30
    }
    ,
     {
        "name": "rakhi",
        "age": 20
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    data = posts
    response = app.response_class(
        response=json.dumps(posts, indent=2, sort_keys=True),
        status=200,
        mimetype='application/json'
        )
    return response


if __name__ == '__main__':
    app.run(debug=True, port=2000)