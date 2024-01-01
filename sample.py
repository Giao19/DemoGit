import serial
import csv

# Số giá trị muốn đọc mỗi lần
num_values_to_read = 5000

# Tạo danh sách để lưu trữ dữ liệu cho mỗi lần đo
measurements = [[]]

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.01)  # Giảm timeout xuống 0.01
ser.reset_input_buffer()
print("Serial OK")

try:
    for i in range(1):  # Chỉ đo 1 lần
        print(f"Starting measurement {i + 1}...")
        while len(measurements[i]) < num_values_to_read:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                measurements[i].append(line)
                print(f"Measurement {i + 1} value: {line}")

except KeyboardInterrupt:
    print("Close all communication.")
    ser.close()

# Lưu dữ liệu vào tệp CSV với 101 cột (1 cột index và 100 cột điện áp)
csv_file = "/home/gianggiao/doan/data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Ghi header cho tệp CSV
    header = ['Index'] + [f'Voltage_{j}' for j in range(1, num_values_to_read + 1)]
    writer.writerow(header)

    # Ghi dữ liệu vào từng hàng
    for i, data in enumerate(measurements, start=1):
        row = [i] + data
        writer.writerow(row)

print(f"Đã viết 1 lần đo vào tệp {csv_file} với tổng cộng {num_values_to_read} giá trị.")

