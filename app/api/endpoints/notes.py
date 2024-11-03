from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from ..models.models import engine, Session, UpdateHistory, Notes, Types
import time


notes_bp = Blueprint('notes_bp', __name__)
Session = sessionmaker(bind=engine)


@notes_bp.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()

    if not data or 'content' not in data or 'title' not in data or 'type_name' not in data:
        return jsonify({"error": "Title, content, and type_name are required!"}), 400

    session = Session()
    try:
        type = session.query(Types).filter_by(type_name=data['type_name']).first()
        if not type:
            return jsonify({"error": "Such type name does not exist!"}), 400
        note = Notes(
            title=data['title'],
            content=data['content'],
            update_date=int(time.time()),
            type_id=type.type_id
        )

        session.add(note)
        session.commit()

        return jsonify({
            'id': note.note_id,
            'title': note.title,
            'content': note.content,
            'update_date': note.update_date,
            'type_id': note.type_id
        }), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@notes_bp.route('/notes', methods=['GET'])
def get_notes():
    session = Session()
    try:
        notes = session.query(Notes).all()
        notes_list = [
            {
                'id': note.note_id,
                'title': note.title,
                'content': note.content,
                'update_date': note.update_date,  # Unix timestamp
                'type_id': note.type_id
            } for note in notes
        ]

        return jsonify(notes_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()  # Close the session

@notes_bp.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    session = Session()
    try:
        note = session.query(Notes).get(note_id)

        if note is None:
            return jsonify({"error": "Note not found"}), 404

        return jsonify({
            'id': note.note_id,
            'title': note.title,
            'content': note.content,
            'update_date': note.update_date,
            'type_id': note.type_id
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@notes_bp.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    session = Session()
    try:
        note = session.query(Notes).get(note_id)

        if note is None:
            return jsonify({"error": "Note not found"}), 404
        #Updateing history table
        update_history = UpdateHistory(
            note_id = note.note_id,
            title = note.title,
            content = note.content,
            update_date = note.update_date,
            type_id = note.type_id
        )
        session.add(update_history)
        #Updateing notes table
        if 'title' in data:
            note.title = data['title']
        if 'content' in data:
            note.content = data['content']
        if 'type_name' in data:
            type = session.query(Types).filter_by(type_name=data['type_name']).first()
            if not type:
                return jsonify({"error": "Such type name does not exist!"}), 400
            note.type_id = type.type_id
        note.update_date = int(time.time())

        session.commit()

        return jsonify({
            'id': note.type_id,
            'title': note.title,
            'content': note.content,
            'update_date': note.update_date,
            'type_id': note.type_id
        }), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@notes_bp.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    session = Session()
    try:
        note = session.query(Notes).get(note_id)

        if note is None:
            return jsonify({"error": "Note not found"}), 404

        #Delete all related history
        session.query(UpdateHistory).filter_by(note_id=note_id).delete()
        #Delete note
        session.delete(note)
        session.commit()

        return jsonify({"message": "Note deleted successfully"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()