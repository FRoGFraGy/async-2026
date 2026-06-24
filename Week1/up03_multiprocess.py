from time import sleep, ctime, time
import multiprocessing

def update_cup_number(customer_name):
    print(f"{ctime()} | หมายเลขถ้วยสำหรับลูกค้า {customer_name} อัปเดตเรียบร้อยแล้ว")

def make_coffee(customer_name):
    print(f"{ctime()} | กำลังทำกาแฟให้ลูกค้า {customer_name} ...")
    sleep(2)  # จำลองเวลาในการทำกาแฟ
    print(f"{ctime()} | กาแฟสำหรับลูกค้า {customer_name} พร้อมแล้ว")
    update_cup_number(customer_name)

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    start_time = time()

    # สร้าง Process สำหรับแต่ละลูกค้า
    processes = []
    for customer in queue:
        process = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(process)
        process.start()

    # รอให้ Process ทั้งหมดเสร็จสิ้น
    for process in processes:
        process.join()

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    main()