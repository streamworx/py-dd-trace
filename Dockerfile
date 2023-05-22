FROM python:3.9.6-slim-buster #this version works with dd-trace v0.57.3
RUN mkdir app
RUN cd app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["index.py"]
