FROM python:3.6
LABEL maintainer="Aurélien Hugues <aurelien.hugues.59@gmail.com>"
LABEL version="1.0.0"
LABEL description="Default Docker container for Flask"
ADD web /app/web
COPY app.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]