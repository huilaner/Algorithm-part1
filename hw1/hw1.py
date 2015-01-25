import sys

def readAry(filename):
	file = open(filename)
	ary = []
	for line in file:
		ary.append(int(line))
	return ary

def count(A,n):
	if(n == 1):
		return (A,0)
	else:
		half = int(n * 0.5)
		# print half
		(B,x) = count(A[:half], half)
		(C,y) = count(A[half:], n-half)
		(D,z) = count_split_inv(A, B, C, n)
	return (D, x+y+z)

def count_split_inv(A, B, C, n):
	# print "A", A, "B", B, "C", C, "n:", n
	i = 0
	j = 0
	D = [None]*n
	count = 0
	for k in range(0,n):
		# print "k:", k
		if(i == len(B) and j < len(C)):
			# print "!!",D, " j:",j
			for k in range(k, n):
				D[k] = C[j]
				j += 1
			break
		elif(j == len(C) and i < len(B)):
			# print "!!",D, " j:",i
			for k in range(k, n):
				D[k] = B[i]
				i += 1
			break
		elif(B[i] < C[j]):
			D[k] = B[i]
			i += 1
		else:
			D[k] = C[j]
			j += 1
			count += len(B) - i 
	# print D, ":", count
	return (D,count) 


def main():
    filename = sys.argv[1]
    ary = readAry(filename)
    print  " len: ", len(ary)
    (R,c) = count(ary, len(ary))
    print  "result",R," num:", c

    # count_split_inv([3,5], [3], [5], 2)


if __name__ == '__main__':
    main()
