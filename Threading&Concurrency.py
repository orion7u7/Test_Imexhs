import json
import threading
import os
import logging
import numpy as np
import queue as Queue

logging.basicConfig(filename="json.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

def element_processor(element):
    elementId = element["id"]
    elementDevice = element["deviceName"]
    elementData = np.array([list(map(int, row.split())) for row in element['data']])
    
    logging.info(f"Processing element {elementId} from {elementDevice}")
    
    avg_before = np.mean(elementData)
    
    max_value = np.max(elementData)
    normalized_data = elementData / max_value
    
    avg_after = np.mean(normalized_data)
    
    logging.info(f"Element {elementId}, Device {elementDevice}, Data Size {elementData.size}, Average Before {avg_before}, Average After {avg_after}")
    print(f"Element {elementId}, Device {elementDevice}, Data Size {elementData.size}, Average Before {avg_before}, Average After {avg_after}")
    
def worker(q):
    while True:
        element = q.get()
        if element is None:
            break
        element_processor(element)
        q.task_done()
        
def main(path, fileName):
    json_file = os.path.join(path, fileName)
    
    with open(json_file) as file:
        data = json.load(file)
    
    q = Queue.Queue()
    threads = []
    
    for i in range(4):
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)
        
    for key, element in data.items():
        q.put(element)
    
    q.join()
    
    for _ in threads:
        q.put(None) 
    for t in threads:
        t.join()
    
if __name__ == "__main__":
    path = "D:/Documentos/pruebas/Test_Imexhs/"
    fileName = "sample-03-01-json.json"
    main(path, fileName)
