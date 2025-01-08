import sys
import random # random module for random number generation
from PyQt5.QtWidgets import QApplication,QPushButton,QVBoxLayout,QWidget,QLabel
from PyQt5.QtGui import QPainter,QPen,QIcon
from PyQt5.QtCore import Qt,QSize

class GraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() # call the initUI method - initalize UI
        self.setWindowIcon(QIcon("image.png"))
    
    def initUI(self):
        #Window Title and Window Size
        self.setWindowTitle("Random Number Graph Gnerator")
        self.setFixedSize(600,400)

        #Layout
        layout = QVBoxLayout()

        #Generator Button
        self.button = QPushButton("Generate Graph",self)
        self.button.clicked.connect(self.generate_graph)
        layout.addWidget(self.button)

        #Label to display the graph
        self.label=QLabel("",self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        #Set Layout
        self.setLayout(layout)

        #Data for drawing->random numbers empty and default stop index
        self.random_numbers=[]
        self.stop_index =-1

    def generate_graph(self):

        #Generate Random Numbers
        self.random_numbers = [random.randint(10, 300) for _ in range(10)]
        self.stop_index = random.randint(0, len(self.random_numbers) - 1)
        stop_number = self.random_numbers[self.stop_index]

        self.label.setText(f"Graph stopped at number: {stop_number}")

        self.update()

    def paintEvent(self,event):
        if not self.random_numbers: #if there are no random numbers(empty list)
            return

        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        #Draw the Graph
        width=self.width()-40
        height=self.height()-100
        x_step=width //len(self.random_numbers)
        y_offset=height

        #Pen for Drawing
        pen=QPen(Qt.black,2)
        painter.setPen(pen)

        #To draw the connecting lines
        for i in range(len(self.random_numbers)-1):
            x1 = 20 + i * x_step
            y1 = y_offset - self.random_numbers[i]
            x2 = 20 + (i + 1) * x_step
            y2 = y_offset - self.random_numbers[i + 1]  # Correct
            painter.drawLine(x1, y1, x2, y2)


        for i, num in enumerate(self.random_numbers):
            x=20+i*x_step
            y=y_offset-num
            if i == self.stop_index:
                pen.setColor(Qt.red)
                painter.setPen(pen)
                painter.setBrush(Qt.red)
            else:
                pen.setColor(Qt.black)
                painter.setPen(pen)
                painter.setBrush(Qt.black)
            painter.drawEllipse(x - 5, y - 5, 10, 10)

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphApp()
    window.show()
    sys.exit(app.exec_())