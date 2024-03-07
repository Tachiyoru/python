__doc__ = """This script implements a simplified version of
    the tqdm progress bar for iteration over a range.

Functions:
- ft_tqdm(lst: range) -> None:
    Displays a progress bar indicating the progress of iteration over
        the given range.
    Prints the progress bar to the console.
    Returns None.

Parameters:
- lst: A range object representing the range over which the
    iteration is performed.

Example Usage:
- Call the ft_tqdm function with a range object as an argument.
- The progress bar will be displayed showing the progress
    of the iteration.

Note:
- This function is a simplified version of the tqdm library's
    progress bar and is intended for basic usage.
- It may not provide all the features or customization
    options available in tqdm.
"""
import time
import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    length = 60
    for i, item in enumerate(lst):
        percent = (i + 1) / total
        progress_length = int(length * percent)
        bar = '█' * progress_length + ' ' * (length - progress_length)
        sys.stdout.write(f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}')
        time.sleep(0.009)
    sys.stdout.write('\n')
    return lst

# return is needed because of the functiun being called in
# a for and so needing someting to iterate and apply the sleep
