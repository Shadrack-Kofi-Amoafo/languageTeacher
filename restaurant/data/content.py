"""Long-form content for the editorial pages: about, story, sustainability,
locations, gallery, events, private dining, gift cards, home and footer."""

RESTAURANT = {
    "name": "Lumière",
    "tagline": "Cook like a grandmother. Plate like a surgeon.",
    "est": 2012,
    "description": "Modern fine dining in three cities. One star, one farm, four hundred bottles, and a menu rewritten every season since 2012.",
}

# ---------------------------------------------------------------- HOME ------
HOME = {
    "hero": {
        "kicker": "Lumière · Est. 2012 · Mayfair · Soho · Kings Cross",
        "headline": "Dinner,\narranged like light.",
        "sub": "Seasonal fine dining from a kitchen that buys whole animals, whole fish, and whole crates of whatever the farm can't sell anywhere else. One star. Three cities. Zero shortcuts.",
        "primary_cta": {"label": "Reserve a table", "href": "/reserve"},
        "secondary_cta": {"label": "Explore the menu ›", "href": "/menu"},
        "scroll_hint": "Drag the plate. Then scroll.",
    },
    "stats": [
        {"value": "1", "label": "Michelin star, held since 2018"},
        {"value": "48", "label": "Seasonal menus written"},
        {"value": "100%", "label": "Whole fish, named day boats"},
        {"value": "98%", "label": "Carcass utilisation"},
    ],
    "signature_title": "The signatures.",
    "signature_sub": "Twelve dishes that built the name. Every one still tastes like the reason you came.",
    "menu_teaser": {
        "kicker": "The menu",
        "title": "Six sections. One argument.",
        "text": "Starters that whisper, mains that roar, seafood that never sees a freezer, a plant section that refuses to be a consolation prize, desserts timed to the minute, and a cellar of four hundred bottles waiting to argue with all of it.",
        "cta": "See the full menu",
    },
    "chefs_teaser": {
        "kicker": "The brigade",
        "title": "Six cooks. One quiet minute.",
        "text": "A founder who still writes the menu in one evening. A fire chef who has lit the grill personally for nine years. A pastry chef whose soufflé service runs on a stopwatch. Meet the people who will be cooking your dinner.",
        "cta": "Meet the chefs",
    },
    "recipes_teaser": {
        "kicker": "The recipes",
        "title": "Everything we know, on a page.",
        "text": "The dough we roll every morning. The stock that starts every sauce. The soufflé with the 22-minute warning. Tested, timed, and written for a home kitchen — because a secret recipe is just a recipe nobody loved enough to share.",
        "cta": "Browse the recipe library",
    },
    "press": [
        {"quote": "Quietly radical. The kind of cooking that resets what you expect from a dinner.", "source": "The Sunday Review"},
        {"quote": "A star earned, not negotiated. Book the lamb and surrender the evening.", "source": "Michelin Guide"},
        {"quote": "The soufflé alone justifies the train fare. Order it first. Always order it first.", "source": "City Eats"},
    ],
    "hours": [
        {"days": "Tuesday – Thursday", "time": "18:00 – 22:30"},
        {"days": "Friday – Saturday", "time": "12:00 – 14:30 · 17:30 – 23:00"},
        {"days": "Sunday", "time": "12:00 – 16:00 (Sunday lunch menu)"},
        {"days": "Monday", "time": "Closed — the kitchen rests, the fire is banked"},
    ],
}

