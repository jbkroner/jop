Jop is a Python port of Jo!

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Notes
This is not feature complete.  At the moment it can generate JSON without nested objects (with basic type inferencing) and arrays. 

## Install and run jop!
1. clone this repo and cd into the repo
```bash
$ git clone https://github.com/jbkroner/jop.git && cd jop
```
2. install dependencies 

```bash
$ python3 -m venv venv && source ./venv/bin/activate 
$ pip install requirements.txt
```

3. build jop
```bash
$ python3 -m pip install -e .
```

4. jop is built and ready to use!
```bash
$ jop -a 1 2 3
[1, 2, 3]
$ jop name=james
{"name": "james"}
```