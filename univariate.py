def myeda(df):
    import pandas as pd
    import seaborn as sns, matplotlib.pyplot as plt

    output_df = pd.DataFrame(columns=['type', 'count', 'missing', 'unique','mode','min',
                                      'q1','median','q3','max','mean','std','skew','kurt'])
    # when a df is recieved, i want it to run obove fn, wheather its 2 columns or 2000

    for col in df:
        # for type
        dtype = df[col].dtype  # dtype to look the type of data inside the col

        # for count
        count = df[col].count()

        # for mising
        missing = df[col].isnull().sum()

        # for unique
        unique = df[col].nunique()

        #for mode
        mode= df[col].mode()[0]
        #adding a if else, to vary from quantitative and qualitative.
        if pd.api.types.is_numeric_dtype(df[col]):
            #calculate metric that apply to numeric
            min =df[col].min()
            q1 = df[col].quantile(.25)
            median = df[col].median()
            q3 = df[col].quantile(.75)
            max = df[col].max()
            mean = df[col].mean()
            std = df[col].std()
            skew = df[col].skew()
            kurt = df[col].kurt()

            output_df.loc[col] = [dtype, count, missing, unique, mode, min, q1, median, q3, max, mean, std, skew, kurt]

            #for graph
            sns.histplot(data=df, x=col)
        else:
            #for objectsss
            output_df.loc[col] = [dtype, count, missing, unique,mode, '-', '-', '-', '-', '-', '-', '-', '-', '-']

            #for these graph
            sns.countplot(data=df, x=col)
        plt.show()

    return output_df
