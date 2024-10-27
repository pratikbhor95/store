FROM python:alpine3.19


WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
RUN python manage.py makemigrations
ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver" , "0.0.0.0:8000"]