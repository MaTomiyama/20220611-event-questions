def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    if target_number in sorted_array:
        start_idx = 0
        len_search_array = len(sorted_array)
        while True:
            middle_idx = start_idx + int(len_search_array / 2)
            if sorted_array[ middle_idx ] == target_number:
                target_index = middle_idx
                break
            elif sorted_array[ middle_idx ] < target_number:
                start_idx = middle_idx + 1
                len_search_array = len_search_array - int(len_search_array / 2) - 1
            else:
                len_search_array = int(len_search_array / 2)
        return target_index
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
