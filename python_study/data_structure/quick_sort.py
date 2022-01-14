def quick_sort(q, l, r):  # 待排数组，起始索引，终止索引
    """
    1.分治
    2.递归
    """
    if l >= r:
        return
    i, j = l, r
    pivot = q[l + r >> 1]
    while i <= j:  # 保证i会穿过j，避免边界问题
        while q[i] < pivot:
            i += 1
        while q[j] > pivot:
            j -= 1
        if i <= j:  # 保证i会穿过j，避免边界问题
            q[i], q[j] = q[j], q[i]
            i += 1
            j -= 1
    quick_sort(q, l, j)  # 递归排左半边数组
    quick_sort(q, i, r)  # 递归排右半边数组
