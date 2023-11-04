# using SQLAlchemy to create a class for each table.
from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"  # use table named stores for this class

    id = db.Column(db.Integer, primary_key=True)  # id is int and is primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # name is string and max length is 80

    # allows store models to see the items that belong to them using store.items. lazy means items are not going to be fetched until we tell them too.
    # cascade means if we delete a store, all the items that belong to that store will be deleted too.
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
