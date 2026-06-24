from time import sleep, ctime, time
import os
import threading

def update_cup_number(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] กำลังอัปเดตหมายเลขถ้วยสำหรับลูกค้า {customer_name} ...")
    sleep(1)  # จำลองเวลาในการอัปเดตหมายเลขถ้วย
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] หมายเลขถ้วยสำหรับ {customer_name} อัปเดตเรียบร้อยแล้ว")

def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] กำลังทำกาแฟให้ลูกค้า {customer_name} ...")
    sleep(2)  # จำลองเวลาในการทำกาแฟ
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] กาแฟสำหรับลูกค้า {customer_name} พร้อมแล้ว")
    update_cup_number(customer_name)

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    start_time = time()

    # สร้าง Thread สำหรับแต่ละลูกค้า
    threads = []
    for customer in queue:
        thread = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(thread)
        thread.start()

    # รอให้ Thread ทั้งหมดเสร็จสิ้น
    for thread in threads:
        thread.join()

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    main()