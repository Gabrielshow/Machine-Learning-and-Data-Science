#measuring the relationship between two values
#the relationship is measured with a value called the r-squared
#the r-squared value ranges from 0 to 1, where 0 means no relationship and 1 means 100 percent related

#how well does my data fit in a linear regression?
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

 

#it shows that there is a relationship, not perfect
#and we could use regression in future predictions

#to predict we could add this function
def myfunc(x):
    return slope * x + intercept

speed = myfunc(10)

print(r) #-0.75859
print(speed) #with this we get a prediction of 86 as the approximate speed of a ten year car


