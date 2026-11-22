from flask import Flask, send_file, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    if os.path.exists("index.html"):
        return send_file("index.html")
    return "Sheru AI is Live!"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    msg = data.get("message", "")
    reply = f"Sheru AI: Maine suna - '{msg}'. Main abhi seekh raha hu, jaldi full AI ban jaunga!"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
