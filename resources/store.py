from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import StoreModel
from schemas import StoreSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("stores", __name__, description="Operations on stores")


# using MethodView to create a class for each endpoint. for different endpoints we have to use another class with MethodView.
# using blueprint to register each endpoint
@blp.route("/store/<int:store_id>")
class Store(MethodView):

    # get a store
    @blp.response(200, StoreSchema)  # it will pass our return value (stores[store_id]) through StoreSchema and includes id in the response
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    # delete a store
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}


@blp.route("/store")
class StoreList(MethodView):
    # get all stores
    @blp.response(200, StoreSchema(many=True))  # since we return many values through StoreSchema, we have to use many=True
    def get(self):
        return StoreModel.query.all()

    # create a store
    @blp.arguments(StoreSchema)  # it will get data from client and validate it
    @blp.response(200, StoreSchema)  # it will pass our return value (store) through StoreSchema and includes id in the response
    def post(self, store_data):  # store_data is JSON which is validated by marshmallow
        store = StoreModel(**store_data)  # create a store object

        # saving store to db
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with the same name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        return store
