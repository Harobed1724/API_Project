FROM python:3.10-slim

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no cache-dir -r requirements.txt

COPY app/ .

COPY Models /app/models

COPY Data /app/Data 

EXPOSE 8000

CMD ["uvicorn", "myapi:app", "--host", "0.0.0.0", "--port"]