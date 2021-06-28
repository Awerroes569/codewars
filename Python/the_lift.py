class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.__floors={}
        self.__capacity=capacity
        self.__inside=[]
        self.__history=[]
        self.__current=0
        self.__lift=[]
        self.__up=True
        self.__up_button=[]
        self.__down_button=[]
        
        self.decode_queques(queues)
    
    def decode_queques(self,queues):
        for i in range(len(queues)):
            ups=[x for x in queues[i] if x > i]
            downs=[x for x in queues[i] if x < i]
            self.__floors[i]=[ups,downs]

    def minmax_detect(self):
        self.__up_button=[k for k,v in self.__floors.items() if v[0]]
        self.__down_button=[k for k,v in self.__floors.items() if v[1]]
            
    def end_procedure(self):
        if self.__history[-1]:
            self.__history.append(0)           
        
    def theLift(self):
        self.__history.append(self.__current)
        while self.total_waiting() or len(self.__inside):
            self.minmax_detect()
            if len(self.__history):
                if self.__history[-1]!=self.__current:
                    self.__history.append(self.__current)
            self.leave_lift()
            self.enter_lift()
            self.next_floor()
        self.end_procedure()
        return self.__history[:]
    
    def total_waiting(self):
        result=sum([ 1 for x in self.__floors.values() for y in x for z in y])
        return result
        
    def leave_lift(self):
        self.__inside=[x for x in self.__inside if x !=self.__current]

    def enter_lift(self):
        updown=1
        if self.__up:
            updown=0
        free_space=self.__capacity-len(self.__inside)
        for _ in range(free_space):
            if len(self.__floors[self.__current][updown]):
                current=self.__floors[self.__current][updown].pop(0)
                self.__inside+=[current]
    
    def next_floor(self):
        next_up_button=[x for x in self.__up_button if x>self.__current]+[x for x in self.__inside if x>self.__current]
        next_down_button=[x for x in self.__down_button if x<self.__current]+[x for x in self.__inside if x<self.__current]
        below_up=[x for x in self.__up_button if x<self.__current]
        higher_down=[x for x in self.__down_button if x>self.__current]
        
        if self.__up and len(next_up_button):
            self.__current=min(next_up_button)
            return
        elif self.__up and len(higher_down):
            self.__current=max(higher_down)
            return
        elif self.__up :
            self.__up=False
            return
        
        if not self.__up and len(next_down_button):
            self.__current=max(next_down_button)
            return
        elif not self.__up and len(below_up):
            self.__current=min(below_up)
            return
        else:
            self.__up=True

