FROM python:3.10

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/app.py /app/
COPY model/ model/
ENV MODEL_PATH=model/

USER analyzer

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", server:app]