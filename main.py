from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from utils import process_image
from pathlib import Path

import requests

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://jamshid.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODERN_GAME_ID = "1"
CLASSIC_GAME_ID = "2"


async def is_valid_token(token):
    """
    :description: Checks if the token is valid from jamshid main api
    :param token: pure token
    :return: True if the token is valid, False otherwise
    """
    headers = {'Authorization': f'Bearer {token}'}
    api_endpoint = 'https://api.mafia.jamshid.app/auth/check-token'
    response = requests.post(api_endpoint, headers=headers)
    response_json = response.json()
    print(response_json["status"])
    if response_json["status"] == 200 or response_json["status"] == 201:
        return True
    elif response_json["status"] == 500:
        return False


@app.get("/roles/{game_id}/{role_id}")
async def get_role_image(game_id: str, role_id: str, token: str = Header(...)):
    """
    :description: Get image of roles from jamshid main api when token is valid<br>
    :param game_id: 1 for modern, 2 for classic<br>
    :param role_id: <br>
    :param token: jwt token <br>
    :return: image of role<br>
    """
    try:
        _, received_token = token.split()
    except Exception as err:
        return "Invalid Input: " + str(err)

    authentication = await is_valid_token(received_token)
    image_path = None

    if authentication is True:
        if game_id == MODERN_GAME_ID:
            image_path = Path(f'static/roles/modern/{role_id}.jpg')
        elif game_id == CLASSIC_GAME_ID:
            image_path = Path(f'static/roles/classic/{role_id}.jpg')
        else:
            raise HTTPException(status_code=404, detail="Invalid Game id")
        if not image_path.is_file():
            raise HTTPException(status_code=404, detail="Invalid Role id")
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
    return FileResponse(process_image(image_path, 50))


@app.get("/cards/{card_id}")
async def get_card_image(card_id: str, token: str = Header(...)):
    """
    :description: Get image of last move cards from jamshid main api when token is valid<br>
    :param card_id: <br>
    :param token: jwt token <br>
    :return: image of last move card<br>
    """

    try:
        _, received_token = token.split()
    except Exception as err:
        return "Invalid Input: " + str(err)

    authentication = await is_valid_token(received_token)
    image_path = None
    if authentication is True:
        image_path = Path(f'static/cards/{card_id}.jpg')
        if not image_path.is_file():
            raise HTTPException(status_code=404, detail="Invalid card id")
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
    return FileResponse(process_image(image_path, 50))
