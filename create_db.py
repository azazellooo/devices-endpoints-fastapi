from app.db import Base, engine

print('Creating database...')

Base.metadata.create_all(engine)
