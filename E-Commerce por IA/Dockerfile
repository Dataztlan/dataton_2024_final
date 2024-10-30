# 
FROM python:3.12

# 
WORKDIR /app

# 
COPY . .
# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 80

# 
CMD ["fastapi", "run", "main.py", "--port", "80"]