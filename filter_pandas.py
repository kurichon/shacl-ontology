import pandas as pd

df = pd.read_csv("your file")

# Your “keep” dictionary
Property_required = {
    "Electrical": {"Resistance", "Capacitance"},
    "Thermal":    {"MaxRating"},
}

# ------------------------------------------------------------------
# OPTION A – super‑simple mask (fine for small/medium data)
# ------------------------------------------------------------------
mask = df.apply(
    lambda r: r["Category"] in Property_required
              and r["SubProperty"] in Property_required[r["Category"]],
    axis=1,
)

filtered = df[mask].copy()

# ------------------------------------------------------------------
# OPTION B – fully vectorised (faster on big tables)
# ------------------------------------------------------------------
lookup = (
    pd.Series(Property_required)     # Category  →  list‑of‑props
      .explode()                    # Category  →  one prop per row
      .reset_index()                # columns:  index, 0
      .rename(columns={"index": "Category", 0: "SubProperty"})
      #  Category   SubProperty
      #0 Electrical Resistance
      #1 Electrical Capacitance
      #2 Thermal    MaxRating
)

filtered = df.merge(lookup, on=["Category", "SubProperty"])