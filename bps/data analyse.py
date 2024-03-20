import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
df = pd.read_csv("invoice.csv")

# Plotting
plt.figure(figsize=(12, 8))

# Plot invoice amount vs invoice ID
plt.subplot(2, 2, 1)
plt.bar(df['invoiceId'], df['invoiceAmount'], color='blue')
plt.xlabel('Invoice ID')
plt.ylabel('Invoice Amount')
plt.title('Invoice Amount vs Invoice ID')

# Plot invoice paid amount vs invoice ID
plt.subplot(2, 2, 2)
plt.bar(df['invoiceId'], df['invoicePaidAmount'], color='green')
plt.xlabel('Invoice ID')
plt.ylabel('Invoice Paid Amount')
plt.title('Invoice Paid Amount vs Invoice ID')

# Plot invoice balance vs invoice ID
plt.subplot(2, 2, 3)
plt.bar(df['invoiceId'], df['invoiceBalance'], color='red')
plt.xlabel('Invoice ID')
plt.ylabel('Invoice Balance')
plt.title('Invoice Balance vs Invoice ID')

# Plot invoice profit vs invoice ID
plt.subplot(2, 2, 4)
plt.bar(df['invoiceId'], df['invoiceProfit'], color='purple')
plt.xlabel('Invoice ID')
plt.ylabel('Invoice Profit')
plt.title('Invoice Profit vs Invoice ID')

plt.tight_layout()
plt.show()



