import time
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# formating
matplotlib.rc('xtick', labelsize=5)
matplotlib.rc('ytick', labelsize=5)

def visualize_explore(examples, title=""):
    """
    :param examples: list of all pairs of arc examples. That is a list of dictionaries
        where each element is a dictionary with keys 'input' and 'output' and double array values representing
        an input and output pair int eh arc dataset
        [{'input'[[], ..., []], 'output:[[], ...[]]}, ..., {'input'[[], ..., []], 'output:[[], ...[]]}]
    :param title:
    :return: nothing is returned

    This method should save 400 plots in a plots directory. The plots should look
    like the example plot in the README file
    """
    fig, ax = plt.subplots(len(examples), 2)
    fig.set_size_inches(15, 5 * len(examples))
    plt.subplots_adjust(hspace=1)

    #  Handle the case when there's only one example
    if len(examples) == 1:
        # Convert ax to a 2D array with shape (1, 2)
        ax = np.expand_dims(ax, axis=0)

    index = 0
    for index, example in enumerate(examples):
        input = example["input"]
        output = example["output"]

        # Plot input
        im_input = ax[index, 0].matshow(input, cmap='tab10')
        ax[index, 0].set_title('Input', pad = '20')
        

    # Annotate cells
        for i in range(input.shape[0]):
            for j in range(input.shape[1]):
                ax[index, 0].text(j, i, str(input[i, j]),
                                ha='center', va='center',
                                color='white')

        # Plot output
        im_output = ax[index, 1].matshow(output, cmap='tab10')
        ax[index, 1].set_title('Output', pad = '20')

        # Annotate cells
        for i in range(output.shape[0]):
            for j in range(output.shape[1]):
                ax[index, 1].text(j, i, str(output[i, j]),
                                ha='center', va='center',
                                color='white')
        index += 1

    
    fig.suptitle(title)
    # TODO save plot to ./plots/<title> , where <title> is title passed to method
    plt.savefig(f'./plots/{title}.png', bbox_inches='tight', dpi=300)
    plt.close()


