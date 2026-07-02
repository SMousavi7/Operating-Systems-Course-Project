class MMU:
    page_faults = 0
    eviction_times = 0
    page_size = 20   # this should be changed in every iteration.
    mem_size = 4000
    def __init__(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.free_places = (MMU.mem_size // MMU.page_size)
        self.LRU = [] 
        # to do
        # you can put any fields you want here and work with them. probably a ram would be necessary here.
    
    def reset(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.free_places = (MMU.mem_size // MMU.page_size)
        self.LRU = [] 
        MMU.page_faults = 0
        MMU.eviction_times = 0

    def handle_request(self, request):
        index_of_page = self.search(request=request)
        if index_of_page != -1:
            self.LRU.pop(index_of_page)
            self.LRU.append(index_of_page)
            return index_of_page
        
        MMU.page_faults += 1
        file_id, selected_page, number_of_pages = request
        
        # put prev page in mmap
        if selected_page > 0:
            index_of_prev_page = self.search(request=(file_id, selected_page - 1))
            
            if index_of_prev_page == -1:
                
                if self.free_places == 0:
                    place_returned = self.eviction_system_LRU()
                    self.mmap[place_returned] = (file_id, selected_page - 1)
                    self.free_places -= 1
                    self.LRU.append(place_returned)

                else:
                    place_returned = self.search(request=(-1,-1))
                    self.mmap[place_returned] = (file_id, selected_page - 1)
                    self.free_places -= 1
                    self.LRU.append(place_returned)
                
        # this place is for putting the selected page in mmap
        if self.free_places == 0:
            place_returned = self.eviction_system_LRU()
            index_of_page = place_returned
            self.mmap[place_returned] = (file_id, selected_page)
            self.free_places -= 1
            self.LRU.append(place_returned)

        else:
            place_returned = self.search(request=(-1,-1))
            index_of_page = place_returned
            self.mmap[place_returned] = (file_id, selected_page)
            self.free_places -= 1
            self.LRU.append(place_returned)
        
        
        # this is for putting next page in mmap
        if selected_page < number_of_pages - 1:
            index_of_next_page = self.search(request=(file_id, selected_page + 1))
            
            if index_of_next_page == -1:
                
                if self.free_places == 0:
                    place_returned = self.eviction_system_LRU()
                    self.mmap[place_returned] = (file_id, selected_page + 1)
                    self.free_places -= 1
                    self.LRU.append(place_returned)

                else:
                    place_returned = self.search(request=(-1,-1))
                    self.mmap[place_returned] = (file_id, selected_page + 1)
                    self.free_places -= 1
                    self.LRU.append(place_returned)
    
        # time.sleep(0.03) # for simulating time
       
        return index_of_page
    
    
    def eviction_system_LRU(self):
        MMU.eviction_times += 1
        self.mmap[self.LRU[0]] = (-1, -1)
        self.free_places += 1
        return self.LRU.pop(0)
        
        
    def search(self, request):
        index = 0
        for file, page in self.mmap:
            if file == request[0] and page == request[1]:
                return index
            index += 1
        return -1