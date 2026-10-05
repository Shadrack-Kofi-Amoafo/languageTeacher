"""Sanity tests: exactly 49 pages, all green, forms persist, API works.

Run:  venv/bin/python test_pages.py
"""
from app import ALL_PAGES, app, get_db

EXPECTED_PAGES = 49


def test_page_count():
    assert len(ALL_PAGES) == EXPECTED_PAGES, (
        f"Expected {EXPECTED_PAGES} pages, got {len(ALL_PAGES)}")


def test_all_pages_render():
    with app.test_client() as c:
        for path, name in ALL_PAGES:
            r = c.get(path)
            assert r.status_code == 200, f"{path} ({name}) -> {r.status_code}"


def test_404():
    with app.test_client() as c:
        assert c.get("/menu/dish/not-a-dish").status_code == 404
        assert c.get("/nope").status_code == 404


def test_form_persists():
    with app.test_client() as c:
        r = c.post("/reserve", data={
            "name": "Test Guest", "email": "guest@example.com",
            "phone": "+44 7700 900000", "location": "Lumière Mayfair",
            "date": "2026-12-01", "time": "19:00", "guests": "2",
        })
        assert r.status_code == 200
        assert b"Table requested" in r.data
    with app.app_context():
        db = get_db()
        row = db.execute(
            "SELECT id FROM submissions WHERE form_type='reserve' ORDER BY id DESC"
        ).fetchone()
        assert row is not None, "reservation was not stored"
        db.execute("DELETE FROM submissions WHERE id = ?", (row["id"],))
        db.commit()


def test_api():
    with app.test_client() as c:
        assert c.get("/api/menu").status_code == 200
        assert c.get("/api/dishes/burrata-figs").status_code == 200
        assert c.get("/api/dishes/burrata-figs").get_json()["name"] == "Burrata & Fig"
        stats = c.get("/api/stats").get_json()
        assert stats["pages"] == EXPECTED_PAGES
        assert stats["dishes"] == 12 and stats["recipes"] == 8 and stats["chefs"] == 6


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"  ✓ {name}")
    print(f"\nAll good — {EXPECTED_PAGES} pages, every one of them green.")
