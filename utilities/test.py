from utilities.logger import Utilities

log = Utilities().custom_logger()

log.info("This is an info message")
log.warning("This is a warning message")
log.error("This is an error message")