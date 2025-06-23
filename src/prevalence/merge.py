import csv
from typing import List, Dict, Tuple, Optional


Row = Dict[str, Optional[str]]


def load_ofh_prevalence(path: str) -> List[Row]:
    """Load OFH prevalence file."""
    rows: List[Row] = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "ofh_condition": r.get("answer", ""),
                "prevalence_OFH": float(r.get("prevalence", "0") or 0),
            })
    return rows


def load_ukb_prevalence(path: str) -> Dict[Tuple[str, str], float]:
    """Load UKB prevalence file keyed by (ukb_code, ukb_category)."""
    data: Dict[Tuple[str, str], float] = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            code = r.get("variable", "")
            category = r.get("category", "")
            prevalence = float(r.get("prevalence", "0") or 0)
            data[(code, category)] = prevalence
    return data


def load_mapping(path: str) -> List[Row]:
    """Load mapping from OFH conditions to UKB conditions."""
    rows: List[Row] = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        for r in reader:
            ofh_cond = r[2]
            ukb_code = r[4]
            ukb_cat = r[6]
            if not ukb_code or ukb_code.lower() == "none in self report":
                continue
            rows.append({
                "ofh_condition": ofh_cond,
                "ukb_code": ukb_code,
                "ukb_category": ukb_cat,
            })
    return rows


def merge_prevalence(ofh_path: str, ukb_path: str, mapping_path: str) -> List[Row]:
    """Merge OFH and UKB prevalence information into a list of rows."""
    ofh_data = {row["ofh_condition"]: row["prevalence_OFH"] for row in load_ofh_prevalence(ofh_path)}
    ukb_data = load_ukb_prevalence(ukb_path)
    mapping_rows = load_mapping(mapping_path)

    merged: List[Row] = []
    for m in mapping_rows:
        ofh_cond = m["ofh_condition"]
        ukb_key = (m["ukb_code"], m["ukb_category"])
        merged.append({
            "ofh_condition": ofh_cond,
            "ukb_code": m["ukb_code"],
            "ukb_category": m["ukb_category"],
            "prevalence_OFH": ofh_data.get(ofh_cond),
            "prevalence_UKB": ukb_data.get(ukb_key),
        })
    return merged
