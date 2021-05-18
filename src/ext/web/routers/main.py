from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from src.ext.auth import logout_current_user, validate_user
from src.ext.web.forms import LoginForm

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        validate, message = validate_user(form.username.data, form.password.data)
        if validate:
            return redirect("index.html")

        flash(message, "warning")
    return render_template("auth/login.html", form=form)


@bp.route("/logout", methods=["GET", "POST"])
def logout():
    logout_current_user()
    return redirect("index.html")
