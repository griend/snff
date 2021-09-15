# Demo03

## Development

### Setup

```shell
cd ~/prj/snff
python3 -m venv venv
source venv/bin/activate
cd ~/prj/snff/demo03
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
cd ~/prj/snff/demo03
docker build --file src/docker/Dockerfile --tag demo03 .
```

## Docker Run

```shell
docker run -d -p 5000:5000 demo03
```
