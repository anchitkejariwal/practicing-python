import matplotlib.pyplot as plt
subjects=["Maths","physics","FE","FME","English "]
marks=[85,78,82,88,90]
study_hours=[3,2,2.5,3.5,2]
plt.figure(figsize=(8,5))
plt.bar(subjects,marks)
plt.title("Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()
plt.figure(figsize=(8,5))
plt.plot(subjects,study_hours,marker="o")
plt.title("Study Hours by Subject")
plt.xlabel("Subject")
plt.ylabel("Study Hours")
plt.show()
plt.figure(figsize=(7,7))
plt.pie(study_hours,labels=subjects,autopct="%1.1f%%")
plt.title("Distribution of study Time")
plt.show()