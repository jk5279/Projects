import csv

# file_path = "/content/drive/MyDrive/SchedulingPractice/5X10/5X10-2.csv"
# file_path = "/content/drive/MyDrive/SchedulingPractice/maxmindatafile.csv"
# file_path = "C:/Users/김종은/Desktop/스케쥴링/maxmindatafile.csv"
# file_path = "C:/Users/user/Desktop/종은/dataset/dataset/m=10/n=400/400x10-5.csv"

file_path = "C:/Users/user/Desktop/종은/maxmindatafile.csv"

task_list = list()

with open(file_path, 'r', newline='') as file:
    read_task = csv.reader(file, delimiter=',')
    task_no = 0
    for task in read_task:
        task_list.append([task_no] + task)
        task_no = task_no + 1

m = len(task_list[0]) - 1
n = len(task_list)



def get_machine_state_list(rj_list):
    machine_state_list = list()
    for a in range(0, m):
        machine_state_list.append(0)

    for task in rj_list:
        machine_state_list[task[1]] += task[2]
    return machine_state_list


int_task_list = list()
for i in range(0, len(task_list)):
    int_task_list.append(list(map(int, task_list[i])))
    int_task_list[i].pop(0)

Eij_list = int_task_list

Cij_list = list()
for i in range(0, m):
    Cij_list.append(list())

rj_list = list()
for task_no, Ti in enumerate(Eij_list):
    rj_list.append([task_no, Ti.index(min(Ti)), Eij_list[task_no][Ti.index(min(Ti))]])

machine_state_list = list()
machine_state_list = get_machine_state_list(rj_list)

makespan = max(machine_state_list)
makespan_machine_idx = machine_state_list.index(makespan)

makespan_list = [makespan, makespan]

makespan_machine_task_list = [item for item in rj_list if item[1] == makespan_machine_idx]
makespan_machine_task_list = list(sorted(makespan_machine_task_list, key= lambda x:x[-1], reverse=True))

print("task_list:", task_list)
print("m:", m, " n:", n)
print("Eij_list:", Eij_list)
print("rj_list:", rj_list)
print("machine state list: ", machine_state_list)
print("makespan: ", makespan)
print("makespan machine id:", makespan_machine_idx)
print("makespan_list:", makespan_list)
print("makespan_machine_task_list:",makespan_machine_task_list)

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
    write.writerow(str(m))
    write.writerows(scheduler_list)
