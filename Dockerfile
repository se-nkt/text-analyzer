FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY analyzer.py test_analyzer.py ./
CMD ["python", "analyzer.py"]
