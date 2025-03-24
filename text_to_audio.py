from decouple import config
from openai import OpenAI


client = OpenAI(
    api_key=config('API_KEY'),
)

# Opções de vozes: 'alloy', 'echo', 'fable', 'onyx', 'nova'

response = client.audio.speech.create(
    model='tts-1',
    voice='onyx',
    input='Estou gostando muito desse curso de Inteligência Artificial.',
)

response.write_to_file('meu_audio.mp3')
