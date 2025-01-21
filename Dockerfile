FROM python:3-bookworm

RUN pip install psycopg2

WORKDIR /myeco_analytic

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["fastapi", "run", "main.py", "--port", "8001"]