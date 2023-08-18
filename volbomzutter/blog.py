from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from volbomzutter.auth import login_required

bp = Blueprint('blog', __name__)

from db_api.api import *
db_api = API(host='127.0.0.1', user='user', db_name='db', password='123')

@bp.route('/')
def index():
    posts = db_api.get_posts()[::-1]
    users = db_api.get_users()
    return render_template('blog/index.html', posts=posts, users=users)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db_api.add_post(Post((None, g.user.id, None, title, content)))
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = db_api.get_post_by_id(id)

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.user_id != g.user.id:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            # db.execute(
            #     'UPDATE post SET title = ?, body = ?'
            #     ' WHERE id = ?',
            #     (title, body, id)
            # )
            # db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    # db = get_db()
    # db.execute('DELETE FROM post WHERE id = ?', (id,))
    # db.commit()
    return redirect(url_for('blog.index'))