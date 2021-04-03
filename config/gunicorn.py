import multiprocessing
import os

port = os.getenv("PORT", "80")

bind = f"0.0.0.0:{port}"
workers = multiprocessing.cpu_count()

accesslog = "-"
errorlog = "-"
loglevel = "info"

graceful_timeout = 120
keepalive = 5
timeout = 60
