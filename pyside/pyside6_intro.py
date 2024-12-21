from PySide6.QtWidgets import QApplication, QWidget
import PySide6.QtCore
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Prints PySide6 version
logger.info(f"PySide6 version: {PySide6.__version__}")


# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.
