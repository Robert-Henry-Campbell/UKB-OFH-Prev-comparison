import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from prevalence.merge import merge_prevalence

OFH = "ofh_prevalence_summary_23.06.25.csv"
UKB = "prevalence_summary_UKB_disease_less_EHR_fixed_labeled.csv"
MAP = "ofh_to_ukb_matches_12.6.25_final.csv"


def get_row(data, condition):
    for row in data:
        if row["ofh_condition"] == condition:
            return row
    raise AssertionError(f"condition {condition} not found")


def test_anaemia_mapping():
    data = merge_prevalence(OFH, UKB, MAP)
    row = get_row(data, "Blood disorders (Anaemia)")
    assert abs(row["prevalence_OFH"] - 0.07364402577505777) < 1e-6
    assert abs(row["prevalence_UKB"] - 0.001804321) < 1e-6


def test_angina_mapping():
    data = merge_prevalence(OFH, UKB, MAP)
    row = get_row(data, "Chest Pain (Angina)")
    assert abs(row["prevalence_OFH"] - 0.07711233408870184) < 1e-6
    assert abs(row["prevalence_UKB"] - 0.0320834528247777) < 1e-6
