from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health_check")
def health_check():
	return jsonify({
		"success": True,
		"status_code": 200
		})


if __name__ == '__main__':
	app.run()
