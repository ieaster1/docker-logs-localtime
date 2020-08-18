#!/usr/bin/env python3
'''
replace all UTC dates to local dates in pipe
by ieaster1 https://github.com/ieaster1

usage: docker logs -t container_name | local-docker-logs
'''

import sys
import re
from datetime import datetime

import tzlocal # pip3 install tzlocal
import pytz # pip3 install pytz
# >>> from pytz import all_timezones
# >>> len(all_timezones)
# 593
# >>> 'America/New_York' in all_timezones
# True
def convert_ts(line):
    tz = str(tzlocal.get_localzone())
    local_tz = pytz.timezone(tz)
    utc = pytz.utc
    
    fmt_d = '%Y-%m-%d'
    fmt_t = '%H:%M:%S'
    fmt_dt = ' '.join([fmt_d, fmt_t])
    
    reg_d = r'\d{4}-\d{1,2}-\d{1,2}'
    reg_t = r'\d{1,2}:\d{1,2}:\d{1,2}'
    reg_dt = '|'.join([reg_d, reg_t])
    reg_dt_sub = r'\d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}.\d{9}Z' # 1999-12-31T23:27:00.923467681Z

    date, time = re.findall(re.compile(reg_dt), line)
    dt = datetime.strptime(' '.join([date, time]), fmt_dt)
    utc_dt = datetime(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second,
        tzinfo=utc)
    local_dt = utc_dt.astimezone(local_tz).strftime(fmt_dt)
    local_d = datetime.strptime(local_dt, fmt_dt).date().strftime(fmt_d)
    local_t = datetime.strptime(local_dt, fmt_dt).time().strftime(fmt_t)
    digested = re.sub(reg_dt_sub, ' '.join([local_d, local_t]), line)

    return digested

def main():
    try:
        for line in iter(sys.stdin.readline, b''):
            output = convert_ts(line)
            print(output, end='', flush=True)
    
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass
    
    except:
        pass

if __name__ == '__main__':
    main()
