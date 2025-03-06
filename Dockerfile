FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project
COPY . .

# Expose the application port
EXPOSE 8005

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8005", "TinTosh_Web.wsgi:application"]