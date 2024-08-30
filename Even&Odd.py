import threading

# This method will print both even and odd numbers from 0 to 200
def both_numbers(start, step):
    for i in range(start, 201, step):
        # Print the current number and the name of the thread that is printing it
        print(f"{threading.current_thread().name}: {i}")
        threading.Event().wait(0.5)
    
# Create two threads, one for even numbers and one for odd numbers
even_thread = threading.Thread(target=both_numbers, args=(2, 2), name="Even")
odd_thread = threading.Thread(target=both_numbers, args=(1, 2), name="Odd")

# Start both threads
odd_thread.start()
even_thread.start()

# Wait for both threads to finish
odd_thread.join()
even_thread.join()