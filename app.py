from flask import flask
app = flask(__name__)
@app.route("/")
def home():
    return "hello, flask!"
if __name__== "__main__":
    app.run(debug=true)
     