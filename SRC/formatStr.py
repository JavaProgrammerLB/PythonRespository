import math
#format最基本的用法
print('{} is a {}'.format('Cescfangs','gooner'))

#{}里加上为从0开始的索引数字的参数
print('{1} is a {0}'.format('Cescfangs','gooner'))

#{}加上参数
print('{Ramsey} is a {gunner}'.format(Ramsey='Cescfangs',gunner='gooner'))

#保留小数点后三位小数
print('value of pi is {0:.3f}'.format(math.pi))

#固定位数输出，让我们的输出更漂亮
arsenal = {'Ramsey':16,'Rosciky':7,'Chambers':21,'Ozil':11}
for player, number in arsenal.items():
    print('{0:10}---->{1:3d}'.format(player,number))
