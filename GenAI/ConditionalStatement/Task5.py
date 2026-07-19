daily = [200, 150, 0, 400,50, -1,300]
total_sales = 0
for sale in daily:
    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break
    if sale == 0:
        print("No sales recorded for this day. Skipping....")
        continue
    total_sales += sale
    print(f"Running total: ${total_sales:.2f}")
print("\nFinal total sales: ${total_sales:.2f}")

