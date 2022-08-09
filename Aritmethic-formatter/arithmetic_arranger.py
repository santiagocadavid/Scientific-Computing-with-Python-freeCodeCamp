def arithmetic_arranger(problems, show_ans=False):

    arranged_problems = ""


    first_operand = []
    second_operand = []
    operator = []

    for i in problems:

        j = i.split(" ")
        first_operand.append(j[0])
        operator.append(j[1])
        second_operand.append(j[2])
        

    if len(problems)>5:
            return "Error: Too many problems."

    for i in operator:
        if i=="*" or i=="/":
            return "Error: Operator must be '+' or '-'."
    

    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
           return "Error: Numbers must only contain digits."

    
    for i in range(len(first_operand)):
        if len(first_operand[i])>4 or len(second_operand[i])>4:
           return "Error: Numbers cannot be more than four digits."
    


    fi_line = []
    se_line = []
    th_line = []
    fo_line = []


    for i in range(len(first_operand)):
        
        if len(first_operand[i])>len(second_operand[i]):

            fi_line.append(" "*2 + first_operand[i])
        else:
            dist = (len(second_operand[i])-len(first_operand[i])+2)
            fi_line.append(" "*dist + first_operand[i])


    for i in range(len(second_operand)):
        
        if len(second_operand[i])>len(first_operand[i]):

            
            se_line.append(operator[i] + " " + second_operand[i])
        else:
            dist = (len(first_operand[i])-len(second_operand[i])+1)
            se_line.append(operator[i] + " "*dist + second_operand[i])

    for i in range(len(first_operand)):
        th_line.append("-"*(max(len(first_operand[i]), len(second_operand[i]))+2))


    for i in range(len(first_operand)):
        
        if operator[i] == "+":

            res = str(int(first_operand[i]) + int(second_operand[i]))
        
        elif operator[i] == "-":

            res = str(int(first_operand[i]) - int(second_operand[i]))
        
        if len(res) > max(int(first_operand[i]), int(second_operand[i])):
            fo_line.append(" " + res)
        
        else:
            fo_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(res) +2) + res)
            #fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)

    

    if show_ans:
        arranged_problems = "    ".join(fi_line) + "\n" + "    ".join(se_line) + "\n" + "    ".join(th_line) + "\n" + "    ".join(fo_line)
        
    else:
        arranged_problems = "    ".join(fi_line) + "\n" + "    ".join(se_line) + "\n" + "    ".join(th_line)
        
    return arranged_problems

  

