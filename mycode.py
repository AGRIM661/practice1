import pandas as pd
import os
data={"name":["rahul","sumit","komal","harry"],
      "age":[12,34,55,21],
      "city":["dehradun","delhi","mumbai","noida"]}
df=pd.DataFrame(data)

##create a directory if not exist
data_dir="data"
os.makedirs(data_dir,exist_ok=True)
##define a csv file
file_path=os.path.join(data_dir,"sample_data.csv")

##save the dataframe to csv file
df.to_csv(file_path,index=False)

print(f"CSV file saved to: {file_path}")

# Display the DataFrame
print(df)