from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World, I'm running on Openshift, now with an updated message"

if __name__ == "__main__":
    application.run()
