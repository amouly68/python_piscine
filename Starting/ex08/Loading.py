import time
import sys

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    last_update_time = start_time
    update_interval = 0.05  # Interval de mise à jour de la barre de progression en secondes

    for i, item in enumerate(lst):
        if time.time() - last_update_time > update_interval or i == total - 1:
            progress = i / total
            bar_length = 30
            blocks = int(round(progress * bar_length))
            progress_bar = "█" * blocks + " " * (bar_length - blocks)
            elapsed_time = time.time() - start_time
            eta = (total - i) * (elapsed_time / (i + 1))
            print(f"\r{int(progress * 100)}%|{progress_bar}| {i}/{total} [{elapsed_time:.2f}s/{eta:.2f}s]", end="", flush=True)
            last_update_time = time.time()
        yield item

    print()