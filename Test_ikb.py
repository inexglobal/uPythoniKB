from time import sleep				                       # ผนวกชุดคำสั่งหน่วงเวลาของ sleep		
import ikb       					                           # ผนวกชุดคำสั่งจากไลบรารี ikb
k = ikb.IKB()                                     # กำหนดการใช้งาน I2C ของ ikb
k.begin()                                            # เริ่มต้นใช้งาน ikb
k.input(0)                                           # คำสั่งใช้งานอินพุตจากพอร์ตหมายเลข 0
k.output(1,1) 			                                 # คำสั่งใช้งานเอาต์พุตจากพอร์ตหมายเลข 1
if k.input(0) == 0 :                                 # ค่าอินพุตมีค่าเท่ากับ 0 หรือ กดสวิตช์ค้าง
  k.output(1,1)			                                   # สั่งค่าลอจิกเอาต์พุตเท่ากับ 1 หรือ ไฟ led ติด
elif k.input(0) == 1 :                               # ค่าอินพุตมีค่าเท่ากับ 1 หรือ ไม่ได้กดสวิตช์
  k.output(1,0)				                                 # สั่งค่าลอจิกเอาต์พุตเท่ากับ 0 หรือ ไฟ led ดับ
  k.analog(2)                                          # คำสั่งใช้งานอ่านค่าแอนาลอกจากพอร์ตหมายเลข 2
print(k.analog(2))                                   # แสดงค่าที่ตรวจจับได้จากพอร์ตหมายเลข 2
k.motor(1,100)                                       # คำสั่งควบคุมมอเตอร์ด้านซ้ายให้เดินหน้า 100 %
k.motor(2,-100) 	                                   # คำสั่งควบคุมมอเตอร์ด้านขวาให้ถอยหลัง 100 %
sleep(1)                                             # หน่วงเวลา 1 วินาที
k.servo(15,0) 	                                     # คำสั่งควบคุมเซอร์โวมอเตอร์พอร์ต 15 ให้หมุนไปที่มุม 0 องศา
sleep(1)                                             # หน่วงเวลา 1 วินาที
k.servo(15,90)                                       # คำสั่งควบคุมเซอร์โวมอเตอร์พอร์ต 15 ให้หมุนไปที่มุม 90 องศา
sleep(1)                                             # หน่วงเวลา 1 วินาที
k.fd(100) 
sleep(1)                                             
k.bk(80) 	
sleep(1)                             
k.sl(60) 	 
sleep(1) 
k.sr(40) 	   
sleep(1) 
k.tl(60) 	 
sleep(1)                                       
k.fd2(100,50) 	                                     # เดินหน้าแบบปรับความเร็วแต่ละมอเตอร์ ล้อซ้าย 100 % ล้อขวา 50 %
sleep(1) 
k.bk2(55,50) 	                                       # ถอยหลังแบบปรับความเร็วแต่ละมอเตอร์ ล้อซ้าย 55 % ล้อขวา 50 %
sleep(1) 
k.stop()	                                           # หยุดเคลื่อนที่
