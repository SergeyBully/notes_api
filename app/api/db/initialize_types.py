from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from ..models.models import engine, Types

Session = sessionmaker(bind=engine)

def initialize_types():
    session = Session()
    default_types = [
        {'type_name': 'general'},
        {'type_name': 'shopping list'},
        {'type_name': 'poem'}
    ]

    try:
        existing_types_count = session.query(Types).count()

        if existing_types_count == 0:
            session.bulk_insert_mappings(Types, default_types)
            session.commit()
            print("Default types added successfully.")
        else:
            print("Types table already has entries. No action taken.")

    except IntegrityError:
        session.rollback()
        print("Error: Duplicate types detected. Make sure unique constraint is applied.")
    finally:
        session.close()