from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    if request.method == "POST":  # if we posted the form
        print("FORM DATA RECEIVED")
        # here are 2 forms to make sure this file exist :
        if "file" not in request.files:  # no file exist/ uploaded
            print(" Debug: Line 1")
            return redirect(request.url)  # redirect the user to the home page

        file = request.files['file']  # if file exist it will give me that file
        if file.filename == "":  # if file is blank/empty, return to the main page
            print(" Debug: Line 2")
            return redirect(request.url)

        if file:
            print(" Debug: Line 3")
            recognizer = sr.Recognizer()  # initilaize instance of the speech recognition class
            audioFile = sr.AudioFile(file)  # pass in the file
            with audioFile as source:  # reading the file
                data = recognizer.record(source)  # through the recognizer
            transcript = recognizer.recognize_google(data, key=None)  # using Google API will return the text

    return render_template('index.html', transcript=transcript)


# create an audio file from the file initially created
# then initialize an instance from the speech recognition class
# then pass that audio file into the record function of the recognizer module
# which will parse the audio file and convert it to understandable format
# which allows us to apply our function: recognize

if __name__ == '__main__':
    app.run(debug=True, threaded=True)  # multiple requests at the ame time for the file
