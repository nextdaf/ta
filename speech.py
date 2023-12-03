import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Adjusting noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 5 seconds...")
        
        recorded_audio = recognizer.listen(source, timeout=5)
        print("Done recording.")

        try:
            print("Recognizing the text...")
            
            # Change language to Indonesian
            text = recognizer.recognize_google(recorded_audio, language="id-ID")
            
            print("Decoded Text: {}".format(text))

            # Tambahkan kondisi untuk mencetak "halo" atau "uhuy" berdasarkan teks yang terdeteksi
            if "halo" in text.lower():
                print("halo")
            elif "leo" in text.lower():
                print("uhuy")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service: {e}")
except Exception as ex:
    print(f"Error during recognition: {ex}")
