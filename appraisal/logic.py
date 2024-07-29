# Logic => 1 start
def Academic_Score(target, cumulative):
    schema = 2
    score = 0

    if target < 75:
        score = 0
    else:
        diff = target - 75
        points = (diff // 5) * schema
        score = min(points, 10)

    return score


# Logic => 1 end


# Logic => 2 start
def online_course(course, cumulative):
    if course + cumulative > 2:
        course = 2
    total = course + cumulative

    score = min(total * 3, 5)
    return score


# Logic => 2 end


# Logic => 3 start
def fdp(weeks, program, cumulative):
    points = 0

    if weeks == 1:
        points = program * 1.5
    elif weeks == 2:
        points = program * 2.5

    return min(points, 5)


# Logic => 3 end


# Logic => 4 start
def counselling(session, cumulative):
    score = session * 1
    if score > 3:
        score = 3
    return score


# Logic => 4 end


# Logic =>  5 start
def online_feedback(feedback, cumulative):
    score = 0
    if feedback < 8:
        score = 0
    elif feedback == 8:
        score = 1
    elif feedback == 8.5:
        score = 2
    elif feedback == 9:
        score = 3
    elif feedback == 9.5:
        score = 4
    elif feedback == 10:
        score = 5
    return score


# Logic =>5 end


# Logic => 6 start
def precption(position, cumulative):
    points = 0
    if position == "Convener":
        points = 5
    elif position == "Co-convener":
        points = 5
    elif position == "Committee Member":
        points = 2
    if points > 5:
        points = 5
    return points


# Logic => 6 end


# Logic => 8 start
def research_paper(no_of_Paper, position):
    score = 0
    if position == 1:
        score = no_of_Paper * 15
    elif position == 2:
        score = no_of_Paper * 10
    elif position == 3:
        score = no_of_Paper * 5
    return min(score, 30)


# Logic => 8 end


# Logic => 9 start
def paper_presentaion(no_ofPaper, conference, cumulative):
    score = 0
    if conference == "National Conference":
        score = no_ofPaper * 3
    elif conference == "International Conference":
        score = no_ofPaper * 4
    return min(score, 8)


# Logic => 9 end


# Logic => 10 start
def research_project(
    no_of_project,
    price,
    position,
    Research_project_sanctioned_cumulative,
):
    FstScore = 0
    secScore = 0
    if price <= 5:
        FstScore = no_of_project * 2.5
        secScore = no_of_project * 1.2
    elif (price > 5) and (price <= 30):
        FstScore = no_of_project * 4
        secScore = no_of_project * 2.5
    elif (price > 30) and (price <= 60) or (price > 60):
        FstScore = no_of_project * 10
        secScore = no_of_project * 5
    if position == "PI":
        return min(FstScore, 10)
    else:
        return min(secScore, 10)


# Logic => 10 end


# Logic => 11 start
def rearsh_proposal(proposal):
    score = 0
    score = proposal * 1.5
    return min(score, 3)


# Logic => 11 end


# Logic => 12 start
def consultancy(no_of_project, price):
    score = 0

    if price <= 1:
        score = no_of_project * 1

    elif (price > 1) and (price <= 2):
        score = no_of_project * 1.5

    elif price > 2:
        score = no_of_project * 3

    return min(score,3)


# Logic => 12 end


# Logic => 13 start
def Pedagogy(number):
    score = number * 0.5
    return min(score, 6)


# Logic => 13 end


# Logic => 14 start
def inovative(number_of_inovative):
    score = number_of_inovative * 1.5
    return min(score, 2.5)


# Logic => 14 end


# Logic => 15 start
def content_developement(no_Of_content_developement):
    score = no_Of_content_developement * 1.5
    return min(score, 2.5)


# Logic => 15 end
