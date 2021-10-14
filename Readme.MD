# Metrics Service

## Run project

### Via venv on local machine

* Clone repo && cd to_project_root
* Create virtualenv, example - `mkvirtualenv $(basename "$PWD") -p $(which python3.8)`
* Install requirements - `pip install -r requirements.txt.txt`
* Create database `python manage.py migrate`
* Content database `python manage.py fill_db`
* Start service `python manage.py runserver`


## API usage examples
1. `/metrics/?ordering=-clicks_count&groupby=channel,country&sums=clicks,impressions&date_to=2017-06-01`
2. `/metrics/?ordering=faced_date&groupby=faced_date&sums=installs&date_to=2017-05-31&date_from=2017-05-01`
3. `/metrics/?ordering=-revenue_count&groupby=os&sums=revenue&date_to=2017-06-01&date_from=2017-06-01`
4. `/metrics/?groupby=channel&sums=spend&country=CA`

## TODO
* The fourth case only outputs spend, without CPI

