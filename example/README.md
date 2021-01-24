# Regula Document Reader web API Python 3.5+ client

:bulb: Before you start: if you just want to play with an online demo, visit our [playground](https://api.regulaforensics.com).

:warning: NOTE: for some systems `python3` and `pip3` commands should be used, instead of `python` and `pip`.

Requirements:
- installed python 3.5 or higher
- installed [pip](https://pip.pypa.io/en/stable/installing/)

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

### Running with local Regula Document Reader web API installation

Follow [the instructions](https://docs.regulaforensics.com/web/quick-start-guide) to run Regula Document Reader web API. 
Assuming you have successfully launched instance, use next line command to run example:
```bash
cd example
python example.py

# If Regula Document Reader web API is running not on localhost, specify host via env variable:
API_BASE_PATH="http://192.168.0.101:8080" python example.py
```

### Running using Regula Document Reader web API test SaaS

Get your [free trial here](https://mobile.regulaforensics.com/). You should obtain `regula.license` file. 
Copy it to **example** folder. You are ready for running!

Execute example:
```bash
cd example
API_BASE_PATH="https://test-api.regulaforensics.com" python example.py
```

### Output 
This sample generates next text output:
```text
    ---------------------------------------------------------------------------
                   Document Overall Status: not valid
                    Document Number Visual: OO0000000
                       Document Number MRZ: OO0000000
        Validity Of Document Number Visual: 0
           Validity Of Document Number MRZ: 0
              MRZ-Visual values comparison: 1
    ---------------------------------------------------------------------------
```
Also, it creates [portrait](portrait.jpg) and [document image](document-image.jpg) pictures inside current folder.
Edit on your own [example.py](./example.py), and re-run to see your results.
