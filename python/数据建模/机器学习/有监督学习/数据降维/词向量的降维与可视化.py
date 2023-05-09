
# 自己实现PCA
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def pca(X, k): 
    # k is the components you want 列数降到多少列
    # mean of each feature
    m, n = np.shape(X)
    mean = np.mean(X, axis=0)  # ! 计算每一列的平均值
    # normalization
    norm_X = X-mean  # !利用广播机制 列上面的每一个元素都减去该列上的平均值
    # scatter matrix 协方差矩阵  norm_x.T dot norm_x
    scatter_matrix = np.dot(np.transpose(norm_X), norm_X)
    # Calculate the eigenvectors and eigenvalues
    eig_val, eig_vec = np.linalg.eig(scatter_matrix)
#     v: 代表特征向量
# 返回值v是一个array类型的数据，其维度和方阵的维度是相同的，对于一个m x m的方阵，v的维度也为m x m，v中包含m个特征向量，每个特征向量的长度为m，
# !v[:,i]对应特征值为w[i]的特征向量，特征向量是进行单位化（除以所有元素的平方和的开方）的形式。
#!print(X[:,0]) 以行向量形式输出第1列
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(n)]
    #todo 这里是 特征值和其所对应的特征向量形成的元祖 按特征值排列的时候我们需要特征向量也跟着移动
    #todo 所以我们需要用元祖绑定对应关系
    # sort eig_vec based on eig_val from highest to lowest
    eig_pairs.sort(key=lambda x: x[0],reverse=True)
    # select the top k eig_vec
    feature = np.array([ele[1] for ele in eig_pairs[:k]])  
    # get new data
    data = np.dot(norm_X, np.transpose(feature))
    return data

# X=np.array([[1.1,2.3,4.2],[1.9,2.0,4.8]])
# print(pca(X,2))

#! 因为map里面不能直接传入 .real 所以我们自己写一个函数 
def func(x):
    return x.real

name_list = ['china', 'japan', 'car', 'canada', 'ship', 'uk', 'fish', 'usa', 'truck', 'dog', 'apple', 'cat',
             'airplane', 'bike', 'banana', 'rabbit', 'grape', 'peach', 'parrot', 'pear', 'motorbike', 'watermelon', 'hamster']

