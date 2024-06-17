import speech_recognition as sr
from googletrans import Translator

translator = Translator()
recognizer = sr.Recognizer()

def speech_to_text(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Listening...')
        audio = recognizer.listen(source)
        print('Done listening.')
        
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return ""

def to_lang(lang, text):
    lang = lang.lower()
    
    LANGUAGES = {
        'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
        'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian',
        'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
        'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
        'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
        'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',
        'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian',
        'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
        'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew',
        'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic',
        'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
        'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh',
        'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
        'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
        'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy',
        'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori',
        'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)',
        'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
        'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
        'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic',
        'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi',
        'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
        'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish',
        'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai',
        'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur',
        'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
        'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'
    }
    
    if lang in LANGUAGES:
        dest_lang = LANGUAGES[lang]
        translations = translator.translate(text, dest=dest_lang)
        return translations.text
    else:
        return f"{lang} not found in supported languages."

if __name__ == "__main__":
    microphone = sr.Microphone()

    while True:
        spoken_text = speech_to_text(recognizer, microphone)
        print(f"Recognized speech: {spoken_text}")
        
        dest_lang_code = input("Enter destination language code (e.g., fr for French): ").strip()
        
        if dest_lang_code:
            translated_text = to_lang(dest_lang_code, spoken_text)
            print(f"Translated text: {translated_text}\n")
        else:
            print("No destination language code entered. Exiting...")
            break
