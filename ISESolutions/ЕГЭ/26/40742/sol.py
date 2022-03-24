with open(r'ISESolutions\ЕГЭ\26\40742\26.txt') as f:
    data_s = f.read().split("\n")

n = int(data_s.pop(0))
del data_s[-1]
data = [list(map(int, i.split(" "))) for i in data_s]

start_time = 1633305600
end_time = start_time + 604800
# count = 0

time_process = [0]*(604800+1)
for start, end in data:
    # print(start, end)
    if not start:
        start = start_time
    if not end:
        end = end_time

    # if start < start_time < end:
    #     count += 1
        # print(count)
    if start_time <= start <= end_time:
        time_process[start - start_time] += 1
    if start_time <= end <= end_time:
        # print(end, start_time, end - start_time)
        time_process[end - start_time] -= 1


count = 0
sum_time = 0
max_process = 0
for time in time_process:
    count += time
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time += 1
    # print(count)

print(max_process, sum_time)
