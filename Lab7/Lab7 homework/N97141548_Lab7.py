# Lab7 資料前處理 - 碩二丙 黃柏憲 N97141548
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = np.loadtxt("../Bank_Customer.csv", skiprows=1, dtype=str, delimiter=',')
# 欄位: 0 customer_id, 1 credit_score, 2 country, 3 gender, 4 age, 5 tenure,
#       6 balance, 7 products_number, 8 credit_card, 9 active_member,
#       10 estimated_salary, 11 churn

# 1. 非數值型資料轉換成數值型資料
# gender: Female=0, Male=1
gender = (data[:, 3] == "Male").astype(float).reshape(-1, 1)
# country: 無順序關係，採 One-hot encoding 拆成三欄
countries = np.array(["France", "Germany", "Spain"])
country = (data[:, 2].reshape(-1, 1) == countries).astype(float)

# 2. 去除無意義的特徵類別 (customer_id)，其餘數值欄位轉為 float
numeric = data[:, [1, 4, 5, 6, 7, 8, 9, 10]].astype(float)
label = data[:, 11].astype(float).reshape(-1, 1)

features = np.hstack([numeric, country, gender])

# 3. 標準化特徵 (StandardScaler)，label 維持 0/1
features = StandardScaler().fit_transform(features)

pre_data = np.hstack([features, label])
header = ("credit_score,age,tenure,balance,products_number,credit_card,"
          "active_member,estimated_salary,country_France,country_Germany,"
          "country_Spain,gender,churn")
np.savetxt("Bank_Customer_Preprocessed.csv", pre_data, delimiter=",",
           header=header, comments="", fmt="%.6f")
print("前處理完成:", pre_data.shape)


from sklearn.linear_model import LogisticRegression
# 決策分類器
clf = LogisticRegression()

# 4. 切割 data 為 Training data (80%) 與 Testing data (20%)
x = pre_data[:, :-1]
y = pre_data[:, -1].astype(int)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
print("Training data:", x_train.shape, " Testing data:", x_test.shape)

# 使用訓練集來訓練我們的分類器
clf.fit(x_train, y_train)
# 測試資料集中進行預測
pred = clf.predict(x_test)

#print (pred) # 預測分類，即客戶是否流失
#print (y_test) # 分類
print (str(accuracy_score(pred, y_test)*100 ) + "% ")   # 預測精度
