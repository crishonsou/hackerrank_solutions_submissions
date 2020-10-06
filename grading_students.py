def gradingStudents(grades):
    x=[]
    for i in grades:
        if i < 38 or i % 5 < 3:
            x.append(i)
        else:
            x.append((i - (i % 5)) + 5)
    return x
