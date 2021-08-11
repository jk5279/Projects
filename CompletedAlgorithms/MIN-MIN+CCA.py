# minmin + cca

import csv

# file_path = "/content/drive/MyDrive/SchedulingPractice/5X10/5X10-2.csv"
# file_path = "/content/drive/MyDrive/SchedulingPractice/maxmindatafile.csv"
# file_path = "C:/Users/김종은/Desktop/스케쥴링/maxmindatafile.csv"

# file_path = "C:/Users/user/Desktop/종은/dataset/dataset/smalldata/m=5/5x80-5.csv"
# file_path = "C:/Users/user/Desktop/종은/dataset/dataset/smalldata/n=50/8x50-5.csv"
file_path = "C:/Users/user/Desktop/종은/dataset/dataset/m=10/n=200/200x10-5.csv"

# file_path = "C:/Users/user/Desktop/종은/maxmindatafile.csv"

def get_task_list(file_path):
    task_list = list()
    with open(file_path, 'r', newline='') as file:
        read_task = csv.reader(file, delimiter=',')
        task_no = 0
        for task in read_task:
            task_list.append([task_no] + task)
            task_no = task_no + 1
    return task_list

def get_machine_state_list(rj_list):
    machine_state_list = list()
    for a in range(0, m):
        machine_state_list.append(0)

    for task in rj_list:
        machine_state_list[task[1]] += task[2]
    return machine_state_list


def get_int_task_list(task_list):
    int_task_list = list()
    for i in range(0, len(task_list)):
        int_task_list.append(list(map(int, task_list[i])))
        int_task_list[i].pop(0)
    return int_task_list

def get_Cij_list(m):
    Cij_list = list()
    for i in range(0, m):
        Cij_list.append(list())
    return Cij_list


#Get U
task_list = get_task_list(file_path)

#Get m, n
m = len(task_list[0]) - 1
n = len(task_list)

#Change list values to int type
task_list = get_int_task_list(task_list)

Eij_list = task_list

#Cij list reset
Cij_list = get_Cij_list(m)

#Get Min Eij for each Ti in U
rj_list = list()
for task_no, Ti in enumerate(Eij_list):
    rj_list.append([task_no, Ti.index(min(Ti)), Eij_list[task_no][Ti.index(min(Ti))]])

#Get final Cij state for all machines
Cij_list = get_machine_state_list(rj_list)

#Get makespan, makespan machine index from Cij list
makespan = max(Cij_list)
makespan_machine_idx = Cij_list.index(makespan)

#Creat a makespan list for stopping condition
makespan_list = [makespan, makespan]


#--------Incorporate parts of CCA---------
#Get list of tasks assigned to makespan machine index(machine with largest Cij)
makespan_machine_task_list = [item for item in rj_list if item[1] == makespan_machine_idx]

#Sort tasks in descending order regarding Eij
makespan_machine_task_list = list(sorted(makespan_machine_task_list, key= lambda x:x[-1], reverse=True))

#Calculate final Cij for task with largest Eij in makespan machine if assigned to all machines(0 ~ m)
temp_Cij_list = list()
for m_idx in range(0,m):
    rj_list[makespan_machine_task_list[0][0]][1] = m_idx
    rj_list[makespan_machine_task_list[0][0]][2] = Eij_list[makespan_machine_task_list[0][0]][m_idx] #Update assigned machine and Eij
    Cij_list = get_machine_state_list(rj_list) #Calculate final Cij with updated rj_list
    temp_Cij_list.append(max(Cij_list)) #Get makespan
makespan = min(temp_Cij_list) #Get the smallest makespan for all probable cases.
makespan_machine_idx = temp_Cij_list.index(min(temp_Cij_list)) #Get the makespan machine for the case above

#update rj_list to case with smallest makespan
rj_list[makespan_machine_task_list[0][0]][1] = makespan_machine_idx
rj_list[makespan_machine_task_list[0][0]][2] = Eij_list[makespan_machine_task_list[0][0]][makespan_machine_idx]

#add makespan to makespan list
makespan_list.append(makespan)

#decide whether makespan is decreasing or not
while makespan_list[-1] != makespan_list[-2] or makespan_list[-2] != makespan_list[-3] and makespan_list[-1] <= makespan_list[-2]:
    temp_Cij_list.clear()
    for m_idx in range(0, m):
        rj_list[makespan_machine_task_list[0][0]][1] = m_idx
        rj_list[makespan_machine_task_list[0][0]][2] = Eij_list[makespan_machine_task_list[0][0]][
            m_idx]  # Update assigned machine and Eij
        Cij_list = get_machine_state_list(rj_list)  # Calculate final Cij with updated rj_list
        temp_Cij_list.append(max(Cij_list))  # Get makespan
    makespan = min(temp_Cij_list)  # Get the smallest makespan for all probable cases.
    makespan_machine_idx = temp_Cij_list.index(min(temp_Cij_list))  # Get the makespan machine for the case above

    # update rj_list to case with smallest makespan
    rj_list[makespan_machine_task_list[0][0]][1] = makespan_machine_idx
    rj_list[makespan_machine_task_list[0][0]][2] = Eij_list[makespan_machine_task_list[0][0]][makespan_machine_idx]

    # add makespan to makespan list
    makespan_list.append(makespan)

    # Get list of tasks assigned to makespan machine index(machine with largest Cij)
    makespan_machine_task_list = [item for item in rj_list if item[1] == makespan_machine_idx]

    # Sort tasks in descending order regarding Eij
    makespan_machine_task_list = list(sorted(makespan_machine_task_list, key=lambda x: x[-1], reverse=True))


print("task_list:", task_list)
print("m:", m, " n:", n)
print("Eij_list:", Eij_list)
print("rj_list:", rj_list)
print("machine state list:", Cij_list)
print("makespan:", makespan)
print("makespan machine id:", makespan_machine_idx)
print("makespan_list:", makespan_list)
print("makespan_machine_task_list:", makespan_machine_task_list)


def get_scheduler_list(rj_list, m):
    scheduler_list = list()
    machine_state_list = list()
    for i in range(0, m):
        machine_state_list.append(0)

    for scheduler_task in rj_list:
        demand_id = scheduler_task[0]
        machine_id = scheduler_task[1]
        demand_type = 'Z'
        p_time = scheduler_task[2]
        s_time = machine_state_list[machine_id]
        c_time = p_time + s_time
        due_date = 999999
        setup = "X"
        violation_time = 0
        scheduler_list.append(
            [demand_id, machine_id, demand_type, p_time, s_time, c_time, due_date, setup, violation_time])
        machine_state_list[machine_id] = c_time

    return scheduler_list

scheduler_list = list(get_scheduler_list(rj_list, m))
with open("C:/Users/user/Desktop/종은/scheduler_file.csv", 'w', newline="") as file:
    write = csv.writer(file)
    write.writerow([m,n])
    write.writerows(scheduler_list)
