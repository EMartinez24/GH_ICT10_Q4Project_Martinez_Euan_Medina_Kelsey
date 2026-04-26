from pyscript import document, display
import numpy as np

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = [0, 0, 0, 0, 0]

def displaying(e):
    day_selected = document.getElementById('dayOfTheWeek').value
    absence_input = document.getElementById('absences').value

    if not absence_input.strip():
        return

    absence_value = int(absence_input)

    if day_selected in days:
        index = days.index(day_selected)
        absences[index] = absence_value

    converted_absences = np.array(absences)

    plt.clf()

    plt.plot(days, converted_absences, marker='o')
    plt.title('Weekly Attendance (Absences)')
    plt.xlabel('Day')
    plt.ylabel('Number of Absences')

    display(plt.gcf(), target='output')