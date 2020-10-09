**1. 项目简介：**

    爬取某个网站的所有小说。
    
**2. 环境依赖：**

    python==3.8.5
    pycharm专业版==2019.3.3 
    requests==2.24.0
    bs4==0.0.1
    multiprocess==0.70.10
    numpy==1.19.2
**3. 技术栈：**


    1.requests 进行 http/https 进行网络请求
    2.re 的 findall 函数对返回文本进行数据筛选
    3.bs4 的 BeautifulSoup 类获取网页返回文本的小说题目和小说文本
    4.multiprocess 创建进程池，并通过 Pool.map_async() 函数进行异步并发请求
    5.numpy 的 mean 函数计算平均每个请求的用时
    
**3. 结果展示：**

    ['2020/10/7/renqinvyou/478461.html', '2020/10/7/renqinvyou/478460.html', '2020/10/7/renqinvyou/478459.html', '2020/10/7/renqinvyou/478458.html', '2020/10/7/renqinvyou/478457.html', '2020/10/7/renqinvyou/478456.html', '2020/10/7/miqingxiaoyuan/478455.html', '2020/10/7/miqingxiaoyuan/478454.html', '2020/10/7/miqingxiaoyuan/478453.html', '2020/10/7/miqingxiaoyuan/478452.html', '2020/10/7/miqingxiaoyuan/478451.html', '2020/10/7/miqingxiaoyuan/478450.html', '2020/10/7/doushijiqing/478449.html', '2020/10/7/doushijiqing/478448.html', '2020/10/7/doushijiqing/478447.html', '2020/10/7/doushijiqing/478446.html', '2020/10/7/doushijiqing/478445.html', '2020/10/7/doushijiqing/478444.html', '2020/10/7/jiatingluanlun/478443.html', '2020/10/7/jiatingluanlun/478442.html', '2020/10/7/jiatingluanlun/478441.html', '2020/10/7/jiatingluanlun/478440.html', '2020/10/7/jiatingluanlun/478439.html', '2020/10/7/jiatingluanlun/478438.html', '2020/10/7/wuxiagudian/478437.html', '2020/10/7/wuxiagudian/478436.html', '2020/10/7/wuxiagudian/478435.html', '2020/10/7/lingleixiaoshuo/478434.html', '2020/10/7/lingleixiaoshuo/478433.html', '2020/10/7/lingleixiaoshuo/478432.html', '2020/10/7/lingleixiaoshuo/478431.html', '2020/10/7/huangsexiaohua/478430.html', '2020/10/7/huangsexiaohua/478429.html', '2020/10/7/huangsexiaohua/478428.html', '2020/10/7/huangsexiaohua/478427.html', '2020/10/7/huangsexiaohua/478426.html', '2020/10/7/huangsexiaohua/478425.html', '2020/10/7/xingaijiqiao/478424.html', '2020/10/7/xingaijiqiao/478423.html', '2020/10/7/xingaijiqiao/478422.html']
    ************************************************************************************************************************************************************************************************************************************************************************************************************
    31 ['https://222cce.com/htm/2020/10/7/renqinvyou/478461.html', 'https://222cce.com/htm/2020/10/7/renqinvyou/478460.html', 'https://222cce.com/htm/2020/10/7/renqinvyou/478459.html', 'https://222cce.com/htm/2020/10/7/renqinvyou/478458.html', 'https://222cce.com/htm/2020/10/7/renqinvyou/478457.html', 'https://222cce.com/htm/2020/10/7/renqinvyou/478456.html', 'https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478455.html', 'https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478454.html', 'https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478453.html', 'https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478452.html', 'https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478451.html', 'https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478450.html', 'https://222cce.com/htm/2020/10/7/doushijiqing/478449.html', 'https://222cce.com/htm/2020/10/7/doushijiqing/478448.html', 'https://222cce.com/htm/2020/10/7/doushijiqing/478447.html', 'https://222cce.com/htm/2020/10/7/doushijiqing/478446.html', 'https://222cce.com/htm/2020/10/7/doushijiqing/478445.html', 'https://222cce.com/htm/2020/10/7/doushijiqing/478444.html', 'https://222cce.com/htm/2020/10/7/jiatingluanlun/478443.html', 'https://222cce.com/htm/2020/10/7/jiatingluanlun/478442.html', 'https://222cce.com/htm/2020/10/7/jiatingluanlun/478441.html', 'https://222cce.com/htm/2020/10/7/jiatingluanlun/478440.html', 'https://222cce.com/htm/2020/10/7/jiatingluanlun/478439.html', 'https://222cce.com/htm/2020/10/7/jiatingluanlun/478438.html', 'https://222cce.com/htm/2020/10/7/wuxiagudian/478437.html', 'https://222cce.com/htm/2020/10/7/wuxiagudian/478436.html', 'https://222cce.com/htm/2020/10/7/wuxiagudian/478435.html', 'https://222cce.com/htm/2020/10/7/lingleixiaoshuo/478434.html', 'https://222cce.com/htm/2020/10/7/lingleixiaoshuo/478433.html', 'https://222cce.com/htm/2020/10/7/lingleixiaoshuo/478432.html', 'https://222cce.com/htm/2020/10/7/lingleixiaoshuo/478431.html']
    获取URL用时2.668358564376831
    ********** 下载完毕！！！ 1.2407960891723633
    ********** 下载完毕！！！ 1.7122986316680908
    ********** 下载完毕！！！ 1.6066803932189941
    ......
    ********** 下载完毕！！！ 5.666915655136108
    ********** 下载完毕！！！ 10.47487187385559
    ********** 下载完毕！！！ 16.813974380493164
    总用时32.888598680496216,平均用时3.517321748118247
    
  