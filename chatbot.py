import json

# Load buyer data
with open("buyers.json") as f:
    buyers = json.load(f)

# Build a lookup by name or phone
buyer_lookup = {}
for buyer in buyers:
    key = buyer["name"].lower()
    buyer_lookup[key] = buyer
    buyer_lookup[buyer["phone"]] = buyer

def get_buyer_by_identifier(identifier):
    id_lower = identifier.strip().lower()
    return buyer_lookup.get(id_lower)

def answer_query(buyer, query):
    prefs = buyer["preferences"]
    query = query.lower()

    if "location" in query or "area" in query:
        return f"{buyer['name']} is interested in locations like {', '.join(prefs['locations'])}." if prefs["locations"] else "No specific locations provided."

    elif "property" in query or "type" in query:
        return f"{buyer['name']} is looking for {prefs['property_type']}."

    elif "budget" in query:
        return f"{buyer['name']}'s budget is {prefs['budget']}."

    elif "purpose" in query:
        return f"{buyer['name']} is looking for property mainly for {prefs['purpose']}."

    elif "comment" in query or "extra" in query or "details" in query:
        return f"Comments: {prefs['comments']}"

    else:
        return "Sorry, I didn’t understand that question. Try asking about budget, location, or property type."