# ---------------------------------------------------------------- ABOUT -----
ABOUT = {
    "kicker": "About",
    "title": "A restaurant built backwards.",
    "lede": "Most restaurants start with a dining room and find a kitchen to fill it. We started with a kitchen — eleven cooks, one farm relationship, and a stubborn belief that if we bought everything whole and cooked everything ourselves, the food would speak quietly enough to be heard over the cutlery.",
    "sections": [
        {
            "title": "Everything from scratch.",
            "text": [
                "The bread is baked at 5 a.m. The stocks start before that. The butter is churned, the vinegars ferment in jars you can see from the chef's table, and the only things in our walk-in that arrive pre-made are the things no human has ever improved: milk, eggs, and the occasonal very good cheese.",
                "It is slower this way. It is also, we would argue after fourteen years, the only way.",
            ],
        },
        {
            "title": "Bought whole, used entirely.",
            "text": [
                "Whole animals from named farms, whole fish from named boats, whole crates of the cosmetically imperfect produce that farms can't sell to anyone else. Bones become jus, trim becomes staff meal, fat becomes pastry. Two percent of what we buy leaves as waste — and we think that two percent is still too much.",
            ],
        },
        {
            "title": "One menu, rewritten six times a year.",
            "text": [
                "Seasons don't care about print schedules, so the menu is written on a single evening, four times a season, after Elena walks the farm and the market. Dishes retire undefeated. The burrata stays. Some rules are permanent.",
            ],
        },
    ],
    "stats": [
        {"value": "14", "label": "Years since opening"},
        {"value": "6", "label": "Menus per year"},
        {"value": "40+", "label": "Live ferments in the lab"},
        {"value": "70+", "label": "Cooks mentored here"},
    ],
    "values": [
        {"icon": "◈", "title": "Precision, invisibly", "text": "The technique should be felt, never noticed. If you can see the effort, we've failed."},
        {"icon": "◎", "title": "Season above all", "text": "No dish outruns its ingredients. When the asparagus is gone, the asparagus is gone."},
        {"icon": "◐", "title": "Nothing wasted", "text": "Bones, fins, trim, peels — everything has a second life. Usually a better one."},
        {"icon": "✦", "title": "Hospitality, honestly", "text": "Warm without theatre. The guest is a friend of the house, not an audience."},
    ],
}

# ---------------------------------------------------------------- STORY -----
STORY = {
    "kicker": "Our story",
    "title": "Fourteen years, told quickly.",
    "lede": "Eleven tables, a borrowed espresso machine, and a lease negotiated over three coffees. Here is how Lumière became Lumière.",
    "timeline": [
        {"year": "2009", "title": "A lunch that wouldn't leave.", "text": "Elena, then a head chef elsewhere, has lunch at a farm kitchen in the Basque country and spends the next three years unable to stop talking about it. The idea has, at this point, a name but no address."},
        {"year": "2012", "title": "Eleven tables.", "text": "Lumière opens in Mayfair. The espresso machine is borrowed from a friend's café (still is). The first menu is nine dishes long and written in an evening. It is profitable by month seven, largely because eleven tables turn twice."},
        {"year": "2014", "title": "The farm, and the ferment shelf.", "text": "The first Bramble Hollow partnership: a standing order for whatever the farm has too much of. Sofia arrives four years later and turns the surplus into a ferment library; in 2014 it is simply Sofia-shaped destiny, pending."},
        {"year": "2015", "title": "The fire.", "text": "Antoine joins and installs the binchotan grill. He lights it personally at 4:45 p.m. every service, a streak now past two thousand. The lamb — his dish from day one — becomes the thing people book tables around."},
        {"year": "2017", "title": "Copper on a plane.", "text": "Yuki arrives from Osaka with forty soufflé moulds in a wheelie bag. The dessert menu doubles in ambition within the season. The soufflé acquires its warning: 22 minutes, order at the start."},
        {"year": "2018", "title": "A star.", "text": "Michelin arrives. Elena requests the menu read 'a nice thing that happened'. The Guide declines, politely. The same month, Amara's raw bar opens — granite, 8 °C, fish cut to order."},
        {"year": "2020", "title": "The year of jars.", "text": "Lockdown. The kitchen cures, ferments, bakes and delivers across the city. Amara's jars marked 'AD 2020' are still on the ferment shelf — nobody has the heart to use them; nobody would dare throw them out."},
        {"year": "2022", "title": "Three cities.", "text": "Lumière Soho opens with its own chef and a menu built around the same farm, the same fire, the same rules. Kings Cross follows eighteen months later, in a converted ticket hall, with a cellar twice the size."},
        {"year": "2024", "title": "The school.", "text": "The Lumière Scholarship launches: one fully paid apprenticeship a year, aimed at cooks from non-culinary backgrounds. Antoine and Elena write the curriculum. It is oversubscribed eleven-fold in year one."},
        {"year": "2026", "title": "Still hungry.", "text": "Forty-eight seasonal menus written. One star, held. The espresso machine, still borrowed. The lamb, still ordered first. The story continues at a table near you — reserve one and find out what's next."},
    ],
}

