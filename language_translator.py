

# Import the following module
import tkinter as tk  # install Tkinter
import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  # install pillow
from deep_translator import GoogleTranslator
# removed googletrans import; using deep_translator.GoogleTranslator instead
from tkinter import messagebox
import pyperclip as pc # install paperclip for copy function
from gtts import gTTS  # install gTTS for text to speech, speech to text functionality
import os
import speech_recognition as spr # install speech recognition for speech to text functionality

# ---------------------------------------------------Language Translator--------------------------------------------------------------
''' This python file consist of all functionalities required for the language translator application to work  '''

# UI is developed using Tkinter library
root = tk.Tk()
root.title('Langauge Translator')
root.geometry('1060x660')
root.attributes('-fullscreen', True)

root.maxsize(1060,660)
root.minsize(1060, 660)
# Tittle bar icon image used in Tkinter GUI (optional)
try:
    title_bar_icon = PhotoImage(file="translation.png")
    root.iconphoto(False, title_bar_icon)
except Exception:
    title_bar_icon = None
cl =''
output=''

# Mapping from combobox language names to ISO language codes
LANG_CODE = {
    'Afrikaans':'af','Albanian':'sq','Arabic':'ar','Basque':'eu','Bengali':'bn','Bosnian':'bs','Bulgarian':'bg',
    'Catalan':'ca','Croatian':'hr','Czech':'cs','Danish':'da','Dutch':'nl','English':'en','Estonian':'et',
    'Filipino':'tl','French':'fr','Frisian':'fy','Galician':'gl','German':'de','Greek':'el','Gujarati':'gu',
    'Hausa':'ha','Hindi':'hi','Hungarian':'hu','Icelandic':'is','Indonesian':'id','Italian':'it','Japanese':'ja',
    'Kannada':'kn','Khmer':'km','Korean':'ko','Latin':'la','Latvian':'lv','Lithuanian':'lt','Malay':'ms',
    'Malayalam':'ml','Marathi':'mr','Nepali':'ne','Odia':'or','Polish':'pl','Portuguese':'pt','Punjabi':'pa',
    'Romanian':'ro','Russian':'ru','Serbian':'sr','Sinhala':'si','Slovak':'sk','Spanish':'es','Sundanese':'su',
    'Swahili':'sw','Swedish':'sv','Tamil':'ta','Telugu':'te','Thai':'th','Turkish':'tr','Ukrainian':'uk',
    'Urdu':'ur','Vietnamese':'vi','Welsh':'cy','Yiddish':'yi'
}

def get_lang_code(name):
    return LANG_CODE.get(name, 'en')

# For Performing Main Translation Function
def translate():
    language_1 = t1.get("1.0", "end-1c")
    global cl
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
    else:
         t2.delete(1.0, 'end')
         global output
         code = get_lang_code(cl)
         try:
             output = GoogleTranslator(source='auto', target=code).translate(language_1)
         except Exception as e:
             messagebox.showerror('Language Translator', f'Translation failed: {e}')
             return
         t2.insert('end', output)
         add_to_history(language_1, cl, output)

# For Clearing Textbox Data
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# For Copying Textbox Data after Translation
def copy():
    pc.copy(str(output))

# For Converting Translated Text to Speech
def texttospeech():
 global cl
 cl = choose_langauge.get()
 if os.path.exists("text_to_speech.mp3"):
  os.remove("text_to_speech.mp3")
 mytext =output
 language='en'
 if cl == 'English':
     language = 'en'
 elif cl == 'Afrikaans':
     language = 'af'
 elif cl == 'Albanian':
     language = 'sq'
 elif cl == 'Arabic':
     language = 'ar'
 elif cl == 'Basque':
     language = 'eu'
 elif cl == 'Bengali':
     language = 'bn'
 elif cl == 'Bosnian':
     language = 'bs'
 elif cl == 'Bulgarian':
     language = 'bg'
 elif cl == 'Catalan':
     language = 'ca'
 elif cl == 'Croatian':
     language = 'hr'
 elif cl == 'Czech':
     language = 'cs'
 elif cl == 'Danish':
     language = 'da'
 elif cl == 'Dutch':
     language = 'nl'
 elif cl == 'English':
     language = 'en'
 elif cl == 'Estonian':
     language = 'et'
 elif cl == 'Finnish':
     language = 'fi'
 elif cl == 'French':
     language = 'fr'
 elif cl == 'Galician':
     language = 'gl'
 elif cl == 'German':
     language = 'de'
 elif cl == 'Greek':
     language = 'el'
 elif cl == 'Gujarati':
     language = 'gu'
 elif cl == 'Hausa':
     language = 'ha'
 elif cl == 'Hindi':
     language = 'hi'
 elif cl == 'Hungarian':
     language = 'hu'
 elif cl == 'Icelandic':
     language = 'is'
 elif cl == 'Indonesian':
     language = 'id'
 elif cl == 'Italian':
     language = 'it'
 elif cl == 'Japanese':
     language = 'ja'
 elif cl == 'Kannada':
     language = 'kn'
 elif cl == 'Khmer':
     language = 'km'
 elif cl == 'Korean':
     language = 'ko'
 elif cl == 'Latin':
     language = 'la'
 elif cl == 'Latvian':
     language = 'lv'
 elif cl == 'Lithuanian':
     language = 'lt'
 elif cl == 'Malay':
     language = 'ms'
 elif cl == 'Malayalam':
     language = 'ml'
 elif cl == 'Marathi':
     language = 'mr'
 elif cl == 'Nepali':
     language = 'ne'
 elif cl == 'Odia':
     language = 'or'
 elif cl == 'Polish':
     language = 'pl'
 elif cl == 'Portuguese':
     language = 'pt'
 elif cl == 'Punjabi':
     language = 'pa'
 elif cl == 'Romanian':
     language = 'ro'
 elif cl == 'Russian':
     language = 'ru'
 elif cl == 'Serbian':
     language = 'sr'
 elif cl == 'Sinhala':
     language = 'si'
 elif cl == 'Slovak':
     language = 'sk'
 elif cl == 'Spanish':
     language = 'es'
 elif cl == 'Sundanese':
     language = 'su'
 elif cl == 'Swahili':
     language = 'sw'
 elif cl == 'Swedish':
     language = 'sv'
 elif cl == 'Tamil':
     language = 'ta'
 elif cl == 'Telugu':
     language = 'te'
 elif cl == 'Thai':
     language = 'th'
 elif cl == 'Turkish':
     language = 'tr'
 elif cl == 'Ukrainian':
     language = 'uk'
 elif cl == 'Urdu':
     language = 'ur'
 elif cl == 'Uzbek':
     language = 'uz'
 elif cl == 'Vietnamese':
     language = 'vi'
 elif cl == 'Welsh':
     language = 'cy'
 elif cl == 'Yiddish':
     language = 'yi'
 
 else:
     language == 'en'
 try:
     myobj = gTTS(text=mytext, lang=language, slow=False)
     myobj.save("text_to_speech.mp3")
     os.system("text_to_speech.mp3")

 except ValueError as e:
     messagebox.showerror('Language Translator', cl+' is currently not supported for Read Aloud (Text to Speech)')
     print(f"An error occurred: {e}")
     # Handle the error or perform any necessary cleanup actions
 except AssertionError as e:
     # Handle the "No text to speak" error
     messagebox.showerror('Language Translator','Please enter the data to be translated before using Read Aloud')
     print("Error:", e)

