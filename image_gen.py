from decouple import config
from openai import OpenAI


client = OpenAI(
    api_key=config('API_KEY'),
)

response = client.image.generate(
    model='dall-e-3',
    prompt='Um programador com seu laptop, no estilo futurista.',
    size='1024x1024',
    quality='standard',
    n=1,
)

image_url = response.data[0].url
print(image_url)
