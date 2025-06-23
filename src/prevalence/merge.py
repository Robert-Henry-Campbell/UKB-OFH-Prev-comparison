import pandas as pd


def load_ofh_prevalence(path: str) -> pd.DataFrame:
    """Load OFH prevalence file."""
    df = pd.read_csv(path)
    df = df.rename(columns={"answer": "ofh_condition", "prevalence": "prevalence_OFH"})
    return df[["ofh_condition", "prevalence_OFH"]]


def load_ukb_prevalence(path: str) -> pd.DataFrame:
    """Load UKB prevalence file."""
    df = pd.read_csv(path)
    df = df.rename(
        columns={"variable": "ukb_code", "category": "ukb_category", "prevalence": "prevalence_UKB"}
    )
    return df[["ukb_code", "ukb_category", "prevalence_UKB"]]


def load_mapping(path: str) -> pd.DataFrame:
    """Load mapping from OFH conditions to UKB conditions."""
    df = pd.read_csv(path, usecols=[2, 4, 6], header=0)
    df.columns = ["ofh_condition", "ukb_code", "ukb_category"]
    df = df[df["ukb_code"].notna()]
    df = df[df["ukb_code"].str.lower() != "none in self report"]
    return df


def merge_prevalence(ofh_path: str, ukb_path: str, mapping_path: str) -> pd.DataFrame:
    """Merge OFH and UKB prevalence information."""
    ofh_df = load_ofh_prevalence(ofh_path)
    ukb_df = load_ukb_prevalence(ukb_path)
    mapping_df = load_mapping(mapping_path)

    merged = mapping_df.merge(ofh_df, on="ofh_condition", how="left")
    merged = merged.merge(ukb_df, on=["ukb_code", "ukb_category"], how="left")
    return merged
