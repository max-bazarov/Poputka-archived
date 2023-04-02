from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()


ride = Table(
    'ride',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('driver', Integer, nullable=False),
    Column('car', Integer, nullable=False),
    Column('places', Integer, nullable=False),
    Column('destination', String, nullable=False),
    Column('departure_point', String, nullable=False),
    Column('time', TIMESTAMP, nullable=False),
)


car = Table(
    'car',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('make', String, nullable=False),
    Column('model', String, nullable=False),
    Column('year', Integer),
    Column('license_plate_number', String, nullable=False),
)
