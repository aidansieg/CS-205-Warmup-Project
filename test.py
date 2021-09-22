test1 = "president barack-obama party"
test2 = "president barack-obama year"
test3 = "president name barack-obama"
test4 = "president barack-obama vp"
test5 = "president number 12"
test6 = "president year 1923"
test7 = "office number 36"
test8 = "office year 1919"
test9 = "president barack-obama number"

t = test9.split(" ")

query_peram = {}

if (t[0] == "president"):
    query_peram["table"] = "presidents"
    query_peram["clause"] = t[1]

if (t[0] == "vice-president"):
    query_peram["table"] = "vice-presidents"
    query_peram["clause"] = t[1]

if (t[0] == "office"):
    query_peram["table"] = "Both"
    
    if (t[1] == "year"):
        query_peram["clause"] = int(t[2])
        query_peram["column"] = "All"
    
    if (t[1] == "number"):
        query_peram["clause"] = t[2]
        query_peram["column"] = "All"

if (t[1] == "year" and t[0] != "office"):
    query_peram["column"] = "year"
    query_peram["clause"] = int(t[2])

if (t[2] == "year"):
    query_peram["column"] = "year"
    query_peram["clause"] = t[1]

if (t[1] == "name"):
    query_peram["column"] = "All"
    query_peram["clause"] = t[2]

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

if (t[1] == "number" and t[0] != "office"):
    query_peram["column"] = "number"
    query_peram["clause"] = t[2]

if (t[2] == "number"):
    query_peram["column"] = "number"
    query_peram["clause"] = t[1]

print(query_peram)
