import speech_recognition as sr

# Fungsi untuk melakukan transkripsi
def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Merekam audio dari file

        try:
            text = recognizer.recognize_google(audio_data)  # Melakukan transkripsi menggunakan Google Web API
            print("Transkripsi:", text)
        except sr.UnknownValueError:
            print("Google Web API tidak dapat mengenali audio")
        except sr.RequestError as e:
            print("Terjadi kesalahan pada Google Web API; {0}".format(e))

# Memberikan path file audio yang ingin di-transcribe
audio_file_path = 'output.wav'

# Melakukan transkripsi
transcribe_audio(audio_file_path)
