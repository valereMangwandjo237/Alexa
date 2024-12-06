import sys
import pyttsx3 # type: ignore
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()

engine = pyttsx3.init('sapi5')
engine.setProperty("voice", "french")  # la parole est en francais
engine.setProperty("rate", 170)  # vitesse de parole du moteur


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greetme():
    current_date = int(datetime.datetime.now().hour)

    if current_date <= 12:
        talk("Bonjour Valère !")
    if 12 < current_date < 18:
        talk("Bon après midi Valère !")
    if current_date >= 18 and current_date != 0:
        talk("Bonsoir Valère !")


# set french female voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
greetme()
talk("Comment vas tu?")


def madara_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.pause_threshold = 5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print(command)
        if 'madara' in command:
            command = command.replace('madara', '')
            print(command)
    return command


def run_madara():
    command = madara_command()
    if "musique" in command:
        song = command.replace("musique", "")
        talk("Musique en cours...")
        print(song)
        pywhatkit.playonyt(song)
    elif "heure" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Il est actuellement " + time)
    elif 'qui es-tu' in command or 'présentes-toi' in command:
        talk("Salut! Je m'appelle Madara. Je suis une intelligence artificielle développée par Valère.")
    elif "qui est" in command:
        person = command.replace("qui est", "")
        wikipedia.set_lang("fr")

        # Rechercher des titres correspondant
        search_results = wikipedia.search(person)

        # Si des résultats sont trouvés, utiliser le premier résultat
        if search_results:
            correct_title = search_results[0]
            info = wikipedia.summary(correct_title, sentences=1)
            talk(info)
        else:
            talk("Je n'ai aucune information sur " + person)
    elif "sort" in command:
        talk("Désolé valère, je suis un peu fatigué aujourd'hui. Une prochaine fois peut être!")
    elif "es-tu en couple" in command:
        talk("Valère, tu m'as crée pour être une intelligence artificielle, alors je n'ai pas de copain")
    elif "blague" in command:
        jokes = [
            "C’est la maîtresse qui demande à Toto « Cite-moi un mammifère qui n’a pas de dents »… « Ma grand-mère ? »",
            "C’est l’histoire de la maîtresse qui demande à Toto : « Récite-moi le verbe marcher au présent. » Toto répond "
            "« Je…marche…tu…tu…marches… », mais la maîtresse le presse, allez, plus vite Toto ! "
            "Et Toto repond « je cours ..…tu cours il court… »", ]
        talk(random.choice(jokes))
    elif "et toi" in command:
        msgs = ["Je suis la!", "Je vais bien merci!", "Un peu fatigué, mais ça ira valère!",
                "Je suis bien et plein d'energie."]
        talk(random.choice(msgs))
    elif "désactive toi" in command:
        talk("Merci de m'avoir utilisé, Valère. Au revoir!")
        sys.exit()
    else:
        talk("pourrais tu repété? je n'ai pas bien compris.")


if __name__ == '__main__':
    while True:
        run_madara()
