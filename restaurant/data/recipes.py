"""Recipe library — tested in the Lumière kitchen, written for your kitchen."""


RECIPES = [
    {
        "slug": "fresh-pasta-dough",
        "title": "Hand-Rolled Tagliatelle",
        "category": "Pasta & Dough",
        "chef": "antoine-dubois",
        "difficulty": "Medium",
        "prep": "30 min",
        "rest": "1 hr",
        "total": "1 hr 45 min",
        "servings": "Serves 4",
        "image": "recipes/fresh-pasta.jpg",
        "intro": (
            "Two ingredients, one rolling pin, and a threshold of patience you didn't know you had. "
            "This is the dough we roll every morning for the service tagliatelle — it has exactly two "
            "ingredients because two is all it needs. The whole trick is in the resting and the final, "
            "thin roll. Everything else is commentary."
        ),
        "equipment": [
            "Large wooden board or clean marble surface",
            "Rolling pin (a wine bottle works, honestly)",
            "Bench scraper",
            "Semolina or fine cornmeal for dusting",
        ],
        "ingredients": [
            {
                "group": "The dough",
                "items": [
                    "400 g '00' Italian flour (or 320 g all-purpose + 80 g semolina)",
                    "4 large eggs (pastured, if you can — the colour is the reward)",
                    "A pinch of fine sea salt",
                ],
            },
            {
                "group": "For rolling and cooking",
                "items": [
                    "Semolina, for dusting",
                    "A generous handful of coarse salt, for the water",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "The well", "duration": "5 min", "text": "Mound the flour on your board and dig a wide crater in the middle, like a volcano with conservative ambitions. Crack the eggs into the crater and add the salt."},
            {"n": 2, "title": "The scramble", "duration": "3 min", "text": "Beat the eggs with a fork, staying inside the crater. When they're uniformly yellow, start flicking flour from the inner walls into the eggs — a little at a time, so the lava never breaches the volcano."},
            {"n": 3, "title": "The shaggy mass", "duration": "5 min", "text": "When the fork gives up, flour your hands and bring everything together into a rough, shaggy, unattractive ball. It will look wrong. It is not wrong. Scrape the board clean with the bench scraper as you go."},
            {"n": 4, "title": "The knead", "duration": "10 min", "text": "Knead with the heel of your hand: push, quarter-turn, fold, repeat. The dough transforms from shaggy to smooth at around minute eight. Keep going until it feels like your earlobe — the classic Italian test, and it is exactly right."},
            {"n": 5, "title": "The rest", "duration": "1 hr", "text": "Wrap tightly in cling film and rest at room temperature for one hour. This relaxes the gluten. Skipping this step is why your last pasta attempt fought back. Do not skip it."},
            {"n": 6, "title": "The roll", "duration": "20 min", "text": "Roll from the centre outward, rotating the sheet a quarter-turn after every pass, until you can see the grain of your board through it — about 1 mm. Dust with semolina whenever it threatens to stick. This takes as long as it takes."},
            {"n": 7, "title": "The nest", "duration": "5 min", "text": "Loosely roll the sheet into a flat cylinder, slice into 7 mm ribbons, then tumble them through your fingers with semolina into loose nests. Rest uncovered for 15 minutes."},
            {"n": 8, "title": "The two minutes", "duration": "2–3 min", "text": "Boil in aggressively salted water. Fresh tagliatelle is done when it floats plus thirty seconds — two to three minutes total. Toss with sauce in the pan, never plate naked. Eat immediately, standing up if necessary."},
        ],
        "tips": [
            "Humidity changes everything: on wet days add flour one tablespoon at a time; on dry days wet your hands instead of adding water.",
            "Antoine's rule: if the dough tears when you stretch a walnut-sized piece thin enough to read through, knead five more minutes.",
            "Nests freeze beautifully on a tray, then bag. Cook from frozen, adding one minute.",
        ],
        "make_ahead": "The dough ball keeps 24 h in the fridge (bring to room temperature before rolling). Rolled nests keep 6 hours at room temp or 2 months frozen.",
        "pairing": "Toss with brown butter, sage and a storm of Parmigiano, and open the Vermentino you chilled 'just in case'.",
    },
    {
        "slug": "sourdough-bread",
        "title": "48-Hour Sourdough",
        "category": "Bread",
        "chef": "sofia-ramos",
        "difficulty": "Advanced",
        "prep": "30 min active",
        "rest": "48 h total",
        "total": "2 days (mostly waiting)",
        "servings": "1 large loaf",
        "image": "recipes/sourdough.jpg",
        "intro": (
            "Our bakery bake, unchanged since 2015. The method is almost entirely waiting: a cold, slow "
            "fermentation over two days that builds a crust like slate and a crumb like a sponge you'd "
            "brag about. Your job is about forty minutes of actual work. The yeast does the rest, and "
            "it does it better than you would."
        ),
        "equipment": [
            "Digital scale (baking is chemistry; guesswork is for soup)",
            "Banneton or bowl lined with a tea towel",
            "Dutch oven, 24 cm+",
            "Bench scraper and a sharp knife or razor",
        ],
        "ingredients": [
            {
                "group": "The levain (build at 8 a.m., day one)",
                "items": [
                    "50 g mature starter",
                    "50 g strong white bread flour",
                    "50 g wholemeal flour",
                    "100 g water at 26 °C",
                ],
            },
            {
                "group": "The dough (that evening)",
                "items": [
                    "450 g strong white bread flour",
                    "50 g wholemeal flour",
                    "375 g water at 24 °C",
                    "10 g fine sea salt",
                    "100 g of the levain (the rest goes back to the jar)",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "Build the levain", "duration": "10 h", "text": "Mix levain ingredients at 8 a.m. and leave somewhere warm. By evening it should be domed, bubbly, and smell like apples and cream. If it smells like nail polish, feed it again and wait."},
            {"n": 2, "title": "Autolyse", "duration": "1 h", "text": "Mix flours and all but 50 g of the water into a shaggy mass. No salt yet. Cover and rest one hour — the flour hydrates and the gluten begins organizing itself without you."},
            {"n": 3, "title": "Add levain & salt", "duration": "10 min", "text": "Squeeze the levain and the salt into the dough with wet hands, along with the reserved 50 g water. Pinch and fold until uniform. It will feel impossibly wet. It is meant to."},
            {"n": 4, "title": "The folds", "duration": "3 hrs", "text": "Every 30 minutes for three hours, grab one edge of the dough, stretch it up, and fold it over the middle. Rotate and repeat four times. Each round the dough gets smoother, stronger, and more obedient."},
            {"n": 5, "title": "Shape & retard", "duration": "5 min + overnight", "text": "Shape into a tight round, tension pulled taut on the surface, and settle seam-up into a floured banneton. Cover and refrigerate 18–24 hours. This cold retard is where all the flavour lives."},
            {"n": 6, "title": "The slash", "duration": "5 min", "text": "Next morning, heat the oven to 250 °C with the Dutch oven inside for 45 minutes. Tip the loaf onto paper, slash one confident 20 cm line at 30°, 1 cm deep. Hesitation shows in the crumb."},
            {"n": 7, "title": "Bake covered", "duration": "20 min", "text": "Lower the loaf into the screaming-hot Dutch oven, lid on, and bake 20 minutes. The lid traps steam — your personal cloud, and the secret to a crust that crackles."},
            {"n": 8, "title": "Bake open & the wait", "duration": "25 min + 1 hr", "text": "Lid off, 220 °C, 20–25 minutes more, until the crust is black-walnut brown and the base sounds hollow when knocked. Then the hardest step: wait one full hour before cutting. The crumb is still finishing. Trust us."},
        ],
        "tips": [
            "Sofia's thermometer rule: the loaf is done at 96 °C in the centre, but 'dark and hollow' gets you 95% of the way.",
            "A splash of water on the oven floor at the start adds steam if your lid doesn't seal well.",
            "Day-three sourdough makes the world's best toast. Day-four makes the world's best breadcrumbs.",
        ],
        "make_ahead": "The whole recipe is make-ahead. The shaped loaf will wait happily in the fridge up to 24 extra hours — bake straight from cold.",
        "pairing": "Still warm, with cultured butter and smoked salt, and a glass of Jura Savagnin if the day allows it.",
    },
    {
        "slug": "beurre-blanc",
        "title": "Classic Beurre Blanc",
        "category": "Sauces",
        "chef": "antoine-dubois",
        "difficulty": "Medium",
        "prep": "5 min",
        "cook": "15 min",
        "total": "20 min",
        "servings": "Makes ~300 ml",
        "image": "recipes/beurre-blanc.jpg",
        "intro": (
            "The sauce that built an empire: shallots, wine, vinegar, and then an almost irresponsible "
            "amount of cold butter, whisked in one cube at a time until the whole thing becomes liquid "
            "silk. It breaks if you look away — which is why we're giving you the exact temperatures. "
            "Master this and you can sauce anything that swims."
        ),
        "equipment": [
            "Heavy-based saucepan, 18 cm",
            "Whisk",
            "Fine sieve",
        ],
        "ingredients": [
            {
                "group": "The reduction",
                "items": [
                    "2 banana shallots, minced very fine",
                    "150 ml dry white wine (drinkable — Pinot Blanc or Muscadet)",
                    "50 ml white wine vinegar",
                    "1 bay leaf, 2 sprigs thyme",
                ],
            },
            {
                "group": "The butter",
                "items": [
                    "250 g cold unsalted butter, cubed (keep it in the fridge until needed)",
                    "Salt and white pepper",
                    "Squeeze of lemon, to finish",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "The reduction", "duration": "10 min", "text": "Simmer shallots, wine, vinegar and aromatics until reduced to about two tablespoons of damp shallot pulp. Watch it like a debt — reducing too far makes it bitter and sad."},
            {"n": 2, "title": "Kill the heat, start the butter", "duration": "1 min", "text": "Take the pan off the flame. Add three cubes of cold butter and whisk hard until they melt completely. The pan's residual heat is doing the work now."},
            {"n": 3, "title": "The rhythm", "duration": "8 min", "text": "Return to the lowest possible flame. Add butter one cube at a time, whisking, adding the next only when the last has vanished. Slow in, fast out. This is not a sauce you can scroll your phone through."},
            {"n": 4, "title": "The emulsion", "duration": "2 min", "text": "Around the 180 g mark, the sauce suddenly thickens, turns opaque, and clings to the whisk. It should coat a spoon and hold a clean channel when you draw a finger through it. That's the moment. Stop adding butter."},
            {"n": 5, "title": "Strain & season", "duration": "2 min", "text": "Sieve out the shallots (decent kitchens argue about this; we strain for silk). Season with salt, white pepper, and the lemon — acid balance is 80% of a beurre blanc."},
            {"n": 6, "title": "Hold it", "duration": "as needed", "text": "Keep it warm — never hot — in a bowl of hand-hot water (40–50 °C). Above 60 °C it splits. Below 35 °C it solidifies. It is a sauce with a temperature window and opinions."},
        ],
        "tips": [
            "If it splits: off the heat, whisk in a tablespoon of cold water or one ice cube. It comes back about 90% of the time. We've all been there.",
            "Antoine's variant for fish: replace a quarter of the butter with brown butter for a deeper, nuttier sauce.",
            "Beurre blanc does not reheat. Make it once, serve it once. Leftovers become the best scrambled eggs of your life.",
        ],
        "make_ahead": "It doesn't, really — that's the point. It holds 30 minutes in a warm bath. For a dinner party, reduce the shallot base in advance and mount the butter while guests find their seats.",
        "pairing": "Spoon it over seared scallops, turbot, or poached eggs. Drink the rest of the wine you opened for the reduction.",
    },
    {
        "slug": "golden-chicken-stock",
        "title": "Golden Chicken Stock",
        "category": "Fundamentals",
        "chef": "elena-marchetti",
        "difficulty": "Easy",
        "prep": "15 min",
        "cook": "4 hrs",
        "total": "4 hrs 30 min (mostly unattended)",
        "servings": "Makes ~2 litres",
        "image": "recipes/chicken-stock.jpg",
        "intro": (
            "The single highest-leverage recipe in this entire library. Every sauce, every risotto, every "
            "soup at Lumière starts from a pot like this one. It costs almost nothing, freezes perfectly, "
            "and will quietly upgrade everything you cook for the rest of your life. Elena makes it every "
            "Monday, and has since cooking school."
        ),
        "equipment": [
            "Large stockpot, 8 L+",
            "Fine sieve or chinois",
            "Storage containers",
        ],
        "ingredients": [
            {
                "group": "The bones & aromatics",
                "items": [
                    "2 kg raw chicken carcasses, wings & necks (roasted: see step 1)",
                    "2 onions, unpeeled, halved",
                    "2 carrots, scrubbed, in thirds",
                    "2 celery sticks, in thirds",
                    "1 head of garlic, halved across the equator",
                ],
            },
            {
                "group": "The quiet extras",
                "items": [
                    "6 black peppercorns",
                    "2 bay leaves",
                    "Small bunch of parsley stalks (save the leaves for something better)",
                    "1 tsp sea salt — only a teaspoon, you can adjust later",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "Roast the bones", "duration": "45 min", "text": "Toss carcasses in a little oil and roast at 220 °C for 45 minutes, until deeply golden. This single step is the difference between stock and liquid chicken. Do not skip, do not rush, do not fear the dark bits."},
            {"n": 2, "title": "Deglaze everything", "duration": "5 min", "text": "Pour a cup of water into the roasting tray, scrape up every browned fragment, and pour it all — bones, scrapings, fat and all — into the pot. Those brown bits are free flavour you already paid for."},
            {"n": 3, "title": "Cold water, always", "duration": "2 min", "text": "Cover the bones with cold water by 5 cm. Hot water traps impurities in the stock; cold draws them out slowly. Chemistry, not folklore."},
            {"n": 4, "title": "The barest simmer", "duration": "4 hrs", "text": "Bring to the faintest simmer — one or two lazy bubbles per second, never a boil — and keep it there for four hours, skimming the grey foam off the top for the first twenty minutes. A boiled stock is a cloudy stock."},
            {"n": 5, "title": "Aromatics, late", "duration": "1 hr", "text": "Add vegetables, garlic and aromatics for the final hour only. Longer than that and the celery goes bitter and the parsley goes grassy. Timing is flavour."},
            {"n": 6, "title": "The strain", "duration": "10 min", "text": "Ladle — don't pour — through a fine sieve into containers. Pressing on the solids is the classic mistake: it clouds the stock instantly. Let gravity do it alone."},
            {"n": 7, "title": "Skim tomorrow", "duration": "overnight", "text": "Cool quickly (an ice bath if you can), refrigerate overnight, and lift off the fat cap in the morning. Keep it — schmaltz is liquid gold for roast potatoes."},
        ],
        "tips": [
            "Elena freezes stock in 500 ml portions and in ice cubes for 'just a splash' moments. A stock cube will never cross this threshold again.",
            "If it gels like jelly in the fridge, congratulations — that's collagen, and you've made it right.",
            "Pressure cooker method: 60 minutes on high does the work of four hours. Weeknight-approved.",
        ],
        "make_ahead": "Keeps 4 days refrigerated, 6 months frozen. Reduce by half and freeze in trays for espresso-cups of pure flavour base.",
        "pairing": "Use it for risotto, pan sauces, soups, and cooking grains. Drink a hot mug of it with salt when the weather turns.",
    },
    {
        "slug": "chocolate-souffle",
        "title": "The Lumière Soufflé",
        "category": "Pastry",
        "chef": "yuki-tanaka",
        "difficulty": "Advanced",
        "prep": "25 min",
        "cook": "19 min",
        "total": "45 min",
        "servings": "Serves 4",
        "image": "recipes/chocolate-souffle.jpg",
        "intro": (
            "The full method for the dessert that requires a 22-minute head start on our menu. Yuki has "
            "kept the timing sheets from every service since 2019 — this recipe is the distilled average "
            "of six hundred perfect soufflés. Your oven will be the wildcard; everything else is on you, "
            "and this page. Rise well."
        ),
        "equipment": [
            "4 × 200 ml ramekins, straight-sided",
            "Stand mixer or electric whisk and a strong wrist",
            "Spatula — a broad, gentle one",
            "Oven thermometer (Yuki insists; ovens lie)",
        ],
        "ingredients": [
            {
                "group": "The base",
                "items": [
                    "140 g Valrhona Guanaja 70% (or any honest 70%), chopped",
                    "120 ml whole milk",
                    "3 egg yolks + 2 whole eggs",
                    "30 g caster sugar",
                    "15 g cornflour",
                    "A pinch of salt",
                ],
            },
            {
                "group": "The meringue & finish",
                "items": [
                    "5 egg whites (from the 3 eggs above, plus 2 more)",
                    "90 g caster sugar, in two additions",
                    "Butter & cocoa, for the ramekins",
                    "Warm salted caramel & good vanilla ice cream, to serve",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "The armour", "duration": "10 min", "text": "Brush ramekins with soft butter in upward strokes — brushstrokes give the soufflé a ladder to climb. Dust with cocoa, tap out the excess. This is not decoration; it is scaffolding."},
            {"n": 2, "title": "The chocolate base", "duration": "8 min", "text": "Warm the milk, pour it over the chopped chocolate, and stir from the centre outward until glossy. Whisk yolks, whole eggs, sugar and cornflour in a bowl, then stream in the chocolate milk and return to low heat, stirring, until it thickens to custard. Cool 10 minutes."},
            {"n": 3, "title": "The French meringue", "duration": "8 min", "text": "Whisk whites with the salt, adding the first 45 g sugar only when they hold soft peaks. Whisk to firm, glossy peaks with the remaining sugar — when the beater leaves a beak that holds but curves, you're there. Under-whipped falls; over-whipped deflates the base. The beak is everything."},
            {"n": 4, "title": "The marriage", "duration": "3 min", "text": "Stir a third of the meringue into the chocolate base to lighten it. Then fold in the rest with a spatula, cutting down the middle, sweeping the bottom, folding over — maybe 20 strokes, no more. It should be homogeneous and you should be calm."},
            {"n": 5, "title": "Fill & level", "duration": "2 min", "text": "Fill ramekins to 5 mm below the rim. Level the surface with a palette knife, then run a thumb around the inside rim — this clean edge is what lets the soufflé rise straight up, crown-like, instead of mushrooming sideways."},
            {"n": 6, "title": "Bake at 190 °C", "duration": "19 min", "text": "Do not open the door. Do not think about opening the door. At 19 minutes the tops will be risen 4 cm, dry on top with a centimetre of visible wobble underneath. That wobble is the molten centre's last defence. Respect it."},
            {"n": 7, "title": "The 90 seconds", "duration": "1.5 min", "text": "Open, serve, open with a spoon in front of your guests, pour caramel or sink a spoonful of ice cream into the cloud. A soufflé waits for no one — everything else should already be on the table."},
        ],
        "tips": [
            "Yuki's rule of the wobble: if the centre doesn't tremble at 19 minutes, your oven runs hot — pull at 17 next time and write it down.",
            "Bases can be made to the end of step 2 and refrigerated up to 2 days. Bring to room temperature before folding in meringue.",
            "Ramekins can be filled and frozen unbaked. Bake from frozen at 180 °C for 26 minutes. Emergency dessert, solved.",
        ],
        "make_ahead": "Base: 2 days refrigerated. Assembled, unbaked: 1 month frozen. Baked: never. Soufflés don't do encores.",
        "pairing": "Tawny port, poured cold, and people you like enough to run plates to the table for.",
    },
    {
        "slug": "croissants",
        "title": "Three-Day Croissants",
        "category": "Pastry",
        "chef": "yuki-tanaka",
        "difficulty": "Advanced",
        "prep": "3 hrs active",
        "rest": "2 overnights",
        "total": "3 days",
        "servings": "12 croissants",
        "image": "recipes/croissants.jpg",
        "intro": (
            "Not a weekend project — a three-day relationship. Day one makes the dough, day two laminates "
            "butter into 27 layers, day three shapes, proofs and bakes. The method is the one our pastry "
            "section uses at 5 a.m., scaled down with zero of the drama. Read all steps before starting. "
            "This is the recipe that earns you a reputation."
        ),
        "equipment": [
            "Stand mixer with dough hook",
            "Rolling pin and a cool work surface",
            "Baking trays and parchment",
            "Pastry brush and a sharp pizza cutter",
            "Patience (the ingredient no one sells)",
        ],
        "ingredients": [
            {
                "group": "Day 1 — the dough (détrempe)",
                "items": [
                    "500 g strong bread flour",
                    "60 g caster sugar",
                    "12 g fine sea salt",
                    "80 g softened unsalted butter",
                    "150 ml cold whole milk",
                    "130 ml cold water",
                    "12 g instant dry yeast",
                ],
            },
            {
                "group": "Day 2 — the butter block",
                "items": [
                    "280 g top-quality butter, 82%+ fat, cold but pliable (European-style — this is not the place to economize)",
                    "Extra flour for dusting",
                ],
            },
            {
                "group": "Day 3 — the finish",
                "items": [
                    "1 egg + pinch of salt, beaten for egg wash",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "Day 1: mix & knead", "duration": "20 min", "text": "Mix all détrempe ingredients 4 minutes on low, then 5 on medium, to a smooth, springy dough — windowpane not required. It should be soft but not sticky."},
            {"n": 2, "title": "Day 1: the cold square", "duration": "overnight", "text": "Roll the dough into a 20 cm square, wrap, and refrigerate overnight. The square shape matters tomorrow; the cold matters now."},
            {"n": 3, "title": "Day 2: the butter sheet", "duration": "10 min", "text": "Beat the cold butter between parchment into a 14 cm square, exactly the consistency of the dough — it should bend without breaking and stay cold. If it melts, everything melts. This is the whole game."},
            {"n": 4, "title": "Day 2: lock it in", "duration": "10 min", "text": "Roll the dough square to 28 cm. Set the butter square diamond-centre on it, fold the four dough points over to enclose it completely — a butter parcel — and press the seams sealed."},
            {"n": 5, "title": "Day 2: the letter turns", "duration": "2 hrs", "text": "Roll the parcel to 45 × 20 cm and fold in thirds like a letter. Rotate 90°, roll and fold again. That's two turns. Rest the dough, wrapped, in the fridge 1 hour between every two turns — four turns total today. Warm butter smears; cold butter layers. Feel the dough, not the clock."},
            {"n": 6, "title": "Day 3: cut the triangles", "duration": "20 min", "text": "Roll the laminated dough to a 40 × 25 cm rectangle, 4 mm thin. Cut two long triangles with 9 cm bases. Stretch each gently, then roll from base to tip, coaxing the point into a crescent with three revolutions. Where the tip ends up decides your reputation."},
            {"n": 7, "title": "Day 3: proof slow", "duration": "2–3 hrs", "text": "Egg wash once, proof at 24 °C until jiggly and visibly inflated — about 2½ hours. Under-proofed croissants leak butter; over-proofed collapse. Jiggle the tray: they should wobble like a set custard. Then egg wash a second time, gently."},
            {"n": 8, "title": "Day 3: bake at 200→180", "duration": "18 min", "text": "Bake at 200 °C for 8 minutes — the oven spring — then reduce to 180 °C for 10 more, until the colour of dark honey. Cool 20 minutes on a rack. The first crack of the crust is the sound of the whole three days."},
        ],
        "tips": [
            "Yuki's thermometer law: butter at 12–14 °C, dough at 12–16 °C, at every turn. A $10 fridge thermometer prevents $40 of ruined butter.",
            "If butter breaks through during rolling, stop, dust with flour, and return everything to the fridge for 20 minutes. The fridge fixes nearly everything in lamination.",
            "Freeze shaped, unproofed croissants solid; proof from frozen overnight in the fridge, then 2 hours at room temperature. Fresh croissants on demand, forever.",
        ],
        "make_ahead": "The dough holds 2 days in the fridge at any pre-shape stage. Baked croissants: same-day only — which is why bakeries sell out.",
        "pairing": "A café au lait, or for the evening crowd, a sweet Tokaji. Croissant crumbs are, technically, a garnish.",
    },
    {
        "slug": "pan-seared-steak",
        "title": "Pan-Seared Ribeye Masterclass",
        "category": "Fire & Pan",
        "chef": "antoine-dubois",
        "difficulty": "Easy",
        "cook": "12 min",
        "rest": "8 min",
        "total": "30 min",
        "servings": "Serves 2",
        "image": "recipes/steak.jpg",
        "intro": (
            "One steak, one pan, zero anxiety. This is the method our chefs use at home, with none of the "
            "restaurant kit — no salamander, no thermopenetry degree, no binchotan. Bring the steak to "
            "temperature slowly, sear it violently, rest it religiously. Follow the timings and you will "
            "pull a medium-rare ribeye with a crust that audibly crackles."
        ),
        "equipment": [
            "Heavy cast-iron or stainless pan — the heaviest you own",
            "Tongs (never a fork — you are not testing it for leaks)",
            "A warm plate and a spoon for basting",
            "Instant-read thermometer, if you want certainty",
        ],
        "ingredients": [
            {
                "group": "The steak",
                "items": [
                    "1 dry-aged ribeye, 3.5–4 cm thick, ~500 g (thinner steaks need faster heat; the timings below assume this thickness)",
                    "Coarse sea salt and freshly cracked pepper",
                ],
            },
            {
                "group": "The baste",
                "items": [
                    "30 g butter",
                    "3 sprigs thyme",
                    "2 garlic cloves, smashed, skin on",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "Dry it — yesterday if you can", "duration": "2–24 h", "text": "Salt the steak generously on all sides and rest it uncovered on a rack in the fridge, ideally overnight. Salt seasons deep; the fridge dries the surface. A dry surface is 50% of the crust. No paper-towel shortcut equals half the crust."},
            {"n": 2, "title": "Temper it", "duration": "60 min", "text": "Take the steak out a full hour before cooking — refrigerator-cold centres make grey bands under beautiful crusts. Room-temperature-ish steak equals even cooking. Meanwhile, set the steak on the counter and preheat nothing yet."},
            {"n": 3, "title": "The empty pan", "duration": "5 min", "text": "Heat the dry, empty pan over medium-high until a drop of water skates across the surface and evaporates in seconds — around 230 °C, past smoking, into serious territory. Then add a neutral, high-smoke-point oil, just a film. Then — only then — the steak."},
            {"n": 4, "title": "First side: don't move it", "duration": "3 min", "text": "Lay the steak away from you and do not touch it for three full minutes. The myth of 'sealing in the juices' is false; the reality of a maillard crust is not. Pressing, flipping early, and poking all ruin the crust. Set a timer. Have faith."},
            {"n": 5, "title": "Flip — once is fine, twice is better", "duration": "3 min", "text": "Flip and leave for another 3 minutes. (Serious home cooks flip every 60 seconds for edge-to-edge evenness — it works, if you can resist fussing.) Pepper now, not before: it burns at crust temperatures."},
            {"n": 6, "title": "The butter bath", "duration": "2 min", "text": "Add butter, thyme and garlic, and when the butter foams, tilt the pan and spoon it over the steak, repeatedly, gloriously, for two minutes. The milk solids brown and glaze the crust. This is the restaurant step and it takes ninety seconds."},
            {"n": 7, "title": "The rest", "duration": "8 min", "text": "Rest the steak on a warm board for eight minutes — half its cooking time. The juices redistribute instead of flooding your board. Cut into it early and you eat a drier steak while watching the good stuff escape. Antoine times the rest longer than the sear. There's a lesson there."},
            {"n": 8, "title": "Slice & season the cut", "duration": "2 min", "text": "Slice against the grain, at 45°, into 1 cm strips. Sprinkle the exposed cut with a final pinch of salt — salt on the cut face is the bite everyone remembers. Serve on a warm plate. Cold plates eat hot steaks."},
        ],
        "tips": [
            "Core temperatures, for the thermometer crowd: 48 °C rare, 52 °C medium-rare, 56 °C medium. Pull it 3° early; it climbs while resting.",
            "A screaming pan that smokes uncontrollably is too hot. Lift the pan off the heat for 20 seconds rather than lowering the steak into a fire.",
            "Save the resting juices plus browned butter: whisk them into a spoon of mustard for the world's quickest pan sauce.",
        ],
        "make_ahead": "The salt-and-dry step IS the make-ahead: up to 24 hours in the fridge. After resting, steak is a 12-minute affair.",
        "pairing": "A big Cabernet or a Northern Rhône Syrah, opened 30 minutes before the pan gets hot.",
    },
    {
        "slug": "everyday-vinaigrette",
        "title": "The Everyday Vinaigrette",
        "category": "Fundamentals",
        "chef": "sofia-ramos",
        "difficulty": "Easy",
        "prep": "10 min",
        "total": "10 min",
        "servings": "Makes ~200 ml",
        "image": "recipes/vinaigrette.jpg",
        "intro": (
            "The most-used recipe in our kitchen — whisked twice daily, tasted forty times a week, argued "
            "about constantly. Three-to-one is where you start, not where you finish. Learn the structure "
            "and you'll never buy bottled dressing again: acid, oil, salt, mustard, and one honest "
            "embellishment. That's the entire curriculum."
        ),
        "equipment": [
            "A jar with a lid (the official vessel)",
            "A teaspoon, for the most important step: tasting",
        ],
        "ingredients": [
            {
                "group": "The permanent structure",
                "items": [
                    "3 tbsp extra-virgin olive oil (a grassy, peppery one)",
                    "1 tbsp good vinegar (red wine to start; the world opens from there)",
                    "1 tsp Dijon mustard — the emulsifier, the diplomat",
                    "Flaky salt & freshly ground pepper",
                ],
            },
            {
                "group": "The seasonal signature (pick one, per season)",
                "items": [
                    "Spring: 1 tsp honey + a scrap of lemon zest",
                    "Summer: 1 crushed garlic clove + 1 tsp basil, shredded",
                    "Autumn: 1 tsp maple + ½ tsp smoked paprika",
                    "Winter: 1 tsp wholegrain mustard + 1 shallot, minced",
                ],
            },
        ],
        "steps": [
            {"n": 1, "title": "Acid first", "duration": "1 min", "text": "Vinegar, mustard, salt and pepper go in the jar first. Salt dissolves in acid, not in oil — order matters more than people think. Shake or whisk these into a smooth paste before anything oily joins."},
            {"n": 2, "title": "The seasonal signature", "duration": "1 min", "text": "Add your embellishment of the season now, so it marinates in the acid. Shallots mellow, garlic mellows, honey dissolves. Give it two minutes; the flavour returns the favour."},
            {"n": 3, "title": "Oil, slowly", "duration": "2 min", "text": "Add the oil a tablespoon at a time, shaking between additions, until it emulsifies into something creamy and unified. Rush this and you get oil with vinegar ideas floating in it."},
            {"n": 4, "title": "Taste on a leaf", "duration": "1 min", "text": "The critical step: dip an actual lettuce leaf, eat it, and adjust. From a spoon, everything tastes too sharp; on a leaf, the truth appears. Acid forward is correct — the salad ingredients will pull it back."},
            {"n": 5, "title": "Dress at the last second", "duration": "30 sec", "text": "Pour the vinaigrette down the sides of the bowl, not onto the leaves, and toss with your hands — the gentlest tools in the kitchen. 30 seconds before serving, never more. Greens wilt on their own schedule."},
        ],
        "tips": [
            "Sofia's ratio ladder: delicate greens 4:1, sturdy greens & veg 3:1, grains and beans 2:1. The salad tells you what it needs.",
            "A jam jar with a tablespoon of leftover jam is a pre-seasoned vinaigrette vessel. Waste nothing.",
            "Split emulsions happen: add a teaspoon of water and shake hard. The mustard usually brings it home.",
        ],
        "make_ahead": "Keeps 5 days in the fridge in its jar. Shake before every use; taste before every service — vinegar fades, garlic grows.",
        "pairing": "Everything green you will eat this week, plus leftover boiled potatoes while they're still warm.",
    },
]


def get_recipe(slug):
    for r in RECIPES:
        if r["slug"] == slug:
            return r
    return None
