def add_time(a, b, day=None):
    t = a.split()
    days = [
        "Monday"
        "Tuesday"
        "Wednesday"
        "Thursday"
        "Friday"
        "Saturday"
        "Sunday"
    ]
    #print(len(tl))
    #print(t[0], t[1])
    t1 = (t[0]).split(':')
    #print(t1)
    hrs = int(t1[0])
    mins = int(t1[1])
    t2 = b.split(':')
    #print(t2)
    hr = int(t2[0])
    min = int(t2[1])
    c = hr//24
    if t[1] == 'PM':
        hrs += 12
    if hr >= 24:
        hr = hr%24
    
    h = hrs + hr

    if h > 24:
        h -= 12
    if h > 12:
        hour = h - 12
        t[1] = 'PM'
    else:
        hour = h
        t[1] = 'AM'
    print(hour)
    print(t[1])
    minute = mins + min
    if minute > 60:
        minute -= 60
        hour += 1
    print(minute)
    #print(c)

    if c == 1:
        m = "The next day"
    elif c > 1:
        c = c + 1
        m = f"{c} days later"
    print(m)

add_time("6:12 PM", "205:30")