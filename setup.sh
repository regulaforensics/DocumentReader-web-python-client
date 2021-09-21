python3 -m venv venv

source venv/bin/activate

pip install -e ./

cd example || exit

python3 example.py
