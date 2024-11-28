from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.gift_list import GiftList, GiftItem
from models.user import User
from models.base import db

bp = Blueprint('wishlist', __name__)

@bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    return render_template('wishlist/dashboard.html', gift_lists=user.gift_lists)

@bp.route('/wishlist/new', methods=['GET', 'POST'])
def new_wishlist():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        wishlist = GiftList(
            name=request.form['name'],
            description=request.form['description'],
            user_id=session['user_id']
        )
        db.session.add(wishlist)
        db.session.commit()
        return redirect(url_for('wishlist.dashboard'))
    
    return render_template('wishlist/new.html')

@bp.route('/wishlist/<int:id>')
def view_wishlist(id):
    wishlist = GiftList.query.get_or_404(id)
    return render_template('wishlist/view.html', wishlist=wishlist)

@bp.route('/wishlist/<int:id>/item/add', methods=['GET', 'POST'])
def add_item(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    wishlist = GiftList.query.get_or_404(id)
    if wishlist.user_id != session['user_id']:
        flash('Unauthorized')
        return redirect(url_for('wishlist.dashboard'))
    
    if request.method == 'POST':
        item = GiftItem(
            url=request.form['url'],
            description=request.form['description'],
            gift_list_id=id
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('wishlist.view_wishlist', id=id))
    
    return render_template('wishlist/add_item.html', wishlist=wishlist)

@bp.route('/item/<int:id>/toggle')
def toggle_item(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    item = GiftItem.query.get_or_404(id)
    item.status = 'purchased' if item.status == 'open' else 'open'
    db.session.commit()
    return redirect(url_for('wishlist.view_wishlist', id=item.gift_list_id))