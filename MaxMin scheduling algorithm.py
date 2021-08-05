#example data
task_list = [[0, '10', '2', '4', '1'], [1, '3', '4', '8', '6'], [2, '9', '5', '8', '6'], [3, '6', '10', '7', '7'], [4, '8', '3', '4', '2'], [5, '3', '6', '6', '8'], [6, '10', '6', '10', '7'], [7, '10', '5', '2', '3']]

for i in range(0, len(task_list)):
  int_task_list.append(list(map(int, task_list[i])))

task_list = int_task_list

m = len(task_list[0]) -1
n = len(task_list)


machine_state_list = list()
for i in range(0,m):
  machine_state = 0
  machine_state_list.append(machine_state)

comp_time = 0
min_list = list()
min_idx_list = list()
temp_idx = list()
schedule_list = list()
for t in range(0, len(task_list)):
  for task in task_list:
    for i in range(1,m+1):
      task_comp_time = int(machine_state_list[i-1]) + int(task[i])
      if i == 1:
        comp_time = task_comp_time
        temp_index = i
      elif task_comp_time < comp_time:
        comp_time = task_comp_time
        temp_index = i
      task_comp_time = 0
    min_list.append(comp_time)
    min_idx_list.append(temp_index)
    
  max_time = max(min_list)
  max_idx = min_list.index(max_time)

  j = max_idx
  k = min_idx_list[max_idx]

  temp_list = [task_list[j][0], k-1,task_list[j][k]]      
  schedule_list.append(temp_list)

  machine_state_list[k-1] = max_time
  task_list.pop(j)
    
  min_list = list()
  min_idx_list = list()
  max_time = 0
  max_idx = 0

print(schedule_list)
