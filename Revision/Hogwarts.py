def portrait(right_password, entered_password):
    return right_password == entered_password




def house_designation(student_qualities):
    knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]
    elements = [['Gryffindor',0],["Hufflepuff",0],["Slytherin",0],["Ravenclaw",0]]
    
    for elm in knowledge:
        for qual in student_qualities:
            if qual in elm[1]:
                for elemts in elements:
                    if elemts[0] == elm[0]:
                        elemts[1] += 1
    new_lst = sorted(elements, key= lambda x: x[1])
    print(new_lst)

house_designation(["brave","smart","wily","loyal","patient"])