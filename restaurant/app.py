"""Lumière — a 3D fine-dining restaurant website.

Flask backend serving exactly 49 detailed pages:

    Home, editorial (about, story, sustainability, locations, gallery,
    events, private dining, gift cards), the menu (overview + 6 categories),
    12 signature dish pages, the recipe library (index + 8 recipes),
    the brigade (index + 6 chefs) and 5 full forms.

Forms POST back to the same pages, are validated server-side, and are
persisted to SQLite. A JSON API exposes the underlying data.

Run:  python app.py   →  http://0.0.0.0:5000
"""

import os
import sqlite3
from datetime import datetime

from flask import (Flask, abort, flash, g, jsonify, redirect,
                   render_template, request, url_for)

from data.chefs import CHEFS, get_chef
from data.content import (EVENTS, FOOTER, GIFT_CARDS, ABOUT, EVENTS as EVENTS_DATA,
                          GALLERY, GIFT_CARDS as GIFT_CARDS_DATA, HOME, LOCATIONS,
                          PRIVATE_DINING, RESTAURANT, STORY, SUSTAINABILITY, FORMS)
from data.dishes import (CATEGORIES, DISHES, MENU_EXTRAS, dishes_by_category,
                         get_category, get_dish)
from data.recipes import RECIPES, get_recipe

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("LUMIERE_SECRET", "lumiere-dev-key-change-me")
app.config["DATABASE"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lumiere.db")

DATABASE = app.config["DATABASE"]

# --------------------------------------------------------------------------
# The canonical 49-page registry (used by the footer sitemap and tests).
STATIC_PAGES = [
    ("/", "Home"),
    ("/menu", "Menu"),
    ("/about", "About"),
    ("/story", "Our Story"),
    ("/sustainability", "Sustainability"),
    ("/locations", "Locations"),
    ("/gallery", "Gallery"),
    ("/events", "Events"),
    ("/private-dining", "Private Dining"),
    ("/gift-cards", "Gift Cards"),
    ("/recipes", "Recipes"),
    ("/chefs", "The Brigade"),
    ("/reserve", "Reserve a Table"),
    ("/contact", "Contact"),
    ("/catering", "Catering"),
    ("/careers", "Careers"),
    ("/feedback", "Feedback"),
]
CATEGORY_PAGES = [(f"/menu/{c['slug']}", c["name"]) for c in CATEGORIES]
DISH_PAGES = [(f"/menu/dish/{d['slug']}", d["name"]) for d in DISHES]
RECIPE_PAGES = [(f"/recipes/{r['slug']}", r["title"]) for r in RECIPES]
CHEF_PAGES = [(f"/chefs/{c['slug']}", c["name"]) for c in CHEFS]
FORM_PAGES = [(f"/{key}", FORMS[key]["title"]) for key in ("reserve", "contact", "catering", "careers", "feedback")]

ALL_PAGES = (STATIC_PAGES + CATEGORY_PAGES + DISH_PAGES
             + RECIPE_PAGES + CHEF_PAGES)
assert len(ALL_PAGES) == 49, f"Expected 49 pages, found {len(ALL_PAGES)}"


# --------------------------------------------------------------------------
# Database (SQLite) — form submissions & gift-card orders.
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            form_type TEXT NOT NULL,
            data TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """
    )
    db.commit()
    db.close()


def store_submission(form_type, data):
    db = get_db()
    db.execute(
        "INSERT INTO submissions (form_type, data, created_at) VALUES (?, ?, ?)",
        (form_type, str(data), datetime.utcnow().isoformat(timespec="seconds") + "Z"),
    )
    db.commit()


def submission_count(form_type=None):
    db = get_db()
    if form_type:
        row = db.execute("SELECT COUNT(*) AS n FROM submissions WHERE form_type = ?", (form_type,)).fetchone()
    else:
        row = db.execute("SELECT COUNT(*) AS n FROM submissions").fetchone()
    return row["n"]


with app.app_context():
    init_db()


# --------------------------------------------------------------------------
# Template helpers.
@app.context_processor
def inject_globals():
    return {
        "restaurant": RESTAURANT,
        "footer": FOOTER,
        "categories": CATEGORIES,
        "all_dishes": DISHES,
        "all_chefs": CHEFS,
        "all_recipes": RECIPES,
        "locations": LOCATIONS,
        "get_chef": get_chef,
        "now_year": datetime.utcnow().year,
    }


# --------------------------------------------------------------------------
# Core pages.
@app.route("/")
def home():
    return render_template("home.html", home=HOME, press=HOME["press"],
                           signatures=DISHES[:6], stats=HOME["stats"])


@app.route("/about")
def about():
    return render_template("about.html", page=ABOUT)


@app.route("/story")
def story():
    return render_template("story.html", page=STORY)


@app.route("/sustainability")
def sustainability():
    return render_template("sustainability.html", page=SUSTAINABILITY)


@app.route("/locations")
def locations():
    return render_template("locations.html", locations=LOCATIONS)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", images=GALLERY)


@app.route("/events")
def events():
    return render_template("events.html", page=EVENTS)


@app.route("/private-dining")
def private_dining():
    return render_template("private_dining.html", page=PRIVATE_DINING)


@app.route("/gift-cards", methods=["GET", "POST"])
def gift_cards():
    order_done = False
    errors = {}
    values = {}
    if request.method == "POST":
        values = {k: request.form.get(k, "").strip() for k in
                  ("sender", "recipient", "recipient_email", "amount", "message", "delivery")}
        if not values["sender"]:
            errors["sender"] = "Your name, please."
        if not values["recipient"]:
            errors["recipient"] = "Who's the lucky one?"
        if "@" not in values["recipient_email"]:
            errors["recipient_email"] = "A valid email for delivery."
        try:
            amount = int(values["amount"] or 0)
            if not (25 <= amount <= 10000):
                errors["amount"] = "Between £25 and £10,000."
        except ValueError:
            errors["amount"] = "Whole numbers only."
            amount = 0
        if not errors:
            store_submission("gift_card", values)
            flash(f"Gift card for {values['recipient']} is on its way. Thank you.", "success")
            order_done = True
            values = {}
    return render_template("gift_cards.html", page=GIFT_CARDS,
                           order_done=order_done, errors=errors, values=values)


# --------------------------------------------------------------------------
# Menu pages.
@app.route("/menu")
def menu():
    return render_template("menu_index.html")


@app.route("/menu/<cat>")
def menu_category(cat):
    category = get_category(cat)
    if not category:
        abort(404)
    return render_template(
        "menu_category.html",
        category=category,
        dishes=dishes_by_category(cat),
        extras=MENU_EXTRAS.get(cat, []),
    )


@app.route("/menu/dish/<slug>")
def dish(slug):
    d = get_dish(slug)
    if not d:
        abort(404)
    related = [x for x in DISHES if x["category"] == d["category"] and x["slug"] != slug][:3]
    return render_template("dish.html", dish=d, related=related)


# --------------------------------------------------------------------------
# Recipe pages.
@app.route("/recipes")
def recipes():
    return render_template("recipes_index.html")


@app.route("/recipes/<slug>")
def recipe(slug):
    r = get_recipe(slug)
    if not r:
        abort(404)
    return render_template("recipe.html", recipe=r)


# --------------------------------------------------------------------------
# Chef pages.
@app.route("/chefs")
def chefs():
    return render_template("chefs_index.html")


@app.route("/chefs/<slug>")
def chef(slug):
    c = get_chef(slug)
    if not c:
        abort(404)
    return render_template("chef.html", chef=c)


# --------------------------------------------------------------------------
# Form pages (5): reserve, contact, catering, careers, feedback.
@app.route("/reserve", methods=["GET", "POST"])
def reserve():
    return render_form("reserve")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_form("contact")


@app.route("/catering", methods=["GET", "POST"])
def catering():
    return render_form("catering")


@app.route("/careers", methods=["GET", "POST"])
def careers():
    return render_form("careers")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    return render_form("feedback")


def render_form(key):
    spec = FORMS[key]
    errors, values, done = {}, {}, False
    if request.method == "POST":
        values = {f["name"]: request.form.get(f["name"], "").strip() for f in spec["fields"]}
        for f in spec["fields"]:
            v = values[f["name"]]
            if f.get("required") and not v:
                errors[f["name"]] = "This one's required."
            elif f["type"] == "email" and v and ("@" not in v or "." not in v):
                errors[f["name"]] = "That email doesn't look right."
        if not errors:
            store_submission(key, values)
            flash(f"{spec['success_title']} {spec['success_text']}", "success")
            done = True
            values = {}
    return render_template(f"form_{key}.html", spec=spec, errors=errors, values=values, done=done)


# --------------------------------------------------------------------------
# JSON API — the same data the pages are built from.
@app.route("/api/menu")
def api_menu():
    return jsonify({
        "categories": [{"slug": c["slug"], "name": c["name"]} for c in CATEGORIES],
        "dishes": [{"slug": d["slug"], "name": d["name"], "category": d["category"],
                    "price": d["price"], "badge": d.get("badge")} for d in DISHES],
    })


@app.route("/api/dishes/<slug>")
def api_dish(slug):
    d = get_dish(slug)
    if not d:
        return jsonify({"error": "not found"}), 404
    return jsonify(d)


@app.route("/api/chefs")
def api_chefs():
    return jsonify([{"slug": c["slug"], "name": c["name"], "role": c["role"]} for c in CHEFS])


@app.route("/api/recipes")
def api_recipes():
    return jsonify([{"slug": r["slug"], "title": r["title"], "category": r["category"],
                     "difficulty": r["difficulty"]} for r in RECIPES])


@app.route("/api/events")
def api_events():
    return jsonify(EVENTS["upcoming"])


@app.route("/api/stats")
def api_stats():
    return jsonify({
        "pages": len(ALL_PAGES),
        "dishes": len(DISHES),
        "recipes": len(RECIPES),
        "chefs": len(CHEFS),
        "categories": len(CATEGORIES),
        "submissions_total": submission_count(),
    })


# --------------------------------------------------------------------------
# Errors & niceties.
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.route("/health")
def health():
    return jsonify({"status": "ok", "pages": len(ALL_PAGES)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n  Lumière — {len(ALL_PAGES)} pages, {len(DISHES)} signature dishes, {len(RECIPES)} recipes.")
    print(f"  Serving on http://0.0.0.0:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=False)
