#  Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project file
COPY . .

# Expose ports
EXPOSE 8000 8501

# Start both FastAPI and Streamlit in parallel
CMD ["bash", "-c", "uvicorn api_main:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
