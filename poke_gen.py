import openai
import requests
import os
import shutil
from PIL import Image

openai.api_key = "key"

def makePokemon(type):
    genImage(type)
    return genMoves(type)


def genImage(type):

    # The text prompt you want to use to generate an image
    prompt = f"A {type} in the style of pokemon pixel art png"

    # Generate an image
    response = openai.Image.create(
        prompt=prompt,
        size="512x512",
        response_format="url"
    )
    url = response['data'][0]['url']

    res = requests.get(url, stream = True)
    dir_path = "images\AISprites"
    if res.status_code == 200:
        with open(os.path.join(dir_path,f'{type}Sprite.png'),'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print(f'Image sucessfully Downloaded: {type}.png')
    else:
        print('Image Couldn\'t be retrieved')
    image = Image.open(os.path.join(dir_path,f'{type}Sprite.png'))
    image = image.convert('RGBA')
    dat = image.getdata()
    newDat = []

    for item in dat:
        if item[0] in list(range(235,256)):
            newDat.append((255,255,255,0))
        else:
            newDat.append(item)
    image.putdata(newDat)
    image.save(os.path.join(dir_path,f'{type}Sprite.png'),"PNG")

    
def genMoves(type):
    rv = "\n"
    while "\n" in rv:
        rv = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Imagine you are creating new Pokemon moves for a {type}. Please generate four moves, formatted as a list separated by commas with no periods and no linebreaks, with solely the name of the move."}
        ]
        ).choices[0].message["content"]

    return rv

    



