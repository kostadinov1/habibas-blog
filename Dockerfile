FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /blog_app
COPY ./requirements.txt /blog_app/
RUN pip install -r requirements.txt
COPY . /blog_app/
