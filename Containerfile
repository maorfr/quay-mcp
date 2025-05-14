FROM registry.redhat.io/ubi9/python-311

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY quay_mcp_server.py ./

CMD ["python", "quay_mcp_server.py"] 