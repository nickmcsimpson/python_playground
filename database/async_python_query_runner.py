"""This actually won't work as written due to the synchronous nature of file manipulation"""
import sys
from pprint import pprint
from codetiming import Timer
import psycopg2.extras

import asyncio


async def worker(worker_name, queue, **kwargs):
    timer = Timer(text=f"Task {worker_name} elapsed time: {{:.3f}}")
    # conn = psycopg2.connect(dbname='dev',
    #                         host=f"{kwargs.get('domain')}.redshift.amazonaws.com",
    #                         port=5439,
    #                         user=kwargs.get('username'),
    #                         password=kwargs.get('password')
    #                         )
    # with conn:
    #     with conn.cursor() as curs:
    #         while not queue.empty():
    #             query = await queue.get()
    #             try:
    #                 timer.start()
    #                 curs.execute(query)
    #                 timer.stop()
    #             except Exception as exception:
    #                 print(exception)
    #                 pprint(f"{worker_name} failed to run query:\n{query}")
    # conn.close()
    while not queue.empty():
        delay = await queue.get()
        print(f"Task {worker_name} running")
        timer.start()
        await asyncio.sleep(delay)
        timer.stop()


async def get_sql_script(file_name):
    async with open(file_name) as file:
        return await file.read()


def main(file_name, schema='', **kwargs):
    queue = asyncio.Queue()

    with open(file_name) as file:
        sql_script = file.read()

    for query in sql_script.split(';'):
        queue.put(query.replace('<schema>', schema))

    # THIS seems to limit to a single worker
    # conn = psycopg2.connect(dbname='dev',
    #                         host=f"{kwargs.get('domain')}.redshift.amazonaws.com",
    #                         port=5439,
    #                         user=kwargs.get('username'),
    #                         password=kwargs.get('password')
    #                         )
    # with conn:
    #     with conn.cursor() as curs:
    #         with Timer(text="\nTotal elapsed time: {:.3f}"):
    #             await asyncio.gather(
    #                 asyncio.create_task(worker('Nick', queue, cursor=curs)),
    #                 asyncio.create_task(worker('Devereux', queue, cursor=curs)),
    #             )
    # conn.close()

    # either way results in the same thing...?
    with Timer(text="\nTotal elapsed time: {:.3f}"):
        await asyncio.gather(
            asyncio.create_task(worker('Nick', queue, **kwargs)),
            asyncio.create_task(worker('Devereux', queue, **kwargs)),
        )

    # Use static data as test:

    # Put some work in the queue
    # for work in [15, 10, 5, 2]:
    #     await queue.put(work)
    #
    # # Run the tasks
    # with Timer(text="\nTotal elapsed time: {:.1f}"):
    #     await asyncio.gather(
    #         asyncio.create_task(worker("One", queue)),
    #         asyncio.create_task(worker("Two", queue)),
    #     )


if __name__ == '__main__':
    asyncio.run(main(sys.argv[1], schema=sys.argv[2], username=sys.argv[3],
                     password=sys.argv[4], domain=sys.argv[5]))
