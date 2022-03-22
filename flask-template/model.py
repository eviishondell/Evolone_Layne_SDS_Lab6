def capital_check(answers):
    correct_answers = {
        'new york':'albany',
        'california':'sacramento',
        'utah':'salt lake city',
        'alabama':'montgomery',
        'ohio':'columbus'
        }
    graded_answers = {}
    for answer in answers:
        if correct_answers[answer] == answers[answer].lower():
            graded_answers[answer] = 'correct'
        else:
            graded_answers[answer] = 'wrong'
    return graded_answers