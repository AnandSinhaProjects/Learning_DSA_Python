test_list = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 2, 1], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
   'query': 6},
  'output': 2}]


def evaluate_test_case(fun_name, test_list):
    import time

    counter = 0
    for test_case in test_list:
        
        print("TEST CASE #", counter, sep='')
        
        Input = test_case["input"]
        Output = test_case["output"]
        
        start = time.time()
        
        fun_output = fun_name(*Input.values())
        
        end = time.time()
        
        exec_time = end - start
        
        if type(Output) == list:
            
            result = "PASSED" if (fun_output in Output) == True else "FAILED"
            
        else:
            result = "PASSED" if (fun_output == Output) == True else "FAILED"
            
        print("\nInput:\n", Input, sep='')
        print("\nExpected Output:\n", Output, sep='')
        print("\nActual Output:\n", fun_output, sep='')
        print("\nExecution Time:\n", exec_time, sep='')
        print("\nTest Result:\n", result, "\n\n", sep='')
        
        counter += 1