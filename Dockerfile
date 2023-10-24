FROM python:3.11.5
 
WORKDIR /app
 
ADD . /app
 
RUN pip install -r requirements.txt

CMD python app.py