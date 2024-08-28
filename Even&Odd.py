import threading

def both_numbers(start, step):
    for i in range(start, 201, step):
        print(f"{threading.current_thread().name}: {i}")
        threading.Event().wait(0.5)
    
        
even_thread = threading.Thread(target=both_numbers, args=(2, 2), name="Even")
odd_thread = threading.Thread(target=both_numbers, args=(1, 2), name="Odd")

odd_thread.start()
even_thread.start()


odd_thread.join()
even_thread.join()