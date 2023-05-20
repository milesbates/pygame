import openai
import requests
import os
import shutil

openai.api_key = "key"

def makePokemon(type):
    genImage(type)
    return genMoves(type)


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
    dir_path = "images\AISprites"
    if res.status_code == 200:
        with open(os.path.join(dir_path,f'{type}Sprite.jpg'),'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print(f'Image sucessfully Downloaded: {type}.jpg')
    else:
        print('Image Couldn\'t be retrieved')
    
def genMoves(type):
    import os
    import openai
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"Imagine you are creating new Pokemon moves for a {type}. Please generate four moves, formatted as a list separated by commas [with no period at the end and no linebreaks], with solely their name."}
    ]
    )

    print(completion.choices[0].message)

    



