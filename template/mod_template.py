#!/usr/bin/env python3

"""

    Feel free while using this template. You can modify it or do
    whatever you want.

"""

############### HUNTER - TOOLKIT MODULE TEMPLATE ####################

try:
    # YOUR MODULES HERE
    # YOUR MODULES HERE
    # YOUR MODULES HERE
except ImportError:
    # Don't forget to put or update your requirements in the
    # requirements.txt file. You will find this file in the req
    # directory.
    raise RuntimeError(""" 
    Oops,
    
    this tool uses important modules, which don't seem to be 
    installed at the moment.
    
    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 
    
    You will find this file in the req directory.
    
    """)

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   YOURNAMEHERE              #
#   Contact :   YOUREMAILADDRESSHERE      #
#   Github  :   @YOURGITHUBUSERNAMEHERE   #
#   Version :   0.0.0                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #


class HunterModule:

    def __init__(
            self,
            # YOUR VARIABLES
            any_param1: str,
            any_param2: str,
            any_param3: int
    ):
        self.any_param3 = any_param3
        self.any_param2 = any_param2
        self.any_param1 = any_param1


    def your_function_name(self):
        while True:
            # STRING:
            # ---------
            if self.any_param1 == 'x' or self.any_param1 == 'exit':
                break
                
               
            # INTEGER:
            # ---------
            if self.any_param1 == 0:
                break

            # YOUR CODE HERE
            # YOUR CODE HERE
            # YOUR CODE HERE
            # break
            # YOUR CODE HERE
            # YOUR CODE HERE
            # YOUR CODE HERE

            input("Press any key to continue")

            break

# if __name__ == "__main__":











