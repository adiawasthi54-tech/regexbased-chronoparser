# Time, Date, Day
import re
from datetime import datetime, date, timedelta
def chrono(string):
    now = datetime.now() 
    if re.search(r"\btoday\b", string) and re.search(r"(\d+):(\d+)", string):
        time = re.search(r"(\d+):(\d+)", string)
        timegrp = time.groups()
    if re.search(r"\bam\b", string):
        ampm = 'am'
    else:
        ampm = 'pm'
    #after keyword
    if re.search(r"\bafter\b", string):
        if re.search(r"\bhrs\b\s\bafter\b\s\d+:\d+", string) or re.search(r"\bhr\b\s\bafter\b\s\d+:\d+", string) or re.search(r"\bhour\b\s\bafter\b\s\d+:\d+", string) or re.search(r"\bhours\b\s\bafter\b\s\d+:\d+", string):
            timegrp = list(timegrp)
            int_timegrp = [int(x) for x in timegrp]
            dec = re.search(r"(\d+)\s*(?:hours?|hrs?)", string)
            decr = int(dec.group(1))
            print(int_timegrp[0]+decr,':',int_timegrp[1],ampm,',',now.date(),',',now.strftime('%A'))
        #else
        else:
            nextday = date.today() + timedelta(days=1)
            print(timegrp[0],':',timegrp[1],ampm,',',nextday,',',nextday.strftime('%A'))
    #before keyword
    elif re.search(r"\bbefore\b", string):
        if re.search(r"\bhrs\b\s\bbefore\b\s\d+:\d+", string) or re.search(r"\bhr\b\s\bbefore\b\s\d+:\d+", string) or re.search(r"\bhour\b\s\bbefore\b\s\d+:\d+", string) or re.search(r"\bhours\b\s\bbefore\b\s\d+:\d+", string):
            timegrp = list(timegrp)
            int_timegrp = [int(x) for x in timegrp]
            dec = re.search(r"(\d+)\s*(?:hours?|hrs?)", string)
            decr = int(dec.group(1))
            print(int_timegrp[0]-decr,':',int_timegrp[1],ampm,',',now.date(),',',now.strftime('%A'))
        #else
        else:
            yesterday = date.today() - timedelta(days=1)
            print(timegrp[0],':',timegrp[1],ampm,',',yesterday,',',yesterday.strftime('%A'))
    #no keyword
    else:
        print(timegrp[0],':',timegrp[1], ampm,',',now.date(),',', now.strftime('%A'))
