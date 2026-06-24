from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)  # จำลองเวลาในการอัปเดตหมายเลขถ้วย
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)  # จำลองเวลาในการทำกาแฟ
    print(f"{ctime()} | Coffee ready for {customer_name}!")
    update_cup_number(customer_name)

def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    start_time = time()

    # สร้าง Thread สำหรับแต่ละลูกค้า
    print(f"{ctime()} | === Multi-threaded Coffee Machine ===")
    threads = []
    for customer in queue:
        thread = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(thread)
        thread.start()

    # รอให้ Thread ทั้งหมดเสร็จสิ้น
    for thread in threads:
        thread.join()

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:0.2f} seconds")

if __name__ == "__main__":
    main()