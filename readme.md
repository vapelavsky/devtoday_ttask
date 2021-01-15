#DevelopsToday Test Task

##Released all subtasks, scheduling released by simple apscheduler

#### How to run it?
```
git clone
virtualenv -p=python3.8 .env
source .env/bin/activate
pip install -r requirements.txt
docker-compose up --build
docker-compose exec web python manage.py migrate --noinput
docker-compose run web gunicorn developstoday_testtask.wsgi:application --bind 127.0.0.1:8000
```

#### Tools for beautiful code in spite of PEP8 convention
```
Black 
flake8
But best of the best is PyCharm IDE where I developed this project,
because I think that this JetBrains product can make your code beautiful as can
as it well
```


###[&lt;Postman collection&gt;](https://www.postman.com/collections/83aa07aa0660073a450f)

###[&lt;Heroku deployed&gt;](https://developstoday-posts.herokuapp.com/)