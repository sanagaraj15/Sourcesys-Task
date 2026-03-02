import numpy as np

def main():
    print("===== SALES DATA ANALYSIS =====")

    products = 4
    months = 12

    sales = np.random.randint(1000, 10000, size=(products, months))

    print("\nSales Data:\n", sales)

    yearly_sales = np.sum(sales, axis=1)
    print("\nYearly Sales per Product:", yearly_sales)

    monthly_total = np.sum(sales, axis=0)
    best_month = np.argmax(monthly_total)
    print("Best Month Index:", best_month)

    best_product = np.argmax(yearly_sales)
    print("Best Selling Product Index:", best_product)

    growth = ((sales[:, -1] - sales[:, 0]) / sales[:, 0]) * 100
    print("Growth Percentage:", growth)

if __name__ == "__main__":
    main()