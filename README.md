# Ne Pişirsem 🍳 (*"What Should I Cook"*)

A recipe recommendation API that suggests dishes based on the ingredients you have on hand — built with Turkish home cooking in mind, and designed to scale toward a full Turkish & world cuisine recipe library.

## The idea

In my family, "ne pişirsem?" (*what should I cook?*) is a question my mother, grandmother, and aunts ask almost every day. This project started as a way to solve that real, everyday problem: tell the app what ingredients you have, and it suggests dishes you can actually make — even if you're missing a couple of items.

## What it does

- **Ingredient-based recipe matching** — enter the ingredients you have, get ranked recipe suggestions
- **Partial-match support** — recipes aren't filtered out just because you're missing one or two ingredients; the API tells you what's missing
- **Structured recipe data** — each recipe includes cooking instructions, prep time, cuisine type, and category (dish / dessert)
- Built as a REST API from the ground up, so it can serve a web frontend, a mobile app, or both

## Tech stack

- **Backend:** Python, FastAPI
- **Database:** Microsoft SQL Server
- **Data validation:** Pydantic
- **Planned:** Flutter mobile app, Azure Computer Vision (photo-based ingredient input), Azure deployment

## How the matching works

The core logic lives in `app/services/matching_service.py`. For every recipe, it counts how many of its *required* ingredients the user already has:

- **Full matches** (all required ingredients present) are ranked first
- **Partial matches** (up to 2 missing required ingredients) are still suggested, with the missing ones listed
- **Optional ingredients** (e.g. garnish, a squeeze of lemon) don't count against a recipe — missing them never excludes a match

This is handled with a SQL query using conditional aggregation (`COUNT` + `CASE WHEN`) rather than pulling all data into Python and filtering — keeping the matching logic close to the database.

## Project structure

```
app/
├── main.py                    # FastAPI entry point, wires up routers
├── database/
│   └── connection.py          # SQL Server connection, reads config from .env
├── schemas/
│   └── recipe_schemas.py      # Pydantic models — defines API request/response shape
├── routers/
│   ├── ingredients.py         # Ingredient-related endpoints
│   └── recipes.py             # Recipe suggestion & detail endpoints
└── services/
    └── matching_service.py    # Core matching logic (SQL query + ranking)
```

### Database schema

Three tables, with a classic many-to-many relationship between recipes and ingredients:

- `ingredients` — id, name
- `recipes` — id, name, cuisine_type, category, instructions, tips, prep_time_minutes
- `recipe_ingredients` — bridge table (recipe_id, ingredient_id, quantity, is_optional)

## Running it locally

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# then fill in your SQL Server connection details in .env

# Start the server
uvicorn app.main:app --reload
```

Once running, visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI to test endpoints directly in the browser.

## Example request

```json
POST /recipes/suggest
{
  "ingredient_names": ["tomato", "onion", "egg"]
}
```

Returns ranked recipe matches, e.g.:

```json
{
  "recipe_id": 1,
  "name": "Menemen",
  "cuisine_type": "Turkish",
  "category": "dish",
  "matched_ingredient_count": 3,
  "total_ingredient_count": 3,
  "missing_ingredients": []
}
```

## Roadmap

- [x] Project scaffolding (FastAPI + SQL Server)
- [x] Ingredient-based matching (full & partial)
- [x] Recipe database with Turkish & international dishes
- [ ] Cooking tips and user comments per recipe
- [ ] User-submitted recipe variations
- [ ] Flutter mobile app
- [ ] Photo-based ingredient recognition (Azure Computer Vision)
- [ ] Deployment on Azure

## Status

Actively in development — backend and matching logic are functional and tested against a live SQL Server database. Mobile interface and deployment are next.

---

*This project is part of my learning path toward a career in cloud engineering. I'm using it to practice API design, SQL, and (soon) Azure deployment.*
