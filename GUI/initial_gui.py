import tkinter as tk
from tkinter import ttk, messagebox

import serial.tools.list_ports

from SerialSetting.serial_setting import SerialSetting


class InitialGUI:
    def __init__(self, serial_setting_instance=SerialSetting):
        self.window = tk.Tk()
        self.serial_setting_instance = serial_setting_instance()
        self.setup_ui()
        self.window.mainloop()

        # components for UI
        self.connect_button = None
        self.port_label = None
        self.port = None
        self.port_dropdown = None
        self.baudrate_label = None
        self.baudrate = None
        self.baudrate_dropdown = None
        self.tcp_frame = None
        self.ip_entry = None
        self.mac_entry = None
        self.status_message_label = None

    def setup_ui(self):
        """ set UI component """
        self.window.title("Serial Connection")

        # dropdown for setting serial port
        self.setup_serial_port_dropdown()

        # dropdown for setting baudrate
        self.setup_baudrate_dropdown()

        # 'Connect' button
        self.connect_button = tk.Button(self.window, text="Connect", command=self.on_connect)
        self.connect_button.grid(column=2, row=0, rowspan=2, sticky='e', padx=10)

        # TCP set UI (hided)
        self.setup_tcp_settings_ui()

        self.status_message_label = tk.Label(self.window, text="message", bg="lightgrey", width=50)
        self.status_message_label.grid(column=0, row=4, columnspan=3, sticky='ew', padx=10, pady=10)

    def setup_serial_port_dropdown(self):
        """ set serial port """
        self.port_label = tk.Label(self.window, text="Serial Port:")
        self.port_label.grid(column=0, row=0)

        self.port = tk.StringVar(self.window)
        ports = self.get_serial_ports()
        self.port_dropdown = ttk.Combobox(self.window, textvariable=self.port, values=ports)
        if ports:
            self.port.set(ports[0])
        self.port_dropdown.grid(column=1, row=0)

    def setup_baudrate_dropdown(self):
        self.baudrate_label = tk.Label(self.window, text="Baud Rate:")
        self.baudrate_label.grid(column=0, row=1)

        self.baudrate = tk.StringVar()
        self.baudrate.set("9600")
        self.baudrate_dropdown = tk.OptionMenu(self.window, self.baudrate, "9600", "19200", "38400", "57600", "115200")
        self.baudrate_dropdown.grid(column=1, row=1)

    @staticmethod
    def get_serial_ports():
        """ return available serial ports """
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def on_connect(self):
        """'Connect' button handler """
        port = self.port.get()
        baudrate = self.baudrate.get()
        if self.serial_setting_instance.connect(port, int(baudrate)):
            self.tcp_frame.grid()
        else:
            messagebox.showerror("Connection Failed", "Unable to establish a serial connection.")

    def setup_tcp_settings_ui(self):
        """ UI for tcp connector """
        self.tcp_frame = tk.Frame(self.window)
        self.tcp_frame.grid(column=0, row=3, columnspan=2, sticky='ew')

        # IP address
        tk.Label(self.tcp_frame, text="IP Address:").grid(column=0, row=0)
        self.ip_entry = tk.Entry(self.tcp_frame)
        self.ip_entry.grid(column=1, row=0)

        # MAC address
        tk.Label(self.tcp_frame, text="MAC Address:").grid(column=0, row=1)
        self.mac_entry = tk.Entry(self.tcp_frame)
        self.mac_entry.grid(column=1, row=1)

        # hide option
        self.tcp_frame.grid_remove()
