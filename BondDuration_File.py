def getBondDuration(y, face, couponRate, m, ppy=1):
    import numpy as np
    n = m * ppy
    coupon = face * couponRate / ppy
    t = np.arange(1, n + 1)
    
    discount_factors = (1 + y / ppy) ** t
    pv_coupons = coupon / discount_factors
    pv_face = face / discount_factors[-1]
    
    cash_flows = np.full(t.shape, coupon)
    cash_flows[-1] += face
    
    pv_cash_flows = cash_flows / discount_factors
    pv_total = np.sum(pv_cash_flows)
    
    weights = pv_cash_flows / pv_total
    duration = np.sum(weights * t)
    
    return duration
