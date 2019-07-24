import numpy as np

class indoor:
    def __init__(self, Gamma = 0.8):
        self._Q = np.zeros([11,11])
        self._R = None
        self._destination = None
        self._gamma = Gamma
    
    def _load_R_matrix(self, destination):
        self._R = np.loadtxt('/home/ketan/Indoormapping/R_file/R'+str(destination)+'.csv', delimiter = ',')
    def save_R_matrix(self, destination):
        np.savetxt('/home/ketan/Indoormapping/R_file/R'+str(destination)+'.csv',self._R,delimiter = ',')
    def create_R_matrix(self):
        pass
    
    def _load_Q_matrix(self, destination):
        self._Q = np.loadtxt('/home/ketan/Indoormapping/Q_file/Q'+str(destination)+'.csv', delimiter = ',')
    def save_Q_matrix(self, destination):
        np.savetxt('/home/ketan/Indoormapping/Q_file/Q'+str(destination)+'.csv',(self._Q/np.max(self._Q)*100), delimiter = ',')
    
    def _available_actions(self, states):
        current_state_row = self._R[states,:]
        av_act = [i for i,v in enumerate(current_state_row) if v >= 0]
        return av_act
    
    def _sample_next_action(available_action_range):
        next_action = np.random.choice(available_action_range)
        return next_action

    def _update(self, current_state, action, gamma):
        max_index = np.where(self._Q[action, :] == np.max(self._Q[action, :]))[0]
        
        if max_index.shape[0] > 1:
            max_index = int(np.random.choice(max_index, size = 1))
        
        else:
            max_index = int(max_index)
        max_value = self._Q[action, max_index]
        
        self._Q[current_state, action] = self._R[current_state, action] + gamma*max_value
     
    def _train_agent(self):
        for i in range(10000):
            current_state = np.random.randint(0,int(self._Q.shape[0]))
            available_act = self.available_actions(current_state)
            action = self.sample_next_action(available_act)
            self._update(current_state, action, self._gamma)
        # save the q matrix
        if self.destination != None:
            self.save_Q_matrix(self._destination)
    
    
    def predict_path(self, current_state, destination):        
        # load the destination file
        try:
            self._load_Q_matrix(destination)
        except:
            return None
        if self._Q == 0:
            print('unknown environment, the agent need to be trained in the environment.')
            return None
        
        steps = [current_state]
        
        while current_state != destination:
            
            next_step_index = np.where(self._Q[current_state, ] == np.max(self._Q[current_state, ]))[0]
            
            if next_step_index.shape[0] > 1:
                next_step_index = int(np.random.choice(next_step_index, size = 1))
            
            else:
                next_step_index = int(next_step_index)
            
            steps.append(next_step_index)
            current_state = next_step_index
            
        return steps