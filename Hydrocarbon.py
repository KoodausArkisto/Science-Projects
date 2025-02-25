# This code automatically balances chemical equation on hydrocarbons burning with oxygen

def balance_combustion(x):
    # Lets calculate the amount of hydrogen
    y = 2 * x + 2

    # Lets calculate the stoiciometric
    co2_stoic = x  # Carbon dioxide stoichiometric coefficent
    h2o_stoic = y // 2  # Water stoichiometric coefficent
    o2_stoic = (co2_stoic + h2o_stoic / 2)  # Oxygen stoichiometric coefficent

    # Lets correct the fractions of oxygen
    if o2_stoic % 1 != 0:  # If oxygen is fraction
        co2_stoic *= 2
        h20_stoic *= 2
        o2_stoic *= 2

    return co2_stoic, h2o_stoic, o2_stoic


def main():
    # User inputs
    x = int(input("Enter the amount of coal (C):"))

    # Lets balance reaction
    co2, h20, o2 = balance_combustion(x)

    # Lets add the outputs of the hydrocarbon
    hydroc_stoic = 1 if x == 1 else x  # This adds the coefficent number
    print(
        f"Reaction:  C{hydroc_stoic}H{2*x + 2} + {int(o2)} O2 -> {co2} CO2 + {h20} H20")


if __name__ == "__main__":
    main()
