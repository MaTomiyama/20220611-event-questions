def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    if len(array) == 2:
        if array[0] > array[1]:
            tmp = array[1]
            array[1] = array[0]
            array[0] = tmp

        return array
    idx_for = 0 ; idx_bac = len(array) - 1
    swp_idx_for = 0 ; swp_idx_bac = len(array) - 1
    move = False
    while True:
        if idx_bac - idx_for < 1:
            break
        if array[idx_for] >= pivot:
            swp_idx_for = idx_for
        if array[idx_bac] < pivot:
            swp_idx_bac = idx_bac
        if array[swp_idx_for] > array[swp_idx_bac]:
            tmp = array[swp_idx_for]
            array[swp_idx_for] = array[swp_idx_bac]
            array[swp_idx_bac] = tmp
            move = True
        if array[idx_for] < pivot and move == False:
            idx_for += 1
        if array[idx_bac] >= pivot and move == False:
            idx_bac -= 1
        if move == True:
            idx_for += 1
            idx_bac -= 1
            move = False
    
    if idx_for - idx_bac == 1:
        split_idx = idx_for
    if idx_for - idx_bac == 0:
        if array[idx_for] > pivot:
            split_idx = idx_for
        else:
            split_idx = idx_for + 1

    array[ : split_idx ] = sort( array[ : split_idx ] )
    array[ split_idx : ] = sort( array[ split_idx : ] )
    return array
    # ここまで記述

if __name__ == '__main__':
    main()
