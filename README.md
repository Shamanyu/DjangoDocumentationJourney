# DjangoDocumentationJourney
Document the journey of a software developer through Django 2.1 documentation

- The project is being tracked at
  https://trello.com/b/sOBEaHUT/djangodocumentation

- System setup for Mac 10.12.6

  1) Install Python 3.6.5
    https://www.python.org/downloads/release/python-365/

  2) Upgrade pip to version 10.0.1 for Python 3.6.5
    pip3 install --upgrade pip

  3) Create virtual-environment in project directory
    virtualenv -p /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 venv-3.6

  4) Activate the virtual environment
    source venv-3.6/bin/activate

  5) Create a 'requirements.txt' file in home directory with the only dependency being
    'Django==2.1a1'

  6) Run 'pip install -r requirements.txt' to install Django 2.1.  
