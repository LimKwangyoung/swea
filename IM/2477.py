import sys

sys.stdin = open('input.txt')
##################################################
import collections

# Solution 1
T = int(input())

for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    clients = collections.deque(list(map(int, input().split())))

    result = 0

    time = 0
    client_id = 1
    waiting = collections.deque([])
    counter_1, counter_2 = [False] * N, [False] * M  # [process time, client id]
    client_set = set()
    while True:
        if not clients and counter_1.count(False) == N and counter_2.count(False) == M and not waiting:
            break

        # repair
        for i, counter in enumerate(counter_2):
            if counter:
                counter_2[i][0] -= 1  # repair
                if counter_2[i][0] == 0:  # complete repair
                    if waiting:  # enter for repair
                        counter_2[i] = [repair[i], waiting.popleft()]
                        if i + 1 == B and counter_2[i][1] in client_set:  # target counter in repair
                            result += counter_2[i][1]
                    else:  # initializing
                        counter_2[i] = False
            elif waiting:  # enter for repair
                counter_2[i] = [repair[i], waiting.popleft()]
                if i + 1 == B and counter_2[i][1] in client_set:  # target counter in repair
                    result += counter_2[i][1]

        # reception
        for i, counter in enumerate(counter_1):
            if counter:
                counter_1[i][0] -= 1  # reception
                if counter_1[i][0] == 0:  # complete reception
                    waiting.append(counter[1])
                    if clients and time >= clients[0]:  # enter for reception
                        counter_1[i] = [reception[i], client_id]
                        clients.popleft()
                        client_id += 1
                        if i + 1 == A:  # target counter in reception
                            client_set.add(counter_1[i][1])
                    else:
                        counter_1[i] = False
            elif clients and time >= clients[0]:  # enter for reception
                counter_1[i] = [reception[i], client_id]
                clients.popleft()
                client_id += 1
                if i + 1 == A:  # target counter in reception
                    client_set.add(counter_1[i][1])

        # client for waiting
        for i, counter in enumerate(counter_2):
            if waiting and not counter:
                counter_2[i] = [repair[i], waiting.popleft()]
                if i + 1 == B and counter_2[i][1] in client_set:  # target counter in repair
                    result += counter_2[i][1]
        time += 1
    print(f'#{t} {result if result else -1}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    clients = list(map(int, input().split()))

    target = set()

    # reception
    waiting = []  # (client id, end time, counter id)
    counters = [0] * N  # end time about reception counter
    for client_id, client in enumerate(clients):
        minimum = float('inf')
        min_idx = -1
        for idx, counter in enumerate(counters):
            if counter <= client:
                counters[idx] = client + reception[idx]
                waiting.append((client_id + 1, counters[idx], idx + 1))

                # check target
                if idx + 1 == A:
                    target.add(client_id + 1)
                break
            if counter < minimum:
                minimum = counter
                min_idx = idx
        else:
            counters[min_idx] += reception[min_idx]
            waiting.append((client_id + 1, counters[min_idx], min_idx + 1))

            # check target
            if min_idx + 1 == A:
                target.add(client_id + 1)

    waiting.sort(key=lambda x: (x[1], x[2]))

    # repair
    result = 0
    counters = [0] * M  # end time about repair counter
    for client_id, client, _ in waiting:
        minimum = float('inf')
        min_idx = -1
        for idx, counter in enumerate(counters):
            if counter <= client:
                counters[idx] = client + repair[idx]

                # check target
                if idx + 1 == B and client_id in target:
                    result += client_id
                break
            if counter < minimum:
                minimum = counter
                min_idx = idx
        else:
            counters[min_idx] += repair[min_idx]

            # target
            if min_idx + 1 == B and client_id in target:
                result += client_id
    print(f'#{t} {result if result else -1}')
