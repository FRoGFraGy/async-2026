from time import sleep, ctime, time

def update_cup_number(customer_name):
    print(f"[{ctime()}] กำลังอัปเดตหมายเลขถ้วยสำหรับ {customer_name}")
    sleep(1)  # จำลองเวลาในการอัปเดตหมายเลขถ้วย
    print(f"[{ctime()}] หมายเลขถ้วยสำหรับ {customer_name} อัปเดตเรียบร้อยแล้ว")

def make_coffee(customer_name):
    print(f"[{ctime()}] กำลังทำกาแฟให้ {customer_name}")
    sleep(2)  # จำลองเวลาในการทำกาแฟ
    print(f"[{ctime()}] กาแฟสำหรับ {customer_name} พร้อมแล้ว")
    update_cup_number(customer_name)

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    start_time = time()

    # ชงกาแฟทีละงานตามลำดับคิวเดียว (ทีละคน)
    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    print(f"[{ctime()}] ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    main()