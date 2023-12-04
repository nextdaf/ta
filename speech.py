import wave
import sys
import pyaudio
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILE = 'output.wav'

# Fungsi untuk melakukan transkripsi
def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Merekam audio dari file

        try:
            # Menggunakan recognizer dengan bahasa Indonesia
            text = recognizer.recognize_google(audio_data, language='id-ID')
            print("Transkripsi:", text)

            # Menambahkan kondisi berdasarkan hasil transkripsi
            if 'halo' in text.lower():
                print("Halo Leo!")
            elif 'anjing' in text.lower():
                print("Mulut Anda Kasar!")
        except sr.UnknownValueError:
            print("Google Web API tidak dapat mengenali audio")
        except sr.RequestError as e:
            print("Terjadi kesalahan pada Google Web API; {0}".format(e))

# Merekam suara
with wave.open(OUTPUT_FILE, 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    print('Katakan Sesuatu...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    print('Selesai')

    stream.close()
    p.terminate()

# Melakukan transkripsi pada file output
transcribe_audio(OUTPUT_FILE)
