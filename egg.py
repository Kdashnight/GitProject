import numpy,copy
def getMinSteps(eggNum,floorNum):
    if(eggNum<1 or floorNum<1):
        pass
    #上一层备忘录，存储鸡蛋数量-1的floorNum层楼条件下的最优化尝试次数
    preCache = numpy.zeros(floorNum+1)
    #当前备忘录，存储当前鸡蛋数量的floorNum层楼条件下的最优化尝试次数
    currentCache = numpy.zeros(floorNum+1)
    #把备忘录每个元素初始化成最大的尝试次数
    for i in range(1,floorNum+1):
        currentCache[i] = i
        print(currentCache)
    for i in range(2,eggNum+1):
        #当前备忘录拷贝给上一次备忘录，并重新初始化当前备忘录
        preCache = copy.copy(currentCache)
        for i in range(1,floorNum+1):
            currentCache[i]=i
            print(currentCache)
        for m in range(1,floorNum+1):
            for k in range(1,m):
                #扔鸡蛋的楼层从1到m枚举一遍，如果当前算出的尝试次数小于上一次算出的尝试次数，则取代上一次的尝试次数。                
                #这里可以打印k的值，从而知道第一个鸡蛋是从第几次扔的。
                currentCache[m] = min(currentCache[m], 1+max(preCache[k-1],currentCache[m-k]))
                print(currentCache)
    return currentCache[floorNum]
print(getMinSteps(2,100))