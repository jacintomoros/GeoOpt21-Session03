# pip3.10 install deep-translator

from flask import Flask
import ghhops_server as hs
from deep_translator import GoogleTranslator

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/wordTranslate",
    name = "wordTranslate",
    inputs=[
        hs.HopsString("Word", "W", "Word to translate", hs.HopsParamAccess.ITEM)


    ],

    outputs=[
        hs.HopsString("Translation","T","Word translated"),

    ]
)
def translateWord(wtranslate):

    translated = GoogleTranslator(source='auto', target='english').translate(text=wtranslate)

    return translated


if __name__== "__main__":
    app.run(debug=True)
