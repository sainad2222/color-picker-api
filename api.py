# ______________________IMPORTS__________________________
from helpers import dominant_color, border_color
from flask import Flask, jsonify, request
import urllib.request
import urllib.parse
import numpy as np
import cv2
import base64

app = Flask(__name__)


# ____________________ENDPOINT___________________________
@app.route("/")
def index():
    try:
        # cleaning URL
        url = request.args.get("src")
        if not url:
            return jsonify({"error": "Invalid url"})
        url = urllib.parse.quote(url)
        url = url.replace("%3A",":")
        res = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(res.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
        # calling helper functions
        border = border_color(img)
        dominant = dominant_color(img)
        return jsonify({"logo_border": border, "dominant_color": dominant})
    except Exception as e:
        print("[ERROR]", e)
        return jsonify({"error": "Unknown Error"})


if __name__ == "__main__":
    app.run()
