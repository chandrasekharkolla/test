from flask import Flask
test = Flask(__name__)
@test.route("/test")
def run():
    return "{\"message\":\"Hey there python from test\"}"

if __name__ == "__main__":
    test.run(host="0.0.0.0", port=int("80"), debug=True)