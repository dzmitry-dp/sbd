import sys
from loguru import logger
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtCore import QPropertyAnimation
# from PyQt5.QtGui import QFont, QFontDatabase

# import config
from qt.window import QtMainWindow
# from db.procurement import ProcurementDataBaseQuery, MySQLwithPandas

def _get_screen_size():
    # размер экрана компьютера 
    screen_geometry= QDesktopWidget().availableGeometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()
    return screen_width, screen_height

class App:
    def __init__(self) -> None:
        logger.info('class App')
        super().__init__()
        # создаю приложение и провожу настройки
        self.app = QApplication(sys.argv)
        # получаю данные о разрешении монитора
        screen_width, screen_height = _get_screen_size()
        self.screen_size = (screen_width, screen_height)
        # центральная точка на мониторе пользователя
        self.center_screen_point = (int(screen_width/2), int(screen_height/2))
        # создаю главное окно
        self.main_window = QtMainWindow(screen_width, screen_height)
        # Класс анимации прозрачности окна
        self.main_window.start_animation = QPropertyAnimation(self, b'windowOpacity')
        self.main_window.start_animation.setDuration(1000)  # Продолжительность: 1 секунда
        self.main_window.start_animation.setStartValue(0)
        self.main_window.start_animation.setEndValue(1)
        self.main_window.start_animation.start()


    def run_qt(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = App()
    # db = ProcurementDataBaseQuery()
    # df = MySQLwithPandas()

    app.run_qt()