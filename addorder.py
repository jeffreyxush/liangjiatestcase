from selenium import webdriver
import time

url="https://23vf634893.51mypc.cn"
wd=webdriver.Chrome()  # 打开 Chrome 浏览器

def login(username,password):

   
    ## 打开百度浏览器
    wd.get(url+'/tsHANILWFj.php/index/login')
    # 定位输入框并输入关键字
    wd.find_element_by_id('pd-form-username').send_keys(username)
    # 点击[百度一下]搜索
    wd.find_element_by_id('pd-form-password').send_keys(password)
    time.sleep(2)
    wd.find_element_by_tag_name('button').click()
    time.sleep(2)

def makeorder():


    #测试代码
    #wd.get('http://liangjiawang.jeffreyitstudio.com/tsHANILWFj.php/user/user?addtabs=1')

    #新增订单链接
    #wd.get('http://liangjiawang.jeffreyitstudio.com/tsHANILWFj.php/recorder/order?addtabs=1')


    wd.get(url+'/tsHANILWFj.php/recorder/order/add?dialog=1')

    #wd.find_element_by_xpath("(//span[text()='商户管理'])[1]").click()
    #time.sleep(2)

    #wd.find_element_by_xpath("(//span[text()='商户管理'])[2]").click()


    #time.sleep(4)
    #测试代码
    #wd.find_element_by_xpath("//div[@id='one']/div[1]/div[1]/div[3]/div[5]/div[2]/table[1]/tbody[1]/tr[1]/td[14]/a[4]/i[1]").click()

    #wd.find_element_by_xpath("(//div[@id='toolbar']//a)[2]").click()

    time.sleep(3)
    wd.find_element_by_id("c-name").send_keys('徐先生')
    wd.find_element_by_id("c-service").send_keys('小张')
    wd.find_element_by_id("c-mobile").send_keys('123456')
    wd.find_element_by_id("c-area").send_keys('100')
    wd.find_element_by_id("c-budget").send_keys('1000000')
    wd.find_element_by_id("lng").send_keys('121.69856')
    wd.find_element_by_id("lat").send_keys('121.69856')
    wd.find_element_by_id("address").send_keys('上海市上海市浦东新区龙东大道6101号B-2号')
    wd.find_element_by_id("c-detailed_address").send_keys('上海市上海市浦东新区龙东大道6101号B-2号')
    wd.find_element_by_id("c-room_number").send_keys('101')
    wd.find_element_by_id("c-content").send_keys('房子很大')
    wd.find_element_by_xpath("//button[text()='确定']").click()

    time.sleep(5)
    

def quit():
    wd.quit() 