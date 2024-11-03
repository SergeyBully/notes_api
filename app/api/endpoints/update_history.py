from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from ..models.models import engine, Session, UpdateHistory, Notes, Types


update_history_bp = Blueprint('update_history_bp', __name__)
Session = sessionmaker(bind=engine)


@update_history_bp.route('/update_history/<int:note_id>', methods=['GET'])
def get_update_history(note_id):
    session = Session()
    try:
        update_history = session.query(UpdateHistory).filter_by(note_id=note_id).all()
        if not update_history:
            return jsonify({"error": "Update history not found"}), 404
        update_history_list = [
            {
                'update_id': history.update_id,
                'note_id': history.note_id,
                'title': history.title,
                'content': history.content,
                'update_date': history.update_date,
                'type_id': history.type_id
            } for history in update_history
        ]

        return jsonify(update_history_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()