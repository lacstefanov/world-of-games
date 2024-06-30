# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install wget, curl, gnupg2, and unzip
RUN apt-get update && apt-get install -y wget curl gnupg2 unzip

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# Determine the latest compatible version of ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -N "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip && \
    rm chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver

# Give execution permissions to chromedriver
RUN chmod +x /usr/local/bin/chromedriver

# Make port 8771 available to the world outside this container
EXPOSE 8771

# Set the PATH environment variable to include /usr/local/bin
ENV PATH="/usr/local/bin:$PATH"

# Run MainScores.py when the container launches
CMD ["python", "/app/MainScores.py"]