#!/usr/bin/env python
# coding: utf-8

# Compares the pricing at different monthly payment transaction
# volumes of three SEPA CSMs for the processing of SEPA Credit
# Transfer (SCT) payments. The three CSMs compared are STEP2-T (EBA
# CLEARING, CENTROlink (Bank of Lithuania) and SEPA-Clearer (Deutsche
# Bundesbank). Produces a data file that can be plotted to explore the
# costs between the CSMs at different volumes.

# The comparison is based on public data and may not reflect all the
# fees charged by each of the CSMs. A number of assumptions have been
# made for the characteristics of the payment volume. Also, the
# assumption is that none optional services are used and no cost
# optimisations available at some of the CSMs is used. Furthermore, it
# is assumed that a given monthly volume can be extrapolated as is to
# an annual volume. Any initial fixed fees for joining a CSM are
# amortised over a five year period in monthly increments.


def step2_pricing(monthly_volume):
    """
    Calculate a STEP2-T SCT per payment price given a monthly volume
    of payments.

    Pricing is calculated for direct participants using bulk
    processing and not participating in optional services like night
    time processing cycles. Assumes 50/50 split of SCT sent and
    received. EBICS connectivity assumed.

    Data source:
    https://www.ebaclearing.eu/services/step2-t-platform/step2-t-pricing/
    """
    quarterly_daily_minimum = 5000.00
    quarterly_fee_minimum = 3750.00
    price_per_payment = 0.002

    daily_volume = monthly_volume / 30

    # First 5k payments of each day are included in the 3750 EUR quarterly minimum fee.
    if daily_volume < quarterly_daily_minimum:
        monthly_payment_fees = quarterly_fee_minimum / 3
    else:
        payment_fees = (monthly_volume-(quarterly_daily_minimum*30)) * price_per_payment
        monthly_payment_fees = payment_fees + (quarterly_fee_minimum/3)

    # Joining fees amortised over five years; assuming that EBICS fee is a one-off
    monthly_joining_fee = (30000.00 + 5000.00) / 5 / 12

    # Annual recurring fees per month (annual fee, settlement fee and
    # relationship fee)
    monthly_recurring_fee = (27500.00 + 12000.00 + 1000.00) / 12

    return (monthly_payment_fees + monthly_joining_fee + monthly_recurring_fee) / monthly_volume


def centrolink_pricing(monthly_volume):
    """
    Calculate a CENTROlink SCT per payment price given a monthly
    volume of payments.

    Assume 50/50 split between sent and received SCT.

    Data source: https://www.lb.lt/en/centrolink
    """
    price_per_sent_low_volume = 0.03
    price_per_sent_high_volume = 0.01
    price_per_received = 0.01
    high_volume_threshold = 10**6  # one million payments per annum
    high_volume_threshold_monthly = high_volume_threshold / 12

    monthly_volume_sent = monthly_volume / 2
    monthly_volume_received = monthly_volume / 2
    daily_volume = monthly_volume / 30
    annual_volume = monthly_volume * 12

    # Sent payments cost
    if monthly_volume_sent < high_volume_threshold_monthly:
        sent_cost = monthly_volume_sent * price_per_sent_low_volume
    else:
        sent_cost_low_volume = high_volume_threshold/12 * price_per_sent_low_volume
        sent_cost_high_volume = (monthly_volume_sent - high_volume_threshold/12) * price_per_sent_high_volume
        sent_cost = sent_cost_low_volume + sent_cost_high_volume

    # Received payments cost
    received_cost = monthly_volume_received * price_per_received

    return max(sent_cost + received_cost, 100.00) / monthly_volume


def sepaclearer_pricing(monthly_volume):
    """
    Calculate a SEPA-Clearer SCT per payment price given a monthly
    volume of payments.

    Assumption is made here that 100% of the payments are sent to
    other CSMs. This is a conservative assumption and in practice the
    price would be less.

    Data source:
    https://www.bundesbank.de/en/tasks/payment-systems/rps/sepa-clearer/fees-and-operating-hours
    """
    price_per_sent = 0.0025 + 0.0025
    price_per_received = 0

    sent_cost = monthly_volume / 2 * price_per_sent
    received_cost = monthly_volume / 2 * price_per_received

    # Fixed fees payable to STEP2 (300.00 EUR initial fee and 250.00
    # EUR per annum)

    fixed_fees = 300 / 12 / 5 + 250 / 12

    return (sent_cost + received_cost + fixed_fees) / monthly_volume


if __name__ == "__main__":

    monthly_volumes = [10**5, 10**6, 10**7]
    pricing_functions = [
        step2_pricing,
        centrolink_pricing,
        sepaclearer_pricing,
    ]

    start = 10 ** 3
    end = 10 ** 8
    increment = 1000


    volume = start
    while volume <= end:
        prices = [func(volume)*100 for func in pricing_functions]
        print("{} {} {} {}".format(volume, *prices))
        volume += increment
