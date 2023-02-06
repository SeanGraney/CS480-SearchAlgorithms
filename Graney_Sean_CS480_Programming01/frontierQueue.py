class FrontierQueue:
    # key lambda x:-x for min heap
    def __init__(self, key):
        self.data = []
        self.key = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2

    @staticmethod
    def _left(idx):
        return (idx*2)+1

    @staticmethod
    def _right(idx):
        return (idx*2)+2

    # reformats the heap
    def heapify(self, idx=0):
        temp_idx = idx
        while True:
            l = FrontierQueue._left(temp_idx)
            r = FrontierQueue._right(temp_idx)
            # if there is a left child and the left child is greater, set temp index to the left childs index
            if l < len(self.data) and self.key(self.data[temp_idx][1]) < self.key(self.data[l][1]):
                temp_idx = l
            # if there is a right child and the right child is greater, set temp index to right child index
            if r < len(self.data) and self.key(self.data[temp_idx][1]) < self.key(self.data[r][1]):               
                temp_idx = r
            # the number is in the correct spot
            if temp_idx == idx:
                break
            else:
                 # swap the values at the temp index and index
                self.data[temp_idx], self.data[idx] = self.data[idx], self.data[temp_idx]
                # reset the value of idx to prep for next iteration
                idx = temp_idx


    def peek(self):
        if len(self.data) == 0:
            return "empty"
        return self.data[0]

    def add(self, lst):
        
        self.data.append(lst)
        # adds val to the last spot in the array list
        v = len(self.data)-1
        # parent of the added val
        p = FrontierQueue._parent(v)

        # while there is more than one val in the list, and the val is not the parent node, and the parent          of val is less than val
        while v > 0 and self.key(self.data[p][1]) < self.key(self.data[v][1]):
            # switch the index of the val and parent
             self.data[p], self.data[v] = self.data[v], self.data[p]
            #  set values to continue up the tree
             v = p
             p = FrontierQueue._parent(v)


    def pop(self):
        # save value at the top of the heap
        ret = self.data[0]
        # set the value at the top of the heap to the last val
        self.data[0] = self.data[len(self.data)-1]
        # delete last val
        del self.data[len(self.data)-1]
        # 'trickle down' the heap
        self.heapify()

        return ret

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __bool__(self):
        return len(self.data) > 0
