#!/usr/bin/env python3

def daily_sales_total(*all_sales):
    total = 0.0
    for each_sale in all_sales:
        total += float(each_sale)
    return total
# сколько угодно элементов кортежа all_sales

if __name__=='__main__':
    result = daily_sales_total(12.889, 33.65, 12.5,'90','77')
    print(result)