data = ['-0.22427 0.27427 0.054742 1.4692 0.061821 -0.51894 0.45027 -0.32164 0.57876 -0.049142 0.52523 -0.18784 0.52539 -0.058431 0.19741 0.30754 -0.45412 0.38268 0.33441 0.42801 0.98406 -0.7637 -0.066755 -1.0027 1.1942 -2.3916 0.24326 -0.40705 -0.63413 -0.20832 3.8851 0.75046 0.14857 0.24485 -1.0143 -0.76356 -0.63824 0.73037 -1.2025 0.18932 -1.2139 -0.55377 1.3033 -0.82461 0.9965 0.15117 -0.65753 0.28569 0.45374 -0.85646',
        '-0.31739 -0.14033 0.32292 1.072 0.33008 0.39406 -0.016682 0.076903 -0.74591 -0.31521 1.0033 -0.12659 0.063252 0.64006 0.70721 0.84303 -0.68832 0.47214 -0.66002 0.73962 1.1116 -0.89428 -0.90364 -0.47281 0.88529 -2.0194 0.30623 -0.31662 -0.44423 -0.52139 3.0287 0.70315 0.92315 0.52263 -0.62674 -0.58995 -0.15876 -0.078332 -1.0794 -0.71552 -1.2764 -0.85554 1.2827 -1.2134 1.0125 0.40329 -0.16276 0.99117 0.031016 -0.35431',
        '0.47685 -0.084552 1.4641 0.047017 0.14686 0.5082 -1.2228 -0.22607 0.19306 -0.29756 0.20599 -0.71284 -1.6288 0.17096 0.74797 -0.061943 -0.65766 1.3786 -0.68043 -1.7551 0.58319 0.25157 -1.2114 0.81343 0.094825 -1.6819 -0.64498 0.6322 1.1211 0.16112 2.5379 0.24852 -0.26816 0.32818 1.2916 0.23548 0.61465 -0.1344 -0.13237 0.27398 -0.11821 0.1354 0.074306 -0.61951 0.45472 -0.30318 -0.21883 -0.56054 1.1177 -0.36595',
        '-0.72491 0.40524 -0.35895 0.65977 -0.27592 0.60496 -1.217 0.14638 0.85096 -0.74799 1.0267 -0.0491 0.40083 -0.11647 0.14594 0.32253 0.38807 -0.72773 -1.0039 -0.015682 0.66613 -0.30068 -0.01085 0.57758 -0.26283 -1.3647 0.17607 -0.54651 -0.40292 -0.14113 2.3757 0.60026 0.072329 -0.4139 -0.30918 -1.166 -0.15287 -0.18237 -0.075067 -0.30076 -0.073329 -0.19173 1.1995 -1.1107 -0.57754 1.011 -0.81894 -0.11035 0.015073 -0.03693',
        '1.5213 0.10522 0.38162 -0.50801 0.032423 -0.13484 -1.2474 0.79813 0.84691 -1.101 0.88743 1.3749 0.42928 0.65717 -0.2636 -0.41759 -0.48846 0.91061 -1.7158 -0.438 0.78395 0.19636 -0.40657 -0.53971 0.82442 -1.7434 0.14285 0.28037 1.1688 0.16897 2.2271 -0.58273 -0.45723 0.62814 0.54441 0.28462 0.44485 -0.55343 -0.36493 -0.016425 0.40876 -0.87148 1.5513 -0.80704 -0.10036 -0.28461 -0.33216 -0.50609 0.48272 -0.66198',
        '-0.63409 0.18108 0.028813 -0.1784 -0.65473 0.52884 -0.9703 -0.27296 1.0972 -0.17847 0.88875 0.26315 -0.26504 0.15846 0.19695 0.26122 0.27818 0.19875 -0.56669 0.20624 1.4837 0.095874 0.52675 1.1784 -0.57104 -0.41051 -0.74757 -0.74453 -0.80702 0.70884 2.8986 -0.13579 0.56254 -0.11565 -0.059798 -0.097914 0.80612 -0.54111 -0.64891 -1.2123 0.60141 -1.019 0.10221 -0.75032 -0.28352 0.45793 -0.71373 -0.17897 0.1129 0.0098408',
        '0.2559 -0.31452 -1.0079 0.1434 0.52982 0.31531 -0.82169 0.0060026 1.5235 -0.40637 0.20401 0.93042 2.061 0.73117 0.44506 -0.0043559 1.2895 -0.16854 -1.1219 -0.80836 -0.19725 -1.2056 1.2739 0.23962 0.44387 -0.77988 0.1557 0.28534 1.0253 -0.61694 2.5009 -0.41019 0.57532 0.51033 -0.060849 0.40419 -0.34696 0.38221 0.629 -0.22291 -0.32009 0.21292 1.0723 0.32437 1.3304 0.54586 -0.22236 -0.80589 0.16487 0.29792',
        '-1.256 0.67149 0.1418 1.5068 -0.54231 -0.014556 -1.0648 -0.60224 0.55127 -0.67244 0.39114 -0.55533 -0.54794 -0.37832 0.35629 0.15954 0.030876 0.31742 -0.87051 0.21663 -0.30207 0.12983 0.19678 0.79039 -0.56554 -0.82879 -0.19614 -0.82778 -0.6898 -1.0809 1.8179 -0.26586 0.065575 -0.1093 -0.66603 -1.1031 0.12164 -0.29828 -0.0003941 -0.72735 0.905 -0.74758 0.76054 -0.4513 0.10696 0.8653 -0.43969 -0.47675 -0.91554 0.9724',
        '0.35016 -0.36192 1.505 -0.070263 0.32708 0.48106 -1.4825 0.07962 0.83452 -0.72912 0.19233 -0.90769 -0.89611 0.33796 0.42153 -0.47797 -0.47473 1.6142 -0.5358 -1.6758 0.64926 0.074053 -0.66378 0.66352 -0.11525 -1.46 -0.31867 0.99803 1.636 -0.11678 1.8673 -0.19582 -0.50549 0.82963 1.3381 0.33233 0.24957 -0.37286 0.2777 0.88405 -0.29343 -0.0033666 0.27167 -1.1805 0.53095 -0.31678 -0.3141 -0.31516 0.96377 -0.55119',
        '0.11008 -0.38781 -0.57615 -0.27714 0.70521 0.53994 -1.0786 -0.40146 1.1504 -0.5678 0.0038977 0.52878 0.64561 0.47262 0.48549 -0.18407 0.1801 0.91397 -1.1979 -0.5778 -0.37985 0.33606 0.772 0.75555 0.45506 -1.7671 -1.0503 0.42566 0.41893 -0.68327 1.5673 0.27685 -0.61708 0.64638 -0.076996 0.37118 0.1308 -0.45137 0.25398 -0.74392 -0.086199 0.24068 -0.64819 0.83549 1.2502 -0.51379 0.04224 -0.88118 0.7158 0.38519',
        '0.52042 -0.8314 0.49961 1.2893 0.1151 0.057521 -1.3753 -0.97313 0.18346 0.47672 -0.15112 0.35532 0.25912 -0.77857 0.52181 0.47695 -1.4251 0.858 0.59821 -1.0903 0.33574 -0.60891 0.41742 0.21569 -0.07417 -0.5822 -0.4502 0.17253 0.16448 -0.38413 2.3283 -0.66682 -0.58181 0.74389 0.095015 -0.47865 -0.84591 0.38704 0.23693 -1.5523 0.64802 -0.16521 -1.4719 -0.16224 0.79857 0.97391 0.40027 -0.21912 -0.30938 0.26581',
        '0.45281 -0.50108 -0.53714 -0.015697 0.22191 0.54602 -0.67301 -0.6891 0.63493 -0.19726 0.33685 0.7735 0.90094 0.38488 0.38367 0.2657 -0.08057 0.61089 -1.2894 -0.22313 -0.61578 0.21697 0.35614 0.44499 0.60885 -1.1633 -1.1579 0.36118 0.10466 -0.78325 1.4352 0.18629 -0.26112 0.83275 -0.23123 0.32481 0.14485 -0.44552 0.33497 -0.95946 -0.097479 0.48138 -0.43352 0.69455 0.91043 -0.28173 0.41637 -1.2609 0.71278 0.23782',
        '1.2977 -0.29922 0.66154 -0.20133 -0.02502 0.28644 -1.0811 -0.13045 0.64917 -0.33634 0.53352 0.32792 -0.43206 1.4613 0.022957 -0.26019 -1.1061 1.077 -0.99877 -1.3468 0.39016 0.43799 -1.0403 -0.36612 0.39231 -1.3089 -0.82404 0.63095 1.2513 0.10211 1.2735 -0.0050163 -0.39469 0.36387 0.65099 -0.21433 0.52291 -0.079013 -0.14676 0.89248 -0.31447 0.090903 0.78216 -0.10842 -0.3186 0.16068 -0.20168 -0.095033 -0.010109 0.19048',
        '-0.066264 0.63021 0.29176 0.09395 -0.86961 0.21042 -0.9703 -0.58522 1.2183 -0.47133 0.091659 -0.67721 -1.0019 -0.049824 0.32277 -0.25881 0.07404 1.366 -0.4845 -1.7933 0.0080712 0.11598 -1.1639 1.147 0.71514 -0.63385 -0.21022 0.41422 0.80306 -0.43057 1.5576 0.77082 -0.61563 0.85375 0.25721 -0.11993 0.45094 0.46682 -0.25706 0.29834 -0.021799 -0.50433 0.02875 0.62155 0.23333 -1.1492 0.78511 -1.4157 0.71565 -0.087735',
        '-0.25522 -0.75249 -0.86655 1.1197 0.12887 1.0121 -0.57249 -0.36224 0.44341 -0.12211 0.073524 0.21387 0.96744 -0.068611 0.51452 -0.053425 -0.21966 0.23012 1.043 -0.77016 -0.16753 -1.0952 0.24837 0.20019 -0.40866 -0.48037 0.10674 0.5316 1.111 -0.19322 1.4768 -0.51783 -0.79569 1.7971 -0.33392 -0.14545 -1.5454 0.0135 0.10684 -0.30722 -0.54572 0.38938 0.24659 -0.85166 0.54966 0.82679 -0.68081 -0.77864 -0.028242 -0.82872',
        '0.53049 -0.63657 -0.53314 -0.37542 0.28821 1.2374 -0.47467 -1.2037 0.58209 -0.55149 -0.2719 0.70193 0.74694 0.34327 0.65301 0.54077 0.66454 0.47677 -1.0837 0.12478 -0.15093 -0.66961 0.55866 0.60741 0.70239 -0.91675 -0.92081 0.59262 0.0070694 -0.95443 0.69853 -0.13292 -0.061585 1.206 -0.58842 0.43482 -0.19392 -0.19351 -0.07301 -0.85527 0.32885 0.57285 -0.57111 0.10893 1.0902 -0.028394 0.78458 -0.97332 0.36124 -0.056677',
        '0.23017 -0.33868 -1.4997 -0.35237 0.16379 0.44121 -0.99947 -0.92632 0.35382 0.92485 0.50485 -0.21886 1.2231 -1.4518 0.71129 -0.21506 0.83317 0.72531 0.11544 -1.5128 -1.1301 -1.5405 0.84343 0.8874 -0.54008 0.31496 -0.59696 0.91315 0.16258 0.055713 1.0624 -0.92158 -0.96032 0.44075 1.0285 -0.45583 -1.656 0.59739 0.49696 0.0047636 -0.09192 -0.11237 -0.30139 -0.81769 1.1218 0.10276 0.47661 -0.12207 -0.30815 -0.4438',
        '-0.57095 0.33932 -1.2084 1.2923 0.57294 0.31393 -0.80738 -0.034238 -0.14482 -0.13699 -0.229 -0.35615 1.0428 -0.70071 0.3643 0.141 -0.17213 0.44281 0.15271 -0.84283 -0.39486 -0.65414 0.62274 0.090617 -0.26859 0.5039 -0.59799 1.1291 0.71964 -1.0768 0.73573 -0.22215 -0.96374 0.91613 0.37015 0.29221 -1.0287 0.088322 0.874 -0.57386 -0.3051 0.27034 -1.4014 -1.1797 0.41814 0.55126 0.62792 -0.78958 0.036288 -0.51798',
        '0.89896 -0.83413 -1.2935 -0.16621 0.74272 0.22436 -0.71655 -0.8758 0.90983 -0.39252 0.59841 0.71412 1.7031 0.22926 0.30447 -0.23914 -0.33619 0.019467 -0.63332 -0.14014 -1.5712 0.042674 -0.016491 0.16081 0.43581 -0.25596 -0.22224 0.647 -0.56614 -0.44331 0.0085787 -0.5729 -0.17573 0.60776 -0.41806 0.14645 0.029666 -0.6182 -0.16481 -0.74397 0.37756 0.56168 0.052964 0.22831 0.58802 0.22718 -0.087574 -0.89636 0.16088 -0.34649',
        '0.47116 0.22231 -1.4249 0.99562 0.53151 0.57153 -0.1787 -0.65411 -0.56121 0.31099 -0.98784 0.22182 0.93362 -0.52826 0.052066 -0.066605 0.25394 0.29872 0.71139 -0.87365 -0.43599 -1.2379 0.98002 0.02822 -0.083416 0.65037 0.1941 1.186 -0.041302 -0.86553 0.91164 -0.90651 -0.20299 1.1567 0.42621 -0.2743 -1.6916 0.35706 0.85355 -0.60975 -0.25831 -0.024144 -0.69701 -0.46122 1.1413 0.53825 0.85636 -0.2622 -0.042144 -0.33228',
        '0.14362 -1.1402 0.39368 0.18135 -0.094088 0.67473 -0.52618 0.21466 0.62416 -0.17217 0.67109 -1.1389 -0.84819 0.085305 0.20975 -0.59836 -0.78554 1.21 -0.90412 -1.009 0.42731 0.39614 -1.0663 0.66758 0.54771 -0.93963 -0.31805 0.14893 0.4489 -0.1986 0.20147 0.47226 -0.31627 0.83248 0.84036 0.40339 0.24902 -0.034884 -0.11794 0.89527 -0.33927 0.13761 -0.037933 -0.26963 0.85965 -1.174 0.31216 -0.62433 1.4447 -1.0968',
        '-0.11169 -0.73634 -0.87099 0.66481 0.8636 -0.078829 0.52128 0.18377 0.21471 0.37623 -0.46969 -0.66462 0.948 -0.17327 0.661 -0.58227 0.079968 0.95237 0.60184 -0.4136 -0.23314 -1.007 1.3132 0.3262 -0.65398 0.40491 -0.60377 1.0947 0.58395 -1.0347 0.54564 0.10824 -0.33077 1.1553 -0.266 0.84132 -1.0607 0.7356 0.84014 -0.81504 -0.47628 -0.23533 -0.81993 -0.40683 0.98664 0.045194 0.4074 -0.41 0.22201 -0.25359',
        '1.1026 0.50368 -0.037258 0.53017 0.19914 1.0735 0.10698 -0.82408 0.07982 0.1144 0.92192 0.81057 0.63845 1.5007 0.10148 0.74576 -0.27965 1.5147 0.13098 -0.15711 -0.8353 -0.266 0.17888 0.41619 1.1804 0.039886 -0.26828 0.51415 -0.50759 -0.40541 -0.12056 0.55774 -0.64963 1.206 -0.47788 0.40368 0.11305 0.24027 -0.17974 -0.23764 -0.14685 -0.28751 -0.78451 0.59574 1.0964 -0.487 0.087508 -0.93495 0.63911 -0.86555']

data = [list(map(float, x.split())) for x in data]
data = np.array(data)
#print(data)
#print(pca(data, 2))#! 多了虚部 为什么变成了复数???

my_data=pca(data, 2)
my_data=np.array([list(map(func,temp)) for temp in my_data])
print(my_data)
print('-----------------')



pca=PCA(n_components=2)
pca.fit(data)
sklearn_data=pca.transform(data)
print(sklearn_data)


#!在同一个画布上画两个图 见收藏夹
#! 显示散点图的标签 见收藏夹
x_value1=my_data[:,0]
y_value1=my_data[:,1]
plt.subplot(1,2,1)
plt.scatter(x_value1,y_value1)
plt.title('My_PCA')
for i,txt in enumerate(name_list):
    plt.annotate(txt,(x_value1[i],y_value1[i]))
#plt.plot()



x_value2=sklearn_data[:,0]
y_value2=sklearn_data[:,1]
plt.subplot(1,2,2)
plt.scatter(x_value2,y_value2)
for i,txt in enumerate(name_list):
    plt.annotate(txt,(x_value2[i],y_value2[i]))
plt.title('Sklearn_PCA')
#plt.plot()
plt.show()


