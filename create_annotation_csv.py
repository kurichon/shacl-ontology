import csv

# annotations = {subject: {property: value, ...}, ...}

# --- Variant A: full table (Entity, Property, Value) -------------
with open("annotations.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Entity", "Property", "Value"])  # header row

    for subj, props in annotations.items():
        for prop, val in props.items():
            writer.writerow([str(subj), str(prop), str(val)])

print("annotations.csv written.")
