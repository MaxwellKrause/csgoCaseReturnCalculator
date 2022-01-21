import selenium
from selenium import webdriver

urls = ['https://csgostash.com/case/308/Operation-Broken-Fang-Case','https://csgostash.com/case/307/Fracture-Case','https://csgostash.com/case/303/Prisma-2-Case','https://csgostash.com/case/293/CS20-Case','https://csgostash.com/case/277/Shattered-Web-Case','https://csgostash.com/case/274/Prisma-Case','https://csgostash.com/case/259/Danger-Zone-Case','https://csgostash.com/case/244/Horizon-Case','https://csgostash.com/case/238/Clutch-Case','https://csgostash.com/case/220/Spectrum-2-Case','https://csgostash.com/case/208/Operation-Hydra-Case','https://csgostash.com/case/207/Spectrum-Case','https://csgostash.com/case/179/Glove-Case','https://csgostash.com/case/172/Gamma-2-Case','https://csgostash.com/case/144/Gamma-Case','https://csgostash.com/case/141/Chroma-3-Case','https://csgostash.com/case/112/Operation-Wildfire-Case','https://csgostash.com/case/111/Revolver-Case','https://csgostash.com/case/80/Shadow-Case','https://csgostash.com/case/50/Falchion-Case','https://csgostash.com/case/48/Chroma-2-Case','https://csgostash.com/case/38/Chroma-Case','https://csgostash.com/case/29/Operation-Vanguard-Weapon-Case','https://csgostash.com/case/19/eSports-2014-Summer-Case','https://csgostash.com/case/18/Operation-Breakout-Weapon-Case','https://csgostash.com/case/17/Huntsman-Weapon-Case','https://csgostash.com/case/11/Operation-Phoenix-Weapon-Case','https://csgostash.com/case/10/CS:GO-Weapon-Case-3','https://csgostash.com/case/7/Winter-Offensive-Weapon-Case','https://csgostash.com/case/5/eSports-2013-Winter-Case','https://csgostash.com/case/4/CS:GO-Weapon-Case-2','https://csgostash.com/case/3/Operation-Bravo-Case','https://csgostash.com/case/2/eSports-2013-Case','https://csgostash.com/case/1/CS:GO-Weapon-Case']
driver = webdriver.Firefox()
driver.set_window_size(1920, 1080)
f = open('contents.txt', 'a', encoding="utf-8")


for i in urls:
    page2 = True
    gloves = False
    skins = []
    driver.get(i)
    loop = True
    counter = 2
    exceptCount = 0
    while(loop):
        try:
            name = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div[' + str(counter) + ']/div/h3/a[1]').text + ' | ' + driver.find_element_by_xpath('/html/body/div[2]/div[7]/div[' + str(counter) + ']/div/h3/a[2]').text
            counter = counter + 1
            skins.append(name)
        except Exception as e:
            if exceptCount != 0:
                print('skin:',e)
                loop = False
                pass
            else:
                exceptCount = exceptCount + 1
                counter = counter + 1
    if(i == 'https://csgostash.com/case/308/Operation-Broken-Fang-Case' or i == 'https://csgostash.com/case/238/Clutch-Case' or i == 'https://csgostash.com/case/208/Operation-Hydra-Case' or i == 'https://csgostash.com/case/179/Glove-Case'):
        driver.get(i + '?Gloves=1')
        gloves = True
    else:
        driver.get(i + '?Knives=1')
    loop = True
    counter = 2
    exceptCount = 0
    while (loop):
        try:
            if gloves:
                name = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div[' + str(counter) + ']/div/h3/a').text
            else:
                name = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div[' + str(
                    counter) + ']/div/h3/a[1]').text + ' | ' + driver.find_element_by_xpath(
                    '/html/body/div[2]/div[7]/div[' + str(counter) + ']/div/h3/a[2]').text
            counter = counter + 1
            skins.append(name)
        except Exception as e:
            if exceptCount != 0:
                print('knife:',e)
                loop = False
                pass
            else:
                exceptCount = exceptCount + 1
                counter = counter + 1
    if(i == 'https://csgostash.com/case/308/Operation-Broken-Fang-Case' or i == 'https://csgostash.com/case/238/Clutch-Case' or i == 'https://csgostash.com/case/208/Operation-Hydra-Case' or i == 'https://csgostash.com/case/179/Glove-Case'):
        try:
            driver.get(i + '?Gloves=1&page=2')
        except:
            page2 = False
            pass
    else:
        try:
            driver.get(i + '?Knives=1&page=2')
        except:
            page2 = False
            pass
    if page2:
        loop = True
        counter = 2
        exceptCount = 0
        while (loop):
            try:
                if gloves:
                    name = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div['+str(counter)+']/div/h3/a').text
                else:
                    name = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div[' + str(
                        counter) + ']/div/h3/a[1]').text + ' | ' + driver.find_element_by_xpath(
                        '/html/body/div[2]/div[7]/div[' + str(counter) + ']/div/h3/a[2]').text
                counter = counter + 1
                skins.append(name)
            except Exception as e:
                if exceptCount != 0:
                    print('knife:', e)
                    loop = False
                    pass
                else:
                    exceptCount = exceptCount + 1
                    counter = counter + 1


    for i in skins:
        f.write(i+'^')
    f.write('\n')
f.close()