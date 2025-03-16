from flask import Flask, request, jsonify, render_template
import torch
from flask_cors import CORS
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)
CORS(app)

# Selección del modelo de traducción inglés-español
model_name = "Helsinki-NLP/opus-mt-en-es"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Página de inicio (opcional: puedes crear una plantilla HTML en la carpeta "templates")
@app.route("/")
def home():
    return render_template("translate.html")

# Endpoint para traducir
@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    if "text" not in data:
        return jsonify({"error": "Missing 'text' parameter"}), 400
    
    text = data["text"]
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
