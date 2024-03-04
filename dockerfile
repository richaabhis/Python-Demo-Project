FROM python:3.9 AS builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirement.txt /app/

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN python -m pip install --upgrade pip

RUN apt-get update -y

RUN pip install --no-cache-dir -r requirement.txt

COPY . /app/

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["manage.py" , "runserver" , "0:8000"]
