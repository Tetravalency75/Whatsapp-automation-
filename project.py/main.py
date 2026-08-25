

import pywhatkit

students = {"ashhaz" : '+917893191196', #enter numbers
        "ayaan" : '+918074223654', }  #enter numbers

name = list(students)
numbers = list(students.values())

for i in range(len(students)):
    message = f"This is an Automated mesage for {name[i]}"
    number = numbers[i]

    print(f"Sending message to {name[i]} at {number}...")
    try:
        pywhatkit.sendwhatmsg_instantly(
            number,
            message,
            wait_time=10,
            tab_close=True,
            close_time=1
        )
        print(f"Message sent to {name[i]} at {number} successfully.")
    except Exception as e:
        print(f"Failed to send message to {name[i]} at {number}: {e}")