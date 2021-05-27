class Calculator(object):
    
    OPERATORS={"+":0,"-":0,"*":1,"/":1,"(":-1}
    
    def evaluate(self, string):
        elements=string.split()
        main=[]
        operators=[]
        for i in elements:
            if i[0].isnumeric():
                main.append(i)
            elif i=="(":
                operators.append(i)
            elif i==")":
                while(operators[-1]!="("):
                    main.append(operators.pop())
                operators.pop()
            elif len(operators)==0:
                operators.append(i)
            else:
                while(len(operators)>0 and operators[-1]!="(" and Calculator.OPERATORS[operators[-1]]>=Calculator.OPERATORS[i]):
                    main.append(operators.pop())
                operators.append(i)
        for i in operators:
            main.append(operators.pop())
        main.reverse()
        while(len(main)>0):
            current=main.pop()
            if current not in Calculator.OPERATORS:
                operators.append(current)
            else:
                b=operators.pop()
                a=operators.pop()
                operators.append(str(Calculator.operate(current,a,b)))
        return float(operators[0])
    def operate(operator,a,b):
        if operator=="+":
            return float(a)+float(b)
        elif operator=="-":
            return float(a)-float(b)
        elif operator=="*":
            return float(a)*float(b)
        elif operator=="/":
            return float(a)/float(b)