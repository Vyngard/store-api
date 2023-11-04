# using SQLAlchemy to create a class for each table.
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"  # use table named items for this class

    id = db.Column(db.Integer, primary_key=True)  # id is int and is primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # name is string and max length is 80
    price = db.Column(db.Float(precision=2), unique=True, nullable=False)  # price is float and precision is 2
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=True, nullable=False)  # store_id is int and is foreign key

    # gives us associated objects that are related to the foreign key for each item
    # also it populates the store model, so we can see items in the store model too
    store = db.relationship("StoreModel", back_populates="items")
    tags = db.relationship("TagModel", secondary="items_tags", back_populates="items")
