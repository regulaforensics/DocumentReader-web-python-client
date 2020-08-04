# Regula Document Reader web API Python 3.5+ client

Before you start: if you just want to play with an online demo, visit our [playground](https://api.regulaforensics.com).

## Running local example

Requirements:
- installed python 3.5 or higher
- installed [pipenv](https://pypi.org/project/pipenv)
- running [Regula Document Reader web API with trial license](https://docs.regulaforensics.com/web/quick-start-guide)

Cloning example
```bash
git clone https://github.com/regulaforensics/DocumentReader-web-python-client.git
cd example
```

Setup project and download dependencies:
```bash
pipenv install
```

Run example:
```bash
pipenv run python example.py

# If Regula Document Reader web API is running not on localhost, also specify host via env variable:
API_BASE_PATH="http://192.168.0.101:8080" pipenv run python example.py
```

This sample generates next text output:
```text
    ---------------------------------------------------------------------------
                   Document Overall Status: not valid
                    Document Number Visual: U0996738
                       Document Number MRZ: U0996738
        Validity Of Document Number Visual: 1
           Validity Of Document Number MRZ: 1
              MRZ-Visual values comparison: 1
    ---------------------------------------------------------------------------
```
Also, it creates [portrait](portrait.jpg) and [document image](document-image.jpg) 
pictures inside current folder.

Edit on your own [example.py](./example.py), and re-run to see your results.

## Detailed guide

tbd
