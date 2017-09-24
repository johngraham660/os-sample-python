from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    message = "Hello World, I'm running on Openshift, now with an updated message"
    return message

if __name__ == "__main__":
    application.run()
