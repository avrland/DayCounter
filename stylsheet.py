stylesheet = """
QMainWindow {
    background-color: #1e1e1e;
    color: #f0f0f0;
}

QTabWidget::pane {
    border: none;
    background-color: #1e1e1e;
}

QTabWidget::tab-bar {
    left: 20px;
}

QTabBar::tab {
    background-color: #1e1e1e;
    color: #f0f0f0;
    border: none;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    min-width: 100px;
    padding: 5px;
    margin-right: 5px;
}

QTabBar::tab:selected {
    background-color: #4d4d4d;
}

QLabel {
    color: #f0f0f0;
}

QComboBox {
    background-color: #4d4d4d;
    color: #f0f0f0;
    border: none;
    padding: 5px;
    border-radius: 5px;
}

QComboBox:hover {
    background-color: #656565;
}

QComboBox::drop-down {
    width: 20px;
    height: 20px;
}

QGraphicsView {
    background-color: #1e1e1e;
}
"""



stylesheet_widget = """
QWidget {
    background-color: #1e1e1e;
    color: #f0f0f0;
}

QLabel {
    color: #f0f0f0;
}

QGraphicsView {
    background-color: #1e1e1e;
}
"""