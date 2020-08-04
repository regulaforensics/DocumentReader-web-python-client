# Regula Document Reader web API Python 3.5+ client

Before you start: if you just want to play with an online demo, visit our [playground](https://api.regulaforensics.com).

## Running local example

NOTE: for some systems `python3` and `pip3` commands should be used, instead of `python` and `pip`.

Requirements:
- installed python 3.5 or higher
- installed [pip](https://pip.pypa.io/en/stable/installing/)
- running [Regula Document Reader web API with trial license](https://docs.regulaforensics.com/web/quick-start-guide)

Verify Python and pip versions:
```bash
python --version  
> Python 3.8.2
pip --version     
> pip 20.2.1 from /home/user/.local/lib/python3.8/site-packages/pip (python 3.8)
```

Cloning example:
```bash
git clone https://github.com/regulaforensics/DocumentReader-web-python-client.git
cd DocumentReader-web-python-client
```

Setup project and download dependencies:
```bash
pip install -e ./
```

Run example:
```bash
cd example
python example.py

# If Regula Document Reader web API is running not on localhost, also specify host via env variable:
API_BASE_PATH="http://192.168.0.101:8080" python example.py
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
