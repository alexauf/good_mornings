import selenium
from numpy import arange
from random import sample
from sys import exit
from time import sleep
from progress.spinner import Spinner
from progress.bar import ChargingBar
from threading import Thread
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def worker():

	finish = False

	sp = Spinner('Loading     ')
	cont = 0

	while(not finish):

		sleep(1)
		cont +=1
		if(cont == 60):
			finish = True
		sp.next()

	return


class YouMotivate:

    def __init__(self):

        print('Managing Firefox Info')
        t = Thread(target=worker)
        t.start()

        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        fp = (r'C:\Users\AlexMS\AppData\Roaming\Mozilla\Firefox\Profiles\hoaiefpi.default-release')
        opts = Options()
        # opts.add_argument("--headless")
        opts.add_argument(r'load-extension=C:\Users\AlexMS\AppData\Roaming\Mozilla\Firefox\Profiles\hoaiefpi.default-release\extensions\uBlock0@raymondhill.net.xpi')
        opts.profile = fp
        self.driver = webdriver.Firefox(options=opts,
                        executable_path='C:\WebDrivers\geckodriver')


        print('Firefox Info Loaded succesfully')
        print('Opening Youtube...')

        self.driver.get("https://www.youtube.com/playlist?list=FLHcrPEhUkZW37RI7c5FQvtw")
        sleep(4)


        #get num of videos in the list
        num = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-primary-info-renderer/div[1]/yt-formatted-string[1]')
        num = int(num.text.split(' ')[0])
        # print('NUM OF VIDEOS:\t' + str(num))

        vids = sample(list(arange(1,num+1)), 3)
        # print('CHOOSEN:\t' + str(vids))

        #choose those videos and open it in new tabs
        bar = ChargingBar(' Opening videos', max=len(vids))
        for i in vids:

            vid_ref = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer['+str(i)+']/div[2]/a')
            ref = vid_ref.get_attribute("href")
            # print(ref)

            self.driver.execute_script("window.open('"+str(ref)+"', 'new_window_"+str(i)+"')")
            # self.driver.execute_script('browser.tabs.create({url:"'+str(ref)+'"});')

            bar.next()

        bar.finish()


ym = YouMotivate()
exit()
