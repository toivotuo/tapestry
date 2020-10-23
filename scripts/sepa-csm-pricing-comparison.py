#!/usr/bin/env python
# coding: utf-8

# # STEP2 SCT
#
# Calculating the pricing for the STEP2 SCT service for the STEP2-T platform.
#
# Pricing is calculated for direct participants using bulk processing and not participating in optional services like night time processing cycles. Assumes 50/50 split of SCT sent and received. EBICS connectivity assumed.
#
# Data source: https://www.ebaclearing.eu/services/step2-t-platform/step2-t-pricing/

# In[42]:


def step2_pricing(monthly_volume):
    """Calculate price per payment given monthly volume"""
    quarterly_daily_minimum = 5000
    quarterly_fee_minimum = 3750
    price_per_payment = 0.002

    daily_volume = monthly_volume / 30

    # First 5k payments of each day are included in the 3750 EUR quarterly minimum fee.
    if daily_volume < quarterly_daily_minimum:
        monthly_payment_fees = quarterly_fee_minimum / 3
    else:
        payment_fees = (monthly_volume-(quarterly_daily_minimum*30)) * price_per_payment
        monthly_payment_fees = payment_fees + (quarterly_fee_minimum/3)

    # Joining fees amortised over five years; assuming that EBICS fee is a one-off
    monthly_joining_fee = (30000+5000) / 5 / 12

    # Annual recurring fees per month
    monthly_recurring_fee = (27500+12000) / 12

    return (monthly_payment_fees + monthly_joining_fee + monthly_recurring_fee) / monthly_volume

volumes = [10**3, 10**4, 10**5, 10**6, 10**7]
for monthly_volume in volumes:
    print("{} {}".format(monthly_volume, step2_pricing(monthly_volume)))



# # CENTROlink
#
# Calculating the pricing for SCT service on the CENTROlink CSM.
#
# Assume 50/50 split between sent and received SCT.
#
# Data source: https://www.lb.lt/en/centrolink

# In[41]:


def centrolink_pricing(monthly_volume):
    """Calculate the price per payment given monthly volume"""
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
        sent_cost_high_volume = (monthly_volume/2 - high_volume_threshold/12) * price_per_sent_high_volume
        sent_cost = sent_cost_low_volume + sent_cost_high_volume

    # Received payments cost
    received_cost = monthly_volume_received * price_per_received

    return max(sent_cost + received_cost, 100) / monthly_volume

volumes = [10**3, 10**4, 10**5, 10**6, 10**7]
for monthly_volume in volumes:
    print("{} {}".format(monthly_volume, centrolink_pricing(monthly_volume)))


# # SEPA-Clearer
#
# Calculating pricing for the Deutsche Bank SEPA-Clearer.
#
# Assumption is made here that 100% of the payments are sent to other CSMs. This is a conservative assumption and in practice the price would be less.
#
# Data source: https://www.bundesbank.de/en/tasks/payment-systems/rps/sepa-clearer/fees-and-operating-hours

# In[45]:


def sepaclearer_pricing(monthly_volume):
    """Calculate the price per payment given monthly volume"""
    price_per_sent = 0.0025 + 0.0025
    price_per_received = 0

    sent_cost = monthly_volume / 2 * price_per_sent
    received_cost = monthly_volume / 2 * price_per_received

    return (sent_cost + received_cost) / monthly_volume

volumes = [10**3, 10**4, 10**5, 10**6, 10**7]
for monthly_volume in volumes:
    print("{} {}".format(monthly_volume, sepaclearer_pricing(monthly_volume)))
