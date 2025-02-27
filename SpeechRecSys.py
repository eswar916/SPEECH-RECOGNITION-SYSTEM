import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(file_path):
   
    recognizer = sr.Recognizer()

    audio = AudioSegment.from_file(file_path)

    temp_wav_path = "temp.wav"
    audio.export(temp_wav_path, format="wav")

 
    with sr.AudioFile(temp_wav_path) as source:
        audio_data = recognizer.record(source) 
        try:
            
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

if __name__ == "__main__":  # Fixed the naming issue
 
    audio_file_path = input("Please enter the path to the audio file (e.g., audio.wav): ")

    transcription = transcribe_audio(audio_file_path)
    

    print("Transcription:")
    print(transcription)
