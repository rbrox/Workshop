def sol(amt) :
    denom = [10, 20, 50, 100, 200, 500, 2000]
    denom.reverse()
    res = {}
    while amt > 10:
        for i in denom:
            res[i] = amt // i
            amt = amt % i
                    
    print(res)
    return res
    
def main():
    amt = 100729434
    sol(amt)
    with open('ans.txt', 'w') as f:
        f.write("Test")
        
main()