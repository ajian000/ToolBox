import sys
from PyQt5.QtWidgets import QApplication
from src.main.main_window import __MainWindow


def main():
	app = QApplication(sys.argv)
	window = __MainWindow()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
