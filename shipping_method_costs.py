# Variables
weight = float(input("Enter package weight: "))
ground_flat_charge = 20
premium_flat_charge = 125

# Ground Shipping
if weight <= 2:
  ground_cost = weight * 1.5 + ground_flat_charge
elif weight > 2 and weight <= 6:
  ground_cost = weight * 3 + ground_flat_charge
elif weight > 6 and weight <= 10:
  ground_cost = weight * 4 + ground_flat_charge
else:
  ground_cost = weight * 4.75 + ground_flat_charge

# Ground Shipping Premium
premium_cost = premium_flat_charge

# Drone Shipping
if weight <= 2:
  drone_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25

drone_vs_ground_cost = ground_cost - drone_cost
ground_vs_drone_cost = drone_cost - ground_cost
premium_vs_ground_cost = ground_cost - premium_cost

# Output
# print(f"""Package weight: {weight}

# Ground Shipping: {ground_cost}

# Ground Shipping Premium: {premium_cost}

# Drone Shipping: {drone_cost}
# """)

print(f"Package weight: {weight}\n")

if weight < 3.4:
  print("We recommend using Drone Shipping\n")
  print(f"Your total cost for shipment will be: {drone_cost}\n")
  print(f"You saved: {drone_vs_ground_cost} over Ground Shipping")
elif weight >= 3.4 and weight < 22.2:
  print("We recommend using Ground Shipping\n")
  print(f"Your total cost for shipment will be: {ground_cost}\n")
  print(f"You saved: {ground_vs_drone_cost} over Drone Shipping")
else:
  print("We recommend using Ground Shipping Premium\n")
  print(f"Your total cost for shipment will be: {premium_cost}\n")
  print(f"You saved: {premium_vs_ground_cost} over Ground Shipping")

# Findings
# As long as prices don't change, if weight less than 3.4, use Drone Shipping
# If weight is greater than or equal to 3.4 and less than 22.2, use Ground Shipping
# If weight is greater than or equal to 22.2, use Ground Shipping Premium
# Eventually find a method to automatically find the cheapest option vs manually entering in weights
# This will help for when shipping costs change.