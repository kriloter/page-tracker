# src/page_tracker/app.py

"""Some module"""
import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """Some function"""
    try:  # pylint: disable=R1705
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}", 500
    else:
        return f"This wonderfull beautifull page 
        has been seen {page_views} times."


@cache
def redis():
    """Some function"""
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
