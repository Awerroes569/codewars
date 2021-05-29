class Nonogram:

    
    possibilities={
            
            ()    :[(0,0,0,0,0)],
            (1,)  :[
                    (1,0,0,0,0),
                    (0,1,0,0,0),
                    (0,0,1,0,0),
                    (0,0,0,1,0),
                    (0,0,0,0,1)                 
                    ],
            (2,)  :[
                    (1,1,0,0,0),
                    (0,1,1,0,0),
                    (0,0,1,1,0),
                    (0,0,0,1,1)                
                    ],
            (3,)  :[
                    (1,1,1,0,0),
                    (0,1,1,1,0),
                    (0,0,1,1,1)                 
                    ],
            (4,)  :[
                    (1,1,1,1,0),
                    (0,1,1,1,1)                 
                    ],
            (5,)  :[
                    (1,1,1,1,1)                 
                    ],
            (1,1) :[
                    (1,0,1,0,0),
                    (1,0,0,1,0),
                    (1,0,0,0,1),
                    (0,1,0,1,0),
                    (0,1,0,0,1),        
                    (0,0,1,0,1)
                    ],
            (1,2) :[
                    (1,0,1,1,0),
                    (1,0,0,1,1),
                    (0,1,0,1,1)
                    ],
            (1,3) :[
                    (1,0,1,1,1)
                    ],
            (2,2) :[
                    (1,1,0,1,1)
                    ],
            (2,1) :[
                    (1,1,0,1,0),
                    (1,1,0,0,1),
                    (0,1,0,1,1)
                    ],
            (3,1) :[
                    (1,1,1,0,1)
                    ],
            (1,1,1) :[
                    (1,0,1,0,1)
                    ],
            
            }
    
    def __init__(self, clues):
        self.horizontal=clues[0]
        self.vertical=clues[1]

    def solve(self):
        for a in Nonogram.possibilities[self.horizontal[0]]:
            for b in Nonogram.possibilities[self.horizontal[1]]:
                for c in Nonogram.possibilities[self.horizontal[2]]:
                    for d in Nonogram.possibilities[self.horizontal[3]]:
                        for e in Nonogram.possibilities[self.horizontal[4]]:
                            zipped = tuple(zip(a,b,c,d,e))
                            if (zipped[0] in Nonogram.possibilities[self.vertical[0]]) and (zipped[1] in Nonogram.possibilities[self.vertical[1]]) and (zipped[2] in Nonogram.possibilities[self.vertical[2]]) and (zipped[3] in Nonogram.possibilities[self.vertical[3]]) and (zipped[4] in Nonogram.possibilities[self.vertical[4]]):
                                   return zipped
