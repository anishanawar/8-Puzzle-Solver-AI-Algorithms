test_cases = [
    {
        "depth": 0,
        "initial_state": [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']],
        "expected_depth": 0,
    },
    {
        "depth": 2,
        "initial_state": [['1', '2', '3'], ['4', '5', '6'], ['0', '7', '8']],
        "expected_depth": 2,
    },
    {
        "depth": 4,
        "initial_state": [['1', '2', '3'], ['5', '0', '6'], ['4', '7', '8']],
        "expected_depth": 4,
    },
    {
        "depth": 8,
        "initial_state": [['1', '3', '6'], ['5', '0', '7'], ['4', '8', '2']],
        "expected_depth": 8,
    },
    {
        "depth": 12,
        "initial_state": [['1', '3', '6'], ['5', '0', '7'], ['4', '8', '2']],
        "expected_depth": 12,
    },
    {
        "depth": 16,
        "initial_state": [['1', '6', '7'], ['5', '0', '3'], ['4', '8', '2']],
        "expected_depth": 16,
    },
    {
        "depth": 20,
        "initial_state": [['7', '1', '2'], ['4', '8', '5'], ['6', '3', '0']],
        "expected_depth": 20,
    },
    {
        "depth": 34,
        "initial_state": [['0', '7', '2'], ['4', '6', '1'], ['3', '5', '8']],
        "expected_depth": 34,
    },
]