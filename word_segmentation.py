#已優化:先算出字典中最長的詞  接下來正向.反向匹配最多就擷取最長詞的長度

#使用正規表達式(regular expression, RE)去除中文字以外的字?
#待優化:使用多執行緒優化


import time 
import matplotlib
import matplotlib.pyplot as plt

def forward_match(text, dict_word, longest_term): 
    """
    正向最長匹配
    
    參數 text : 要分詞的文字

    參數 dict_word : 繁體中文詞語字典

    參數 longest_term : 字典中最長詞語的長度
    
    回傳值 : 一個串列 內部元素為 詞語的(起始索引,結束索引)
    """
    result_list = []
    start = 0  #要尋找的字首
    while start < len(text):    #使用類似反向雙指標的方法
        if start + longest_term - 1 >= len(text):
            end = len(text) - 1
        else:
            end = start + longest_term - 1
        while start <= end:  
            word = text[start : end + 1]
            if word in dict_word:
                result_list.append((start, end))
                start += len(word)
                break
            end -= 1 
            if start > end:  #完全找不到可匹配的詞  代表是標點符號或是字母
                start += 1             
    return result_list
        
def reverse_match(text, dict_word, longest_term):
    """
    反向最長匹配  
    
    參數 text : 要分詞的文字

    參數 dict_word : 繁體中文詞語字典

    參數 longest_term : 字典中最長詞語的長度
    
    回傳值 : 一個串列 內部元素為 詞語的(起始索引,結束索引)
    """
    result_list = []
    stack = []        #因為反向最長匹配是由後往前進行分詞 所以使用堆疊的資料結構
    end = len(text) - 1
    while end >= 0:    
        if end - longest_term + 1 < 0:
            start = 0
        else:
            start = end - longest_term + 1
        while start <= end:  
            word = text[start : end + 1]
            if word in dict_word:
                stack.append((start, end))
                end -= len(word)
                break
            start += 1 
            if start > end:
                end -= 1    
    while len(stack) > 0:
        result_list.append(stack.pop())
    return result_list           