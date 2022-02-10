# Regula Document Reader web API Python 3.5+ client

:bulb: Before you start: if you just want to play with an online demo, visit our [playground](https://api.regulaforensics.com).

:warning: NOTE: for some systems, `python3` and `pip3` commands should be used instead of `python` and `pip`.

:warning: NOTE: If a custom Document Reader endpoint is not specified, demo web API will be used by default.
By sending requests to demo Regula Document Reader web API, 
you agree with our [Privacy Policy](https://regulaforensics.com/en/company/privacy/) 
and [License Agreement](https://downloads.regulaforensics.com/work/SDK/doc/Eula.pdf).

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

### Running the client with demo Regula Document Reader web API

Execute example:
```bash
cd example
python example.py
```

### Running the client with local Regula Document Reader web API installation

Get your [free trial here](https://mobile.regulaforensics.com/). When you receive the `regula.license` file, 
copy it to the [example](../example) folder. Now you are ready for start!

Follow [the instructions](https://docs.regulaforensics.com/develop/doc-reader-sdk/web-service/) to run Regula Document Reader web API.
If the instance has been launched successfully, use the following line command to run the example:

```bash
cd example
API_BASE_PATH="http://127.0.0.1:8080" python example.py
```

### Output 
This sample generates the following text output:
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
Also, it stores [portrait](portrait.jpg) and [document image](document-image.jpg) images in the current folder.
You can modify [this example](../example/example.py) and re-run it to get your own results.
