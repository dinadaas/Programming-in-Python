
def hw2_answers(problem_number):
    if problem_number == "3.1.1":
        return "A benefit of adding an inequality constraint is that it allows for the handling of each case by looping through the set. However, a drawback is that it may be ineficient when applied to many constraints. The benefit of using an allDiff constraint is that it allows for the handling of the constraint in a much more effiricent fashion than a general-purpose algorithm, so there is no need to define each inequality that wouldn't satisfy the constraint. A drawback of this approach is that it would be difficult to detect wich term is causing an error since it checks them all in one go. I used an inequality constraint in my CSP implementation because I had a better conceptual understanding of it, and becasue I wanted to detect which term, if any, would be causing an error."
    if problem_number == "3.1.2":
        return '''
    puzzle constraints
        N1 = 5
        A1 = 4
        D1 = 2
        Both N1 and D1 = 1
        Both N1 and D3 = 0
        Both N1 and N2 = 0
        All N1, N2, N3 = 0
    all-diff constraints
        N1 = 8
        A1 = 8
        D1 = 8
        Both N1 and D1 = 0
        Both N1 and D3 = 0
        Both N1 and N2 = 2
        All N1, N2, N3 = 0
'''

    if problem_number == "3.2.1":
        return '''
            forward:
            n = 4 , states examied = 4, time =0.00257802009583
            n = 8 , states examied =17, time =0.0106120109558
            n = 12 , states examied =25, time =0.0214061737061
            n = 16 , states examied =79, time =0.043053150177
            no forward:
            n = 4 , states examied =8, time =0.00433397293091
            n = 8 , states examied =68, time =0.0661170482635
            n = 12 , states examied =118, time =0.2009370327
            n = 16 , states examied =17224, time =51.580783844
            
            '''
    if problem_number == "3.2.2":
        return "YOUR 3.2.2 ANSWER HERE"
    if problem_number == "3.2.3":
        return "YOUR 3.2.3 ANSWER HERE"
    if problem_number == "3.2.4":
        return "Around 10000 before it starts to take over 2 minutes"

    if problem_number == "3.3.1":
        return "All in PDF"
    if problem_number == "3.3.2":
        return "All in PDF"
    if problem_number == "3.3.3":
        return "All in PDF"
    if problem_number == "3.3.4":
        return "All in PDF"

    return "Invalid problem number"
