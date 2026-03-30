from PyQt5.QtWidgets import (
	QMainWindow,
	QWidget,
	QHBoxLayout,
	QVBoxLayout,
	QSplitter,
	QApplication
)
from PyQt5.QtCore import Qt


class __MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("VectorKit")
		self.resize(1000, 700)
		self._init_ui()

	def _init_ui(self):
		central_widget = QWidget()
		self.setCentralWidget(central_widget)

		main_layout = QVBoxLayout(central_widget)
		main_layout.setContentsMargins(0, 0, 0, 0)
		main_layout.setSpacing(0)

		h_splitter = QSplitter(Qt.Horizontal)
		h_splitter.setStyleSheet("QSplitter::handle { background-color: #cccccc; }")

		left_panel = QWidget()
		left_panel.setAutoFillBackground(True)
		left_panel.setStyleSheet("background-color: white;")

		right_panel = QWidget()
		right_panel.setAutoFillBackground(True)
		right_panel.setStyleSheet("background-color: white;")

		h_splitter.addWidget(left_panel)
		h_splitter.addWidget(right_panel)
		h_splitter.setSizes([500, 500])

		bottom_panel = QWidget()
		bottom_panel.setAutoFillBackground(True)
		bottom_panel.setStyleSheet("background-color: white;")

		v_splitter = QSplitter(Qt.Vertical)
		v_splitter.setStyleSheet("QSplitter::handle { background-color: #cccccc; }")
		v_splitter.addWidget(h_splitter)
		v_splitter.addWidget(bottom_panel)
		v_splitter.setSizes([400, 300])

		main_layout.addWidget(v_splitter)
