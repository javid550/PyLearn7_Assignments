from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt

class SudokuGrid(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        # self.grid_layout.setSpacing(0)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pen = QPen(QColor("gray"), 2)
        painter.setPen(pen)

        cell_size = 50  # match your QLineEdit size
        for i in range(1, 3):
            # Vertical lines
            x = i * 3 * cell_size
            painter.drawLine(x, 0, x, 9 * cell_size)
            # Horizontal lines
            y = i * 3 * cell_size
            painter.drawLine(0, y, 9 * cell_size, y)
            



# from sudoku_grid import SudokuGrid  # if you move the class to a file
# self.grid_layout_widget = SudokuGrid(self.centralwidget)
# self.grid_layout = self.grid_layout_widget.grid_layout

# from sudoku_grid import SudokuGrid  # You can also define this class inline
# self.gridLayoutWidget = SudokuGrid(self.centralwidget)
# self.gridLayoutWidget.setGeometry(QRect(9, 9, 451, 451))
# self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
# self.grid_layout = self.gridLayoutWidget.grid_layout