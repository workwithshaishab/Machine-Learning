# Interpolation is the technique of filling missing values with estimated values.

# why this?
# preserve data integrity
# smooth trend
# avoid data loss

import pandas as pd
data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,40,None]
}
df= pd.DataFrame(data)
print(df)

# linear, polynomial, time

df["Value"].interpolate(method="linear",axis=0, inplace=True)
print(df)