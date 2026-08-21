import pywhatkit

students = {"raouf" : '+91', #enter numbers
        "ayaan" : '+91' }  #enter numbers

name = list(students)
numbers = list(students.values())

for i in range(len(students)):
    message = f"This is an Automated mesage for {name[i]}"
    number = numbers[i]

    pywhatkit.sendwhatmsg_instantly(
        number,
        message,
        wait_time=15,
        tab_close=True,
        close_time=1
    )