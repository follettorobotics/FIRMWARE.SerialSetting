import serial
import tkinter

from loguru import logger


class SerialSetting:

    def __init__(self):
        self.serial_prot = None

    def connect(self, port, baudrate, timeout=1):
        try:
            self.serial_prot = serial.Serial(port, baudrate, timeout=timeout)
            return True
        except Exception as e:
            logger.debug(f"{self.__class__.__name__} except occur as {e}")
            return False
