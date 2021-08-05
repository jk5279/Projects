#Simualted Annealing Scheduling Algorithm using HASA as a base
import time
import itertools
import numpy as np
import os
import math
import random as rand
from itertools import chain
import csv



task_list = list()

with open (file_path, 'r', newline='') as file:
  read_task = csv.reader(file, delimiter=',')
  task_no = 0
  for task in read_task:
    task_list.append([task_no] + task)
    task_no = task_no + 1

int_task_list = list()
for i in range(0, len(task_list)):
    int_task_list.append(list(map(int, task_list[i])))

task_list = int_task_list

def get_max_span(state,task_time_list):
    state = state
    mach_sum_list = list()
    for a in state:
        machine_sum = 0
        for i in a:
            n_i = i
            m_i = state.index(a)
            machine_sum = machine_sum + int(task_time_list[m_i+1][n_i])
        mach_sum_list.append(machine_sum)
        machine_sum = 0
    tot_sum = max(mach_sum_list)
    return tot_sum


def get_machine_task_time_list(task_list):
    task_time_list = list()
    n = len(task_list)
    m = len(task_list[0])
    for i in range(0, m):
        task_time_list.append(list())
    for i in range(0, n):
        for j in range(0, m):
            task_time_list[j].append(task_list[i][j])
    return task_time_list

def get_neighbor_state_list(m, n_change, state_list, state):
    state_list.clear()
    state = sum(state, [])
    data = list(state)
    rand.shuffle(data)
    for i in range(0, n_change):
        indexes = sorted([rand.randint(1, len(data) - 1) for _ in range(m - 2)])
        indexes = [0] + indexes + [None]
        result = list(data[s:e] for s, e in zip(indexes, indexes[1:]))
        state_list.append(result)
    return state_list

#데이터 모양 변환
task_time_list = list(get_machine_task_time_list(task_list))

#최적 스케쥴에 근접하는 스케쥴 설정
near_opt_schedule = hasa_schedule_list
# near_opt_schedule = minmax_schedule_list


state = list(near_opt_schedule)
tot_sum = 0

n = len(task_list)
m = len(task_list[0])

#해당 스케쥴에 대한 makespan 계산
tot_sum = get_max_span(state,task_time_list)

#담금질 기법 0번째 횟수
cnt = 0
anneal_temp = tot_sum * 0.99 * 100
max_span = 0
z = 0
euler_z = 0.0
yes_cnt = 0
check_yes = 0

neighbor_list = list()

neighbor_state = list(chain.from_iterable(state))
n_change = len(neighbor_state)
state_list = list()

max_span = tot_sum

state_list = get_neighbor_state_list(m, n_change, state_list, state)

rand_val = rand.randint(0, n_change - 1)
state = state_list[rand_val]

#담금질 온도 감소
anneal_temp = 0.99 * max_span
cnt = cnt + 1
change_cnt = 0
a_timer = time.time()
b_timer = time.time()

#담금질 반복 시작
while yes_cnt != 3:
    a_timer = time.time()
    tot_sum = get_max_span(state,task_time_list)
    if tot_sum > max_span:
        z = abs(max_span - tot_sum) / anneal_temp
        euler_z = math.e ** (z * -1)
        rand_val = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1) #이웃해 탐색 진행 여부를 판단하기 위한 난수 생성

        if euler_z > rand_val:
            yes_cnt = yes_cnt + 1
            state_list = get_neighbor_state_list(m, n_change, state_list, state) #무작위 이웃해 탐색

            rand_val = rand.randint(0, n_change - 1)
            state = state_list[rand_val] #탐색된 이웃해 선택

        else:
            if change_cnt != n_change:
                rand_val = rand.randint(0, n_change - 1)
                state = state_list[rand_val]
                change_cnt = change_cnt + 1
            else:
                state_list = get_neighbor_state_list(m, n_change, state_list, state)
                rand_val = rand.randint(0, n_change - 1)
                state = state_list[rand_val]

                change_cnt = 0

    else:
        yes_cnt = yes_cnt + 1
        max_span = tot_sum
        near_opt_schedule = state
        state_list = get_neighbor_state_list(m, n_change, state_list, state)

        rand_val = rand.randint(0, n_change - 1)
        state = state_list[rand_val]

    anneal_temp = 0.99 * anneal_temp
    cnt = cnt + 1

#탐색된 최적해에 근접하는 스케쥴 및 해당 스케쥴 Makespan 출력
max_span = get_max_span(near_opt_schedule,task_time_list)
print(max_span)
print(near_opt_schedule)
