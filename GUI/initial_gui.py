from tkinter import *
from tkinter import ttk
import serial.tools.list_ports


class InitialGUI:
    def __init__(self, serial_setting_instance):
        self.window = Tk()
        self.serial_setting_instance = serial_setting_instance()
        self.setup_ui()
        self.window.mainloop()

    def setup_ui(self):
        """ set UI component """
        self.window.title("Serial Connection")

        # dropdown for setting serial port
        self.setup_serial_port_dropdown()

        # dropdown for setting baudrate
        self.setup_baudrate_dropdown()

        # 'Connect' button
        self.connect_button = Button(self.window, text="Connect", command=self.on_connect)
        self.connect_button.grid(column=1, row=2)

    def setup_serial_port_dropdown(self):
        """ set serial port """
        self.port_label = Label(self.window, text="Serial Port:")
        self.port_label.grid(column=0, row=0)

        self.port = StringVar(self.window)
        ports = self.get_serial_ports()
        self.port_dropdown = ttk.Combobox(self.window, textvariable=self.port, values=ports)
        if ports:
            self.port.set(ports[0])
        self.port_dropdown.grid(column=1, row=0)

    def setup_baudrate_dropdown(self):
        """보드레이트 선택 드롭다운 메뉴를 설정합니다."""
        self.baudrate_label = Label(self.window, text="Baud Rate:")
        self.baudrate_label.grid(column=0, row=1)

        self.baudrate = StringVar()
        self.baudrate.set("9600")
        self.baudrate_dropdown = OptionMenu(self.window, self.baudrate, "9600", "19200", "38400", "57600", "115200")
        self.baudrate_dropdown.grid(column=1, row=1)

    def get_serial_ports(self):
        """사용 가능한 시리얼 포트 목록을 반환합니다."""
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def on_connect(self):
        """'Connect' 버튼 클릭 이벤트 핸들러입니다."""
        port = self.port.get()
        baudrate = self.baudrate.get()
        self.serial_setting_instance.connect(port, int(baudrate))
