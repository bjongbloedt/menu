import pytest
import os
import uuid
from project.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
