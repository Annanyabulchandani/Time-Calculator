def add_time(start, duration, starting_day=""):
    pieces = start.split()
    time = pieces[0].split(":")
    ampm = pieces[1]

    duration_pieces = duration.split(":")
    
    if ampm == "PM":
        time[0] = int(time[0]) + 12
        
    ending_h = int(time[0]) + int(duration_pieces[0])
    ending_min = int(time[1]) + int(duration_pieces[1])

    days_add = 0
    
    if ending_min >= 60:
        hours_add = ending_min // 60
        ending_min -= hours_add * 60
        ending_h += hours_add
    
    if ending_h > 24:
        days_add = ending_h // 24
        ending_h -= days_add * 24
    
    if ending_h > 12:
        ending_h -= 12
        ampm = "PM"
    elif ending_h == 12:
        ampm = "PM"
    elif ending_h > 0 and ending_h < 12:
        ampm = "AM"
    else: #ending_h == 0
        ampm = "AM"
        ending_h += 12
    
    if days_add > 0:
        if days_add == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(days_add) + " days later)"
    else:
        days_later = ""
    
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday')
    
    if starting_day:
        b = int(days_add) + weekdays.index(starting_day.title())
        c = b // 7
        b = b - c * 7
        end_day = str(", " + weekdays[b])
    else:
        end_day = starting_day
    
    new_time = str(ending_h) + ":" + \
        (str(ending_min) if ending_min > 9 else ("0" + str(ending_min))) + \
        " " + ampm + "" + end_day + days_later
        
    print(new_time)

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)