import serial
ser = serial.Serial('COM5', 9600)  # 請確認 COM3 是否是您的序列埠
def convyor_motor(choice):
    try:
        if choice == 1:
            # print('motor1')
            ser.write(b'w\n')  # 訊息必須是位元組類型 #2
            # 暫停0.5秒，再執行底下接收回應訊息的迴圈
            
        elif choice == 2 :
            # print('motor2')  
            ser.write(b's\n') #3
                
    except KeyboardInterrupt:
        ser.close()
