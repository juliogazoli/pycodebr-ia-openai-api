from decouple import config
from openai import OpenAI


client = OpenAI(
    api_key=config('API_KEY'),
)

audio_file = open('meu_audio.mp3', 'rb')

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file,
)

print(transcription.text)
