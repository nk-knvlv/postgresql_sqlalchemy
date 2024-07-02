from sqlalchemy import text, insert
from database import sync_engine, async_engine, session_factory, async_session_factory
from models import metadata_obj, WorkersOrm


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')


async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

#
# def insert_data():
#     worker_bobr = WorkersOrm(username='Bobr')
#     worker_volk = WorkersOrm(username='Woltswagen')
#     with session_factory() as session:
#         session.add_all([worker_bobr, worker_volk])
#         session.commit()



async def insert_data():
    async with async_session_factory() as session:
        worker_bobr = WorkersOrm(username='Bobr')
        worker_volk = WorkersOrm(username='Goblin')
        session.add_all([worker_bobr, worker_volk])
        await session.commit()
