import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball in range(1, 6):
        print(f'Силач {name} поднял {ball} шар')
        await asyncio.sleep(1/power)
    print(f'Силач {name}  закончил соревнования.')


async def start_tournament():
    task = asyncio.create_task(start_strongman('Pasha', 15))
    task2 = asyncio.create_task(start_strongman('Yasha', 14))
    task3 = asyncio.create_task(start_strongman('Sasha', 13))
    await task
    await task2
    await task3


asyncio.run(start_tournament())
