#!/usr/bin/env python3
"""Rank platforms from structured research results using the weighted rubric.

Usage:
  rank_platforms.py results.json [--out ranking.md] [--json ranking.json]
                    [--weights feature_breadth=0.3,adoption=0.3,...]

results.json: list of objects with at least `id`, `name`, `scores` (dict of
0-10 values). Extra fields (platform_types, company_founded, pricing_summary)
are carried into the table when present.
"""
import argparse
import json
import sys

DEFAULT_WEIGHTS = {
    "feature_breadth": 0.30,
    "adoption": 0.30,
    "advanced_features": 0.20,
    "ux_mobile": 0.10,
    "interoperability": 0.10,
}


def parse_weights(raw):
    if not raw:
        return dict(DEFAULT_WEIGHTS)
    weights = {}
    for part in raw.split(","):
        key, value = part.split("=")
        weights[key.strip()] = float(value)
    total = sum(weights.values())
    if abs(total - 1.0) > 1e-6:
        sys.exit(f"weights must sum to 1.0 (got {total})")
    return weights


def weighted(scores, weights):
    return round(sum(float(scores.get(k, 0)) * w for k, w in weights.items()), 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results")
    ap.add_argument("--out", default="ranking.md")
    ap.add_argument("--json", default="ranking.json")
    ap.add_argument("--weights")
    args = ap.parse_args()

    weights = parse_weights(args.weights)
    items = json.load(open(args.results, encoding="utf-8"))
    for item in items:
        item["weighted_score"] = weighted(item.get("scores", {}), weights)
    items.sort(
        key=lambda i: (
            -i["weighted_score"],
            -float(i.get("scores", {}).get("adoption", 0)),
            -float(i.get("scores", {}).get("advanced_features", 0)),
        )
    )
    for rank, item in enumerate(items, 1):
        item["rank"] = rank

    dims = list(weights)
    header = "| Rank | Platform | " + " | ".join(dims) + " | Weighted |"
    sep = "|" + "---|" * (len(dims) + 3)
    rows = [header, sep]
    for item in items:
        s = item.get("scores", {})
        rows.append(
            f"| {item['rank']} | {item['name']} | "
            + " | ".join(str(s.get(d, "-")) for d in dims)
            + f" | {item['weighted_score']} |"
        )
    open(args.out, "w", encoding="utf-8").write("\n".join(rows) + "\n")
    json.dump(items, open(args.json, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Ranked {len(items)} items -> {args.out}, {args.json}")


if __name__ == "__main__":
    main()
