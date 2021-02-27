# smlr

### Prerequisites
* Install Python (3.9)
* Install Python Package Manager (pip/pip3) :
    ```
    apt-get install python-pip
    ```
    ```
    apt-get install python3-pip
    ```
* Install [virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) :
    ```
    apt-get install virtualenv
    ```
* Install [`mysqlclient`](https://pypi.org/project/mysqlclient/) prerequisites :
    * You may need to install the Python and MySQL development headers and libraries like so:
        ```
        sudo apt-get install python-dev default-libmysqlclient-dev
        ```
    * If you are using python3 then you need to install python3-dev using the following command :
        ```
        sudo apt-get install python3-dev
        ```
    * Install from PyPI:
        ```
        pip install mysqlclient
        ```
* Install [redis](https://redis.io/) :
    ```
    sudo apt-get install redis-server
    ```

### Project Installation

1. Clone the repository - `git clone <remote-url>`
1. Go to the project directory - `cd <cloned-repo>`
1. Set up the environment :
    * Create virtual environment files - `python3 -m venv venv`
    * Activate virtual environment - `source venv/bin/activate`
1. Install dependencies - `pip install -r requirements.txt`
1. Create a database - `smlr`
1. Copy contents of `.env.example` to a new file `.env` - `cp .env.example .env`
    * Set DB_USERNAME and DB_PASSWORD to your localhost mysql credentials
    * `APP_BASE_URL = 'http://localhost:8000'`
    * `API_BASE_URL = 'http://localhost:8000/api'`
1. Make migrations - `python3 manage.py makemigrations`
1. Run migrations - `python3 manage.py migrate`
1. Open a new terminal and start celery workers - `celery -A smlr worker -l info -P gevent -c 200`
1. Start server - `python3 manage.py runserver`


#### Note
* Everytime you install packages or run the server, activate your virtual environment - `source venv/bin/activate`
* To deactivate the activated virtual environment - run the command `deactivate` in terminal.
* If you ran into any errors while running the server with python version incompatabilities, check your python version. Try `python3` instead of `python` while running the server.
* If you install any python packages, please update the file `requirements.txt`
