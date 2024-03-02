import serial
import time

from loguru import logger


class SerialSetting:

    def __init__(self):
        self.serial_port = None

    def connect(self, port, baudrate, timeout=1):
        try:
            # self.serial_port = serial.Serial(port, baudrate, timeout=timeout)
            # self.serial_port.write(data='ping')
            # data = self.serial_port.readline()
            #
            # if data == 'pong':
            #     return True

            return True

        except Exception as e:
            logger.debug(f"{self.__class__.__name__} except occur as {e}")
            return False

