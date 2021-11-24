
FROM python:3.9.5


WORKDIR /code


COPY ./ /code/service_a


WORKDIR /code/service_a


RUN pip install --no-cache-dir --upgrade -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]