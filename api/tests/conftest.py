import pytest
from apistar.test import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.project.models import Base
from api.app import app


@pytest.fixture(scope="function")
def db_session():
    """
    pytest fixtures that creates a unit.db, creats the tables for the
    project, and returns a session.

    After test completed, session is closed, all tables are dropped, and
    the engine is disposed of.
    """
    test_engine = create_engine('sqlite://')
    Base.metadata.create_all(test_engine)
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=test_engine)
    test_engine.dispose()


@pytest.fixture(scope="function")
def client_empty_db():
    app.main(['create_tables'])
    yield TestClient(app)
    app.main(['drop_tables'])