# -------------------------------------------------------- SUSTAINABILITY ----
SUSTAINABILITY = {
    "kicker": "Sustainability",
    "title": "Zero waste is a menu item.",
    "lede": "We don't treat sustainability as a department. It is the way the kitchen has run since it had eleven tables and couldn't afford to throw anything away. Now it can afford to — and doesn't.",
    "pillars": [
        {
            "title": "Root to leaf, fin to tail.",
            "text": "Whole animals, whole fish, whole crates of the imperfect. Bones to stock, trim to staff meal, fat to pastry, peels to vinegar. Our carcass utilisation sits at 98%; the last 2% goes to the farm's compost, which grows next year's menu.",
            "metric": "98% utilisation",
        },
        {
            "title": "One farm, one fleet.",
            "text": "Bramble Hollow, fifty acres, fifty miles: a third of our produce, planned in January, picked to order. Our fish comes from four named day boats and arrives whole on ice. If a boat doesn't sail, the menu changes. We consider this a feature.",
            "metric": "3 cities, 1 supply chain",
        },
        {
            "title": "The ferment library.",
            "text": "Forty-plus live cultures — misos, garums, kojis, vinegars — season dishes across the whole menu. Fermentation is how we make surplus delicious and winter taste like summer's memory. It is also, Sofia notes, extremely cheap physics.",
            "metric": "40+ live cultures",
        },
        {
            "title": "Heat, light, and the banked fire.",
            "text": "Induction on the line, a single charcoal service, hot water recaptured from the pastry section's chillers. The grill is banked, never doused — the coals are reborn the next day, like everything else around here.",
            "metric": "-31% energy vs 2019",
        },
    ],
    "partners": [
        {"name": "Bramble Hollow Farm", "detail": "50 acres · 50 miles · ⅓ of all produce, seed to order"},
        {"name": "The Mary Rose & three sister boats", "detail": "Day-boat fish, landed daily, named on the menu"},
        {"name": "Commonsend Dairy", "detail": "Cheese and cream from 30 miles out, delivered by van that runs on chip fat — ours"},
        {"name": "Hopkin & Sons Mill", "detail": "Stoneground flour; our sourdough, from field to board"},
        {"name": "Grove Street Apiary", "detail": "Hives on our own roof; honey on the cheese trolley"},
    ],
    "stats": [
        {"value": "98%", "label": "Carcass utilisation"},
        {"value": "0", "label": "Air-freighted ingredients"},
        {"value": "50", "label": "Miles to the farm"},
        {"value": "31%", "label": "Energy reduction since 2019"},
    ],
}

# ---------------------------------------------------------------- LOCATIONS -
LOCATIONS = [
    {
        "slug": "mayfair",
        "name": "Lumière Mayfair",
        "flagship": True,
        "address": "18 Chesterfield Mews, Mayfair, London W1J 5BR",
        "phone": "+44 (0)20 7946 0012",
        "email": "mayfair@lumiere.example",
        "image": "locations/mayfair.jpg",
        "seats": 46,
        "opened": 2012,
        "chef": "elena-marchetti",
        "description": [
            "The original. Eleven tables grew to twenty-two, but the room still holds its first-evening hush: linen, oak, low light, and the pass visible from the chef's counter where the quiet minute happens.",
            "Home of the binchotan grill, the dry-aging room, the ferment library and the soufflé service. If you're eating one Lumière dinner in your life, the consensus is: here.",
        ],
        "hours": [
            {"days": "Tue – Thu", "time": "18:00 – 22:30"},
            {"days": "Fri – Sat", "time": "12:00 – 14:30 · 17:30 – 23:00"},
            {"days": "Sun", "time": "12:00 – 16:00"},
            {"days": "Mon", "time": "Closed"},
        ],
        "features": ["Chef's counter (6 seats)", "Dry-aging viewing room", "The original binchotan grill", "Rooftop apiary"],
    },
    {
        "slug": "soho",
        "name": "Lumière Soho",
        "flagship": False,
        "address": "4 Carlisle Passage, Soho, London W1D 3QT",
        "phone": "+44 (0)20 7946 0102",
        "email": "soho@lumiere.example",
        "image": "locations/soho.jpg",
        "seats": 38,
        "opened": 2022,
        "chef": "antoine-dubois",
        "description": [
            "The louder sibling. Opened in a former print works with the same farm, the same fire and the same rules, but a menu that leans towards Soho's appetite: bigger flavours, a longer bar, and a raw counter facing the street.",
            "The bar here pours the full cellar plus a cocktail list that plays the greatest hits from a decade of Lumière menus. Last kitchen order is a civilised 22:15.",
        ],
        "hours": [
            {"days": "Tue – Thu", "time": "17:30 – 22:45"},
            {"days": "Fri – Sat", "time": "12:00 – 15:00 · 17:00 – 23:30"},
            {"days": "Sun – Mon", "time": "Closed"},
        ],
        "features": ["Street-facing raw bar", "Full cellar, 400+ labels", "Late kitchen till 22:15", "Walk-ins at the bar (10 seats)"],
    },
    {
        "slug": "kings-cross",
        "name": "Lumière Kings Cross",
        "flagship": False,
        "address": "The Old Ticket Hall, Goods Way, London N1C 4BQ",
        "phone": "+44 (0)20 7946 0187",
        "email": "kingscross@lumiere.example",
        "image": "locations/kings-cross.jpg",
        "seats": 54,
        "opened": 2023,
        "chef": "amara-diallo",
        "description": [
            "The grand room: a Victorian ticket hall with a six-metre ceiling, our largest cellar, and a private dining gallery mezzanine for up to eighteen. The kitchen here is led from the fish section — expect the raw bar to be the loudest voice on the menu.",
            "Two minutes from the platforms, which makes it the correct answer to 'where should we eat before/after the train' for the entire eastern seaboard of the country.",
        ],
        "hours": [
            {"days": "Mon – Fri", "time": "12:00 – 14:30 · 17:30 – 22:30"},
            {"days": "Sat", "time": "17:00 – 23:00"},
            {"days": "Sun", "time": "12:00 – 16:00"},
        ],
        "features": ["Private mezzanine gallery (18)", "Largest cellar of the three", "Station-side, 2 min walk", "Sunday lunch service"],
    },
]

