print ("== Positivity Machine ==")
print (" ")
name = input ("What's your first name?  ")
surname = input ("What's your surname?  ")
goals = input ("What do you want to achieve?  ")
hobbies = input ("What do you love to do in your spare time?  ")
print ("")

day = input ("What day of the week is it?  ")
task = input ("What task do you hope to achieve today?  ")
print ("")

if day == "Sunday" or "sunday":
  print ("Today's task is to", task)
elif day == "Monday" or "monday":
  print ("Today's task is to", task)
elif day == "Tuesday" or "tuesday":
  print ("Today's task is to", task)
elif day == "Wednesday" or "wednesday":
  print ("Today's task is to", task)
elif day == "Thursday" or "thursday":
  print ("Today's task is to", task)
elif day == "Friday" or "friday":
  print ("Today's task is to", task)
elif day == "Saturday" or "saturday":
  print("Today's task is to", task)
else:
  print ("Put in the correct day")
print ("")

print ("Okay. So", name, surname, "on this beautiful", day+", you must strive to", task, "for today to achieve", goals+". Just in time to go back to", hobbies+". Come on. Get to it now!!! You can do this.")