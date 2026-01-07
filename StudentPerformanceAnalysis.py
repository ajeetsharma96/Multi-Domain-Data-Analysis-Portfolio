import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance.csv")


df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)


df['result'] = df['average_score'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

pass_fail = df['result'].value_counts()

plt.figure()
pass_fail.plot(kind='pie', autopct='%1.1f%%')
plt.title("Overall Pass/Fail Rate")
plt.ylabel("")
plt.show()


subject_avg = {
    'Math': df['math_score'].mean(),
    'Reading': df['reading_score'].mean(),
    'Writing': df['writing_score'].mean()
}

subject_avg = pd.Series(subject_avg)

plt.figure()
subject_avg.plot(kind='bar')
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()


correlation = df['attendance_percentage'].corr(df['average_score'])
print("Correlation between Attendance and Average Score:", correlation)

plt.figure()
sns.scatterplot(x='attendance_percentage', y='average_score', data=df)
plt.title("Attendance vs Average Score")
plt.xlabel("Attendance Percentage")
plt.ylabel("Average Score")
plt.show()
