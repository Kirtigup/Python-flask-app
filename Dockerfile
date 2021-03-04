FROM python:latest
COPY . /
RUN pip install Flask
RUN python3 -m venv venv
RUN export FLASK_APP=main.py
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["main.py"]



