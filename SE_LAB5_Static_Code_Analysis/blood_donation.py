
"""Blood donation register and blood stock management demo."""

import os
import tempfile
from datetime import date, timedelta

OFFICER_PASSWORD = os.environ.get("BLOOD_BANK_OFFICER_PASSWORD")

DONORS = []
STOCK = {
    "A+": 0, "A-": 0,
    "B+": 0, "B-": 0,
    "O+": 0, "O-": 0,
    "AB+": 0, "AB-": 0,
}

COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "A-": ["A-", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "B-": ["B-", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(STOCK),
    "AB-": ["AB-", "A-", "B-", "O-"],
}


def register_donor(donor_name, blood_group, age, last_donation=None,
                   notes=None):
    """Register an eligible donor and record any age-related rejection."""
    if notes is None:
        notes = []

    if blood_group not in STOCK:
        raise ValueError("Unknown blood group")

    if age < 18 or age > 65:
        notes.append(
            f"{donor_name} is not eligible because of age"
        )
        return False

    DONORS.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def can_donate(donor):
    """Return whether a donor meets the 90-day donation interval."""
    if donor["last"] is None:
        return True

    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation if the named donor is eligible."""
    for donor in DONORS:
        if donor["name"] == donor_name and can_donate(donor):
            STOCK[donor["group"]] += units
            donor["last"] = date.today()
            return True

    return False


def units_for(patient_group):
    """Return available units compatible with the patient's blood group."""
    if patient_group not in COMPATIBLE:
        return 0

    return sum(STOCK[group] for group in COMPATIBLE[patient_group])


def is_universal(blood_group):
    """Check whether the group is universal donor or recipient blood."""
    return blood_group in {"O-", "AB+"}


def low_stock(threshold=2):
    """Return blood groups whose stock is below the given threshold."""
    return [
        group for group, units in STOCK.items()
        if units < threshold
    ]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".csv", delete=False
    ) as temp_file:
        return temp_file.name


def notify_donors(phone_list):
    """Validate phone numbers for a future notification service."""
    if not all(
        isinstance(phone, str) and phone.strip()
        for phone in phone_list
    ):
        raise ValueError("Phone numbers must be non-empty strings")

    return list(phone_list)


def main():
    """Run the blood donation demonstration."""
    register_donor("Arjun", "O+", 25)
    register_donor(
        "Priya", "A+", 30,
        date.today() - timedelta(days=30),
    )
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)

    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")

    print("Stock:", STOCK)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())  # Below 2 units

    eligible = [
        donor["name"] for donor in DONORS
        if can_donate(donor)
    ]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
