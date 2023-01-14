import random
import math

class strategy0:  #take input from user
    def __init__(self,n_options):
        self.n_options = n_options
        self.max_so_far = float("-inf")
        self.n_options_seen_far = 0

    def decision(self, current_option):
        self.n_options_seen_far += 1
        self.max_so_far = max(self.max_so_far, current_option)
        i = input(f"current option is {self.n_options_seen_far}. max {self.max_so_far} current_option {current_option}: ")
        if i == "1":
            return 1
        return 

class strategy1(strategy0): 
    def __init__(self,n_options):
        self.n_options = n_options
        self.max_so_far = float("-inf")
        self.n_options_seen_far = 0
        self.stop_exploring_after = math.ceil(self.n_options / math.e)

    def decision(self,current_option):
        self.n_options_seen_far += 1

        #exploration or data collection phase
        if self.n_options_seen_far <= self.stop_exploring_after:
            self.max_so_far = max(self.max_so_far, current_option)
            return 0

        #start deciding
        return current_option > self.max_so_far 


class strategy2(strategy1): 
    def __init__(self,n_options):
        self.n_options = n_options
        self.max_so_far = float("-inf")
        self.n_options_seen_far = 0
        self.stop_exploring_after = math.ceil(self.n_options * 0.1)


def evaluate_strategy(strategy, n_numbers=100, n_iterations=1000, min_num=0, max_num=1e9, verbose=0):
    
    scores = []
    
    for iter_ind in range(n_iterations):
        #initialize environment
        s_numbers = set()
        while len(s_numbers) < n_numbers:
        #both min num and max num are included in the list of possibilities including all nums in between
            s_numbers.add(random.randint(min_num, max_num)) 
        
        l_numbers = list(s_numbers)
        random.shuffle(l_numbers)
        
        opt_value = max(l_numbers)
        
        #initialize bot
        bot1 = strategy(n_numbers)
        bots_choice = -1
    
        #evaluate bot
        for ind, val in enumerate(l_numbers):
            if bot1.decision(val) == 1:
                bots_choice = val
                break
    
        scores.append(opt_value == bots_choice)
        if verbose:
            print(bots_choice, opt_value)
    print(strategy, sum(scores)/len(scores))
        
evaluate_strategy(strategy1)
evaluate_strategy(strategy2)
evaluate_strategy(strategy0, 10, 1, 0, random.randint(1000,14000), 1)
