import os

from requests import get

def 读写文件(file_name, name=None, date=None, bools=True, size=''):
    if bools and size == 'r':
        with open(file_name, size, encoding='utf-8') as f:
            g = f.readlines()
            for i in g:
                if name in i:
                    for x in i.split('\n\t'):
                        z = x.split('\t')
                        return [int(z[1]),int(z[2]),float(z[3]), g, g.index(i)]
            return[0, 0, 0.00, g, None ]
    elif bools and size == 'w':
        with open(file_name, size, encoding='utf-8') as f:
            f.writelines(date)
    else:
        with open(file_name, encoding='utf-8') as f:
            pass


def 高级猜数字():
    name = input('请输入你的名字：')
    file_name = 'game_user.txt'
    if not os.path.isfile(file_name):
        读写文件(file_name, bools=False)
    while True:
        b = 0#本次猜出答案轮数
        size, low, a, lst, x = 读写文件(file_name, name=name, size='r')
        print(f'{name},你已经玩了{size}次，最少{low}轮猜出答案，平均{a}轮猜出答案，开始游戏！')
        num = int(get('https://python666.cn/cls/number/guess/').text)
        while 1:
            try:
                ipt = int(input('请输入一个1 - 100的整数：'))
            except ValueError:
                print('ERROR：输入错误，有非整数字符输入，请重新输入')
                b += 1
                continue
            if ipt > 0 and ipt <= 100:
                if ipt > num :
                    print('猜大了，再试试!')
                    b += 1
                elif ipt < num:
                    print('猜小了再试试')
                    b += 1
                else:
                    b += 1
                    if low == 0 or low != 0 and low > b :
                        low = b
                    if a == 0.00:
                        a = float(b)
                    else:
                        a = float(((a*size)+b)/(size+1))
                    print(f'恭喜，你猜对了，你一共猜了{b}轮。')
                    b = 0
                    size += 1
                    print(f'{name},你已经玩了{size}次，最少{low}轮猜出答案，平均{a:.2f}轮猜出答案')
                    a = float(f'{a:.2f}')
                    if x != None:
                        g = '\t'.join([name, str(size), str(low), str(a)])
                        lst[x] = g + '\n'
                    else:
                        lst.append('\t'.join([name, str(size), str(low), str(a)])+'\n')
                    读写文件(file_name, date=lst, size='w')
                    q = input('是否继续游戏？（输入y并敲回车继续，其他退出）')
                    if q == 'y' or q == 'Y':
                        num = int(get('https://python666.cn/cls/number/guess/').text)
                        continue
                    else:
                        break
            else:
                print('ERROE:输入错误，输入数值不在1-100范围内，请重新输入')
                b += 1
                continue
        break
    print('退出游戏，欢迎下次再来')
if __name__ == '__main__':
    高级猜数字()