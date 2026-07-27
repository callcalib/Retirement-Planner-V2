def pension_tax(country, pension):

    if country in [
        "Georgia (Batumi)",
        "Philippines (Baguio)",
        "Thailand",
        "Albania",
        "North Macedonia (Ohrid)"
    ]:
        return 0


    if country == "Cyprus (Mountain)":

        allowance = 19500

        taxable = max(0, pension - allowance)

        return taxable * 0.05


    return pension * 0.20
