from tkinter import *
from tkinter import ttk
import random
import math

def calculateTeamDistribution(numOfMembers, numOfTeams):
    teamSize = []
    lastEvenSize = 0
    mathSize = math.ceil(numOfMembers / numOfTeams)
    for i in range(numOfMembers, 0, -1):
        if i % numOfTeams == 0:
            lastEvenSize = i
            break

    for i in range(0, numOfTeams):
        teamSize.append(int(lastEvenSize / numOfTeams))

    while not sum(teamSize) == numOfMembers:
        minEle = min(teamSize)
        idx = teamSize.index(minEle)
        teamSize[idx] = teamSize[idx] + 1
    return teamSize
def provideTeamMembers():
    teamMembers = []
    print("Please provide teams members to choose from: ")
    for i in range (0, numberOfMembers):
        ele = input()
        teamMembers.append(ele)
    return teamMembers
def randomizeTeams(numOfTeams, teamDistro, mbrs):
    result=''
    counter=0
    for i in range(1, numOfTeams + 1):
        result = result + "Team " + str(i)
        result = result + '\n'
        for j in range(0, teamDistro[counter]):
            pick = random.choice(mbrs)
            result = result + pick + '\n'
            mbrs.remove(pick)
            if len(mbrs) == 0:
                break
        counter = counter + 1
        result = result + '\n\n'
    return result

def calculate(*args):
    
    numOfTeams = int(numberOfTeams.get())
    mbrs = members.get()
    mbrs = mbrs.replace(' ', '')
    mbrs = mbrs.split(',')
    numOfMembers = int(len(mbrs))
    if checkboxState.get() == 0:
        teamDistribution = calculateTeamDistribution(numOfMembers, numOfTeams)
        algResult.set("Algorithm calculated that the best Teams distribution would be: " + str(teamDistribution))
        finalTeams.set(randomizeTeams(numOfTeams, teamDistribution, mbrs))
    elif checkboxState.get() == 1:
        numberOfActualMembers = int(numOfMembers / int(numOfTeams)) * int(numOfTeams)
        teamDistribution = calculateTeamDistribution(numberOfActualMembers, numOfTeams)
        algResult.set("Algorithm calculated that the best Teams distribution would be: " + str(teamDistribution))
        finalTeams.set(randomizeTeams(numOfTeams, teamDistribution, mbrs))
    else:
        print("Checkbox problem detected!")

def hide_widget(widget):
   widget.pack_forget()

def show_widget(widget):
   widget.pack()

def toggle():
    label = ttk.Label(mainframe, text="Please provide number of desired Teams").grid(column=4, row=1, sticky=N)

    if checkboxState.get() == 1:
        lambda:show_widget(label)
        entry.grid(column=4, row=2, sticky=N)
    else:
        entry.grid_forget()
        lambda:hide_widget(label)
        

root = Tk()
entryValue = IntVar()
entry = Entry(root, width=3, textvariable=entryValue)
root.title("Random Team Generator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="OPTIONS").grid(column=3, row=1, sticky=N)
checkboxState = IntVar()
ttk.Checkbutton(mainframe, text="Should we make Teams equal in size?", variable=checkboxState).grid(column=3, row=2, stick=W)

ttk.Label(mainframe, text="----------------").grid(column=3, row=3, sticky=N)

ttk.Label(mainframe, text="----------------").grid(column=3, row=3, sticky=N)

ttk.Label(mainframe, text="Please provide number of desired Teams").grid(column=3, row=4, sticky=N)
numberOfTeams = StringVar()
numberOfTeams_entry = ttk.Entry(mainframe, width=3, textvariable=numberOfTeams)
numberOfTeams_entry.grid(column=3, row=5, sticky=S)

ttk.Label(mainframe, text="Please provide people to choose from").grid(column=3, row=8, sticky=N)
members = StringVar()
members_entry = ttk.Entry(mainframe, width=30, textvariable=members)
members_entry.grid(column=3, row=9, sticky=S)

ttk.Button(mainframe, text="Randomize", command=calculate).grid(column=3, row=10, sticky=S)

algResult = StringVar()
ttk.Label(mainframe, textvariable=algResult).grid(column=3, row=11, sticky=(W, E))

finalTeams = StringVar()
ttk.Label(mainframe, textvariable=finalTeams).grid(column=3, row=13, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()