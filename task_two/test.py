#%%
import pandas as pd
days = [ 'Saturday' , 'Sunday' , 'Monday' , 'Tuesday' ,
        'Wednesday' , 'Thursday' , 'Friday' ]
calories = [ 1670 , 2011 , 1853 , 2557 ,
            1390 , 2118 , 2063 ]
df_days_calories = pd.DataFrame(
    { 'day' : days , 'calories' : calories })
print(df_days_calories)
df_days_calories.plot( 'day' , 'calories' )



# # Define the remote URL
# url = "https://data.nasdaq.com/api/v3/datasets/BSE/BOM500325.csv?api_key=3s9tJcNpDR92v3kYK2Cy&start_date=1992-01-02"


# df = pd.read_csv(url)
# df.dropna(inplace=True)

# print(df.to_csv())

# data = requests.get(url)
# lines = data.text.split('\n')
# print(len(lines[1].split(",")))


# print(df)

# # Send HTTP GET request via requests
# data = urllib3
# cr = csv.reader(data)
# print(type(cr))
# i=1
# for row in cr:
#     if i==5:
#         break
#     print(row)
#     i = i+1
# header = next(cr)
# print(header)

# # Convert to iterator by splitting on \n chars
# lines = data.json()
# print(type(lines))


# Parse as CSV object
# file = open('employee_data.csv','r')
# print(type(file))

# reader = csv.reader(file)
# print(reader)
# header = next(reader)
# print(header)
# print(reader)

# View Result
# for row in reader:
#     pass
   
    # print(row)


