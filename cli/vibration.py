import argparse
import serial
import time

import serial.tools
import serial.tools.list_ports

def send_data(ser, data):
    print(f"Send: {data}")
    ser.write(data.encode())

def read_data(ser):
    # while True:
    if ser.in_waiting > 0:
        data = ser.readline().endcode().strip()
        print(f"Data: {data}")
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description='The program handles command line parameters.')
    parser.add_argument('-p', '--port', help='COM port')
    parser.add_argument('-i', '--id', help='Device id')
    parser.add_argument('-v', '--vibrate', help='Vibrate time')

    args = parser.parse_args()

    print(f'COM: {args.port}')
    print(f'ID: {args.id}')
    print(f'Vibrate: {args.vibrate}')

    # serial.tools.list_ports()
    # Khởi tạo đối tượng serial
    ser = serial.Serial(args.port, 9600)
    # Gửi dữ liệu qua cổng COM với định dạng: "DESTINATION_RADIO_ID VibrationTime Message"
    send_data(ser ,f"{args.id} {args.vibrate} message")
    # Đọc dữ liệu
    # read_data(ser)
    # Đảm bảo rằng chúng ta đã đóng cổng COM
    ser.close()

if __name__ == '__main__':
    main()