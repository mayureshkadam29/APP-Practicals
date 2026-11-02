import logging

# Create a logger and set its level
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="w")

# Set level for each handler
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatters and attach them to handlers
console_format = logging.Formatter("%(levelname)s - %(message)s")
file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages of all severity levels
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

# Log an exception with its stack trace
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Division failed")