"""
https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX%3A32007R0861
"""

"""
Art. 5
dispatch from court: 14 days
defendant - response within 30 days
dispatch of response by the court: 14 days
if counterclaim:
    claimant: 30 days to respond

Art. 7
30 days from last exchange of documents:
    (a) judgment
    (b) ask more details (max 30 days)
    (b) take evidence

if (a) or (b) or (c): 30 days -> judgment
"""

import re
from datetime import datetime, timedelta


HOLIDAYS = [
    (1, 1), (6, 1), (25, 4), (1, 5), (2, 6), (15, 8), (1, 11), (8, 12), (25, 12), (26, 12)
]
# monday after easter


AVG_SERVICE_TIME = timedelta(days=7)
COURT_DISPATCH_DAYS = timedelta(days=14)
DEFAULT_RESPONSE_TIME = timedelta(days=30)


def is_holiday(date):
    if date.weekday() in (5, 6):  # saturday or sunday
        return True
    if (date.day, date.month) in HOLIDAYS:
        return True
    return False


def add_days(date, td):
    new_date = date + td
    while is_holiday(new_date):
        new_date += timedelta(days=1)
    return new_date


def art_5():
    claimant_to_court_str = input("When did the claimant bring Form A to the court? (dd/mm/yyy) ")
    claimant_to_court = datetime.strptime(claimant_to_court_str, "%d/%m/%Y")

    while is_holiday(claimant_to_court):
        claimant_to_court += timedelta(days=1)

    court_dispatch_claim = claimant_to_court + COURT_DISPATCH_DAYS

    while is_holiday(court_dispatch_claim):
        court_dispatch_claim += timedelta(days=1)

    print("The court must dispatch the claim to the defendant within", court_dispatch_claim.strftime("%d/%m/%Y"))

    defendant_served = add_days(court_dispatch_claim, AVG_SERVICE_TIME)

    print("The defendant was served on", defendant_served.strftime("%d/%m/%Y"))

    defendant_reply = add_days(defendant_served, DEFAULT_RESPONSE_TIME)
    
    print("The defendant must reply within", defendant_reply.strftime("%d/%m/%Y"))

    court_dispatch_reply = add_days(defendant_reply, COURT_DISPATCH_DAYS)

    print("The court must dispatch the reply within", court_dispatch_reply.strftime("%d/%m/%Y"))

    claimant_got_reply = add_days(court_dispatch_reply, AVG_SERVICE_TIME)

    print("The claimant got their reply on", claimant_got_reply.strftime("%d/%m/%Y"))

    last_exchange_of_docs = claimant_got_reply

    is_there_cnt_claim = input("Was there a counter claim? ")
    if re.match(r"y(es|eah)?", is_there_cnt_claim, re.I):
        counter_claim_response = add_days(claimant_got_reply, DEFAULT_RESPONSE_TIME)
        print("The claimant responded to counterclaim on", counter_claim_response.strftime("%d/%m/%Y"))
        last_exchange_of_docs = counter_claim_response

    print("The last exchange of docs was on", last_exchange_of_docs.strftime("%d/%m/%Y"))

    return last_exchange_of_docs


def art_7(last_exchange_of_docs):
    print("What does the judge want to do?")

    judge_choices = {
        "j": "Issue a judgment",
        "a": "demand further details concerning the claim from the parties within a specified period of time, not exceeding 30 days;",
        "b": "take evidence in accordance with Article 9;",
        "c": "summon the parties to an oral hearing to be held within 30 days of the summons."
    }

    for k, v in judge_choices.items():
        print(f"[{k}]: {v}")
    print()
    user_ans = None
    while user_ans not in judge_choices.keys():
        user_ans = input(">>> ").lower().strip()
    
    if user_ans == "j":
        judge_decision = add_days(last_exchange_of_docs, DEFAULT_RESPONSE_TIME)
        print("The judge must issue a decision within", judge_decision.strftime("%d/%m/%Y"))
    elif user_ans == "a":
        further_details = add_days(last_exchange_of_docs, DEFAULT_RESPONSE_TIME)
        print("The judge must gather new details within", further_details.strftime("%d/%m/%Y"))
        judge_decision = add_days(further_details, DEFAULT_RESPONSE_TIME)
        print("The judge must issue a decision within", judge_decision.strftime("%d/%m/%Y"))
    elif user_ans == "b":
        gather_evidence = add_days(last_exchange_of_docs, DEFAULT_RESPONSE_TIME)
        print("The judge must gather new evidence within", gather_evidence.strftime("%d/%m/%Y"))
        judge_decision = add_days(gather_evidence, DEFAULT_RESPONSE_TIME)
        print("The judge must issue a decision within", judge_decision.strftime("%d/%m/%Y"))
    elif user_ans == "c":
        summon_hearing = add_days(last_exchange_of_docs, DEFAULT_RESPONSE_TIME)
        print("The judge must summon a hearing within", summon_hearing.strftime("%d/%m/%Y"))
        hearing_date = add_days(summon_hearing, DEFAULT_RESPONSE_TIME)
        print("The hearing must be held within", hearing_date.strftime("%d/%m/%Y"))
        judge_decision = add_days(hearing_date, DEFAULT_RESPONSE_TIME)
        print("The judge must issue a decision within", judge_decision.strftime("%d/%m/%Y"))
    else:
        raise ValueError("Don't know what to do")
    return judge_decision


if __name__ == "__main__":
    _laod = art_5()
    art_7(_laod)
