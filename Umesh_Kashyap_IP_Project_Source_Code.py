import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

main= """\n \n Main Menu
1) To write CSV to DataFrame
2) To manipulate data
3) To analyse Data
4) To visualise Data
5) Exit"""

analyse= """\n \n ----------Analysis Data Menu ----------
1) All Data
2) Top Records
3) Bottom Records
4) Total population, total male population and total female population
   aged 10 to 24 in India
5) Compare the sex ratio of urban areas and rural areas.
6) Which state is home to the maximum no. of ST in India? Which state
   has the minimum no. of ST in India?
7) Which State or Union Territory in India has the maximum number
   of illiterates in the youth ages?
8) Return to Main Menu
"""

visualize= """\n \n ----------Visualisation Data Menu----------
1) Line Chart(Agricultural Labourers age wise in a state)
2) Line Chart(ST Males age wise in a state)
3) Line Chart(Rural illiterates age wise in a state)
4) Bar Chart (Total population, total male population and total
   female population aged 10 to 24 in India)
5) Bar Chart (Sex ratio of urban areas and rural areas.)
6) Bar Chart (No. of SCs age wise in a state)
7) Bar Chart (No. of female illiterates age wise in a state)
8) Return to Main Menu
"""

manipulate= """\n \n ----------Manipulation Data Menu----------
1) To append a record
2) To remove a record"""

#Data Source OGD PCA_AY_2011_Revised
#Selected columns are chosen
def main_menu():
    df=pd.read_csv(r"C:\Users\Umesh\Desktop\IP PROJECT\PCA_AY_2011_Revised.csv",
     usecols=["State Code","District Code", "Area Name","Total/ Rural/ Urban",
     "Adolescent and youth categories","Total Population - Persons",
     "Total Population - Males", "Total Population - Females",
     "Scheduled Caste - Persons","Scheduled Tribe - Persons",
     "Scheduled Tribe - Males", "Illiiterates - Total - Persons",
     "Illiiterates - Total - Males","Illiiterates - Total - Females",
     "Main Worker - Agricultural labourers - Persons"])
    print(main)
    ch=int(input("Enter choice"))
    if ch==1:
        print(df)
        main_menu()
    elif ch==2:
        manipulate_menu()
    elif ch==3:
        analyse_data()
    elif ch==4:
        visualise_data()
    elif ch==5:
        sys.exit()

def analyse_data():
    df=pd.read_csv(r"C:\Users\Umesh\Desktop\IP PROJECT\PCA_AY_2011_Revised.csv",
     usecols=["State Code","District Code",
    "Area Name","Total/ Rural/ Urban","Adolescent and youth categories",
    "Total Population - Persons","Total Population - Males",
    "Total Population - Females","Scheduled Caste - Persons",
    "Scheduled Tribe - Persons","Scheduled Tribe - Males",
    "Illiiterates - Total - Persons","Illiiterates - Total - Males",
    "Illiiterates - Total - Females",
    "Main Worker - Agricultural labourers - Persons"])
    print(analyse)
    ch=int(input("Enter choice"))
    if ch==1:
        print(df)
    elif ch==2:
        x=int(input("How many records from top do you want?"))
        print(df.head(x))
    elif ch==3:
        x=int(input("How many records from bottom do you want?"))
        print(df.tail(x))
    elif ch==4:
        df1=df.loc[(df['Area Name'] == 'INDIA'),
        'Area Name':'Total Population - Females']
        df1.columns= ['Area', 'Class', 'Category', 'TotalPop', 'MalePop',
         'FemalePop']
        d=df1.loc[1:3]
        d=d.drop(["Area","Class"],axis=1)
        print(d)
    elif ch==5:
        df1=df.loc[(df["Area Name"] == "INDIA"),
        ["Total/ Rural/ Urban","Adolescent and youth categories" ,
        "Total Population - Males","Total Population - Females"]]
        df1.columns=["Type","Category", "MalePop","FemalePop"]
        d=df1.loc[[6,12]]
        d["Sex Ratio"]=d["FemalePop"]/d["MalePop"] * 1000
        d=d.drop(["Category","MalePop","FemalePop"],axis=1)
        print(d)
    elif ch==6:
        df1=df.loc[(df['Area Name'].str.contains('State'))&
        (df["Adolescent and youth categories"]== "All Ages")&
        (df["Total/ Rural/ Urban"]=="Total")
        ,["Area Name","Adolescent and youth categories",
        "Scheduled Tribe - Persons"]]
        print("State with maximum number of ST is:")
        mx=int(df1.max(numeric_only=True).values)
        dfmax=df1.loc[(df1["Scheduled Tribe - Persons"]==mx),
        ["Area Name","Scheduled Tribe - Persons"]]
        print(dfmax)
        print("States with minimum number of ST are:")
        mn=int(df1.min(numeric_only=True).values)
        dfmin=df1.loc[(df1["Scheduled Tribe - Persons"]==mn),
        ["Area Name","Scheduled Tribe - Persons"]]
        print(dfmin)
    elif ch==7:
        df1=df.loc[(df['Area Name'].str.contains('State'))&
        (df["Adolescent and youth categories"]== "Youth (15-24)")&
        (df["Total/ Rural/ Urban"]=="Total"),
        ["Area Name","Illiiterates - Total - Persons"]]
        print("""State or UT which has maximum number of illiterates
        in the youth ages is:""")
        mx=int(df1.max(numeric_only=True).values)
        dfmax=df1.loc[(df1["Illiiterates - Total - Persons"]==mx),
        ["Area Name","Illiiterates - Total - Persons"]]
        print(dfmax)
    elif ch==8:
        main_menu()

