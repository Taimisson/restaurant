import sys
from PySide6.QtWidgets import QApplication
from views.tela_principal import TelaPrincipal

def main():
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()