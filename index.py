from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/test")
def run():
    return "{\"message\":\"Hey there python from test\"}"

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("80"), debug=True)