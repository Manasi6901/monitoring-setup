from flask import Flask
import time
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask Microservice!"

@app.route('/metrics')
def metrics():
    # Simulated metrics
    response = f"""
    custom_requests_total {random.randint(1, 100)}
    custom_response_time_seconds {random.uniform(0.1, 1.0)}
    """
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

