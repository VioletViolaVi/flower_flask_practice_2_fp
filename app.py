from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)
