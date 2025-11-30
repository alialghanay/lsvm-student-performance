import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('StudentsPerformance.csv')
df['math_pass'] = (df['math score'] >= 70).astype(int)
le = LabelEncoder()
for col in ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']:
    df[col] = le.fit_transform(df[col])
    
X = df.drop(['math score', 'reading score', 'writing score', 'math_pass'], axis=1)
y = df['math_pass']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
lsvm = LinearSVC()
lsvm.fit(scaler.fit_transform(X_train), y_train)
y_pred = lsvm.predict(scaler.transform(X_test))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")