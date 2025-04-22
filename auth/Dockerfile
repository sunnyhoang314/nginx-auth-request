FROM python:3.9-slim

WORKDIR /app

COPY auth.py .
RUN pip install flask

EXPOSE 5000

CMD ["python", "auth.py"] 