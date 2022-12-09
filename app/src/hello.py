import asyncio

async def coro(n):
  await asyncio.sleep(n)
  return n

async def main():
  # task1=asyncio.create_task(coro(1))
  # task2=asyncio.create_task(coro(2))
  # task3=asyncio.create_task(coro(3))
  # print(await task1)
  # print(await task2)
  # print(await task3)
  print(await coro(1))
  print(await coro(2))
  print(await coro(3))

asyncio.run(main())

