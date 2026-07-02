from Thread import Thread
from MMU import MMU

class CPU:
    def __init__(self, mmu):
        self.list_thread = []
        self.mmu = mmu
        
    def AddThread(self, Thread):
        self.list_thread.append(Thread)
    
    def reset(self):
        for t in self.list_thread:
            t.reset()

    def run(self):
        for i in range(50):
            for i in range(len(self.list_thread)):
                selected_thread = self.list_thread[i]
                file_id, selected_page, number_of_pages_in_file = selected_thread.start()
            
                request = (file_id, selected_page, number_of_pages_in_file)
                self.mmu.handle_request(request)
                