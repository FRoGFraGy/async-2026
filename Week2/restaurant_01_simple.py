from time import sleep, time, ctime

def greet_customer(customer):
    print(f"{ctime()} -> Greeting for Customer-{customer}...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Greeting for Customer-{customer}...Done!")

def take_order(customer):
    print(f"{ctime()} -> Taking Order for Customer-{customer}...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Taking Order for Customer-{customer}...Done!")

def do_cooking(customer):
    print(f"{ctime()} -> Cooking for Customer-{customer}...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Cooking for Customer-{customer}...Done!")

def mini_bar(customer):
    print(f"{ctime()} -> Mini Bar for Customer-{customer}...")
    sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Mini Bar for Customer-{customer}...Done!")

if __name__ == "__main__":  
    customers = ["A", "B", "C", "D"]  # List of customers to serve
    start_time = time()

    for customer in customers:
        greet_customer(customer)
        take_order(customer)
        do_cooking(customer)
        mini_bar(customer)

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:.2f} seconds")