# For converting Speech to Text [ Please Note : Only English is currently supported as from-language in Speech to Text Translation ]
def speechtotext():
   cl = choose_langauge.get()
   language = 'en'

   if cl == 'English':
       language = 'en'
   elif cl == 'Afrikaans':
       language = 'af'
   elif cl == 'Albanian':
       language = 'sq'
   elif cl == 'Arabic':
       language = 'ar'
   elif cl == 'Basque':
       language = 'eu'
   elif cl == 'Bengali':
       language = 'bn'
   elif cl == 'Bosnian':
       language = 'bs'
   elif cl == 'Bulgarian':
       language = 'bg'
   elif cl == 'Catalan':
       language = 'ca'
   elif cl == 'Croatian':
       language = 'hr'
   elif cl == 'Czech':
       language = 'cs'
   elif cl == 'Danish':
       language = 'da'
   elif cl == 'Dutch':
       language = 'nl'
   elif cl == 'English':
       language = 'en'
   elif cl == 'Estonian':
       language = 'et'
   elif cl == 'Finnish':
       language = 'fi'
   elif cl == 'French':
       language = 'fr'
   elif cl == 'Galician':
       language = 'gl'
   elif cl == 'German':
       language = 'de'
   elif cl == 'Greek':
       language = 'el'
   elif cl == 'Gujarati':
       language = 'gu'
   elif cl == 'Hausa':
       language = 'ha'
   elif cl == 'Hindi':
       language = 'hi'
   elif cl == 'Hungarian':
       language = 'hu'
   elif cl == 'Icelandic':
       language = 'is'
   elif cl == 'Indonesian':
       language = 'id'
   elif cl == 'Italian':
       language = 'it'
   elif cl == 'Japanese':
       language = 'ja'
   elif cl == 'Kannada':
       language = 'kn'
   elif cl == 'Khmer':
       language = 'km'
   elif cl == 'Korean':
       language = 'ko'
   elif cl == 'Latin':
       language = 'la'
   elif cl == 'Latvian':
       language = 'lv'
   elif cl == 'Lithuanian':
       language = 'lt'
   elif cl == 'Malay':
       language = 'ms'
   elif cl == 'Malayalam':
       language = 'ml'
   elif cl == 'Marathi':
       language = 'mr'
   elif cl == 'Nepali':
       language = 'ne'
   elif cl == 'Odia':
       language = 'or'
   elif cl == 'Polish':
       language = 'pl'
   elif cl == 'Portuguese':
       language = 'pt'
   elif cl == 'Punjabi':
       language = 'pa'
   elif cl == 'Romanian':
       language = 'ro'
   elif cl == 'Russian':
       language = 'ru'
   elif cl == 'Serbian':
       language = 'sr'
   elif cl == 'Sinhala':
       language = 'si'
   elif cl == 'Slovak':
       language = 'sk'
   elif cl == 'Spanish':
       language = 'es'
   elif cl == 'Sundanese':
       language = 'su'
   elif cl == 'Swahili':
       language = 'sw'
   elif cl == 'Swedish':
       language = 'sv'
   elif cl == 'Tamil':
       language = 'ta'
   elif cl == 'Telugu':
       language = 'te'
   elif cl == 'Thai':
       language = 'th'
   elif cl == 'Turkish':
       language = 'tr'
   elif cl == 'Ukrainian':
       language = 'uk'
   elif cl == 'Urdu':
       language = 'ur'
   elif cl == 'Vietnamese':
       language = 'vi'
   elif cl == 'Welsh':
       language = 'cy'
   elif cl == 'Yiddish':
       language = 'yi'
   else:
       language == 'en'

   from_lang = "en"
   to_lang = language

   recog1 = spr.Recognizer()
   mc = spr.Microphone()
   with mc as source:
        # Increase ambient noise adjustment duration for better noise calibration
        recog1.adjust_for_ambient_noise(source, duration=3)
        messagebox.showinfo("Voice Input", "Please speak now...")

        try:
            # Increase listening timeout and phrase time limit for longer capture
            audio = recog1.listen(source, timeout=10, phrase_time_limit=25)
        except spr.WaitTimeoutError:
            t1.insert("end", "No speech detected. Please try again.\n")
            return

    # Use retry logic for recognition to improve robustness
   get_sentence = None
   for attempt in range(2):
        try:
            get_sentence = recog1.recognize_google(audio)
            break
        except spr.UnknownValueError:
            if attempt == 1:
                t1.insert("end", "Unable to understand the input.\n")
                return
            else:
                time.sleep(0.5)
        except spr.RequestError as e:
            t1.insert("end", f"Unable to provide required output; {e}\n")
            return

   if get_sentence:
        t1.insert("end", get_sentence + "\n")
        # translate recognized sentence using deep_translator
        try:
            text = GoogleTranslator(source=from_lang, target=to_lang).translate(get_sentence)
        except Exception as e:
            t1.insert("end", f"Translation error: {e}\n")
            return
        global output
        output = text
        t2.insert("end", output + "\n")

#    with mc as source:

#        recog1.adjust_for_ambient_noise(source, duration=2)
#        audio = recog1.listen(source)
#        get_sentence = recog1.recognize_google(audio)

#    try:
#        t1.insert("end",get_sentence + "\n")
#        translator = Translator()
#        text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
#        text = text_to_translate.text

#        speak = gTTS(text=text, lang=to_lang, slow=False)
#        global output
#        output = speak.text
#        t2.insert("end",output + "\n")
#        translate()

#    except spr.UnknownValueError:
#            t1.insert("Unable to Understand the Input")

#    except spr.RequestError as e:
#            t1.insert("Unable to provide Required Output".format(e))


# Background Image settings using Tkinter
try:
    img = ImageTk.PhotoImage(Image.open('translator.png'))
except Exception:
    # fallback to a blank image if file missing
    img = ImageTk.PhotoImage(Image.new('RGBA', (1060, 660), (255, 255, 255, 0)))
label = Label(image=img)
label.place(x=0, y=0)

# combobox for from-language selection
a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20,textvariable=a, state='readonly', font=('Corbel', 20, 'bold'), )

auto_detect['values'] = ( 'Afrikaans','Albanian','Arabic', 'Basque',  'Bengali', 'Bosnian', 'Bulgarian', 'Catalan',    'Croatian', 'Czech', 'Danish', 'Dutch', 'English',  'Estonian', 'Filipino',  'French', 'Frisian', 'Galician',  'German', 'Greek', 'Gujarati',  'Hausa',  'Hindi',  'Hungarian', 'Icelandic',  'Indonesian',  'Italian', 'Japanese',  'Kannada',  'Khmer',  'Korean',    'Latin', 'Latvian', 'Lithuanian',   'Malay', 'Malayalam',  'Marathi',  'Nepali',  'Odia', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian',  'Serbian',  'Sinhala', 'Slovak',  'Spanish', 'Sundanese', 'Swahili', 'Swedish',  'Tamil',  'Telugu', 'Thai', 'Turkish',  'Ukrainian', 'Urdu',  'Vietnamese', 'Welsh', 'Yiddish', )
auto_detect.place(x=50, y=140)
auto_detect.current(0)
l = tk.StringVar()

# combobox for to-language selection
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_langauge['values'] = ( 'Afrikaans','Albanian','Arabic',  'Basque', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan',   'Croatian', 'Czech', 'Danish', 'Dutch', 'English',  'Estonian', 'Filipino',  'French', 'Frisian', 'Galician',  'German', 'Greek', 'Gujarati',  'Hausa',  'Hindi', 'Hungarian', 'Icelandic',  'Indonesian',  'Italian', 'Japanese',  'Kannada', 'Khmer', 'Korean',  'Latin', 'Latvian', 'Lithuanian',  'Malay', 'Malayalam',  'Marathi', 'Nepali', 'Odia',  'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian',  'Serbian', 'Sinhala', 'Slovak',  'Spanish', 'Sundanese', 'Swahili', 'Swedish',  'Tamil', 'Telugu', 'Thai', 'Turkish',  'Ukrainian', 'Urdu',  'Vietnamese', 'Welsh', 'Yiddish',  )
choose_langauge.place(x=600, y=140)
choose_langauge.current(0)

# Load and resize the icon images for buttons
def _load_icon(path):
    try:
        img = Image.open(path)
        resized = img.resize((32, 32), Image.Resampling.LANCZOS)
    except Exception:
        resized = Image.new('RGBA', (32, 32), (200, 200, 200, 0))
    return ImageTk.PhotoImage(resized)

translate_text_icon = _load_icon("documents.png")
clear_text_icon = _load_icon("eraser.png")
copy_text_icon = _load_icon("copy.png")
read_aloud_icon = _load_icon("text_to_speech.png")
voice_input_icon = _load_icon("voice_recognition.png")


# Text Widget settings used in Tkinter GUI
t1 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t1.place(x=20, y=200)
t2 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t2.place(x=550, y=200)

# Button settings used in Tkinter GUI
translate_button = Button(root, text=" Translate Text ",image=translate_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 9, 'bold'), cursor="hand2",
                command=translate,bg="#141413",fg="#F3F3F3")
translate_button.place(x=40, y=565)

clear_button = Button(root, text=" Clear ",image=clear_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 9, 'bold'), cursor="hand2",
               command=clear,bg="#141413",fg="#F3F3F3")
