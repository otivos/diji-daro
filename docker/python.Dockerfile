FROM python:3.9.13

# specify the working directory inside the container
WORKDIR /user/src/app

# installs the Python dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copies the contents of our app inside the container
COPY ./server/app .

# defines environment variables
ENV FLASK_APP=application.py
#watch application files
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

#running Flask as a module
# sleep 5 ensures the database is fully instantiated before running our app.
CMD ["sh", "-c", "sleep 5 \
    && python3 -m flask run --host=0.0.0.0"]