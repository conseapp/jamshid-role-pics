# jamshid-role-pics


Method = GET

api url = https://roles.api.jamshid.app
api docs = https://roles.api.jamshid.app/docs

usage:

path : https://roles.api.jamshid.app/roles/{game_id}/{role_id}

required header : token
    pass jwt token



install python environment
```console
sudo apt install python3.10-venv
```
initialize environment
```console
python3 -m venv jamshidenv
```
activate environment
```console
source jamshidenv/bin/activate
```
insatll project requirements
```console
pip3 install -r requirements.txt
```
run app
```console
uvicorn main:app --host 0.0.0.0 --port 3455
```