clear_button.place(x=180, y=565)

copy_button = Button(root, text=" Copy ",image=copy_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 9, 'bold'), cursor="hand2",
                command=copy,bg="#141413",fg="#F3F3F3")
copy_button.place(x=390, y=565)

read_aloud = Button(root, text=" Read Aloud ",image=read_aloud_icon, compound="right" ,relief=RIDGE, borderwidth=0, font=('Corbel', 9, 'bold'), cursor="hand2",
                command=texttospeech,bg="#141413",fg="#F3F3F3")
read_aloud.place(x=690, y=565)

voice_input = Button(root, text=" Voice Input ", image=voice_input_icon, compound="right", relief=RIDGE, borderwidth=0,
                     font=('Corbel', 9, 'bold'), cursor="hand2", command=speechtotext, bg="#141413",fg="#F3F3F3")
voice_input.place(x=850, y=565)
import tkinter as tk
from tkinter import ttk, font

# Define a creative font (if available) or use a bold, larger font
creative_font = font.Font(family="Comic Sans MS", size=8, weight="bold")

style = ttk.Style()
current_mode = "light"

def toggle_mode():
    global current_mode
    if current_mode == "light":
        root.config(bg="#191724")  # Aesthetic deep purple
        t1.config(bg="#282a36", fg="#ffb86c", insertbackground="#ffb86c")
        t2.config(bg="#282a36", fg="#bd93f9", insertbackground="#bd93f9")
        style.configure('TCombobox',
                        fieldbackground='#282a36',
                        background='#282a36',
                        foreground='#ffb86c')
        # Button changes to Sun for Light
        mode_btn.config(
            text="☀️",  # Emoji + Text
            bg="#44475a", fg="#ffb86c",
            activebackground="#6272a4",
            activeforeground="#ffd700"
        )
        current_mode = "dark"
    else:
        root.config(bg="#f8f8f2")
        t1.config(bg="#ffffff", fg="#22223b", insertbackground="#22223b")
        t2.config(bg="#ffffff", fg="#4a4e69", insertbackground="#4a4e69")
        style.configure('TCombobox',
                        fieldbackground='#ffffff',
                        background='#ffffff',
                        foreground='#22223b')
        # Button changes to Moon for Dark
        mode_btn.config(
            text="🌙",
            bg="#ffeecc", fg="#4a4e69",
            activebackground="#dbe6fd",
            activeforeground="#22223b"
        )
        current_mode = "light"

# Place your creative button in your UI:
mode_btn = tk.Button(
    root,
    text="🌙",  # Start with dark mode invitation
    command=toggle_mode,
    font=creative_font,
    bg="#ffeecc",
    fg="#4a4e69",
    activebackground="#dbe6fd",
    activeforeground="#22223b",
    borderwidth=3,
    relief="ridge",
    cursor="hand2",
    padx=20,
    pady=8
)
mode_btn.place(x=920, y=120)  # Position as desired
# Place these button creations AFTER your t2 widget has been placed, 
# but BEFORE root.mainloop()
from tkinter import messagebox
import datetime
favorite_translations = []


def add_to_favorites():
    language_1 = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()
    if language_1 and t2.get("1.0", "end-1c").strip():
        output = t2.get("1.0", "end-1c").strip()
        favorite_translations.append((language_1, cl, output))
        messagebox.showinfo('Favorites', 'Added to favorites!')
    else:
        messagebox.showwarning('Favorites', 'No translation to favorite.')


# Function to show favorite translations
def show_favorites():
    popup = tk.Toplevel(root)
    popup.title("Favorite Translations")
    popup.geometry("600x400")
    listbox = tk.Listbox(popup, width=90, font=('Calibri', 12))
    listbox.pack(fill="both", expand=True)
    for source, lang, result in favorite_translations:
        listbox.insert('end', f"[{lang}] {source} → {result}")

# "Add to Favorites" button: positioned beneath or beside the right (output) box
add_favorite_btn = tk.Button(
    root,
    text="Add to Fav",
    command=add_to_favorites,
    font=("Arial", 9, "bold"),
    bg="#141413",
    fg="#F3F3F3",
    relief="ridge",
    cursor="hand2",
    width=9,
    height=2
)
add_favorite_btn.place(x=556, y=565)  # Adjust x/y for your layout, this is just below t2

# Make sure this is near the top with your other imports

from tkinter import messagebox
import datetime

# Global variable to store your translation history


# import tkinter as tk
from tkinter import messagebox
import datetime

# -------- 1. GLOBAL VARIABLES --------
translation_history = []

import tkinter as tk
from tkinter import ttk, messagebox
import datetime

translation_history = []

