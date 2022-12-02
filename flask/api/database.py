from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

from .config import APP_CONFIG


db = SQLAlchemy()


def init_database(app: Flask) -> None:
    db.init_app(app)


class DBMixin():
    __table_args__ = {'schema': APP_CONFIG.DB_SCHEMA, }

    id: uuid.UUID = db.Column(UUID(as_uuid=True),
                              primary_key=True,
                              default=uuid.uuid4)
    created: datetime = db.Column(db.DateTime(timezone=True),
                                  default=datetime.now)
    updated: datetime = db.Column(db.DateTime(timezone=True),
                                  default=datetime.now,
                                  onupdate=datetime.now)

    def save(self) -> None:
        db.session.commit()

    @classmethod
    def all(cls) -> list[Any]:
        return cls.query.all()

    @classmethod
    def get_by_id(cls, item_id: uuid.UUID) -> Any:
        return cls.query.filter(cls.id == item_id).first()


class DBActiveStatusMixin():

    is_active = db.Column(db.Boolean, default=True, )

    def activate(self) -> None:
        self.is_active = True
        self.save()

    def deactivate(self) -> None:
        self.is_active = False
        self.save()


class DBTools():

    @staticmethod
    def create(obj: Any) -> None:
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def create_with_callback(obj: Any) -> Any:
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        db.session.refresh(obj)
        return obj

    @staticmethod
    def delete(obj: Any) -> None:
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def init_db():
        db.create_all()
        db.session.commit()
