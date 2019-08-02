import asyncio
from argparse import ArgumentParser
from typing import List

from tqdm import tqdm


async def async_do(n: int) -> List[bool]:
    async def do() -> bool:
        await asyncio.sleep(10)
        return True

    tasks = [do() for i in range(n)]
    return [await f for f in tqdm(asyncio.as_completed(tasks), total=len(tasks))]

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-n', default=100, required=False, help='compute count')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_do(args.n))
