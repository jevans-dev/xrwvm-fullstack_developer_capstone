FROM python:3.9-slim

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

CMD ["python", "app.py"]
