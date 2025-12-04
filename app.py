import os
import logging
import time
import random
from flask import Flask

app = Flask(__name__)

# Configure Logging to show up in Azure Log Stream
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    # Log a standard information message
    app.logger.info("Home page accessed successfully.")
    return "<h1>Operations Lab</h1><p>System Online. Visit <a href='/crash'>/crash</a> to test errors.</p>"

@app.route('/crash')
def crash():
    # Log a warning before the crash
    app.logger.warning("User is attempting to access the unstable route!")
    
    # Simulate a calculation error (Division by Zero)
    result = 10 / 0 
    return f"Result is {result}"

@app.route('/slow')
def slow():
    # Simulate a slow database query
    app.logger.info("Starting heavy process...")
    time.sleep(5)
    app.logger.info("Heavy process finished.")
    return "This page loaded slowly."

if __name__ == '__main__':
    app.run()
