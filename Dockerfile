FROM python:3.11.5
 
WORKDIR /app

# ADD ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

ADD . /app

# CMD python app.py
CMD ["sh", "app-start-up.sh"]