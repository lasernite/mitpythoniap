def convert_knuts(knuts):
    sickles = 0
    galleons = 0
    while knuts >= 29:
        sickles += 1
        knuts -= 29
        if sickles >= 17:
            galleons += 1
            sickles -= 17
    return galleons, "galleons,", sickles, "sickles, and", knuts, "knuts."


convert_knuts(232)

def prime(n):
    for x in range(2,n):
        if float(n) % x == 0:
            return False
    else:
        return True


def mod(m, n):
    num = float(m)/n
    print num
    near = m/n
    print near
    fraction = num - near
    print fraction
    remainder = fraction * n
    print remainder
    a = round(remainder)
    print a
    return int(a)

def div(m, n):
    answer = 0
    for x in range(n, m+1, n):
        print x
        answer += 1
    print answer
        

def multwhile(m, n):
	count = 1
	answer = 0
	while count <= n:
		answer += m
		count += 1
	return answer

print multwhile(5.01,5)

def multIA(m, n):
    ans = 0
    for x in range(n):
        ans += n
    return ans

def multIAgen(m, n):
    ans = 0
    for x in range(abs(n)):
        if abs(n) == n and abs(m) == m:
            ans += abs(m)
        elif abs(n) != n and abs(m) != m:
            ans += abs(m)
        elif abs(n) != n and abs(m) == m:
            ans += -m
        else:
            ans += m
    return ans


