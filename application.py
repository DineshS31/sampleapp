from flask import Flask, jsonify

application = Flask(__name__)


@application.route('/')
def home():
	return "Welcome to Demo Project!"


@application.route("/health_check")
def health_check():
	return jsonify({
		"success": True,
		"status_code": 200
		})


if __name__ == '__main__':
	application.run()
