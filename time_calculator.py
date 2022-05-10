def add_time(start, duration, day=None):
  start = start.replace(':', ' ').split(' ')
  duration = duration.split(':')
  startHour = start[0]
  startMin = start[1]
  noonSuffix = originalSuffix = (start[2])
  durationHour = duration[0]
  durationMin = duration[1]
  daysOfTheWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  
  if day: 
    day = day.lower().capitalize()
    indexDay = daysOfTheWeek.index(day)
  newMin = (int(startMin) + int(durationMin)) % 60
  overflowMin = ((int(startMin) + int(durationMin)) / 60)
  if overflowMin > 1: newHour = (int(startHour) + int(durationHour)) % 12 + 1
  else: newHour = (int(startHour) + int(durationHour)) % 12

  totalTime = (((int(startHour) + int(durationHour)) * 60) + (int(startMin) + int(durationMin))) / 60 / 12

  switches = str(totalTime).split('.')
  switches = int(switches[0])
  if (switches % 2 != 0):
    if (noonSuffix == 'AM'): noonSuffix = 'PM'
    else: noonSuffix = 'AM'

  finalString = str(newHour) + ":" + str(newMin).rjust(2, '0') + ' ' + noonSuffix
  numDaysLater = round(switches / 2)
  numDaysLaterString = ' (' + str(numDaysLater) + ' days later)'

  if not day:
    if (switches == 1 and originalSuffix == 'PM') or (switches == 2): return finalString + ' (next day)'
    if switches > 2 and originalSuffix == 'PM':
      switches += 1
      return finalString + numDaysLaterString
    elif switches > 2: return finalString + ' ' +  numDaysLaterString
  else:
    indexToAdd = (numDaysLater + indexDay) % 7
    day = daysOfTheWeek[indexToAdd]
    if (switches == 1 and originalSuffix == 'PM') or (switches == 2): return finalString + ', ' +  day + ' (next day)'
    if switches > 2 and originalSuffix == 'PM':
      switches += 1
      return finalString + ', ' +  day + numDaysLaterString
    elif switches > 2: return finalString + ', ' + day + numDaysLaterString
    else: return finalString + ', ' +  day

  return finalString