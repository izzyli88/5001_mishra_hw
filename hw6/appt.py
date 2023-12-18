"""_Isabelle Li - CS5001 HW6 - 17DEC2023
Appointments_
"""


class User:
    # define class variables
    user_list = []

    def __init__(self, uid, appt_diary):
        self.uid = uid
        self.appt_diary = appt_diary
        self.appt_diary = []


class Time:
    def __init__(self, hr, min, ampm):
        self.hr = hr
        self.min = min
        self.ampm = ampm


class Date:
    def __init__(self, yr, month, day):
        self.yr = yr
        self.month = month
        self.day = day


class Appt:
    pass


class ApptDiary:
    pass
