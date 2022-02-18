hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
hour_mins=hour*60#convert entered hour to mins
enteredtime_mins=hour_mins+mins#convert entered hour and min to total mins
end_time=(enteredtime_mins+dura)/60
if end_time>24:
    end_time=end_time%24

print(end_time)