# ---------------------------------------------------------------- GALLERY ---
GALLERY = [
    {"src": "gallery/pass.jpg", "title": "The pass, 6:45 p.m.", "caption": "The quiet minute, one course in.", "tag": "Kitchen"},
    {"src": "gallery/grill.jpg", "title": "The binchotan grill", "caption": "Lit at 4:45 p.m. daily since 2015.", "tag": "Kitchen"},
    {"src": "gallery/room.jpg", "title": "The Mayfair room", "caption": "Twenty-two tables, one hush.", "tag": "Rooms"},
    {"src": "gallery/bar.jpg", "title": "The Soho bar", "caption": "Clarified punches and 400 labels.", "tag": "Rooms"},
    {"src": "gallery/pastry.jpg", "title": "The pastry lab", "caption": "Chocolate tempered to the half-degree.", "tag": "Kitchen"},
    {"src": "gallery/farm.jpg", "title": "Bramble Hollow, July", "caption": "A third of the menu, fifty miles out.", "tag": "Farm"},
    {"src": "gallery/produce.jpg", "title": "Thursday's crates", "caption": "The imperfect, chosen on purpose.", "tag": "Farm"},
    {"src": "gallery/ferments.jpg", "title": "The ferment library", "caption": "Forty-plus jars. Some older than the apprentices.", "tag": "Kitchen"},
    {"src": "gallery/hall.jpg", "title": "The ticket hall", "caption": "Kings Cross, six metres of Victorian sky.", "tag": "Rooms"},
    {"src": "gallery/service.jpg", "title": "Full house", "caption": "Saturday, second sitting.", "tag": "Rooms"},
    {"src": "gallery/bread.jpg", "title": "5 a.m. bread", "caption": "Sourdough, 48 hours in the making.", "tag": "Kitchen"},
    {"src": "gallery/cellar.jpg", "title": "The cellar", "caption": "Four hundred arguments, temperature-held.", "tag": "Rooms"},
]

