FROM python:latest
ADD main.py /
RUN pip install Flask
RUN python2 -m venv venv
RUN export FLASK_APP=main.py
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["main.py"]

