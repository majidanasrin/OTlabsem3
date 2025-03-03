import math

def calculate_eoq(demand, ordering_cost, holding_cost):
    
  
    eoq = math.sqrt((2 * demand * ordering_cost) / holding_cost)
    return eoq

demand = float(input("Enter the annual demand (units): "))
ordering_cost = float(input("Enter the ordering cost per order: "))
holding_cost = float(input("Enter the holding cost per unit per year: "))


eoq = calculate_eoq(demand, ordering_cost, holding_cost)


print(f"The Economic Order Quantity (EOQ) is: {eoq:.2f} units")
