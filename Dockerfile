# Use official Python image as the base
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirement files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project files
COPY . .

# Expose port for the API
EXPOSE 8000

# Run the API
CMD ["python", "app.py"]
