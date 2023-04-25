from flask import Flask
from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv('.env') # take environment variables from .env.
app = Flask(__name__)
redisDb = Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))

@app.route('/')
def welcome():
#    redisDb.incr('visitorCount')
#    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
#    return "Welcome to My Flask App! - VisitorCount: " + visitCount
    return "Welcome to My Flask App! - Currently running in : " + os.environ.get("ENVIRONMENT")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)