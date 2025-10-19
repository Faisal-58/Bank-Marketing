# 1️⃣ Use official Python base image
FROM python:3.11-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Copy project file
COPY . .

# 5️⃣ Expose ports
EXPOSE 8000 8501

# 6️⃣ Start both FastAPI and Streamlit in parallel
CMD ["bash", "-c", "uvicorn api_main:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
