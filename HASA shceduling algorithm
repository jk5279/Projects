task_list = [[0, '10', '2', '4', '1'], [1, '3', '4', '8', '6'], [2, '9', '5', '8', '6'], [3, '6', '10', '7', '7'], [4, '8', '3', '4', '2'], [5, '3', '6', '6', '8'], [6, '10', '6', '10', '7'], [7, '10', '5', '2', '3']]

int_task_list = list()
for i in range(0, len(task_list)):
    int_task_list.append(list(map(int, task_list[i])))

task_list = int_task_list
print(task_list)
m = len(task_list[0]) - 1
n = len(task_list)

machine_state_list = list()
for i in range(0, m):
    machine_state = 0
    machine_state_list.append(machine_state)

comp_time = 0
min_list = list()
min_idx_list = list()
temp_idx = list()
schedule_list = list()
abs_val_list = list()
for t in range(0, len(task_list)):
    for task in task_list:
        for i in range(1, m + 1):
            task_comp_time = int(machine_state_list[i - 1]) + int(task[i])
            if i == 1:
                comp_time = task_comp_time
                temp_index = i
            elif task_comp_time < comp_time:
                comp_time = task_comp_time
                temp_index = i
            task_comp_time = 0
        min_list.append(comp_time)
        min_idx_list.append(temp_index)

    comptime_average = 0.0
    comptime_average = float(sum(min_list)) / float(len(min_list))
    comptime_average = float(comptime_average) / 2.0

    min_abs_val = 0.0
    min_abs_val_idx = 0
    temp = 0.0
    for val in min_list:
        temp = abs(val - comptime_average)
        abs_val_list.append(temp)

    min_abs_val = min(abs_val_list)
    min_abs_val_idx = abs_val_list.index(min_abs_val)

    j = min_abs_val_idx
    k = min_idx_list[j]

    temp_list = [task_list[j][0], k - 1, task_list[j][k]]
    schedule_list.append(temp_list)

    machine_state_list[k - 1] = machine_state_list[k - 1] + task_list[j][k]
    task_list.pop(j)

    min_list = list()
    min_idx_list = list()

    abs_val_list = list()

print(schedule_list)
hasa_schedule_list = list()
for i in range(0,m):
  hasa_schedule_list.append(list())

for l in schedule_list:
  task_no = l[0]
  machine_no = l[1]
  hasa_schedule_list[machine_no].append(task_no)

print(hasa_schedule_list)
