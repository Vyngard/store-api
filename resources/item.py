from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    # get an item
    @jwt_required()  # we cannot create an item unless we are logged in
    @blp.response(200, ItemSchema)  # it will pass our return value (items[item_id]) through ItemSchema and includes id in the response
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # delete an item
    @jwt_required()  # we cannot create an item unless we are logged in
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}

    # update an item
    @blp.arguments(ItemUpdateSchema)  # # it will get data from client and validate it
    @blp.response(200, ItemSchema)  # it will pass our return value (items[item_id]) through ItemSchema and includes id in the response
    def put(self, item_data, item_id):  # item_data is JSON which is validated by marshmallow
        item = ItemModel.query.get(item_id)

        # if item exist update it, else create it
        if item:
            item.name = item_data["name"]
            item.price = item_data["price"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.commit()
        return item


@blp.route("/item")
class ItemList(MethodView):
    # get all items
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))  # since we have many ItemSchema, we have to use many=True
    def get(self):
        return ItemModel.query.all()  # because of the schema, it will return a list of items

    # create an item
    @jwt_required(fresh=True)  # we cannot create an item unless we are logged in - and fresh token must be used for that
    @blp.arguments(ItemSchema)  # it will get data from client and validate it
    @blp.response(201, ItemSchema)  # it will pass our return value (item) through ItemSchema and includes id in the response
    def post(self, item_data):  # item_data is JSON which is validated by marshmallow
        item = ItemModel(**item_data)  # create an item object

        # saving item to db
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item
