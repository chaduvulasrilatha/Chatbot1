from flask import Flask, request , render_template
from google import genai

client = genai.Client(api_key="AIzaSyC7EjAgMh66lhxiCWHLmSW0BH_cD9v3yHAp")

app = Flask(__name__)

@app.route("/" )
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.json["msg"]
    ).text

app.run(port=5002)