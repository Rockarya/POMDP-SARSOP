# roll number used = 2019101082
roll_num = 2020121011
no_of_states = 128
no_of_cells = 8
no_of_actions = 5
actions = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0], [0, 0], [0, -1], [0, 1], [1, 0], [-1, 0]]
target_action_prob = [0.6, 0.1, 0.1, 0.1, 0.1]
target_call_prob = [[0.5, 0.5], [0.1, 0.9]]
agent_success_prob = 1 - ((roll_num % 10000) % 30 + 1) / 100
agent_action_prob = [1.0, agent_success_prob, agent_success_prob, agent_success_prob, agent_success_prob]
final_reward = roll_num % 90 + 10

print("discount: 0.5")
print("values: reward")
print("states: 128")
print("actions: 5")
print("observations: 6")


def convert_to_num(a, b, c):
    # a is target position
    # b is agent position
    # c is call state value
    return a * 16 + b * 2 + c


def give_new_cell(cell, action):
    a, b = convert_to_tuple(cell)
    a = min(1, max(0, a + actions[action][1]))
    b = min(3, max(0, b + actions[action][0]))
    return a * 4 + b


def give_state_tuple(num):
    a = int(num / 16)
    num = num % 16
    b = int(num / 2)
    return a, b, num % 2


def convert_to_tuple(num):
    a = int(num / 4)
    # a is y value in grid and num%4 is x
    return a, num % 4


probabs = [[[0.0 for i in range(128)] for i in range(128)] for i in range(5)]
# transition function


# agent's cell
for k in range(no_of_cells):
    # target's cell
    for j in range(no_of_cells):
        for call in range(2):
            # agent's action
            for m in range(no_of_actions):
                temp = 0.0
                # target's action
                for i in range(no_of_actions):
                    prob = 1
                    if k is j and call is 1:
                        probabs[m][convert_to_num(k, j, call)][convert_to_num(k, j, 1-call)] = 1.0
                        continue
                    # call remaining the same as it was and agent action is successful
                    probabs[m][convert_to_num(k, j, call)][convert_to_num(give_new_cell(k, m),
                                                                          give_new_cell(j, i),
                                                                          call)] += \
                        prob * target_call_prob[call][call] * target_action_prob[i] * agent_action_prob[m]

                    # call unchanged but agent action is unsuccessful
                    probabs[m][convert_to_num(k, j, call)][convert_to_num(give_new_cell(k, m+5),
                                                                          give_new_cell(j, i),
                                                                          call)] += \
                        prob * target_call_prob[call][call] * target_action_prob[i] * (1-agent_action_prob[m])

                    # call changes now and agent action is successful
                    probabs[m][convert_to_num(k, j, call)][convert_to_num(give_new_cell(k, m),
                                                                          give_new_cell(j, i),
                                                                          1-call)] += \
                        prob * target_call_prob[call][1-call] * target_action_prob[i] * agent_action_prob[m]

                    # call changes now and agent action is unsuccessful
                    probabs[m][convert_to_num(k, j, call)][convert_to_num(give_new_cell(k, m+5),
                                                                          give_new_cell(j, i),
                                                                          1-call)] += \
                        prob * target_call_prob[call][1-call] * target_action_prob[i] * (1-agent_action_prob[m])


for i in range(no_of_actions):
    for j in range(no_of_states):
        for k in range(no_of_states):
            print("T: {} : {} : {} {}".format(i, j, k, probabs[i][j][k]))
# observations here
observation = [0 for i in range(no_of_states)]


def printa(num, i):
    print(num, "1")
    observation[i] = num


for i in range(no_of_states):
    agent, target, call_state = give_state_tuple(i)
    print("O : * : {} : ".format(i), end='')
    if target == agent:
        printa(0, i)
    elif abs(target % 4 - agent % 4) + abs(int(target / 4) - int(agent / 4)) == 1:
        if target % 4 > agent % 4:
            printa(1, i)
        elif target % 4 < agent % 4:
            printa(3, i)
        elif target / 2 > agent / 2:
            printa(4, i)
        else:
            printa(2, i)
    else:
        printa(5, i)

# rewards here at the end
for i in range(no_of_actions):
    for j in range(no_of_states):
        a, b, c = give_state_tuple(j)
        r = 0
        if a == b and c == 1:
            r = final_reward
        if i != 0:
            r -= 1
        print("R: {} : * : {} : {} {}".format(i, j, observation[j], r))
