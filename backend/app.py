from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Connect to Redis using the Service Name we defined in Step 2
redis_host = os.environ.get('REDIS_HOST', 'redis-service')
cache = Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    # Increment the counter in Redis
    count = cache.incr('hits')
    # Return the count to the browser
    return f"Hello! You have visited this page {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