# ---------------------------------------------------------------- EVENTS ----
EVENTS = {
    "kicker": "Events",
    "title": "Nights with a shape of their own.",
    "lede": "One-off dinners, standing clubs, and masterclasses small enough to ask questions. Everything below is bookable; nothing below repeats exactly.",
    "upcoming": [
        {
            "date": "Oct 21", "day": "Tuesday", "time": "19:00",
            "title": "Fire & Patience: The Butchery Masterclass",
            "chef": "liam-osullivan",
            "text": "Liam breaks down a whole carcass, explains every decision, and Antoine cooks three cuts from it over binchotan while you eat them in sequence. Includes the 60-day ribeye, if the aging room cooperates.",
            "price": "£120 · 12 seats",
            "badge": "6 seats left",
        },
        {
            "date": "Nov 04", "day": "Tuesday", "time": "19:00",
            "title": "The Soufflé Supper",
            "chef": "yuki-tanaka",
            "text": "A five-course dessert tasting built entirely around the soufflé — savoury first, then five risings, the last with tawny port poured tableside. Yuki explains the stopwatch between courses.",
            "price": "£95 · 20 seats",
            "badge": "Sold out · waiting list",
        },
        {
            "date": "Nov 18", "day": "Tuesday", "time": "18:30",
            "title": "Farm Table: The November Harvest",
            "chef": "sofia-ramos",
            "text": "Sofia cooks the farm's November crate as a six-course menu, with the ferment library running through every course. Bramble Hollow's growers join for the first two courses and answer everything.",
            "price": "£110 · 16 seats",
            "badge": "9 seats left",
        },
        {
            "date": "Dec 02", "day": "Tuesday", "time": "19:00",
            "title": "Old World vs. New: A Cellar Argument",
            "chef": "elena-marchetti",
            "text": "Eight wines, four courses, and our sommelier defending old-world orthodoxy against a very persuasive new-world guest. You vote. The losing bottles get drunk anyway.",
            "price": "£140 · 24 seats",
            "badge": "14 seats left",
        },
        {
            "date": "Dec 09", "day": "Tuesday", "time": "19:00",
            "title": "Whole Fish, Start to Finish",
            "chef": "amara-diallo",
            "text": "Amara breaks down a turbot and a bluefin, then serves the raw bar's greatest hits while the trim becomes dinner's second half. The staff fishcakes make a cameo, as tradition demands.",
            "price": "£105 · 14 seats",
            "badge": "5 seats left",
        },
        {
            "date": "Dec 16", "day": "Tuesday", "time": "19:00",
            "title": "The Staff Meal Supper",
            "chef": "antoine-dubois",
            "text": "The food the kitchen cooks for itself — family mince, staff fishcakes, the pasta from the recipe card — served to guests, at family tables, at family prices. All profits fund the Lumière Scholarship.",
            "price": "£45 · 30 seats",
            "badge": "Charity night",
        },
    ],
    "clubs": [
        {"name": "The Sunday Roast Club", "text": "Last Sunday of the month, Mayfair room. Liam's dry-aged beef, all the trimmings, unreasonably good gravy. Members book first; everyone else takes what's left.", "freq": "Monthly · £55"},
        {"name": "The Ferment Society", "text": "First Wednesday, Soho bar. Sofia opens one jar per month — some two years old — pairs it with something from the kitchen, and explains the microbes like old friends.", "freq": "Monthly · £35"},
        {"name": "The Côte de Boeuf Table", "text": "First Friday, Kings Cross. One 1.2 kg côte de boeuf for every two guests, triple-cooked chips, the biggest reds in the cellar. Not subtle. Fully booked most months.", "freq": "Monthly · £85"},
    ],
}

# --------------------------------------------------------- PRIVATE DINING ---
PRIVATE_DINING = {
    "kicker": "Private dining",
    "title": "Your table, raised.",
    "lede": "Three rooms across two houses, each with its own kitchen rhythm. Buy out a room or the whole restaurant; either way the menu is written for you, with you, from the season's crates.",
    "rooms": [
        {
            "name": "The Chef's Table",
            "location": "Mayfair",
            "capacity": "6 – 8",
            "image": "private/chefs-table.jpg",
            "text": "Six seats at the pass itself. You watch the quiet minute happen. Elena or Antoine cooks for the table personally, narrates the courses, and answers everything — including, if you ask nicely, where the espresso machine is really from.",
            "price": "From £180 per guest · tasting menu only",
        },
        {
            "name": "The Gallery Mezzanine",
            "location": "Kings Cross",
            "capacity": "10 – 18",
            "image": "private/mezzanine.jpg",
            "text": "The ticket hall's iron-railed mezzanine, suspended over the main room with the six-metre ceiling all to itself. Full à la carte or bespoke menu, its own bar station, and the cellar hoisted up by the glass.",
            "price": "From £120 per guest · room minimum applies",
        },
        {
            "name": "The Print Room",
            "location": "Soho",
            "capacity": "8 – 14",
            "image": "private/print-room.jpg",
            "text": "A candlelit private room in the old print works' proofing suite, with the raw bar's chilled larder on one wall. Best for celebrations with opinions — the menu flexes to one guest's no-shellfish, another's everything-shellfish.",
            "price": "From £95 per guest · bespoke menus",
        },
    ],
    "experiences": [
        {"title": "Full buyout", "text": "The entire room, the entire brigade, one menu written for the night. Mayfair (46), Soho (38), Kings Cross (54)."},
        {"title": "Kitchen takeover", "text": "Up to four guests cook a course with the section of their choice, then sit down to the rest. Aprons provided; burns theoretically preventable."},
        {"title": "The whole animal", "text": "A carcass, a fire, and a menu built around the entire animal — from carpaccio to stew. Minimum twelve guests, one very happy butcher."},
    ],
    "process": [
        {"step": "01", "title": "Tell us the shape", "text": "Date, room, headcount, and the occasion — or the absence of one. Some of our best nights celebrated nothing in particular."},
        {"step": "02", "title": "We write the menu", "text": "A chef calls within 48 hours. Together you build the menu from the season's crates and the cellar's margins."},
        {"step": "03", "title": "The night itself", "text": "Your room, your pace, your playlist if you want it. The kitchen's rules apply; everything else is negotiable."},
    ],
}

