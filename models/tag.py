from db import db


class TagModel(db.Model):
    __tablename__ = "tags"  # use table named tags for this class

    id = db.Column(db.Integer, primary_key=True)  # id is int and is primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # name is string and max length is 80
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)  # store_id is int and is foreign key

    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", secondary="items_tags", back_populates="tags")