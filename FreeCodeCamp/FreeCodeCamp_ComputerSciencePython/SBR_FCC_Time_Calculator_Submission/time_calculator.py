def add_time(start, duration, day=""):
    
  start_hour_and_minute = start.split(' ')
  start_hour = int(start_hour_and_minute[0].split(":")[0])
  start_minute = int(start_hour_and_minute[0].split(':')[1])
  start_am_pm = start.split(' ')[1]

  duration_hour_and_minute = duration.split(':')
  hours_added = int(duration_hour_and_minute[0])
  minutes_added = int(duration_hour_and_minute[1])

  minutes_total = start_minute + minutes_added
  if minutes_total >= 60:
    minutes_total = minutes_total % 60
    hours_added += 1

  hours_total = start_hour + hours_added

  hours_modulo = 0

  hours_output = 0

  days_count = 0

  if days_count == 0 and hours_total <= 12:
    hours_output += hours_total  
  elif days_count == 0 and hours_total <= 24:
    hours_modulo += hours_total 
    hours_modulo %= 12
    hours_output += hours_modulo 
    if start_am_pm == "PM":
      days_count += 1
  elif hours_total > 24:
    days_count = round(hours_added // 24)
    hours_modulo += hours_total 
    hours_modulo %= 12
    hours_output += hours_modulo  
    if start_am_pm == "PM":
      days_count += 1

  if day == "":
    day_output = day
  else:
    day = day.lower().capitalize()
    week_day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day in week_day_list:
      i = week_day_list.index(day)
      for x in week_day_list:
        new_index = i + days_count
        if new_index <= 6:
          index_out = new_index
        elif new_index > 6: 
          index_out = new_index % 7

    day_output = ', ' + week_day_list[index_out]

  return print_time(hours_total, hours_output, minutes_total, start_am_pm, day_output, days_count, hours_added, minutes_added)

def print_time(hours_total, hours_output, minutes_total, start_am_pm, day_output, days_count, hours_added, minutes_added):

  hour_string = ""
  minute_string = ""
  end_am_pm_string = ""
  day_string = ""
  days_later_string = ""

  if hours_output == 0:
    hour_string += "12"
  else:
    hour_string += str(hours_output)

  if len(str(minutes_total)) == 1:
    minute_string += "0" + str(minutes_total)
  else:
    minute_string += str(minutes_total)

  if hours_total <= 12:
    if start_am_pm == "AM":
      end_am_pm_string = " PM"
    else:
      end_am_pm_string = " " + start_am_pm
  elif hours_total > 12 and hours_total < 24:
    if start_am_pm == "PM":
      end_am_pm_string += " AM"
      days_later_string += " (next day)"
    else:
      end_am_pm_string += " PM"

  if hours_added == 0 and minutes_added == 0:
    end_am_pm_string = " " + start_am_pm

  if hours_added == 24:
    end_am_pm_string = " " + start_am_pm
    days_later_string += " (next day)"
  elif hours_total > 24:
    if start_am_pm == "PM":
      end_am_pm_string += " AM"
      days_later_string += " " + "(" + str(days_count) + " days later)"
    else:
      end_am_pm_string += " PM"
      days_later_string += " " + "(" + str(days_count) + " days later)"

  day_string += day_output

  time_string = hour_string + ":" + minute_string + end_am_pm_string + day_string + days_later_string

  return time_string