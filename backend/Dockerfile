# Use an official Python image as the base
FROM python:3.14-rc-slim

# Set the working directory to /app
WORKDIR /app

# Copy the application code
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the command to start the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:message_board"]