def visualise_data():
    df=pd.read_csv(r"C:\Users\Umesh\Desktop\IP PROJECT\PCA_AY_2011_Revised.csv",
     usecols=["State Code","District Code",
    "Area Name","Total/ Rural/ Urban","Adolescent and youth categories",
    "Total Population - Persons","Total Population - Males",
    "Total Population - Females","Scheduled Caste - Persons",
    "Scheduled Tribe - Persons","Scheduled Tribe - Males",
    "Illiiterates - Total - Persons","Illiiterates - Total - Males",
    "Illiiterates - Total - Females",
    "Main Worker - Agricultural labourers - Persons"])
    print(visualize)
    ch=int(input("Enter choice"))
    if ch==1:
        df1=df.loc[(df['Area Name'].str.contains('State'))
        &(df["Total/ Rural/ Urban"]=="Total"),
        ["Area Name","Adolescent and youth categories",
        "Main Worker - Agricultural labourers - Persons"]]
        b=input("Which state graph do you want?(IN CAPITALS)")
        df2=df1.loc[(df1["Area Name"].str.contains(b)),["Area Name",
        "Adolescent and youth categories","Main Worker - Agricultural labourers - Persons"]]
        print(df2)
        plt.plot(df2["Adolescent and youth categories"],df2["Main Worker - Agricultural labourers - Persons"]
        ,color="Gold")
        plt.xlabel("Category(age)")
        plt.ylabel("No. of Agricultural Labourers")
        plt.title("No of agricultural workers age wise")
        plt.grid(True)
        plt.show()
    elif ch==2:
        df1=df.loc[(df['Area Name'].str.contains('State'))
        &(df["Total/ Rural/ Urban"]=="Total"),
        ["Area Name","Adolescent and youth categories",
        "Scheduled Tribe - Males"]]
        b=input("Which state graph do you want?(IN CAPITALS)")
        df2=df1.loc[(df1["Area Name"].str.contains(b)),["Area Name",
        "Adolescent and youth categories","Scheduled Tribe - Males"]]
        print(df2)
        plt.plot(df2["Adolescent and youth categories"],df2["Scheduled Tribe - Males"]
        ,color="orange")
        plt.xlabel("Category(age)")
        plt.ylabel("No. of ST Males")
        plt.title("No of ST Males age wise")
        plt.grid(True)
        plt.show()
    elif ch==3:
        df1=df.loc[(df['Area Name'].str.contains('State'))
        &(df["Total/ Rural/ Urban"]=="Rural"),
        ["Area Name","Adolescent and youth categories",
        "Illiiterates - Total - Persons"]]
        b=input("Which state graph do you want?(IN CAPITALS)")
        df2=df1.loc[(df1["Area Name"].str.contains(b)),["Area Name",
        "Adolescent and youth categories","Illiiterates - Total - Persons"]]
        print(df2)
        plt.plot(df2["Adolescent and youth categories"],df2["Illiiterates - Total - Persons"])
        plt.xlabel("Category(age)")
        plt.ylabel("No. of rural illiterates")
        plt.title("No of rural illiterates age wise")
        plt.grid(True)
        plt.show()
    elif ch==4:
        df1=df.loc[(df['Area Name'] == 'INDIA'),
        'Area Name':'Total Population - Females']
        df1.columns= ['Area', 'Class', 'Category', 'TotalPop', 'MalePop',
         'FemalePop']
        d=df1.loc[1:3]
        d=d.drop(["Area","Class"],axis=1)
        d.index=["10-14","15-19","20-24"]
        d.plot(kind="bar",title="Total Population Age wise in youth")
        plt.xlabel("Age category")
        plt.ylabel("Population")
        plt.show()
    elif ch==5:
        df1=df.loc[(df["Area Name"] == "INDIA"),
        ["Total/ Rural/ Urban","Adolescent and youth categories" ,
        "Total Population - Males","Total Population - Females"]]
        df1.columns=["Type","Category", "MalePop","FemalePop"]
        d=df1.loc[[6,12]]
        d["Sex Ratio"]=d["FemalePop"]/d["MalePop"] * 1000
        d=d.drop(["Category","MalePop","FemalePop"],axis=1)
        d.index=["Rural","Urban"]
        d.plot(kind="bar")
        plt.xlabel("Area type")
        plt.ylabel("Sex Ratio")
        plt.show()
    elif ch==6:
        df1=df.loc[(df['Area Name'].str.contains('State'))
        &(df["Total/ Rural/ Urban"]=="Total"),
        ["Area Name","Adolescent and youth categories",
        "Scheduled Caste - Persons"]]
        b=input("Which state graph do you want?(IN CAPITALS)")
        df2=df1.loc[(df1["Area Name"].str.contains(b)),["Area Name",
        "Adolescent and youth categories","Scheduled Caste - Persons"]]
        df2=df2.drop(["Area Name"],axis=1)
        df2.plot(kind="bar",x="Adolescent and youth categories",color="red",edgecolor="gold")
        plt.xlabel("Category(age)")
        plt.ylabel("No. of SCs")
        plt.title("No of SCs age wise")
        plt.show()
    elif ch==7:
        df1=df.loc[(df['Area Name'].str.contains('State'))
        &(df["Total/ Rural/ Urban"]=="Total"),
        ["Area Name","Adolescent and youth categories",
        "Illiiterates - Total - Females"]]
        b=input("Which state graph do you want?(IN CAPITALS)")
        df2=df1.loc[(df1["Area Name"].str.contains(b)),["Area Name",
        "Adolescent and youth categories","Illiiterates - Total - Females"]]
        df2=df2.drop(["Area Name"],axis=1)
        print(df2)
        df2.plot(kind="bar",x="Adolescent and youth categories",color="green",edgecolor="silver",linewidth=3)
        plt.xlabel("Category(age)")
        plt.ylabel("No. of female illiterates")
        plt.title("No of female illiterates age wise")
        plt.show()
    elif ch==8:
        main_menu()

