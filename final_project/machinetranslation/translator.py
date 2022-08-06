"""This test check the functionality of the translador from french to english and viceversa"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator("TChzmDRK096B8_eltjjXHIk6i2QL2FgDA1-ZVCSpZPER")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.us-east.language-translator.watson.cloud.ibm.com/instances/43c908d2-77ee-4432-9c67-03025cbb659c")

def english_to_french(english_text):
    """This function test English to French text"""
    french_text = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    """This function test French to English text"""
    english_text = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]