# ------------------------------------------------------------- GIFT CARDS ---
GIFT_CARDS = {
    "kicker": "Gift cards",
    "title": "Give someone a very good evening.",
    "lede": "Physical cards pressed on cotton paper, or digital cards that arrive in ninety seconds. Both spend at all three houses, on everything from the tasting menu to the bar snacks. Neither expire. We think expiry dates on generosity are absurd.",
    "tiers": [
        {"amount": 100, "name": "An evening", "text": "Two courses and a glass each at the Soho bar. A very good Tuesday."},
        {"amount": 250, "name": "A dinner", "text": "Three courses for two with a bottle from the cellar's friendly shelf. The classic gift."},
        {"amount": 500, "name": "The full light", "text": "Tasting menus for two, the pairing flight, and the service charge handled. A complete evening, no decisions required."},
    ],
    "custom": {
        "title": "Any amount you like",
        "text": "From £25 upward — for the person who orders the cheapest thing they actually want, as is their right.",
    },
    "how": [
        {"step": "01", "title": "Choose", "text": "Pick a tier or a custom amount. Add a note if the occasion demands one; we print it by hand."},
        {"step": "02", "title": "Send", "text": "Digital arrives in ninety seconds by email. Physical cards are pressed, boxed, and couriered within two working days."},
        {"step": "03", "title": "Spend", "text": "Any house, any menu, any bar. The balance simply comes off — and what's left stays put, with no clock ticking."},
    ],
    "fine_print": [
        "Valid at all three Lumière houses, on food and drink alike.",
        "No expiry. Ever.",
        "Lost a card? Call the house; we'll sort it out over the phone like adults.",
        "Balances are transferable — pass it on if the evening finds a worthier recipient.",
    ],
}