def manipulate_menu():
    print(manipulate)
    df=pd.read_csv(r"C:\Users\Umesh\Desktop\IP PROJECT\PCA_AY_2011_Revised.csv",
     usecols=["State Code","District Code",
    "Area Name","Total/ Rural/ Urban","Adolescent and youth categories",
    "Total Population - Persons","Total Population - Males",
    "Total Population - Females","Scheduled Caste - Persons",
    "Scheduled Tribe - Persons","Scheduled Tribe - Males",
    "Illiiterates - Total - Persons","Illiiterates - Total - Males",
    "Illiiterates - Total - Females",
    "Main Worker - Agricultural labourers - Persons"])
    ch=int(input("Enter choice"))
    if ch==1:
        a1=int(input('State Code'))
        a2=int(input('District Code'))
        a3=input('Area Name')
        a4=input('Total/ Rural/ Urban')
        a5=input('Adolescent and youth categories')
        a6=int(input('Total Population - Persons'))
        a7=int(input('Total Population - Males'))
        a8=int(input('Total Population - Females'))
        a9=int(input('Scheduled Caste - Persons'))
        a10=int(input('Scheduled Tribe - Persons'))
        a11=int(input('Scheduled Tribe - Males'))
        a12=int(input('Illiiterates - Total - Persons'))
        a13=int(input('Illiiterates - Total - Males'))
        a14=int(input('Illiiterates - Total - Females'))
        a15=int(input('Main Worker - Agricultural labourers - Persons'))
        l1=[a1,a2,a3,a4,
            a5,a6,a7,a8,
            a9,a10,a11,a12,
            a13,a14,a15]
        df.loc[-1]=l1
        print("DataFrame is updated")
        o=input("Do you want to update in CSV? (Yes/No)")
        if o=="Yes":
            df.to_csv(r"C:\Users\Student\Desktop\IP PROJECT\PCA_AY_2011_Revised.csv"
            ,index=False)
        elif o=="No":
            pass
    elif ch==2:
        a=int(input("Enter index number of the record to be removed"))
        df=df.drop([a],axis=0)
        print("DataFrame is updated")
        o=input("Do you want to update in CSV? (Yes/No)")
        if o=="Yes":
            df.to_csv(r"C:\Users\Student\Desktop\IP PROJECT\PCA_AY_2011_Revised.csv"
            ,index=False)
        elif o=="No":
            pass

main_menu()
