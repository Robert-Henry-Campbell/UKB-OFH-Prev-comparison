import pandas as pd
from prevalence.merge import merge_prevalence

OFH = "ofh_prevalence_summary_23.06.25.csv"
UKB = "prevalence_summary_UKB_disease_less_EHR_fixed_labeled.csv"
MAP = "ofh_to_ukb_matches_12.6.25_final.csv"


def test_anaemia_mapping():
    df = merge_prevalence(OFH, UKB, MAP)
    row = df[df["ofh_condition"] == "Blood disorders (Anaemia)"].iloc[0]
    assert abs(row["prevalence_OFH"] - 0.07364402577505777) < 1e-6
    assert abs(row["prevalence_UKB"] - 0.001804321) < 1e-6


def test_angina_mapping():
    df = merge_prevalence(OFH, UKB, MAP)
    row = df[df["ofh_condition"] == "Chest Pain (Angina)"].iloc[0]
    assert abs(row["prevalence_OFH"] - 0.07711233408870184) < 1e-6
    assert abs(row["prevalence_UKB"] - 0.0320834528247777) < 1e-6
