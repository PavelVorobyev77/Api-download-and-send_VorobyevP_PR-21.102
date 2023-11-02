from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def returnUserInfo():
    id = int(request.args.get("id"))

    users = {
        1: {"name": "Alex", "age": 25, "city": "London"},
        2: {"name": "Max", "age": 28, "city": "Miami"},
        3: {"name": "Egor", "age": 15, "city": "LA"},
        4: {"name": "Anton", "age": 19, "city": "Las Vegas"},
        5: {"name": "Misha", "age": 22, "city": "Moscow"},
        6: {"name": "Petr", "age": 17, "city": "St.Petersburg"},
        7: {"name": "Pavel", "age": 33, "city": "Novosibirsk"},
    }

    return jsonify(users[id])


@app.route("/send/<filename>", methods=["GET"])
def send(filename):
    return send_from_directory("Files", filename)


@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    return send_from_directory("Files", filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
