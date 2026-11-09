import serial
import tm1637

CLK = 5   # GPIO5 (實體第29腳)
DIO = 4   # GPIO4 (實體第7腳)

tm = tm1637.TM1637(clk=CLK, dio=DIO)
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

try:
    print("UART 自傳自收測試，按 Ctrl+C 結束")
    while True:
        msg = input("輸入要傳送的數字或字元（最多4個）: ").strip()[:4]
        if not msg:
            continue

        ser.reset_input_buffer()          # 清掉舊資料
        ser.write(msg.encode())           # 從 TXD 送出
        data = ser.read(len(msg)).decode(errors="ignore")  # 從 RXD 收回

        if data:
            print(f"送出: {msg}   收到: {data}")
            tm.show(data.ljust(4))        # 顯示在七段顯示器
        else:
            print("沒有收到資料，請檢查第 8、10 腳的接線")

except KeyboardInterrupt:
    print("\n結束")

finally:
    tm.write([0, 0, 0, 0])
    ser.close()
