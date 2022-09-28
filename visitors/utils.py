from datetime import datetime , date

def str_to_date(request, session_key):
    str_date = request.session.get(session_key)
    return datetime.strptime(str_date, "%Y/%m/%d").date()
