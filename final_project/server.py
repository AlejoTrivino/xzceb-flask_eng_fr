"""Server for translation from English to French and viceversa"""
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """English to French call"""
    textToTranslate = request.args.get('textToTranslate')
    return "Translated text to French: " + translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    """French to English call"""
    return "Translated text to English: " + translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    """Render Index.html page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
