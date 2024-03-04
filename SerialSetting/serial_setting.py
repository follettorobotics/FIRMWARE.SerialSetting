import time

import serial

from loguru import logger


class SerialSetting:

    def __init__(self):
        self.serial_port = None

    def connect(self, port, baudrate, timeout=1):
        try:
            self.serial_port = serial.Serial(port, baudrate, timeout=timeout)
            time.sleep(1)
            self.serial_port.write(data=b'\x00')
            data = self.serial_port.readline()
            data = data.decode('utf-8').strip()

            if data == 'success':
                return True

            return False

        except Exception as e:
            logger.debug(f"{self.__class__.__name__} except occur as {e}")
            return False

    def write(self, data):
        if self.serial_port and self.serial_port.isOpen():
            self.serial_port.write(data.encode())
            return True

