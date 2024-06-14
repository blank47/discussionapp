from flask import request, jsonify, abort
from app import db
from app.main.models import User, Discussion, Base
from app.main import bp

# ---------------- User APIs ---------------- #
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'email', 'mobile_no']):
        abort(400, description="Missing data for required fields.")
    if User.query.filter_by(email=data['email']).first():
        abort(409, description="Email already registered.")
    user = User(name=data['name'], email=data['email'], mobile_no=data['mobile_no'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.mobile_no = data.get('mobile_no', user.mobile_no)
    db.session.commit()
    return jsonify(user.to_dict()), 200

@bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204

@bp.route('/users/search', methods=['GET'])
def search_users():
    name = request.args.get('name', None)  # Get 'name' from query parameters
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400

    # Query the database for users matching the name
    users = User.query.filter(User.name.ilike(f"%{name}%")).all()
    if not users:
        return jsonify([]), 404  # Return an empty list if no users found

    return jsonify([user.to_dict() for user in users]), 200

# ---------------- Discussion APIs ---------------- #
@bp.route('/discussions', methods=['POST'])
def create_discussion():
    data = request.get_json()
    if not data or not all(key in data for key in ['text', 'user_id']):
        abort(400, description="Missing data for required fields.")
    discussion = Discussion(text=data['text'], user_id=data['user_id'], image=data.get('image'), hashtags=data.get('hashtags'))
    db.session.add(discussion)
    db.session.commit()
    return jsonify(discussion.to_dict()), 201

@bp.route('/discussions/<int:discussion_id>', methods=['GET'])
def get_discussion(discussion_id):
    discussion = Discussion.query.get_or_404(discussion_id)
    return jsonify(discussion.to_dict())

@bp.route('/discussions', methods=['GET'])
def get_discussions():
    tag = request.args.get('tag')
    text = request.args.get('text')
    if tag:
        discussions = Discussion.query.filter(Discussion.hashtags.contains(tag)).all()
    elif text:
        discussions = Discussion.query.filter(Discussion.text.contains(text)).all()
    else:
        discussions = Discussion.query.all()
    return jsonify([discussion.to_dict() for discussion in discussions]), 200

@bp.route('/discussions/<int:discussion_id>', methods=['PUT'])
def update_discussion(discussion_id):
    discussion = Discussion.query.get_or_404(discussion_id)
    data = request.get_json()
    discussion.text = data.get('text', discussion.text)
    discussion.image = data.get('image', discussion.image)
    discussion.hashtags = data.get('hashtags', discussion.hashtags)
    db.session.commit()
    return jsonify
