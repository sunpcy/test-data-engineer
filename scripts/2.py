'''
สร้าง function สำหรับคำนวนผลบวกของ array ช่องที่ a ถึงช่องที่ b โดยมี interface function คือ
	
	function sumOfArray(arr: int[], inputs: int[][2]) int[]

	โดย arr.length < 100000 และ input.length < 100000
	และ input[x][0] คือ a และ input[x][1] คือ b
	1 <= a <= b <= arr.length
	
	Example
	Arr: [1,2,3,4,1]
	Inputs: [ [1, 3], [3,3], [4,5] ]
	
	Expect Outputs: [ 6, 3, 5 ]

sumOfArray([1,2,3,4,1], [ [1,3], [3,3] , [4,5] ]) => expect([6,3,5])

'''

def sumOfArray(arr, inputs):
    result = []
    for a, b in inputs:
        total = sum(arr[a-1:b])
        # print(a,b)
        result.append(total)
        # print(total)
        # print(result)
    return result

arr = [1, 2, 3, 4, 1]
inputs = [[1, 3], [3, 3], [4, 5]]
output = sumOfArray(arr, inputs)
print(output)
    