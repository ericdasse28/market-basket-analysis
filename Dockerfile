FROM python:3.10

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./models/associations_rules.pkl ./models/associations_rules.pkl
COPY src/serve.py src/serve.py

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", server:app]