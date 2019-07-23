import numpy as np

# creating R matrix
R = np.array([[],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              [],])

# creatiang the Q matrix
Q = np.zeros([10,10])

# gamma
gamma = 0.8

#initial state
initial_state = np.random.choice([0,1,2,3,4,5,6,7,8,9,10])

def available_actions(states):
    current_state_row = R[state,:]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act

available_act = available_actions(initial_state)

def sample_next_action(available_action_range):
    next_action = int(np.random.choice(available_act, 1))
    return next_action

action = sample_next_action(available_act)

def update(current_state, action, gamma):
    max_index = np.where(Q[action, :] == np.max(Q[action, :]))[1]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
    
    else:
        max_index = int(max_index)
    max_value = q[action, max_index]
    
    # Q learning formula
    Q[current_state, action] = R[current_state, action] + gamma*max_value
    
# update Q matrix
update(initial_state, action, gamma)

# Training
for i in range(10000):
    current_state = np.random.randint(0,int(Q.shape[0]))
    available_act = available_action(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)
    
# normalizing the Q matrix
print("trained Q matrix:")
print(Q/np.max(Q)*100)

# testing
# goal state = 


current_state = np.random.choice([0,1,2,3,4,5,6,7,8,9,10])
steps = [current_state]

while current_state != 5:
    
    next_step_index = np.where(Q[current_state, ] == np.max(Q[current_state, ]))[1]
    
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_shape_index, size = 1))
    
    else:
        next_step_index = int(next_step_index)
    
    steps.append(next_step_index)
    current_state = next_step_index
    
print("you have to follow the following path: ")
print(steps)