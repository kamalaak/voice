import speech_recognition as sr
import pyttsx3
import time
import wikipedia




def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        speak("Say something")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")
        return None


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def play_music():
    time.sleep(1)
    speak('Playing')


def tell_time():
    current_time = time.strftime("%H:%M:%S")
    print("The time is " + current_time)
    speak("The time is " + current_time)


def get_response(query):
    try:
        summary = wikipedia.summary(query)
        print(summary)
        speak(summary)
    except wikipedia.DisambiguationError as e:
        print(e.options)
        speak("There are multiple options. Can you please specify?")
    except wikipedia.PageError:
        print("Sorry, I couldn't find any information.")
        speak("Sorry, I couldn't find any information.")
    except Exception as e:
        print("An error occurred: ", str(e))
        speak("Sorry, something went wrong.")


def main():
    speak("Welcome to Transendynamics")
    while True:
        text = get_audio()
        if text is not None:
            text = text.lower()  # Convert to lowercase for case-insensitive comparison
            
            if text == "play":
                play_music()
            elif text == "tell me the time":
                tell_time()
            elif text == "what is your name":
                speak("My name is Clara.")
            elif text == "do you believe in god":
                speak("No, I believe in science.")
            elif text == "who invented you":
                speak("Kennith Raj")
            elif text == "what is your age":
                speak("I am five years old.")
            elif text == "what is your goal":
                speak("My goal is to make life simple.")
            elif text == "who created you":
                speak("Kennith Raj Sir")
            elif text == "bye":
                speak("You're welcome.")
            elif text == "what do you do":
                speak("I can do everything.")
            elif text == "who is chief minister of tamil nadu":
                time.sleep(1)
                speak("M. K. Stalin")
            elif text == "date of birth of vijay":
                speak("Vijay's date of birth is 22 June 1974.")
            elif text == "dravidian ideology" or text == "what do you think about dravidian ideology":
                speak(
                    "The ideology emphasizes social justice, equality, rationalism, and the empowerment of marginalized communities. It seeks to challenge traditional caste hierarchies, Brahminical dominance, and the perceived cultural and political hegemony of North India. The Dravidian ideology has promoted progressive social reforms, including reservation policies to uplift historically disadvantaged communities.")
            elif text == "who is ambedkar":
                get_response("Ambedkar")
            elif text == "vijay date of birth":
                speak("Vijay's date of birth is 22 June 1974.")
            elif text == 'vijay birthday':
                speak("Vijay's birthday is on 22 June 1974.")
            elif text == "article 53":
                get_response("President of India")
            elif text == "constitution of india":
                get_response("Constitution of India")
            elif text == "indian labour law" or text == "what is indian labour law":
                get_response("Indian labour law")
            elif text == "neet exam":
                speak(
                    "We don't need the NEET exam. It is the duty of the Medical colleges, professors, and the University doctors! It is not the duty of an entrance test - NEET. Anyone who claims otherwise is either ignorant or has vested interests. Any system of admission into higher education should be inclusive, accessible, affordable, and equitable! NEET-UG satisfies none of the above!")
            else:
                speak("I don't know what you mean.")


if __name__ == "__main__":
    main()
