import numpy as np

# destination = int(input())
R = np.loadtxt('/home/ketan/Indoormapping/R_file/R6.csv', delimiter = ',')

#np.savetxt('/home/ketan/Indoormapping/R_file/R6.csv',R,delimiter = ',')

# creatiang the Q matrix
Q = np.zeros([11,11])

# gamma
gamma = 0.8

#initial state
initial_state = 1

def available_actions(states):
    current_state_row = R[states,:]
    av_act = [i for i,v in enumerate(current_state_row) if v >= 0]
    return av_act

available_act = available_actions(initial_state)

def sample_next_action(available_action_range):
    next_action = np.random.choice(available_action_range)
    return next_action

action = sample_next_action(available_act)

def update(current_state, action, gamma):
    max_index = np.where(Q[action, :] == np.max(Q[action, :]))[0]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
    
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]
    
    # Q learning formula
    Q[current_state, action] = R[current_state, action] + gamma*max_value
    
# update Q matrix
# update(initial_state, action, gamma)

# Training
for i in range(10000):
    current_state = np.random.randint(0,int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)
    
# normalizing the Q matrix
print("trained Q matrix:")
print(Q/np.max(Q)*100)

# use the following format when the database is ready
np.savetxt('/home/ketan/Indoormapping/Q_file/Q6.csv',(Q/np.max(Q)*100), delimiter = ',')

# testing
# goal state = destination


current_state = np.random.choice([0,1,2,3,4,5,6,7,8,9,10])
steps = [current_state]

while current_state != 6:
    
    next_step_index = np.where(Q[current_state, ] == np.max(Q[current_state, ]))[0]
    
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size = 1))
    
    else:
        next_step_index = int(next_step_index)
    
    steps.append(next_step_index)
    current_state = next_step_index
    
print("you have to follow the following path: ")
print(steps)