test_usr = input("Search: ")
t = test_usr.split(" ")

query_peram = {}

if (t[0] == "president"):
    query_peram["table"] = "presidents"
    query_peram["clause"] = t[0]

if (t[0] == "vice-president"):
    query_peram["table"] = "vice-presidents"
    query_peram["clause"] = t[1]

if (t[0] == "office"):
    query_peram["table"]

if (t[1] == "year"):
    query_peram["column"] = "year"
    query_peram["clause"] = t[2]

# talk to group about formatting search this way 
if (t[1] == "name"):
    query_peram["column"] = "name"
    query_peram["clause"] = t[1]

if (t[2] == "party"):
    query_peram["column"] = "party"
    query_peram["clause"] = t[1]

if (t[2] == "vp"):
    query_peram["table"] = "Both"
    query_peram["column"] = "vp for clause"
    query_peram["clause"] = t[1]

if (t[2] == "p"):
    query_peram["table"] = "Both"
    query_peram["column"] = "p for clause"
    query_peram["clause"] = t[1]

# talk to group about formatting search this way
if (t[1] == "number"):
    query_peram["column"] = "number"
    query_peram["clause"] = t[2]

print(query_peram)
