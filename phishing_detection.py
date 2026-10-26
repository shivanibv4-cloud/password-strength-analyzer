import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample email dataset
emails = [
    "You won a prize click here to claim now",
    "Urgent verify your bank account password",
    "Congratulations you won free money",
    "Click this link to update your account",
    "Your account is suspended verify immediately",
    "Limited offer claim your reward now",
    "Meeting scheduled for tomorrow morning",
    "Please find the college assignment attached",
    "Your class starts at ten tomorrow",
    "Thank you for attending the meeting",
    "The project report is ready for review",
    "Your appointment is confirmed"
]

labels = [
    "Phishing", "Phishing", "Phishing",
    "Phishing", "Phishing", "Phishing",
    "Safe", "Safe", "Safe", "Safe", "Safe", "Safe"
]

# Convert email text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)
y = labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions, labels=["Safe", "Phishing"]))
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Check a new email
new_email = ["Urgent! Verify your password to claim your prize"]
new_features = vectorizer.transform(new_email)
result = model.predict(new_features)

print("\nNew Email:", new_email[0])
print("Prediction:", result[0])