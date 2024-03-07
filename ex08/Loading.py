import time
import sys
__doc__ = "    Decorate an iterable object, returning an iterator \
    which acts exactly like the original iterable, but prints a \
    dynamically updating progressbar every time a value is requested."


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    length = 50
    for i, item in enumerate(lst):
        percent = (i + 1) / total
        progress_length = int(length * percent)
        bar = '█' * progress_length + ' ' * (length - progress_length)
        sys.stdout.write(f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}')
        time.sleep(0.009)
    sys.stdout.write('\n')
    return lst #return is needed because of the functiun being called in
# a for and so needing someting to iterate and apply the sleep
