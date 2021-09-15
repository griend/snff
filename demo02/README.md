# Demo01

## Development

### Setup

```shell
cd ~/prj/snff
python3 -m venv venv
source venv/bin/activate
cd ~/prj/snff/demo02
pip3 install -U pip
pip3 install -r requirements.txt
```

### Run

```shell
export FLASK_ENV=development
flask run
```

## Docker Build

```shell
cd ~/prj/snff/demo02
docker build --file src/docker/Dockerfile --tag demo02 .
```

## Docker Run

```shell
docker run -d -p 5000:5000 demo02
```
