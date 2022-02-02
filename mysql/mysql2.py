import mysql

query1 = """
    SELECT ActivityName FROM ACTIVITY ORDER BY ACode DESC
"""

query2 = """
    SELECT sum(PrizeMoney) FROM ACTIVITY GROUP BY ParticipantsNum
"""

query3 = """
    SELECT Name, Acode FROM COACH ORDER BY ACode DESC
"""

query4 = """
    SELECT * FROM ACTIVITY WHERE ScheduleDate > 01/01/2004 ORDER BY ParticipantNum AESC
"""

query5 = """

"""