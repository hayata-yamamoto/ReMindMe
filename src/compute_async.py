import asyncio
from argparse import ArgumentParser
import time
from typing import List, Dict

from tqdm import tqdm


async def async_do(n: int) -> List[bool]:
    async def do() -> bool:
        await asyncio.sleep(1)
        return True

    tasks = [do() for i in range(n)]
    return [await f for f in tqdm(asyncio.as_completed(tasks), total=len(tasks))]


def execute(n: int) -> Dict[str, float]: 
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(async_do(n))
    end = time.time()
    return {"time": end - start, "n": n}


if __name__ == '__main__':
    import matplotlib.pyplot as plt 
    import pandas as pd
    import seaborn as sns 

    n_arr = [10 ** i for i in range(1, 8)] 
    records = []
    df = pd.DataFrame.from_records([execute(n) for n in n_arr])

    # Visualization
    sns.lineplot(data=df, x="n", y="time")
    plt.title("how long does it spend to execute?")
    plt.ylabel("time (sec)")
    plt.xscale("log")
    plt.savefig("compute_time.png")

