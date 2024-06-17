# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Set the PATH environment variable to include /usr/local/bin
ENV PATH="/usr/local/bin:$PATH"  # This is the new line

# Run MainScores.py when the container launches
CMD ["python", "/app/MainScores.py"]