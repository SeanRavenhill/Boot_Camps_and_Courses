def add_time(start, duration, day=""):
    
  # Extracts, separates and stores data from the (start) argument.
  start_hour_and_minute = start.split(' ')
  start_hour = int(start_hour_and_minute[0].split(":")[0])
  start_minute = int(start_hour_and_minute[0].split(':')[1])
  start_am_pm = start.split(' ')[1]
  
  # Extracts, separates and stores data from the (duration) argument.
  duration_hour_and_minute = duration.split(':')
  hours_added = int(duration_hour_and_minute[0])
  minutes_added = int(duration_hour_and_minute[1])

  ############################################################
  ####   BLOCK OF LOGIC TO COMPUTE UPDATED TIME OUTPUT   #####        
  ############################################################

  # Adds up the minutes total & adds an hour to the duration hour,
  # if the total of the minutes is greater than 60 minutes.
  minutes_total = start_minute + minutes_added
  if minutes_total >= 60:
    minutes_total = minutes_total % 60
    hours_added += 1

  # Adds up the total hours from both start hour and duration hour.
  hours_total = start_hour + hours_added
  # Variable to store hours_total, to apply Modulus operator, so the hours_total is not overwritten.
  hours_modulo = 0
  # Variable to contation final hour calculations output.
  hours_output = 0
  # Creates variable to store days_count ouput. 
  days_count = 0

  # Used to calculate the hour of the time, the (next day) 
  # and (x days later) requirements of the project brief.
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

  ############################################################
  #######   BLOCK OF LOGIC TO COMPUTE WEEKDAY OUTPUT   #######
  ############################################################

  # Used to keep day variable as an empty string if no optional variable provided.
  if day == "":
    day_output = day
  else:
  # Takes the day optional variable and converts to all lower case
  # then capitalises the first charater.
    day = day.lower().capitalize()

    week_day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # First finds the index of the optional variable input of day in
    # relation to the week_day_list variable above. Then uses that 
    # index added to the day count to find the new index/day progression 
    # in the list. If that amount goes over the index terminus of 6 (Which 
    # is the seventh day of of the week) Then the Modulus operater to a 
    # value of 7 is applied to that new index number to get the index_out.
    if day in week_day_list:
      i = week_day_list.index(day)
      for x in week_day_list:
        new_index = i + days_count
        if new_index <= 6:
          index_out = new_index
        elif new_index > 6: 
          index_out = new_index % 7

    # Creates a string varible with the day out output.
    day_output = ', ' + week_day_list[index_out]

  return print_time(hours_total, hours_output, minutes_total, start_am_pm, day_output, days_count, hours_added, minutes_added)

############################################################
##   FUNCTION RETURNS STRING OF FINAL TIME, DAY & COUNT   ##
############################################################

# Wrote this as a seperate function to reduce cyclomatic complexity of add_time function.
def print_time(hours_total, hours_output, minutes_total, start_am_pm, day_output, days_count, hours_added, minutes_added):

  # Variables to store final string outputs.
  hour_string = ""
  minute_string = ""
  end_am_pm_string = ""
  day_string = ""
  days_later_string = ""

  # Creates the hour output string and stores it in he hours_string variable.
  if hours_output == 0:
    hour_string += "12"
  else:
    hour_string += str(hours_output)

  # Creates the minute output string and stores it in he minute_string variable.
  if len(str(minutes_total)) == 1:
    minute_string += "0" + str(minutes_total)
  else:
    minute_string += str(minutes_total)

  ############################################################
  ########   BLOCK OF LOGIC TO ADDRESS UNIT TESTS   ##########
  ############################################################

  # Addresses test_same_period(self) & test_different_period(self) functions in test_module.py
  if hours_total <= 12:
    if start_am_pm == "AM":
      end_am_pm_string = " PM"
    else:
      end_am_pm_string = " " + start_am_pm
  # Addresses test_next_day(self) & test_period_change_at_twelve(self) functions in test_module.py
  elif hours_total > 12 and hours_total < 24:
    if start_am_pm == "PM":
      end_am_pm_string += " AM"
      days_later_string += " (next day)"
    else:
      end_am_pm_string += " PM"
  # Addresses test_no_change(self) function in test_module.py
  if hours_added == 0 and minutes_added == 0:
    end_am_pm_string = " " + start_am_pm
  # Addresses test_twenty_four(self) function in test_module.py
  if hours_added == 24:
    end_am_pm_string = " " + start_am_pm
    days_later_string += " (next day)"
  # Addresses test_two_days_later(self) & test_high_duration(self) functions in test_module.py
  elif hours_total > 24:
    if start_am_pm == "PM":
      end_am_pm_string += " AM"
      days_later_string += " " + "(" + str(days_count) + " days later)"
    else:
      end_am_pm_string += " PM"
      days_later_string += " " + "(" + str(days_count) + " days later)"
  
  # Addresses all unit test function with _with_day(self) requirements. ie. test_same_period_with_day(self).
  # Because the variable at the beggining of this function, being an empty string. If no optional variable
  # is declared in the add-time functions parameters, the final string does not render anything at days_later_string.
  day_string += day_output

  # Uses string concatenation from the string variable declared at the start of this function to create a final string for output. 
  time_string = hour_string + ":" + minute_string + end_am_pm_string + day_string + days_later_string

  return time_string