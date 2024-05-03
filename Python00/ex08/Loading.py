import time
import sys
from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    """Displays a progress bar indicating the progress of iteration over
        the given range."""
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


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()


# return is needed because of the functiun being called in
# a for and so needing someting to iterate and apply the sleep
