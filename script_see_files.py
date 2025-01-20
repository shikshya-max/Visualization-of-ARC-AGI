from data_loader import *
from explore_data import *

# Replace 'your_directory_path' with the path of the directory you want to walk
training_json = walk_files('./data/training')
evaluation_json = walk_files('./data/evaluation')
count = 0

# get the data in a usable format
for example in training_json:
    print(f"example_{count}")
    print("JSON Structure:")
    print(json.dumps(example))
    examples = get_example_train_elements(example)
    visualize_explore(examples, f"example_train_{count}")
    time.sleep(2)
    count += 1

# Visualizing a single example
# if training_json:
#     # Get the first JSON example
#     example = training_json[0]
    
#     # Print the JSON structure to inspect it
#     print("JSON Structure:")
#     print(json.dumps(example, indent=4)) 
    
#     # Extract and process train elements
#     examples = get_example_train_elements(example)
    
#     # Visualize the example (using a title like 'example_train_0')
#     visualize_explore(examples, "example_train_0")
#     print("Visualization created for the first example.")
# else:
#     print("No JSON files found in the specified directory.")
   