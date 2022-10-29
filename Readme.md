To run docker run -e PORT="8000"  -p 8000:8000 -ti django-docker-app

heroku login
heroku create #secret-plains-63806
heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a limitless-atoll-51647 #for env variable

heroku stack:set container -a limitless-atoll-51647

docker build -t django-docker-app .
docker run -e PORT="8000"  -p 8000:8000 -ti django-docker-app


/companywise/?company=RELIANCE&start_date=2020-01-01&end_date=2021-01-01
