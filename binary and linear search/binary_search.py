import bs_test

def locate(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number<query:
        return 'left'
    else:
        return 'right'

def bs(cards, query):
    lo, hi = 0,len(cards) - 1

    while lo <= hi:
        mid = (lo+hi)//2
        check=locate(cards, query, mid)
        if check=='found':
            return mid
        elif check=='left':
            hi = mid-1
        elif check=='right':
            lo = mid+1
    return -1
        
bs_test.evaluate_test_case(bs,bs_test.test_list)