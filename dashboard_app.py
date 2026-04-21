import pandas as pd
import matplotlib.pyplot as plt

# بيانات تجريبية للمبيعات
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [4500, 5200, 6100, 5900]
}
df = pd.DataFrame(data)

# رسم بياني احترافي
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Performance')
plt.grid(True)

# حفظ النتيجة كصورة
plt.savefig('sales_performance.png')
print("Dashboard saved as sales_performance.png")