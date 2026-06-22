from app.database.database import engine
from app.models.bug_model_sql import Base


def init_db():
    print("Running DB initialization...")
    Base.metadata.create_all(bind=engine)
    print("Database created successfully")


    print("Engine URL:", engine.url)
    print("Database path:", engine.url.database)


if __name__ == "__main__":
    init_db()