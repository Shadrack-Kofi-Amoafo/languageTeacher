# Lumière — a 3D fine-dining restaurant website

A demo restaurant website with **exactly 49 pages**, an Apple-inspired UI, an
interactive **Three.js 3D hero** (a levitating cloche over a signature dish —
drag it), and a **Python (Flask) backend** with server-rendered pages, form
handling and a JSON API.

## The 49 pages

| Section | Pages | Count |
| --- | --- | --- |
| Home | 3D hero, signatures, teasers, press, hours | 1 |
| Menu | Overview + 6 categories (starters, mains, seafood, plants, desserts, drinks) | 7 |
| Dishes | Full detail pages — story, ingredients, allergens, nutrition, pairing, reviews | 12 |
| Recipes | Library index + 8 complete recipes (ingredients, timed steps, chef tips) | 9 |
| Chefs | Brigade index + 6 profiles (bios, timelines, awards, signatures) | 7 |
| Editorial | About, Our Story, Sustainability, Locations, Gallery, Events, Private Dining, Gift Cards | 8 |
| Forms | Reserve, Contact, Catering, Careers, Feedback (all POST to Flask + SQLite) | 5 |
| **Total** | | **49** |

## Run it

```bash
cd restaurant
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python app.py        # → http://0.0.0.0:5000
```

Or with any WSGI server: `venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app`

## Architecture

```
restaurant/
├── app.py                  # Flask: 49 routes, forms → SQLite, JSON API
├── data/                   # The whole site is data-driven
│   ├── dishes.py           #   12 signature dishes + category extras
│   ├── recipes.py          #   8 recipes
│   ├── chefs.py            #   6 chef profiles
│   └── content.py          #   editorial copy, events, locations, forms
├── templates/              # Jinja2 (base + 20 page templates)
├── static/
│   ├── css/main.css        # Apple-inspired design system
│   ├── js/three-hero.js    # 3D scene (drag, parallax, particles)
│   ├── js/main.js          # Nav, reveal-on-scroll, tilt cards
│   ├── vendor/three.min.js # Three.js r147 (vendored, MIT)
│   └── img/                # 50 optimised images
└── lumiere.db              # SQLite (form submissions — gitignored)
```

### Backend features

- All 49 pages server-rendered from the `data/` modules
- 5 forms + gift-card orders with server-side validation → SQLite
- JSON API: `/api/menu`, `/api/dishes/<slug>`, `/api/chefs`, `/api/recipes`,
  `/api/events`, `/api/stats`, `/health`
- Custom 404, flash messages, route registry that asserts the 49-page count

### Design language (Apple-inspired)

Frosted-glass fixed nav (`backdrop-filter`), SF system typography with tight
tracking, `#f5f5f7` alternating bands, pill buttons, 22px-radius cards,
restrained gold accent, scroll-reveal choreography, and subtle 3D card tilt.

> Lumière is a fictional restaurant. The recipes, however, genuinely work.
