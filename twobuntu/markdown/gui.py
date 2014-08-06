from PyQt5 import QtCore, QtWidgets

from .converter import TwobuntuConverter


class ConversionGUI(QtWidgets.QDialog):
    """
    A graphical interface for performing markdown conversion.
    """

    def __init__(self):
        """
        Initialize the dialog.
        """
        super().__init__()
        self._converter = TwobuntuConverter()
        self.setWindowTitle("2buntu Markdown Converter")
        vbox = QtWidgets.QVBoxLayout()
        # Create the two text controls
        self._original = QtWidgets.QTextEdit()
        self._converted = QtWidgets.QTextEdit()
        self._converted.setReadOnly(True)
        splitter = QtWidgets.QSplitter()
        splitter.addWidget(self._original)
        splitter.addWidget(self._converted)
        vbox.addWidget(splitter)
        # Create the button for performing the conversion
        button = QtWidgets.QPushButton("Convert")
        button.clicked.connect(self._convert)
        vbox.addWidget(button)
        self.setLayout(vbox)

    def _convert(self):
        """
        Perform conversion.
        """
        original = self._original.toPlainText()
        converted = self._converter.convert(original)
        self._converted.setPlainText(converted)
