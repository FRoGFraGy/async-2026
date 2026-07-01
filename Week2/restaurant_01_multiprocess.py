import multiprocessing
from time import sleep, time, ctime

def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer}...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} Greeting for Customer-{customer}...Done!")

def customer_private_workflow(customer):
    #take_order(customer)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")

    print(f"{ctime()} [Thread-{customer}] Cooking ...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} [Thread-{customer}] Cooking ...Done!")

    print(f"{ctime()} [Thread-{customer}] Mini Bar ...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} [Thread-{customer}] Mini Bar ...Done!")

if __name__ == "__main__":
    customers = ["A", "B", "C"]  # List of customers to serve
    start_time = time()

    for customer in customers:
        greet_diners(customer)
        
    print(f"\n{ctime()} -> All customers greeted. Splitting into threads for private workflows...\n")

    processes = []
    for customer in customers:
        p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()  # Wait for all processes to complete

    duration = time() - start_time
    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")