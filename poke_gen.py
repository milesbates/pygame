import openai
import requests
import shutil

openai.api_key = "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"
def genImage(type):

    # The text prompt you want to use to generate an image
    prompt = f"A {type} in the style of pokemon pixel art jpg"

    # Generate an image
    response = openai.Image.create(
        prompt=prompt,
        size="512x512",
        response_format="url"
    )
    url = response['data'][0]['url']

    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(f'{type}Sprite.jpg','wb') as f:
            shutil.copyfileobj(res.raw, f)
        print(f'Image sucessfully Downloaded: {type}.jpg')
    else:
        print('Image Couldn\'t be retrieved')

genImage("hornet")


