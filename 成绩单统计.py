def 冒泡排序法(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(2, n - i - 1):
            if int(arr[j][10]) < int(arr[j+1][10]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def 成绩单统计():
    rf_lst1 = []
    with open('成绩单.txt',encoding='utf-8')as rf:
        rf_lst = rf.readlines()
        for i in rf_lst:
            rf_lst1.append(i.split())
    rf_lst1[0].append('总分')
    rf_lst1[0].append('平均分')
    #print(rf_lst1)
    a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for z in range(1,len(rf_lst1)):
        #对每列算出平均分
        for l in range(1,len(rf_lst1[z])):
            rf_lst1[z][l] = int(rf_lst1[z][l])
        a += rf_lst1[z][1]
        b += rf_lst1[z][2]
        c += rf_lst1[z][3]
        d += rf_lst1[z][4]
        e += rf_lst1[z][5]
        f += rf_lst1[z][6]
        g += rf_lst1[z][7]
        h += rf_lst1[z][8]
        i += rf_lst1[z][9]
    a, b, c, d, e, f, g, h, i = a/len(rf_lst1[1:]), b/len(rf_lst1[1:]), c/len(rf_lst1[1:]), d/len(rf_lst1[1:]), \
                                e/len(rf_lst1[1:]), f/len(rf_lst1[1:]), g/len(rf_lst1[1:]), h/len(rf_lst1[1:]), \
                                i/len(rf_lst1[1:])
    rf_lst1.insert(1,['平均', a, b, c, d, e, f, g, h, i])
    for i in range(1,len(rf_lst1)):
        #计算每行的平均分和总分
        result = 0
        for l in range(1,len(rf_lst1[i])):
            result += rf_lst1[i][l]
        rf_lst1[i].append(result)
        rf_lst1[i].append('{:.2f}'.format(result/9))
    for i in range(1, 11):
        rf_lst1[1][i] = '{:.2f}'.format(rf_lst1[1][i])
    for i in range(2,len(rf_lst1)):
        for l in range(1,10):
            if rf_lst1[i][l] < 60:
                rf_lst1[i][l] = '不及格'
    asx = 冒泡排序法(rf_lst1)
    asx[0].insert(0,'名次')
    with open('result.txt','w',encoding='utf-8') as f:
        for i in range(len(asx[0][:-1])):
            asx[0][i] = asx[0][i]+'    '
        asx[0][-1] = asx[0][-1].join('\n')
        f.writelines(asx[0])
        size = 0
        for i in range(1,len(asx)):
            for j in range(len(asx[0][:-1])):
                if isinstance(asx[i][j],int):
                    asx[i][j] = str(asx[i][j])+ '    '
                else:
                    asx[i][j] = asx[i][j] + '    '
            asx[i].insert(0,str(size)+ '    ')
            asx[i][-1] = asx[i][-1]+'\n'
            f.writelines(asx[i])
            size += 1
成绩单统计()