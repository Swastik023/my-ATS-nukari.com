# Stage 1: Build React Frontend
FROM node:18-alpine AS build

WORKDIR /app

# Install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy and build the React application
COPY frontend/ ./
RUN npm run build

# Stage 2: Setup Flask Backend
FROM python:3.9-slim

WORKDIR /app

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Copy the built React frontend from the previous stage
COPY --from=build /app/build /app/frontend/build

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