# -------- 2. FUNCTION: Add translation to history --------
def add_to_history(source_text, language, translated_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    translation_history.append((timestamp, source_text, language, translated_text))

# -------- 3. FUNCTION: Show translation history in popup --------
# -------- 3. FUNCTION: Show translation history in popup --------
def show_history():
    popup = tk.Toplevel(root)
    popup.title("Translation History")
    popup.geometry("950x500")
    popup.config(bg="#ebe6fa")

    # Heading label
    history_label = tk.Label(
        popup,
        text="Your Translation History",
        font=("Arial", 16, "bold"),
        bg="#ebe6fa",
        fg="#6247aa"
    )
    history_label.place(x=330, y=10)

    # If no translations yet
    if not translation_history:
        msg = tk.Label(
            popup,
            text="No translations yet!",
            font=("Arial", 12),
            bg="#ebe6fa",
            fg="#333"
        )
        msg.place(x=370, y=200)
        return

    # Scrollable Frame for history content
    frame = tk.Frame(popup, bg="#ebe6fa")
    frame.place(x=20, y=50, width=900, height=400)

    canvas = tk.Canvas(frame, bg="#ebe6fa", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    vsb = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    vsb.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=vsb.set)

    inner_frame = tk.Frame(canvas, bg="#ebe6fa")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Populate all translations fully (multi-line visible)
    for i, (timestamp, source, lang, result) in enumerate(translation_history, start=1):
        card = tk.Frame(inner_frame, bg="#f5f0ff", relief="groove", bd=2)
        card.pack(fill="x", pady=5, padx=10)

        tk.Label(card, text=f"🕒 {timestamp}", font=("Arial", 10, "bold"), bg="#f5f0ff", fg="#6247aa").pack(anchor="w", padx=5, pady=2)
        tk.Label(card, text=f"🌐 Language: {lang}", font=("Arial", 10, "italic"), bg="#f5f0ff", fg="#3b3b3b").pack(anchor="w", padx=5)

        # Full source text (multi-line)
        src_label = tk.Label(card, text="Source Text:", font=("Arial", 10, "bold"), bg="#f5f0ff", fg="#000").pack(anchor="w", padx=5)
        src_text = tk.Text(card, height=len(source.split("\n")) + 1, wrap="word", font=("Arial", 10), bg="#ffffff", fg="#000000")
        src_text.insert("1.0", source)
        src_text.config(state="disabled")
        src_text.pack(fill="x", padx=10, pady=2)

        # Full translated text (multi-line)
        res_label = tk.Label(card, text="Translated Text:", font=("Arial", 10, "bold"), bg="#f5f0ff", fg="#000").pack(anchor="w", padx=5)
        res_text = tk.Text(card, height=len(result.split("\n")) + 1, wrap="word", font=("Arial", 10), bg="#ffffff", fg="#000000")
        res_text.insert("1.0", result)
        res_text.config(state="disabled")
        res_text.pack(fill="x", padx=10, pady=2)

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


# -------- 4. HISTORY BUTTON --------
history_btn = tk.Button(
    root,
    text="🕘 History",
    command=show_history,
    font=("Arial", 12, "bold"),
    bg="#141413",
    fg="#F3F3F3",
    relief="ridge",
    cursor="hand2",
    width=7,
    height=1
)
history_btn.place(x=0, y=10)


# -------- 5. CALL 'add_to_history' IN YOUR TRANSLATE FUNCTION --------
# Example for inside your translate function, after translating:
# add_to_history(language_1, cl, output)


# "Favorites" button: next to "History"
favorites_btn = tk.Button(
    root,
    text="⭐ Favorites",
    command=show_favorites,
    font=("Arial", 7, "bold"),
    bg="#141413",
    fg="#F3F3F3",
    relief="ridge",
    cursor="hand2",
    width=7,
    height=1
)
favorites_btn.place(x=0, y=50)  # Adjust as needed

# --- Top 30 Languages and Lesson Theory ---
# ---- Learn Mode Phrasebook ----

# The phrasebook data structure



def show_learn_mode():
    popup = tk.Toplevel(root)
    popup.title("Learn Mode Phrasebook")
    popup.geometry("900x550")
    popup.config(bg="#d1dae8")

    # Supported languages with codes and phrases for categories
    languages = {
    "Telugu": {
        "code": "te",
        "phrases": {
            "Most Popular": {
                "హలో": "Hello",
                "శుభోదయం": "Good morning",
                "మీరు ఎలా ఉన్నారు?": "How are you?",
                "ధన్యవాదాలు": "Thank you",
                "వీడ్కోలి": "Good bye",
                "దయచేసి": "Please",
                "క్షమించండి": "Excuse me",
                "నేను క్షమించాడు": "I am sorry",
                "మీకు స్వాగతం": "You are welcome",
                "శుభ రాత్రి": "Good night",
                "అక్కడ లేరు": "No thank you"
            },
            "Basics": {
                "పేరేమిటి?": "What is your name?",
                "నాకు సహాయం కావాలి": "I need help",
                "ఇది ఎంత ఉంది?": "How much is this?",
                "ఇది ఎక్కడ ఉంది?": "Where is this?",
                "నేను అర్థం చేసుకోలేను": "I don't understand",
                "నీరు": "Water",
                "అందుకు": "That's enough",
                "నేను తెలుగులో మాట్లాడతాను": "I speak Telugu",
                "నేను ఇతర భాష మాట్లాడతాను": "I speak another language",
                "వచ్చే వారుఎప్పుడు?": "When will you come?"
            },
            "Social": {
                "మీకు సహాయం కావాలా?": "Do you need help?",
                "మీరు ఎక్కడుంటారు?": "Where do you live?",
                "మీ కుటుంబంలో ఎవరున్నారు?": "Who is in your family?",
                "మీరు ఏమి చేస్తారు?": "What do you do?",
                "మీకు సంతోషంగా ఉందా?": "Are you happy?",
                "మీరు శుభంగా ఉన్నారా?": "Are you well?",
                "మీరు ఎలా ఉన్నారు?": "How are you?",
                "మీ పేరు ఏమిటి?": "What is your name?",
                "మీరు ఎక్కడికి వెళ్ళుతున్నారు?": "Where are you going?",
                "మీ పిల్లలు ఎలా ఉన్నారు?": "How are your children?"
            },
            "Travel": {
                "హోటల్ ఎక్కడ ఉంది?": "Where is the hotel?",
                "బస్సు స్టాండ్ ఎక్కడ ఉంది?": "Where is the bus stop?",
                "రైల్వే స్టేషన్ ఎక్కడ ఉంది?": "Where is the railway station?",
                "నేను టాక్సీ అవసరం": "I need a taxi",
                "స్థానం ఎటు?": "Which way to go?",
                "బోర్డ్ చేసుకోండి": "Book a ticket",
                "బిల్లు ఎంత?": "What is the fare?",
                "సమయం ఎంత?": "What time is it?",
                "ఇక్కడ ఎటు పోవాలి?": "Where to go from here?",
                "పాస్‌పోర్ట్ చూపించండి": "Show your passport"
            },
            "Dining": {
                "మీకు మెనూ ఇవ్వండి": "Please give me the menu",
                "నేను శాకాహారి": "I'm vegetarian",
                "నీరు కావాలి": "I need water",
                "ఇది చాలా రుచికరంగా ఉంది": "This tastes very good",
                "బిల్ ఇవ్వండి": "Please bring the bill",
                "బిర్యానీ ఎక్కడ ఉంది?": "Where is good biryani?",
                "నీరు మరొకటి కావాలి": "I want some more water",
                "తాగడానికి నీళ్లు ఇవ్వండి": "Give water to drink",
                "నేను చేప తింటాను": "I eat fish",
                "మీరు అర్థం చేసుకుంటారా?": "Do you understand me?"
            },
            "Emergency": {
                "సహాయం చేయండి": "Help",
                "అంబులెన్స్ కాల్ చేయండి": "Call an ambulance",
                "আগুন লাগింది": "Fire",
                "పోలీసు": "Police",
                "నేను తప్పిపోయాను": "I am lost",
                "నాకు డాక్టర్ అవసరం": "I need a doctor",
                "ప్రమాదం": "Danger",
                "నేను అనారోగ్యంగా ఉన్నాను": "I feel sick",
                "గాయపడినది": "I am injured",
                "మాకు సహాయం చేయండి": "Help us"
            }
        }
    },

    "Hindi": {
        "code": "hi",
        "phrases": {
            "Most Popular": {
                "नमस्ते": "Hello",
                "सुप्रभात": "Good morning",
                "आप कैसे हैं?": "How are you?",
                "धन्यवाद": "Thank you",
                "अलविदा": "Good bye",
                "कृपया": "Please",
                "माफ़ कीजिए": "Excuse me",
                "मुझे खेद है": "I am sorry",
                "आपका स्वागत है": "You are welcome",
                "शुभ रात्रि": "Good night",
                "धन्यवाद नहीं": "No thank you"
            },
            "Basics": {
                "आपका नाम क्या है?": "What is your name?",
                "मुझे मदद चाहिए": "I need help",
                "यह कितना है?": "How much is this?",
                "यह कहाँ है?": "Where is this?",
                "मुझे समझ नहीं आया": "I don't understand",
                "धन्यवाद": "Thank you",
                "पानी": "Water",
                "काफ़ी है": "That's enough",
                "मैं हिंदी बोलता हूँ": "I speak Hindi",
                "मैं दूसरी भाषा बोलता हूँ": "I speak another language"
            },
            "Social": {
                "क्या आपको मदद चाहिए?": "Do you need help?",
                "आप कहाँ रहते हैं?": "Where do you live?",
                "आपके परिवार में कौन हैं?": "Who is in your family?",
                "आप क्या करते हैं?": "What do you do?",
                "क्या आप खुश हैं?": "Are you happy?",
                "क्या आप ठीक हैं?": "Are you well?",
                "आप कैसे हैं?": "How are you?",
                "आपका नाम क्या है?": "What is your name?",
                "आप कहाँ जा रहे हो?": "Where are you going?"
            },
            "Travel": {
                "होटल कहाँ है?": "Where is the hotel?",
                "बस स्टॉप कहाँ है?": "Where is the bus stop?",
                "रेलवे स्टेशन कहाँ है?": "Where is the railway station?",
                "मुझे टैक्सी चाहिए": "I need a taxi",
                "कौन सा रास्ता है?": "Which way to go?",
                "टिकट बुक करें": "Book a ticket",
                "किराया कितना है?": "What is the fare?",
                "समय क्या है?": "What time is it?",
                "यहाँ कहाँ जाना है?": "Where to go here?",
                "पासपोर्ट दिखाओ": "Show your passport"
            },
            "Dining": {
                "मेन्यू दो": "Please give me the menu",
                "मुझे शाकाहारी खाना चाहिए": "I want vegetarian food",
                "मुझे पानी चाहिए": "I want water",
                "यह स्वादिष्ट है": "This tastes good",
                "बिल दें": "Please bring the bill",
                "क्या आप मांस खाते हैं?": "Do you eat meat?",
                "मैं मछली खाता हूँ": "I eat fish",
                "मुझे कॉफी चाहिए": "Give me coffee",
                "क्या बच्चों के लिए विशेष भोजन है?": "Is there special food for kids?",
                "मेज़ कहाँ है?": "Where is the table?"
            },
            "Emergency": {
                "मदद करें": "Help",
                "एम्बुलेंस कॉल करें": "Call an ambulance",
                "आग लग गई है": "Fire",
                "पुलिस": "Police",
                "मैं खो गया हूँ": "I am lost",
                "मुझे डॉक्टर चाहिए": "I need a doctor",
                "खतरा": "Danger",
                "मैं बीमार हूँ": "I feel sick",
                "दुर्घटना": "Accident",
                "वहाँ मदद चाहिए": "Help needed there"
            }
        }
    },

    "Malayalam": {
        "code": "ml",
        "phrases": {
            "Most Popular": {
                "ഹലോ": "Hello",
                "ശുഭപ്രഭാതം": "Good morning",
                "സന്തോഷമാണോ?": "How are you?",
                "നന്ദി": "Thank you",
                "വിട": "Good bye",
                "ദയവായി": "Please",
                "ക്ഷമിയ്ക്കണം": "Excuse me",
                "എനിക്ക് ക്ഷമിയ്ക്കണം": "I am sorry",
                "സ്വാഗതം": "You are welcome",
                "ശുഭ രാത്രി": "Good night",
                "അതിന് നന്ദി": "No thank you"
            },
            "Basics": {
                "നിങ്ങളുടെ പേര് എന്ത്?": "What is your name?",
                "എനിക്ക് സഹായം വേണം": "I need help",
                "ഇതിന്റെ വില എന്ത്?": "How much is this?",
                "ഇത് എവിടെയാണ്?": "Where is this?",
                "എനിക്ക് മനസ്സിലായില്ല": "I don't understand",
                "വെള്ളം": "Water",
                "പോതുണ്ട്": "That's enough",
                "ഞാൻ മലയാളം സംസാരിക്കുന്നു": "I speak Malayalam",
                "ഞാൻ മറ്റൊരു ഭാഷ സംസാരിക്കുന്നു": "I speak another language"
            },
            "Social": {
                "താങ്കളുടെ സഹായം വേണോ?": "Do you need help?",
                "താങ്കൾ എവിടെ താമസിക്കുന്നു?": "Where do you live?",
                "നിങ്ങളുടെ കുടുംബത്തിൽ ഏവരാണ്?": "Who is in your family?",
                "താങ്കൾ എന്ത് ചെയ്യുന്നു?": "What do you do?",
                "തനിക്ക് സന്തോഷമുണ്ടോ?": "Are you happy?",
                "താങ്കൾ സുഖമാണോ?": "Are you well?",
                "നിങ്ങൾ എങ്കിൽ എങ്കിൽ?": "How are you?",
                "താങ്കളുടെ പേര് എന്ത്?": "What is your name?",
                "നീ എവിടേക്കു പോയിരിക്കുന്നു?": "Where are you going?"
            },
            "Travel": {
                "ഹോട്ടൽ എവിടെയാണ്?": "Where is the hotel?",
                "ബസ് സ്റ്റോപ്പ് എവിടെയാണ്?": "Where is the bus stop?",
                "റെയിൽവേ സ്റ്റേഷൻ എവിടെയാണ്?": "Where is the railway station?",
                "എനിക്ക് ടാക്‌സി വേണം": "I need a taxi",
                "എങ്ങോട്ടു പോകണം?": "Which way to go?",
                "ടിക്കറ്റ് ബുക്ക് ചെയ്യുക": "Book a ticket",
                "വേനൽക്കാല സമയമന്ത്?": "What time is it?",
                "ഇവിടെ എവിടെയാണ് പോകേണ്ടത്?": "Where to go here?",
                "പാസ്പോർട്ട് കാണിക്കുക": "Show your passport"
            },
            "Dining": {
                "ദയവായി മெனു തരിക": "Please give me the menu",
                "ഞാൻ ഓഫറിട്ട ഭക്ഷണം ഉണ്ട്": "I want vegetarian food",
                "എനിക്ക് വെള്ളം വേണം": "I need water",
                "ഇത് രുചികരമാണ്": "This tastes very good",
                "ബിൽ തരം തരിക": "Please bring the bill",
                "നല്ല ബിരിയാണി എവിടെയാണ്?": "Where is good biryani?",
                "കൂടെ വെള്ളം വേണം": "I want some water",
                "തെളിയാൻ വെള്ളം തരിക": "Give water to drink",
                "ഞാൻ മത്സ്യം കഴിക്കുന്നു": "I eat fish",
                "താങ്കൾ എന്നെ മനസിലാക്കുമോ?": "Do you understand me?"
            },
            "Emergency": {
                "സഹായിക്കണം": "Help",
                "ആംബുലൻസ് വിളിക്കൽ": "Call an ambulance",
                "വൻകിടക്കുക": "Fire",
                "പോലീസ്": "Police",
                "ഞാൻ കെട്ടിവന്നിട്ടുണ്ട്": "I am lost",
                "എനിക്ക് ഡോക്ടർ വേണം": "I need a doctor",
                "അപകടം": "Danger",
                "ഞാൻ രോഗം പിടിച്ചു": "I feel sick",
                "പൊട്ടിത്തെറി": "I am injured",
                "ഞങ്ങളെ സഹായിക്കുക": "Help us"
            }
        }
    },

    "Punjabi": {
        "code": "pa",
        "phrases": {
            "Most Popular": {
                "ਸਤ ਸ੍ਰੀ ਅਕਾਲ": "Hello",
                "ਸ਼ੁਭ ਸਵੇਰ": "Good morning",
                "ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?": "How are you?",
                "ਧੰਨਵਾਦ": "Thank you",
                "ਅਲਵਿਦਾ": "Good bye",
                "ਕਿਰਪਾ ਕਰਕੇ": "Please",
                "ਮਾਫ਼ ਕਰਨਾ": "Excuse me",
                "ਮੈਂ ਮਾਫ਼ੀ ਚਾਹੁੰਦਾ ਹਾਂ": "I am sorry",
                "ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ": "You are welcome",
                "ਸ਼ੁਭ ਰਾਤਰੀ": "Good night",
                "ਨਹੀਂ ਧੰਨਵਾਦ": "No thank you"
            },
            "Basics": {
                "ਤੁਹਾਡਾ ਨਾਮ ਕੀ ਹੈ?": "What is your name?",
                "ਮੈਨੂੰ ਮਦਦ ਦੀ ਲੋੜ ਹੈ": "I need help",
                "ਇਹ ਕਿੰਨਾ ਹੈ?": "How much is this?",
                "ਇਹ ਕਿੱਥੇ ਹੈ?": "Where is this?",
                "ਮੈਂ ਸਮਝ ਨਹੀਂ ਪਾਇਆ": "I don't understand",
                "ਪਾਣੀ": "Water",
                "ਬਹੁਤ ਹੈ": "That's enough",
                "ਮੈਂ ਪੰਜਾਬੀ ਬੋਲਦਾ ਹਾਂ": "I speak Punjabi",
                "ਮੈਂ ਹੋਰ ਭਾਸ਼ਾ ਬੋਲਦਾ ਹਾਂ": "I speak another language"
            },
            "Social": {
                "ਕੀ ਤੁਹਾਨੂੰ ਮਦਦ ਚਾਹੀਦੀ ਹੈ?": "Do you need help?",
                "ਤੁਸੀਂ ਕਿੱਥੇ ਰਹਿੰਦੇ ਹੋ?": "Where do you live?",
                "ਤੁਹਾਡੇ ਪਰਿਵਾਰ ਵਿੱਚ ਕੌਣ ਹੈ?": "Who is in your family?",
                "ਤੁਸੀਂ ਕੀ ਕਰਦੇ ਹੋ?": "What do you do?",
                "ਕੀ ਤੁਸੀਂ ਖੁਸ਼ ਹੋ?": "Are you happy?",
                "ਕੀ ਤੁਸੀਂ ਠੀਕ ਹੋ?": "Are you well?",
                "ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?": "How are you?",
                "ਤੁਹਾਡਾ ਨਾਮ ਕੀ ਹੈ?": "What is your name?",
                "ਤੁਸੀਂ ਕਿੱਥੇ ਜਾ ਰਹੇ ਹੋ?": "Where are you going?"
            },
            "Travel": {
                "ਹੋਟਲ ਕਿੱਥੇ ਹੈ?": "Where is the hotel?",
                "ਬੱਸ ਸਟਾਪ ਕਿੱਥੇ ਹੈ?": "Where is the bus stop?",
                "ਰੇਲਵੇ ਸਟੇਸ਼ਨ ਕਿੱਥੇ ਹੈ?": "Where is the railway station?",
                "ਮੈਨੂੰ ਟੈਕਸੀ ਚਾਹੀਦੀ ਹੈ": "I need a taxi",
                "ਕਿਹੜਾ ਰਸਤਾ ਹੈ?": "Which way to go?",
                "ਟਿਕਟ ਬੁਕ ਕਰੋ": "Book a ticket",
                "ਕਿਰਾਇਆ ਕਿੰਨਾ ਹੈ?": "What is the fare?",
                "ਸਮਾਂ ਕੀ ਹੈ?": "What time is it?",
                "ਇੱਥੇ ਕਿੱਥੇ ਜਾਣਾ ਹੈ?": "Where to go here?",
                "ਪਾਸਪੋਰਟ ਵੇਖਾਓ": "Show your passport"
            },
            "Dining": {
                "ਮੈਨੂੰ ਮੀਨੂ ਦਿਓ": "Please give me the menu",
                "ਮੈਂ ਸਬਜ਼ੀਆਂ ਵਾਲਾ ਖਾਧਾ ਚਾਹੁੰਦਾ ਹਾਂ": "I want vegetarian food",
                "ਮੈਨੂੰ ਪਾਣੀ ਚਾਹੀਦਾ ਹੈ": "I need water",
                "ਇਹ ਬਹੁਤ ਸਵਾਦ ਹੈ": "This tastes very good",
                "ਬਿੱਲ ਦਿਓ": "Please bring the bill",
                "ਮੈਨੂੰ ਕੋਈ ਮਾਸਾਹਾਰੀ ਨਹੀਂ ਖਾਣਾ": "I don’t eat meat",
                "ਮੈਂ ਮੱਛੀ ਖਾਂਦਾ ਹਾਂ": "I eat fish",
                "ਮੈਨੂੰ ਕਾਫੀ ਦਿਓ": "Give me coffee",
                "ਕੀ ਬੱਚਿਆਂ ਲਈ ਖਾਸ ਭੋਜਨ ਹੈ?": "Is there special food for kids?",
                "ਟੇਬਲ ਕਿੱਥੇ ਹੈ?": "Where is the table?"
            },
            "Emergency": {
                "ਮਦਦ ਕਰੋ": "Help",
                "ਐਂਬੂਅਲੈਂਸ ਲਈ ਕਾਲ ਕਰੋ": "Call an ambulance",
                "ਅੱਗ ਲੱਗੀ ਹੈ": "Fire",
                "ਪੁਲਿਸ ਨੂੰ ਕਾਲ ਕਰੋ": "Call the police",
                "ਮੈਂ ਗੁੰਮ ਹੋ ਗਿਆ ਹਾਂ": "I am lost",
                "ਮੈਨੂੰ ਡਾਕਟਰ ਦੀ ਲੋੜ ਹੈ": "I need a doctor",
                "ਖ਼ਤਰਾ": "Danger",
                "ਮੈਂ ਬੀਮਾਰ ਹਾਂ": "I feel sick",
                "ਮੈਂ ਜ਼ਖ਼ਮੀ ਹਾਂ": "I am injured",
                "ਮਦਦ ਕਰੋ": "Help us"
            }
        }
    },

    
    "Bengali": {
        "code": "bn",
        "phrases": {
            "Most Popular": {
                "হ্যালো": "Hello",
                "শুভ সকাল": "Good morning",
                "আপনি কেমন আছেন?": "How are you?",
                "ধন্যবাদ": "Thank you",
                "বিদায়": "Good bye",
                "অনুগ্রহ করে": "Please",
                "ক্ষমা করবেন": "Excuse me",
                "আমি দুঃখিত": "I am sorry",
                "আপনাকে স্বাগতম": "You are welcome",
                "শুভ রাত্রি": "Good night",
                "না ধন্যবাদ": "No thank you"
            },
            "Basics": {
                "আপনার নাম কি?": "What is your name?",
                "আমার সাহায্য দরকার": "I need help",
                "এটার দাম কত?": "How much is this?",
                "এটা কোথায়?": "Where is this?",
                "আমি বুঝতে পারছি না": "I don't understand",
                "জল": "Water",
                "এটা যথেষ্ট": "That's enough",
                "আমি বাংলা বলতে পারি": "I speak Bengali",
                "আমি অন্য ভাষায় কথা বলি": "I speak another language"
            },
            "Social": {
                "আপনার কি সাহায্য দরকার?": "Do you need help?",
                "আপনি কোথায় থাকেন?": "Where do you live?",
                "আপনার পরিবারের সদস্যরা কে?": "Who is in your family?",
                "আপনি কি করেন?": "What do you do?",
                "আপনি কি সুখী?": "Are you happy?",
                "আপনি কি ভাল আছেন?": "Are you well?",
                "আপনি কেমন আছেন?": "How are you?",
                "আপনার নাম কি?": "What is your name?",
                "আপনি কোথায় যাচ্ছেন?": "Where are you going?"
            },
            "Travel": {
                "হোটেল কোথায়?": "Where is the hotel?",
                "বাস স্টপ কোথায়?": "Where is the bus stop?",
                "রেলওয়ে স্টেশন কোথায়?": "Where is the railway station?",
                "আমার একটি ট্যাক্সি দরকার": "I need a taxi",
                "কোন দিকে যেতে হবে?": "Which way to go?",
                "টিকিট বুক করুন": "Book a ticket",
                "ভাড়া কত?": "What is the fare?",
                "সময় কত?": "What time is it?",
                "এখানে কোথায় যেতে হবে?": "Where to go here?",
                "দয়া করে পাসপোর্ট দেখাও": "Show your passport"
            },
            "Dining": {
                "আমাকে মেনু দিন": "Please give me the menu",
                "আমি নিরামিষাশী": "I want vegetarian food",
                "আমাকে পানি দিন": "I need water",
                "এটি খুব সুস্বাদু": "This tastes very good",
                "বিল দাও": "Please bring the bill",
                "ভাল বিরিয়ানি কোথায়?": "Where is good biryani?",
                "আরও পানি চাই": "I want some more water",
                "পানীয় দিন": "Give water to drink",
                "আমি মাছ খাই": "I eat fish",
                "তুমি আমাকে বোঝো?" : "Do you understand me?"
            },
            "Emergency": {
                "সাহায্য করুন": "Help",
                "অ্যাম্বুলেন্স ডাকুন": "Call an ambulance",
                "আগুন লেগেছে": "Fire",
                "পুলিশ ডাকুন": "Call the police",
                "আমি হারিয়ে গেছি": "I am lost",
                "আমাকে চিকিৎসক দরকার": "I need a doctor",
                "ঝুঁকি": "Danger",
                "আমি অসুস্থ": "I feel sick",
                "আমি আহত": "I am injured",
                "দয়া করে আমাকে সাহায্য করুন": "Help us"
            }
        }
    },

    "Marathi": {
        "code": "mr",
        "phrases": {
            "Most Popular": {
                "नमस्कार": "Hello",
                "शुभ सकाळ": "Good morning",
                "तुम्ही कसे आहात?": "How are you?",
                "धन्यवाद": "Thank you",
                "निरोप": "Good bye",
                "कृपया": "Please",
                "माफ करा": "Excuse me",
                "मला खेद आहे": "I am sorry",
                "आपले स्वागत आहे": "You are welcome",
                "शुभ रात्री": "Good night",
                "धन्यवाद नाही": "No thank you"
            },
            "Basics": {
                "तुमचं नाव काय आहे?": "What is your name?",
                "मला मदत हवी आहे": "I need help",
                "हे किती आहे?": "How much is this?",
                "हे कुठे आहे?": "Where is this?",
                "मला समजत नाही": "I don't understand",
                "पाणी": "Water",
                "आणि पुरेसे आहे": "That's enough",
                "मी मराठी बोलतो": "I speak Marathi",
                "मी दुसरी भाषा बोलतो": "I speak another language"
            },
            "Social": {
                "तुला मदत हवी आहे का?": "Do you need help?",
                "तू कुठे राहत आहेस?": "Where do you live?",
                "तुझ्या कुटुंबात कोण आहे?": "Who is in your family?",
                "तू काय करतोस?": "What do you do?",
                "तुला आनंद आहे का?": "Are you happy?",
                "तू ठीक आहेस का?": "Are you well?",
                "तू कसा आहेस?": "How are you?",
                "तुला नाव काय आहे?": "What is your name?",
                "तू कुठे चालला आहेस?": "Where are you going?"
            },
            "Travel": {
                "हॉटेल कुठे आहे?": "Where is the hotel?",
                "बस थांबा कुठे आहे?": "Where is the bus stop?",
                "रेल्वे स्थानक कुठे आहे?": "Where is the railway station?",
                "मला टॅक्सी हवी आहे": "I need a taxi",
                "कुठे जायचं आहे?": "Which way to go?",
                "तिकीट बुक करा": "Book a ticket",
                "किराया किती आहे?": "What is the fare?",
                "वेळ किती आहे?": "What time is it?",
                "इथे कुठे जायचं आहे?": "Where to go here?",
                "पासपोर्ट दाखवा": "Show your passport"
            },
            "Dining": {
                "कृपया मला मेन्यू द्या": "Please give me the menu",
                "मी शाकाहारी आहे": "I want vegetarian food",
                "मला पाणी हवं आहे": "I need water",
                "हे अतिशय स्वादिष्ट आहे": "This tastes very good",
                "बिल आणा": "Please bring the bill",
                "चांगला बिर्याणी कुठे आहे?": "Where is good biryani?",
                "मला अजून पाणी द्या": "I want some more water",
                "पिण्याचं पाणी द्या": "Give water to drink",
                "मी मासे खाईन": "I eat fish",
                "तुला माझं बोलणं समजतं का?": "Do you understand me?"
            },
            "Emergency": {
                "मदत करा": "Help",
                "अँब्युलन्सला कॉल करा": "Call an ambulance",
                "आगीची खबर द्या": "Fire",
                "पोलीसांना कॉल करा": "Call the police",
                "मी हरवलो आहे": "I am lost",
                "मला डॉक्टर पाहिजे": "I need a doctor",
                "धोका": "Danger",
                "मी आजारी आहे": "I feel sick",
                "मी जखमी आहे": "I am injured",
                "मदत करा": "Help us"
            }
        }
    },
     "Spanish": {
        "code": "es",
        "phrases": {
            "Most Popular": {
                "Hola": "Hello",
                "Buenos días": "Good morning",
                "¿Cómo estás?": "How are you?",
                "Gracias": "Thank you",
                "Adiós": "Good bye",
                "Por favor": "Please",
                "Perdón": "Excuse me",
                "Lo siento": "I am sorry",
                "De nada": "You are welcome",
                "Buenas noches": "Good night",
                "No, gracias": "No thank you"
            },
            "Basics": {
                "¿Cuál es tu nombre?": "What is your name?",
                "Necesito ayuda": "I need help",
                "¿Cuánto cuesta esto?": "How much is this?",
                "¿Dónde está esto?": "Where is this?",
                "No entiendo": "I don't understand",
                "Agua": "Water",
                "Estoy cansado": "I am tired",
                "¿Dónde está el baño?": "Where is the bathroom?",
                "Habla despacio, por favor": "Speak slowly, please",
                "Estoy perdido": "I am lost"
            },
            "Social": {
                "¿Quieres salir?": "Do you want to go out?",
                "¿Dónde vives?": "Where do you live?",
                "¿Tienes familia?": "Do you have family?",
                "¿Qué haces?": "What do you do?",
                "Me gusta": "I like it",
                "Estoy feliz": "I am happy",
                "¿Qué hora es?": "What time is it?",
                "Estoy ocupado": "I am busy",
                "Cuídate": "Take care",
                "Nos vemos": "See you"
            },
            "Travel": {
                "¿Dónde está el hotel?": "Where is the hotel?",
                "Necesito un taxi": "I need a taxi",
                "¿A qué hora sale el tren?": "What time does the train leave?",
                "¿Dónde puedo comprar un boleto?": "Where can I buy a ticket?",
                "¿Cómo llego al aeropuerto?": "How do I get to the airport?",
                "¿Dónde está la estación de autobuses?": "Where is the bus station?",
                "¿Tiene un mapa?": "Do you have a map?",
                "¿Dónde está la playa?": "Where is the beach?",
                "¿Hay restaurantes cerca?": "Are there restaurants nearby?",
                "¿Puedo ayudarle?": "Can I help you?"
            },
            "Dining": {
                "¿Me trae el menú, por favor?": "Please bring me the menu",
                "Soy vegetariano": "I am vegetarian",
                "Quisiera agua": "I would like water",
                "La comida está deliciosa": "The food is delicious",
                "La cuenta, por favor": "The check, please",
                "¿Me recomienda algo?": "Do you recommend something?",
                "¿Está picante?": "Is it spicy?",
                "No como pescado": "I don't eat fish",
                "¿Hay postres?": "Are there desserts?",
                "¿Pueden ayudarme?": "Can you help me?"
            },
            "Emergency": {
                "¡Ayuda!": "Help!",
                "Llame a una ambulancia": "Call an ambulance",
                "Fuego": "Fire",
                "Llame a la policía": "Call the police",
                "Estoy perdido": "I am lost",
                "Necesito un médico": "I need a doctor",
                "Estoy herido": "I am injured",
                "Es una emergencia": "It is an emergency",
                "Por favor, ayúdeme": "Please help me",
                "Estoy enfermo": "I am sick"
            }
        }
    },
    "French": {
        "code": "fr",
        "phrases": {
            "Most Popular": {
                "Bonjour": "Hello",
                "Bon matin": "Good morning",
                "Comment ça va?": "How are you?",
                "Merci": "Thank you",
                "Au revoir": "Good bye",
                "S'il vous plaît": "Please",
                "Excusez-moi": "Excuse me",
                "Je suis désolé": "I am sorry",
                "De rien": "You are welcome",
                "Bonne nuit": "Good night",
                "Non merci": "No thank you"
            },
            "Basics": {
                "Comment vous appelez-vous?": "What is your name?",
                "J'ai besoin d'aide": "I need help",
                "Combien ça coûte?": "How much is this?",
                "Où est-ce?": "Where is this?",
                "Je ne comprends pas": "I don't understand",
                "De l'eau": "Water",
                "Je suis fatigué": "I am tired",
                "Où sont les toilettes?": "Where is the bathroom?",
                "Parlez lentement, s'il vous plaît": "Speak slowly please",
                "Je suis perdu": "I am lost"
            },
            "Social": {
                "Veux-tu sortir?": "Do you want to go out?",
                "Où habitez-vous?": "Where do you live?",
                "As-tu une famille?": "Do you have family?",
                "Que faites-vous?": "What do you do?",
                "J'aime ça": "I like it",
                "Je suis heureux": "I am happy",
                "Quelle heure est-il?": "What time is it?",
                "Je suis occupé": "I am busy",
                "Prends soin de toi": "Take care",
                "À bientôt": "See you"
            },
            "Travel": {
                "Où est l'hôtel?": "Where is the hotel?",
                "J'ai besoin d'un taxi": "I need a taxi",
                "À quelle heure part le train?": "What time does the train leave?",
                "Où puis-je acheter un billet?": "Where can I buy a ticket?",
                "Comment aller à l'aéroport?": "How do I get to the airport?",
                "Où est la gare routière?": "Where is the bus station?",
                "Avez-vous une carte?": "Do you have a map?",
                "Où est la plage?": "Where is the beach?",
                "Y a-t-il des restaurants à proximité?": "Are there restaurants nearby?",
                "Puis-je vous aider?": "Can I help you?"
            },
            "Dining": {
                "Apportez-moi le menu, s'il vous plaît": "Please bring me the menu",
                "Je suis végétarien": "I am vegetarian",
                "Je voudrais de l'eau": "I would like water",
                "La nourriture est délicieuse": "The food is delicious",
                "L'addition, s'il vous plaît": "The check, please",
                "Pouvez-vous me recommander quelque chose?": "Do you recommend something?",
                "Est-ce épicé?": "Is it spicy?",
                "Je ne mange pas de poisson": "I do not eat fish",
                "Y a-t-il des desserts?": "Are there desserts?",
                "Pouvez-vous m'aider?": "Can you help me?"
            },
            "Emergency": {
                "Au secours!": "Help!",
                "Appelez une ambulance": "Call an ambulance",
                "Feu": "Fire",
                "Appelez la police": "Call the police",
                "Je suis perdu": "I am lost",
                "J'ai besoin d'un médecin": "I need a doctor",
                "Je suis blessé": "I am injured",
                "C'est une urgence": "It is an emergency",
                "S'il vous plaît, aidez-moi": "Please help me",
                "Je suis malade": "I am sick"
            }
        }
    },
    "Korean": {
        "code": "ko",
        "phrases": {
            "Most Popular": {
                "안녕하세요": "Hello",
                "좋은 아침": "Good morning",
                "어떻게 지내세요?": "How are you?",
                "감사합니다": "Thank you",
                "안녕히 가세요": "Good bye",
                "제발": "Please",
                "실례합니다": "Excuse me",
                "죄송합니다": "I am sorry",
                "천만에요": "You are welcome",
                "안녕히 주무세요": "Good night",
                "괜찮아요": "No thank you"
            },
            "Basics": {
                "이름이 뭐에요?": "What is your name?",
                "도움이 필요해요": "I need help",
                "이거 얼마에요?": "How much is this?",
                "이거 어디에요?": "Where is this?",
                "이해하지 못했어요": "I don't understand",
                "물": "Water",
                "저는 피곤해요": "I am tired",
                "화장실 어디에요?": "Where is the bathroom?",
                "천천히 말해 주세요": "Speak slowly please",
                "길을 잃었어요": "I am lost"
            },
            "Social": {
                "밖에 나가고 싶어요?": "Do you want to go out?",
                "어디에 살아요?": "Where do you live?",
                "가족이 있나요?": "Do you have family?",
                "무엇을 하세요?": "What do you do?",
                "좋아해요": "I like it",
                "저는 행복해요": "I am happy",
                "지금 몇 시에요?": "What time is it?",
                "바빠요": "I am busy",
                "조심하세요": "Take care",
                "또 봐요": "See you"
            },
            "Travel": {
                "호텔 어디에요?": "Where is the hotel?",
                "택시가 필요해요": "I need a taxi",
                "기차 언제 출발해요?": "What time does the train leave?",
                "티켓 어디서 사요?": "Where can I buy a ticket?",
                "공항 어떻게 가요?": "How do I get to the airport?",
                "버스 정류장 어디에요?": "Where is the bus station?",
                "지도 있어요?": "Do you have a map?",
                "해변 어디에요?": "Where is the beach?",
                "근처에 식당 있어요?": "Are there restaurants nearby?",
                "도와줄까요?": "Can I help you?"
            },
            "Dining": {
                "메뉴 주세요": "Please give me the menu",
                "저는 채식주의자예요": "I am vegetarian",
                "물 주세요": "I want water",
                "음식이 맛있어요": "The food is delicious",
                "계산서 주세요": "The check, please",
                "추천해 주세요": "Do you recommend something?",
                "매운가요?": "Is it spicy?",
                "저는 생선 안 먹어요": "I don't eat fish",
                "디저트 있어요?": "Are there desserts?",
                "도와줄 수 있어요?": "Can you help me?"
            },
            "Emergency": {
                "도와주세요": "Help!",
                "구급차 불러 주세요": "Call an ambulance",
                "불이 났어요": "Fire",
                "경찰을 불러 주세요": "Call the police",
                "길을 잃었어요": "I am lost",
                "의사가 필요해요": "I need a doctor",
                "부상당했어요": "I am injured",
                "응급 상황이에요": "It is an emergency",
                "도와주세요": "Please help me",
                "아파요": "I am sick"
            }
        }
    }
    
}


       
    curr_lang = tk.StringVar(value=list(languages.keys())[0])
    curr_cat = tk.StringVar()

    tab_frame = tk.Frame(popup, bg="#eeedf2")
    tab_frame.pack(fill="x", pady=(16, 4))

    category_frame = None
    phrase_frame = None

    categories = ["Most Popular", "Basics", "Social", "Travel", "Dining", "Emergency"]  # Add others as needed

    def update_languages():
        for widget in tab_frame.winfo_children():
            widget.destroy()
        for lang in languages:
            btn = tk.Button(
                tab_frame, text=lang,
                font=("Arial", 9, "bold"),
                relief="groove",
                bg="#8f7dd5" if lang == curr_lang.get() else "#8f7dd5",
                fg="white" if lang == curr_lang.get() else "#22223b",
                command=lambda n=lang: [curr_lang.set(n), update_categories(n), update_phrases(n, None)]
            )
            btn.pack(side="left", padx=4, pady=3)
        update_categories(curr_lang.get())

    def update_categories(lang):
        nonlocal category_frame
        if category_frame:
            category_frame.destroy()
        category_frame = tk.Frame(popup, bg="#feffff")
        category_frame.pack(fill="x", pady=(2, 4))
        curr_cat.set(categories[0])
        for cat in categories:
            btn = tk.Button(
                category_frame, text=cat,
                font=("Arial", 10),
                relief="ridge",
                bg="#8f7dd5" if cat == curr_cat.get() else "#8f7dd5",
                fg="white" if cat == curr_cat.get() else "#22223b",
                command=lambda c=cat: [curr_cat.set(c), update_phrases(lang, c)]
            )
            btn.pack(side="left", padx=4, pady=2)
        update_phrases(lang, categories[0])

    def update_phrases(lang, category):
        nonlocal phrase_frame
        if phrase_frame:
            phrase_frame.destroy()
        phrase_frame = tk.Frame(popup, bg="#78a6e6")
        phrase_frame.pack(fill="both", expand=True, padx=18, pady=12)
        if not category:
            category = curr_cat.get()
        phrases_dict = languages[lang]["phrases"].get(category, {})
        if not phrases_dict:
            label = tk.Label(phrase_frame, text=f"No phrases available for {category}", bg="#f7f9fc", font=("Arial", 12))
            label.pack(pady=10)
            return
        for local, eng in phrases_dict.items():
            row = tk.Frame(phrase_frame, bg="#f7f9fc")
            row.pack(fill="x", pady=4)
            tk.Label(row, text=local, width=30, anchor="w", font=("Arial", 11, "bold"), bg="#f7f9fc").pack(side="left")
            tk.Label(row, text=eng, width=26, anchor="w", font=("Arial", 11), bg="#e7df4e").pack(side="left")
            btn = tk.Button(row, text="🔊", width=3,
                            font=("Arial", 11), bg="#5234c8", fg="white", relief="groove",
                            command=lambda t=local, l=languages[lang]["code"]: speak_phrase(t, l))
            btn.pack(side="left", padx=8)

    def speak_phrase(text, lang_code):
        try:
            from gtts import gTTS
            import tempfile
            import sys
            speech = gTTS(text=text, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=True) as fp:
                fname = fp.name + ".mp3"
                speech.save(fname)
                if sys.platform.startswith("win"):
                    os.system(f'start {fname}')
                elif sys.platform.startswith("darwin"):
                    os.system(f"afplay {fname}")
                else:  # Linux
                    os.system(f"mpg123 {fname}")
        except Exception as e:
            messagebox.showerror("Speak Error", f"Could not speak phrase: {e}")

    back_btn = tk.Button(
        popup, text="Back", font=("Arial", 12, "bold"),
        command=popup.destroy, bg="#dc3545", fg="white", relief="ridge", padx=19, pady=6
    )
    back_btn.pack(side="bottom", pady=10)

    update_languages()


# Add this Learn Mode button to your main UI
learn_mode_btn = tk.Button(
    root,
    text="🎓Learn Mode",
    font=("Arial", 10, "bold"),
    bg="#141413",
    fg="#F3F3F3",
    relief="ridge",
    cursor="hand2",
    width=10,
    height=2,
    command=show_learn_mode
)
learn_mode_btn.place(x=270, y=565)



root.mainloop()


