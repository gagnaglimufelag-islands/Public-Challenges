FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY flag .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0"]