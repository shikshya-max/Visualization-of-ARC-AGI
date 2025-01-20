import os
import numpy as np
import json


def walk_files(directory):
    """

    :param directory: path where data dir is "./data"

    :return: an array of all the files in the data/training directory as dictionaries
        Example: [{'train': [{'input': [[0, 0, 5], [0, 5, 0], [5, 0, 0]], 'output': [[3, 3, 3], [4, 4, 4], [2, 2, 2]]},
        {'input': [[0, 0, 5], [0, 0, 5], [0, 0, 5]], 'output': [[3, 3, 3], [3, 3, 3], [3, 3, 3]]},
        'test': [{'input': [[0, 0, 5], [5, 0, 0], [0, 5, 0]], 'output': [[3, 3, 3], [2, 2, 2], [4, 4, 4]]}],
        ...,
        [...]}
    """
    json_data = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if file_path.endswith('.json'):
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    json_data.append(data)
    return json_data


def get_example_train_elements(json_example):
    """
    Convert the values in the dictionary to np arrays
    :param json_example:
    :return:
    """
    train = json_example["train"]

    pairs = []
    for pair in train:
        input = pair["input"]
        output = pair["output"]

        example = {}
        # making it a numpy array
        example["input"] = np.array(input)
        # None # TODO replace None with converted input to numpy array
        example["output"] = np.array(output)
        # None # TODO replace None with converted output to numpy array
        pairs.append(example)
    return pairs

def get_example_test_elements(json_example):
    #TODO do what you did for train above here for test
    test = json_example["test"]

    pairs = []
    for pair in test:
        input = pair["input"]
        output = pair["output"]

        example = {}
        # making it a numpy array
        example["input"] = np.array(input)
        # None # TODO replace None with converted input to numpy array
        example["output"] = np.array(output)
        # None # TODO replace None with converted output to numpy array
        pairs.append(example)
    return pairs





