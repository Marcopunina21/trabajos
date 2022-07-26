def isYearLeap(year):
	 if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


#
# Codigo from LAB Listas y return
def daysInMonth(year, month):
	
#
# put your new code here
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
