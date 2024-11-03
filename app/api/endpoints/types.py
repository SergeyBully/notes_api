from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from ..models.models import engine, Session, Types


types_bp = Blueprint('types_bp', __name__)
Session = sessionmaker(bind=engine)


@types_bp.route('/types', methods=['POST'])
def create_type():
    data = request.get_json()

    if not data:
        return jsonify({"error": "type_name is required!"}), 400

    session = Session()
    try:
        types = session.query(Types.type_name).all()
        if data['type_name'] in [t[0] for t in types]:
            return jsonify({"error": "This type name already exists!"}), 400
        type = Types(
            type_name=data['type_name']
        )

        session.add(type)
        session.commit()

        return jsonify({
            'id': type.type_id,
            'title': type.type_name,
        }), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@types_bp.route('/types', methods=['GET'])
def get_types():
    session = Session()
    try:
        types = session.query(Types).all()
        types_list = [
            {
                'id': type.type_id,
                'type_name': type.type_name,
            } for type in types
        ]

        return jsonify(types_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@types_bp.route('/types/<int:type_id>', methods=['PUT'])
def update_type(type_id):
    data = request.get_json()
    session = Session()
    try:
        type = session.query(Types).get(type_id)

        if type is None:
            return jsonify({"error": "Type not found"}), 404
        if not data['type_name']:
            return jsonify({"error": "type_name is required!"}), 404
        types = session.query(Types.type_name).all()
        if data['type_name'] in [t[0] for t in types]:
            return jsonify({"error": "This type name already exists!"}), 400
        type.type_name = data['type_name']

        session.commit()

        return jsonify({
            'id': type.type_id,
            'type_name': type.type_name,
        }), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@types_bp.route('/types/<int:type_id>', methods=['DELETE'])
def delete_type(type_id):
    session = Session()
    try:
        type = session.query(Types).get(type_id)

        if type is None:
            return jsonify({"error": "Type not found"}), 404

        session.delete(type)
        session.commit()

        return jsonify({"message": "Type deleted successfully"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()