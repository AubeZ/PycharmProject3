def isStraight(nums):
    # repeat = set()
    # ma, mi = 0, 14
    # for num in nums:
    #     if num == 0: continue # 跳过大小王
    #     ma = max(ma, num) # 最大牌
    #     mi = min(mi, num) # 最小牌
    #     if num in repeat: return False # 若有重复，提前返回 false
    #     repeat.add(num) # 添加牌至 Set
    # return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

    repeat = set()
    count_0 = 0
    for num in nums:
        if num in repeat and num != 0: return False
        if num == 0:
            count_0 += 1
        else: repeat.add(num)

    if count_0 + min(repeat) + len(repeat) - 1 >= max(repeat):
        return True
    return False
if __name__ == '__main__':
    nums = [0,0,8,5,4]
    s = isStraight(nums)
    print(s)