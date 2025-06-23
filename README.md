# UKB-OFH Prevalence Comparison

This repository compares the prevalence of diseases between the
Oxford Family Health (OFH) study and the UK Biobank (UKB).

Data files (`*.csv`) are provided in the repository:

- `ofh_prevalence_summary_23.06.25.csv` – prevalence counts for OFH
- `prevalence_summary_UKB_disease_less_EHR_fixed_labeled.csv` – prevalence counts for UKB
- `ofh_to_ukb_matches_12.6.25_final.csv` – mapping of OFH conditions to UKB codes

## Repository Structure

```
src/
  prevalence/
    __init__.py
    merge.py      # merging logic

tests/
  test_merge.py   # ground truth checks
```

## Usage

The main helper function is `merge_prevalence` in `src/prevalence/merge.py`:

```python
from prevalence.merge import merge_prevalence

merged = merge_prevalence(
    "ofh_prevalence_summary_23.06.25.csv",
    "prevalence_summary_UKB_disease_less_EHR_fixed_labeled.csv",
    "ofh_to_ukb_matches_12.6.25_final.csv",
)
```

`merged` is a pandas `DataFrame` containing the OFH prevalence alongside the
prevalence of mapped UKB diseases.

Run tests with:

```bash
python -m pip install -r requirements.txt
pytest
```

`pandas` is required for the scripts and the tests.
