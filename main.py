from flask import Flask
app = Flask(__name__)

@app.route("/")
def greet():
    return "Testing CI/CD"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4440"), debug=True)