import pandas as pd
def calculate_demographic_data():
    df = pd.read_csv('adult.data.csv')
    print(df.head())
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)
    q1 = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    q2 = df['salary'] == '>50K'
    higher_education_rich = round((q1 & q2).sum() / q1.sum() * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    q1 = df['hours-per-week'] == min_work_hours
    q2 = df['salary'] == '>50K'
    rich_percentage = round((q1 & q2).sum() / q1.sum() * 100, 1)
    p = (df[q2]['native-country'].value_counts()
         / df['native-country'].value_counts() * 100).sort_values(ascending=False)

    highest_earning_country = p.index[0]
    highest_earning_country_percentage = round(p.iloc[0], 1)
    print(race_count)
    print(average_age_men)
    print(percentage_bachelors)
    print(higher_education_rich)
    print(min_work_hours)
    print(rich_percentage)
    print(highest_earning_country)
    print(highest_earning_country_percentage)
    
calculate_demographic_data()


























