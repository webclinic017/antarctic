# -*- coding: utf-8 -*-
"""global fixtures"""
from __future__ import annotations

from pathlib import Path

import pytest
from mongoengine import connect
from mongoengine import disconnect

# import mongomock


@pytest.fixture(scope="session", name="resource_dir")
def resource_fixture():
    """resource fixture"""
    return Path(__file__).parent / "resources"


@pytest.fixture(scope="session", name="client")
def client_fixture():
    """database fixture"""
    yield connect(db="test_pandas")  # , mongo_client_class=mongomock.MongoClient)

    disconnect()
