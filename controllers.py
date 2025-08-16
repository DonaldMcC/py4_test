"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from yatl.helpers import A

from py4web import URL, abort, action, redirect, request
from py4web.utils.form import Form, FormStyleBootstrap4
from py4web.utils.grid import Grid

from .common import (
    T,
    auth,
    authenticated,
    cache,
    db,
    flash,
    logger,
    session,
    unauthenticated,
)


@action("index")
@action.uses("index.html", auth, T)
def index():
    user = auth.get_user()
    message = T("Hello {first_name}").format(**user) if user else T("Hello")
    form = Form(db.parent)
    return dict(message=message, form=form)


@action("childform")
@action.uses("childform.html", auth, T)
def childform():
    form = Form(db.child)
    return dict(form=form)


@action("childgrid")
@action.uses("childgrid.html", auth, T)
def childgrid():
    grid = Grid(db.child)
    return dict(grid=grid)


@action("parentgrid")
@action.uses("parentgrid.html", auth, T)
def parentdgrid():
    grid = Grid(db.parent)
    return dict(grid=grid)

@action("childrows")
@action.uses("childrows.html", auth, T)
def childrows():
    rows = db(db.child.id>0).select()
    return dict(rows=rows)


@action("parentrows")
@action.uses("parentrows.html", auth, T)
def childrows():
    rows = db(db.parent.id>0).select()
    return dict(rows=rows)