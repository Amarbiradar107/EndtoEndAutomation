FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the repository
COPY . .

# default command when the container is run
CMD ["pytest", "-vs"]