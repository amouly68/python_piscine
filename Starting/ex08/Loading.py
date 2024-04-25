import time


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    last_update_time = start_time
    update_interval = 0.05

    for i, item in enumerate(lst):
        if time.time() - last_update_time > update_interval or i == total - 1:
            progress = i / total
            bar_length = 60
            blocks = int(round(progress * bar_length))
            progress_bar = "█" * blocks + " " * (bar_length - blocks)
            elapsed_time = time.time() - start_time
            eta = (total - i) * (elapsed_time / (i + 1))

            elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed_time))
            eta_str = time.strftime("%M:%S", time.gmtime(eta))

            iterations_per_second = (i + 1) / elapsed_time

            if i % 20 == 0:
                print(f"\r{int(progress * 100)}%|", end="")
                print(f"{progress_bar}|{i}/{total}", end="")
                print(f"[{elapsed_str}<{eta_str}]", end="")
                print(f"{iterations_per_second:.2f}it/s)", end="", flush=True)
            last_update_time = time.time()
        yield item

    i = i + 1
    progress = i / total
    print(f"\r{int(progress * 100)}%|", end="")
    print(f"{progress_bar}|{i}/{total}", end="")
    print(f"[{elapsed_str}<{eta_str}]", end="")
    print(f"{iterations_per_second:.2f}it/s)", end="", flush=True)
