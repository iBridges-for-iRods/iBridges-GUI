import sys
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QLineEdit
from PyQt6.uic import loadUi

from gui.ui_files.irodsLogin import Ui_irodsLogin
from ibridges import Session
from ibridges.session import LoginError

class IrodsLoginWindow(QDialog, Ui_irodsLogin):
    """Definition and initialization of the iRODS login window.

    """

    def __init__(self, session_dict):
        super().__init__()
        if getattr(sys, 'frozen', False):
            super().setupUi(self)
        else:
            loadUi("gui/ui_files/irodsLogin.ui", self)

        self.session_dict = session_dict
        self.irods_path = Path('~', '.irods').expanduser()
        self._init_envbox()
        self.cached_pw = self._init_password()
        self._load_gui()
        self.setWindowTitle("Connect to iRODS server")

    def _load_gui(self):
        """

        """
        self.connectButton.clicked.connect(self.login_function)
        self.cancelButton.clicked.connect(self.close)
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

    def _init_envbox(self):
        env_jsons = [
            path.name for path in
            self.irods_path.glob('irods_environment*json')]
        if len(env_jsons) == 0:
            self.envError.setText(f'ERROR: no "irods_environment*json" files found in {self.irods_path}')
        self.envbox.clear()
        self.envbox.addItems(env_jsons)
        self.envbox.setCurrentIndex(0)

    def _init_password(self):
        #Check if there is a cached password
        passwdFile = self.irods_path.joinpath('.irodsA')
        if passwdFile.is_file():
            self.passwordField.setText("***********")
            return True
        return False

    def close(self):
        self.done(0)

    def login_function(self):
        self.passError.clear()
        env_file = self.irods_path.joinpath(self.envbox.currentText())
        try:
            if self.cached_pw is True and self.passwordField.text() == "***********":
                self.session = Session(irods_env=env_file)
            else:
                self.session = Session(irods_env=env_file, password=self.passwordField.text())
            self.session_dict['session'] = self.session
            self.close()
        except LoginError as e:
            self.passError.setText(repr(e))
        except:
            raise()
            self.passError.setText("Unknown Error")

