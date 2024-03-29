# Jamshid Role & Last Move Pics Api

Simple Api that responses requests from jamshid main server to serve image of roles<br>
with authentication of requested user per request

### Built With
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## Usage

Method = GET

api docs
* https://roles.api.jamshid.app/docs

### roles request path
```console
https://roles.api.jamshid.app/roles/{game_id}/{role_id}
```

### last move cards request path
```console
https://roles.api.jamshid.app/cards/{card_id}
```

### be sure to pass jwt token as "token" in headers
token example
  ```console
  Bearer <token>
  ```


## Deploy

### 1. install python environment
```console
sudo apt install python3.10-venv
```
### 2. initialize environment
```console
python3 -m venv jamshidenv
```
### 3. activate environment
```console
source jamshidenv/bin/activate
```
### 4. install requirements
```console
pip3 install -r requirements.txt
```
### 5. run
```console
uvicorn main:app --host 0.0.0.0 --port 3455
```
