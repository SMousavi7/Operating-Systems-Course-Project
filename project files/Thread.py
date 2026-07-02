import random
from File import File 
import numpy as np
from MMU import MMU
import math
import numpy as np
class Thread:
    number = 0
    MAXIMUM_NUMBER_OF_FILES = 5
    def __init__(self):
        self.id = Thread.number
        Thread.number += 1
        self.files = []
        self.file_weights = []
        temp = random.randint(1, Thread.MAXIMUM_NUMBER_OF_FILES)
        for i in range(temp):
            selected = random.randint(0, len(File.list_of_files) - 1)
            chosen = File.list_of_files.pop(selected)
            self.files.append(chosen)
            self.file_weights.append(1)
    
    def reset(self):
        for weight in self.file_weights:
            weight = 1
    
    def start(self):
        if not self.files:
            return
        
        # Choose a file index based on weights
        selected_index = random.choices(range(len(self.files)), weights=self.file_weights, k=1)[0]
        file = self.files[selected_index]
        
        # Increase weight to favor future selections
        self.file_weights[selected_index] += 1

        # Simulate selecting a random offset in file
        # Sadra's bs:
        # number_of_pages_in_file = math.ceil((file.ending_point - file.starting_point) / MMU.page_size)
        # selected_page = random.randint(0, number_of_pages_in_file - 1)
        # return (file.id, selected_page, number_of_pages_in_file)
        # Farzin's bs:
        number_of_pages_in_file = math.ceil((file.ending_point - file.starting_point) / MMU.page_size)        
        selected_page = generate_random_file_access(file.starting_point, file.ending_point) // MMU.page_size
        return (file.id, selected_page, number_of_pages_in_file)
    
def generate_random_file_access(a, b):
    mean =  (a + b) / 2
    std_dev = 25
    num = int(np.clip(np.random.normal(mean, std_dev), a, b))
    return num

