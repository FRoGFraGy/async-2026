from time import sleep, ctime, time
import multiprocessing

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

    # สร้าง Process สำหรับแต่ละลูกค้า
    print(f"{ctime()} | === Multi-processing Coffee Machine ===")
    processes = []
    for customer in queue:
        process = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(process)
        process.start()

    # รอให้ Process ทั้งหมดเสร็จสิ้น
    for process in processes:
        process.join()

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:0.2f} seconds")

if __name__ == "__main__":
    main()