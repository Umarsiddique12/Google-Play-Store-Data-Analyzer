def run_eda(df):
    print("\nTotal apps:", len(df))
    print("\nTop Categories:")
    print(df['Category'].value_counts().head(10))

    print("\nAverage Rating:", df['Rating'].mean())
    print("\nTop Free Apps by Rating:")
    print(df[df['Type'] == 'Free'].sort_values(by='Rating', ascending=False)[['App', 'Rating']].head(5))

    print("\nTop Paid Apps:")
    print(df[df['Type'] == 'Paid'].sort_values(by='Rating', ascending=False)[['App', 'Rating', 'Price']].head(5))