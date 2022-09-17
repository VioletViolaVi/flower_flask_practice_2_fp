from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/flowers", methods=["GET"])
def flowers():
    flowers = [
        {"id": 1, "name": "Rose", "colour": "red", "need_water": True},
        {"id": 2, "name": "Lily", "colour": "white", "need_water": False},
        {"id": 3, "name": "Tulip", "colour": "purple", "need_water": True},
        {"id": 4, "name": "Sunflower", "colour": "yellow", "need_water": True},
        {"id": 5, "name": "Orchid", "colour": "orange", "need_water": False},
    ]
    return render_template("flowers.html", page_title="My Flowers List", flowers=flowers)


@app.route("/flowers/new", methods=["GET", "POST"])
def new_flower():
    if request.method == "GET":
        return "This route works for POST requests"
    else:
        data = request.get_json()
        if data["colour"] != "invisible":
            return "This is a real flower", 201
        else:
            return "Nah...", 400


# ignored in testing
if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True)
