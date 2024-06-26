def getBondPrice(y, face, couponRate, m, ppy=1):
    import numpy as np
    n = m * ppy
    coupon = face * couponRate / ppy
    t = np.arange(1, n + 1)
    discount_factors = (1 + y / ppy) ** t
    pv_coupons = coupon / discount_factors
    pv_face = face / discount_factors[-1]
    bond_price = np.sum(pv_coupons) + pv_face
    return bond_price
