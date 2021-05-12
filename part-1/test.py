# Amin
import numpy as np

roll_num_last4 = 1056
roll_num_last2 = 56


# x = 1.00 - ((roll_num_last4%30) + 1)/100.0
# y = roll_num_last2%4 + 1

x = 0.93
y = 1

print(x,y)
p_red = 0.0 
p_green = 0.0

if y==1:
    p_red = 0.95
    p_green = 0.8

if y==2:
    p_red = 0.9
    p_green = 0.85

if y==3:
    p_red = 0.85
    p_green = 0.9

if y==4:
    p_red = 0.8
    p_green = 0.95



belief = [1/3,0.0,1/3,0.0,0.0,1/3]

for action in range(0,3):
    belief_upd = [0.0,0.0,0.0,0.0,0.0,0.0]
    if action == 0:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (1.00-p_red)*((1-x)*belief[0] + (1-x)*(belief[1]))
            if i==1:
                belief_upd[i] = (p_green)*(x*belief[0] + (1-x)*belief[2])
            if i==2:
                belief_upd[i] = (1.00-p_red)*(x*belief[1] + (1-x)*belief[3])
            if i==3:
                belief_upd[i] = (p_green)*(x*belief[2] + (1-x)*belief[4])
            if i==4:
                belief_upd[i] = (p_green)*(x*belief[3] + (1-x)*belief[5])
            if i==5:
                belief_upd[i] = (1.00- p_red)*(x*belief[4] + x*belief[5])

    if action == 1:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (p_red)*(x*belief[0] + x*belief[1])
            if i==1:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[0] + (x)*belief[2])
            if i==2:
                belief_upd[i] = (p_red)*((1-x)*belief[1] + (x)*belief[3])
            if i==3:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[2] + (x)*belief[4])
            if i==4:
                belief_upd[i] = (1.00-p_green)*((1-x)*belief[3] + (x)*belief[5])
            if i==5:
                belief_upd[i] = (p_red)*((1-x)*belief[4] + (1-x)*belief[5])

    if action == 2:
        for i in range(0,6):
            if i==0:
                belief_upd[i] = (1.00-p_red)*((x)*belief[0] + (x)*(belief[1]))
            if i==1:
                belief_upd[i] = (p_green)*((1-x)*belief[0] + (x)*belief[2])
            if i==2:
                belief_upd[i] = (1.00-p_red)*((1-x)*belief[1] + (x)*belief[3])
            if i==3:
                belief_upd[i] = (p_green)*((1-x)*belief[2] + (x)*belief[4])
            if i==4:
                belief_upd[i] = (p_green)*((1-x)*belief[3] + (x)*belief[5])
            if i==5:
                belief_upd[i] = (1.00- p_red)*((1-x)*belief[4] + (1-x)*belief[5])
    const = 0.0
    for j in range(0,6):
        belief[j] = belief_upd[j]
        print(belief[j])
        const += belief[j]
    
    print("const: ",const)
    for j in range(0,6):
        belief[j] = belief[j]/const
        print("Action: ",action+1,"State: ",j+1,"Belief: ",belief[j])
    print()