# ---------------------------------------------------------------- FORMS -----
FORMS = {
    "reserve": {
        "kicker": "Reservations",
        "title": "The table is waiting.",
        "lede": "Bookings open sixty days ahead and roll daily at 9 a.m. We hold each table for fifteen minutes past your booking time; after that the room earns it back. Parties of seven or more, email mayfair@lumiere.example.",
        "success_title": "Table requested.",
        "success_text": "We'll confirm by email within the hour (during service hours). If the room is full, we'll offer the bar or the next seating with honest regret.",
        "fields": [
            {"name": "name", "label": "Full name", "type": "text", "required": True, "placeholder": "Ada Lovelace"},
            {"name": "email", "label": "Email", "type": "email", "required": True, "placeholder": "ada@example.com"},
            {"name": "phone", "label": "Phone", "type": "tel", "required": True, "placeholder": "+44 7700 900123"},
            {"name": "location", "label": "House", "type": "select", "required": True,
             "options": ["Lumière Mayfair", "Lumière Soho", "Lumière Kings Cross"]},
            {"name": "date", "label": "Date", "type": "date", "required": True},
            {"name": "time", "label": "Time", "type": "select", "required": True,
             "options": ["12:00", "12:30", "13:00", "13:30", "14:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]},
            {"name": "guests", "label": "Guests", "type": "select", "required": True,
             "options": ["1", "2", "3", "4", "5", "6"]},
            {"name": "occasion", "label": "Occasion", "type": "select", "required": False,
             "options": ["Just dinner", "Birthday", "Anniversary", "Business", "A proposal (discretion advised)", "Other"]},
            {"name": "seating", "label": "Seating preference", "type": "select", "required": False,
             "options": ["No preference", "Dining room", "Chef's counter", "Bar", "Quiet corner", "Window"]},
            {"name": "notes", "label": "Allergies, requests, anything", "type": "textarea", "required": False,
             "placeholder": "One coeliac, one pescatarian, one engagement we're pretending isn't happening…"},
        ],
    },
    "contact": {
        "kicker": "Contact",
        "title": "Talk to the house.",
        "lede": "Press, partnerships, lost property (the umbrella count is currently nine), or a simple hello — it all lands in the same inbox and is answered by a person within one working day.",
        "success_title": "Message received.",
        "success_text": "A person — not an autoresponder — will reply within one working day. During Friday and Saturday service, give us until Monday.",
        "fields": [
            {"name": "name", "label": "Your name", "type": "text", "required": True, "placeholder": "Grace Hopper"},
            {"name": "email", "label": "Email", "type": "email", "required": True, "placeholder": "grace@example.com"},
            {"name": "topic", "label": "Topic", "type": "select", "required": True,
             "options": ["General", "Press & media", "Feedback", "Lost property", "Accessibility", "Supplier inquiry", "Something else"]},
            {"name": "location", "label": "House (if relevant)", "type": "select", "required": False,
             "options": ["Not house-specific", "Lumière Mayfair", "Lumière Soho", "Lumière Kings Cross"]},
            {"name": "subject", "label": "Subject", "type": "text", "required": True, "placeholder": "A short line that says it all"},
            {"name": "message", "label": "Message", "type": "textarea", "required": True,
             "placeholder": "Write freely. We read everything, including the long ones."},
        ],
    },
    "catering": {
        "kicker": "Catering & events",
        "title": "We'll bring the fire.",
        "lede": "Weddings, launches, long-table dinners, and full buyouts of anywhere with a serviceable kitchen and a load-bearing ceiling. Within the M25 we bring the grill. Beyond it, we bring everything but the ceiling.",
        "success_title": "Catering inquiry received.",
        "success_text": "Our events lead will call within two working days to talk through the shape of the night.Menus follow within the week.",
        "fields": [
            {"name": "name", "label": "Your name", "type": "text", "required": True, "placeholder": "Josephine Baker"},
            {"name": "email", "label": "Email", "type": "email", "required": True, "placeholder": "jo@example.com"},
            {"name": "phone", "label": "Phone", "type": "tel", "required": True, "placeholder": "+44 7700 900456"},
            {"name": "company", "label": "Company / household (optional)", "type": "text", "required": False, "placeholder": "Optional"},
            {"name": "event_type", "label": "Event type", "type": "select", "required": True,
             "options": ["Wedding", "Corporate dinner", "Launch or party", "Long-table lunch", "Buyout (our houses)", "Other"]},
            {"name": "date", "label": "Date (or rough window)", "type": "text", "required": True, "placeholder": "14 March, or 'a Saturday in April'"},
            {"name": "guests", "label": "Estimated guests", "type": "select", "required": True,
             "options": ["10 – 20", "20 – 40", "40 – 80", "80 – 120", "120+"]},
            {"name": "budget", "label": "Budget per head", "type": "select", "required": False,
             "options": ["Under £75", "£75 – £120", "£120 – £200", "£200+", "Not sure yet"]},
            {"name": "details", "label": "The shape of the night", "type": "textarea", "required": True,
             "placeholder": "Cocktail reception for 60, then a seated dinner for 24. One vegetarian, two vegans, and a surprise toast at 9 p.m.…"},
        ],
    },
    "careers": {
        "kicker": "Careers",
        "title": "Cook with us.",
        "lede": "We hire for curiosity and stamina; we teach the rest. Every role comes with family meal, a real schedule, and the standing invitation to argue with the menu. The Lumière Scholarship runs yearly for cooks from non-culinary backgrounds.",
        "success_title": "Application received.",
        "success_text": "We read every application ourselves — expect a reply within five working days, and a staged interview (you cook, we talk) if it's a match.",
        "fields": [
            {"name": "name", "label": "Full name", "type": "text", "required": True, "placeholder": "Your name"},
            {"name": "email", "label": "Email", "type": "email", "required": True, "placeholder": "you@example.com"},
            {"name": "phone", "label": "Phone", "type": "tel", "required": True, "placeholder": "+44 7700 900789"},
            {"name": "role", "label": "Role", "type": "select", "required": True,
             "options": ["Commis chef", "Chef de partie", "Sous chef", "Pastry", "Fish section", "Front of house", "Sommelier", "Bakery", "Scholarship (paid apprenticeship)", "Dishpit — genuinely, the best training"]},
            {"name": "house", "label": "Preferred house", "type": "select", "required": True,
             "options": ["Any", "Mayfair", "Soho", "Kings Cross"]},
            {"name": "experience", "label": "Experience", "type": "select", "required": True,
             "options": ["Career changer / none yet", "Under 1 year", "1 – 3 years", "3 – 7 years", "7+ years"]},
            {"name": "portfolio", "label": "Link — CV, portfolio, or anything that shows your cooking (optional)", "type": "url", "required": False, "placeholder": "https://…"},
            {"name": "why", "label": "Why Lumière?", "type": "textarea", "required": True,
             "placeholder": "One honest paragraph beats five polished ones. What do you want to learn, and what do you bring?"},
        ],
    },
    "feedback": {
        "kicker": "Feedback",
        "title": "Tell us the truth.",
        "lede": "Praise goes on the kitchen wall, verbatim. Criticism goes into service notes the next morning, also verbatim. Both make the restaurant better; only one makes us blush.",
        "success_title": "Thank you — genuinely.",
        "success_text": "Feedback is read at the next morning's briefing, by name, out loud. If you asked for a reply, expect one within two working days.",
        "fields": [
            {"name": "name", "label": "Your name", "type": "text", "required": True, "placeholder": "Or 'anonymous', if you prefer"},
            {"name": "email", "label": "Email (for a reply)", "type": "email", "required": False, "placeholder": "Only if you'd like a reply"},
            {"name": "visited", "label": "Visit date", "type": "date", "required": False},
            {"name": "house", "label": "House", "type": "select", "required": True,
             "options": ["Lumière Mayfair", "Lumière Soho", "Lumière Kings Cross", "Delivery / catering"]},
            {"name": "occasion", "label": "What was it?", "type": "select", "required": False,
             "options": ["Dinner", "Lunch", "Bar only", "Private dining", "Event", "Delivery"]},
            {"name": "overall", "label": "Overall — how was it?", "type": "rating", "required": True},
            {"name": "food", "label": "The food", "type": "rating", "required": False},
            {"name": "service", "label": "The service", "type": "rating", "required": False},
            {"name": "room", "label": "The room", "type": "rating", "required": False},
            {"name": "return", "label": "Would you come back?", "type": "select", "required": True,
             "options": ["Already booked the next one", "Yes", "Probably", "Unlikely", "I'm writing this from the train home, still full"]},
            {"name": "comments", "label": "Say it in your own words", "type": "textarea", "required": True,
             "placeholder": "The good, the bad, and the detail we'd never notice ourselves."},
        ],
    },
}

# ---------------------------------------------------------------- FOOTER ----
FOOTER = {
    "blurb": "Seasonal fine dining. One farm, one fire, one rule: buy it whole, waste none of it, and let the ingredient finish the sentence.",
    "columns": [
        {
            "title": "Eat",
            "links": [
                ("The menu", "/menu"),
                ("Starters", "/menu/starters"),
                ("Mains", "/menu/mains"),
                ("Seafood", "/menu/seafood"),
                ("Plants", "/menu/plants"),
                ("Desserts", "/menu/desserts"),
                ("Drinks & wine", "/menu/drinks"),
            ],
        },
        {
            "title": "Learn",
            "links": [
                ("Recipe library", "/recipes"),
                ("The brigade", "/chefs"),
                ("Our story", "/story"),
                ("Sustainability", "/sustainability"),
                ("Gallery", "/gallery"),
            ],
        },
        {
            "title": "Visit",
            "links": [
                ("Reserve a table", "/reserve"),
                ("Locations & hours", "/locations"),
                ("Events", "/events"),
                ("Private dining", "/private-dining"),
                ("Gift cards", "/gift-cards"),
            ],
        },
        {
            "title": "House",
            "links": [
                ("About", "/about"),
                ("Contact", "/contact"),
                ("Careers", "/careers"),
                ("Catering", "/catering"),
                ("Feedback", "/feedback"),
            ],
        },
    ],
    "fine_print": "Lumière is a fictional restaurant created for this demonstration site. All dishes, chefs and events are illustrative — but every recipe here genuinely works.",
}
