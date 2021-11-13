

To run the project install python version 3.8.5 and higher, redis, postgres 

Clone the repository:
```bash
git clone https://github.com/azazellooo/devices-endpoints-fastapi.git
```

After cloning, go to the cloned folder, create virtual environment and activate it:


```bash
python3 -m virtualenv -p python3 venv
source venv/bin/activate

```

install dependencies:


```bash
pip install -r requirements.txt
```


Create .env file and fill as showed in .env.example .

setup the database:
```bash
python3 create_db.py
```

Run the project with command:
```bash
uvicorn main:app --reload

```
