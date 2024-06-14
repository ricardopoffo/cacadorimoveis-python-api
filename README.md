# Cacadorimoveis API
- This API was developed with [flask](https://flask.palletsprojects.com/en/3.0.x/)

## Setup

### Virtual Environment (Optional)
- Create and activate
```
python -m venv .venv
source myenv/bin/activate
``` 

### Install dependencies
`pip install -r requirements.txt`

### Create database
```shell
flask shell
db.create_all()
db.session.commit()
exit()
```

## Run the application
```shell
python -m flask --app app run --port 8000 --debug
```