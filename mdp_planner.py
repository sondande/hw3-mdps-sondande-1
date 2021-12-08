import sys

"""
Value Iteration 
"""


def value_iteration(mdp, gamma_value):
    # 1. Initialize Q table and V values to all zeros
    q_table = [] # Stores expected utilities using the bellman equation
    v_table = [] # Stores possible utilities for each action a state can take
    for state in range(len(mdp[0])):
        # the index in the q_table should be equal to the unique identifier of the state
        v_table.append(0)

        # the index in the v_table should be equal to the unique identifier of the action
        action_list = []
        for action in range(len(mdp[1])): # for the number of possible actions for every state
            action_list.append(0)
        q_table.append(action_list)

    #### Personal notes of things to think about #####
    # (Aka step 4. Repeat Steps 2-3 until V values converge * Largest change in V(s) is less than e)
    # While loop (until the largest change in V < e aka the covergence criteria is met)
    # TODO add after testing 2-3 and ensuring it is correct

    # Grab dictionaries
    states = mdp[0]
    actions = mdp[1]
    state_transitions = mdp[2]
    rewards = mdp[3]

    # Step 2: Update entire Q table using Bellman equation
    for s in range(len(states)): # returns the state uniqueID key
        for a in range(len(actions)): # returns the action uniqueID key
            # Calculate Q(s, a) with Bellman
            # See if the reward from our state to the next state is in our MDP. If not, use the value 0 where we need it

            # Grab probability if it exists from state transitions
            probability = state_transitions[str(s)]
            for transitions in probability:
                if str(a) in transitions.keys(): # see if the current state and action combination is in the dictionary
                    next_state = transitions[str(a)]
                    probability_value = int(next_state.values())
                    # Just in case to break for loop
                    break

            # Grab reward if it exists from rewards


            # for every state transition for current state and next state in S,
            q_function = probability_value * ()

            # TODO first! Find out how to access calues we put in dictionary to be able to calculate Q values
            # print(mdp[s][a])
            # TODO if we run into an error that a possible transition doesn't have a reward or a reward doens't have a transition, the value is zero. Was specified in the homework assignment listing as
            # The ones not listed in the MDP have values of 0 for probability or reward value. Dependant on which one is missing


    return


"""
Main function to call program

Values are stored in the stateTransition and Rewards dictionary in the format of the key being the currentState, and every element in the list are possible state transitions given or rewards for that current state

StateTransition: State(key), [Action, Next_State, Probability] (list of state transition options for State)
Reward: State(key), [Action, Next_State, Reward] (list of reward options for State)
"""


def main():
    # Create Dictionaries
    states = {}
    actions = {}
    stateTransitions = {}
    rewards = {}

    # Creation of Markov Decision Process
    mdp = [states, actions, stateTransitions, rewards]

    # Read file in from arguments
    filename = sys.argv[1]

    # Read in gamma value from arguments
    gamma_value = sys.argv[2]

    # Read in policyFileName from arguments
    # policyFileName = sys.argv[3]

    # Open File
    f = open(filename)

    # Iterating through the file, placing data into the dictionaries
    line = next(f)
    line = next(f)

    # Going through states, splitting into id and label, removing \n and putting in dictionary
    while line != '\n':
        data = line.split(",")
        label = data[1]
        label = label[:-1]
        states[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # going through actions, splitting into id and label, removing \n and putting in dictionary
    while line != '\n':
        data = line.split(",")
        label = data[1]
        label = label[:-1]
        actions[data[0]] = label
        line = next(f)
    line = next(f)
    line = next(f)

    # going through state transitions, splitting into 4 parts and nesting them into layers in the dictionary

    while line != '\n':
        data = line.split(",") #Removes commas
        label = data[3] # Grabs the last value in the state transitions
        label = label[:-1] # Eliminates the \n from the integer
        last = {}
        last[data[2]] = label # Assigns the last value in State Transition as the value for the key of the value before it
        slast = {}
        slast[data[1]] = last # Assigns the second value as the key to the dictionary last that stores the 3 and 4 values in State Transitions
        if(data[0] in stateTransitions): # We see if the leading current state in the state transition is in our dictionary. If so, add new reward to list
            newList = stateTransitions[data[0]]
            newList.append(slast)
            stateTransitions[data[0]] = newList
        else: # if not, append it to our stateTransition dictionary
            newList = []
            newList.append(slast)
            stateTransitions[data[0]] = newList
        line = next(f)
    line = next(f)
    line = next(f)

    # going through rewards, splitting into 4 parts and nesting them into layers in the dictionary
    for line in f:
        data = line.split(",")
        label = data[3]
        label = label[:-1]
        last = {}
        last[data[2]] = label
        slast = {}
        slast[data[1]] = last
        if(data[0] in rewards):
            newList = rewards[data[0]]
            newList.append(slast)
            rewards[data[0]] = newList
        else:
            newList = []
            newList.append(slast)
            rewards[data[0]] = newList
    

    #print(rewards['4'])
    value_iteration(mdp, gamma_value)


main()
