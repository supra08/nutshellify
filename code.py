import web

# -*- coding: utf-8 -*-
import indicoio

import requests
import json
from bs4 import BeautifulSoup

#---------------------------------
app_id = 'ab613e1f'
app_key = 'f4d01407f8c87890c34470ef3af2a4c1'

language = 'en'
#__________________________________

#__________________________________
subscription_key="5d162a1f02724f6daf4489f4220413a4"
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

#___________________________________

#x = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
#req = requests.get(x)
#soup = BeautifulSoup(req.text, "lxml")

#print(soup.h1)
indicoio.config.api_key = '9676afc992432e62687fc09e1dc059b3'
#x = indicoio.summarization('Brazil hit by more punches amid historic recession Brazil\'s problems keep piling up. Amid its historic recession, things are getting worse for many Brazilians since an impeachment trial began last May against former President Dilma Rousseff, who was forced to step down in late August. About 12 million Brazilians are now out of work, up from 8.8 million a year ago, recent government figures show. On Tuesday, officials announced that Brazils industrial production declined so much in August, it wiped out the gains from the past five months. The International Monetary Fund gave a rough assessment of Brazil as well on Tuesday. "Confidence appears to have bottomed out in Brazil," IMF economists wrote in their World Economic Outlook. "Policy credibility has been severely dented by events leading up to the regime change." Brazil is mired in in its longest recession since the 1930s and the IMF estimates meager growth next year. Latin Americas largest economy shrank 3.8 last year and the IMF now forecasts it will fall another 3.3% this year. Brazils job market is in tatters. Wages in Brazil declined 3 in August and the unemployment rate rose to 11.8%, up from 8.7 a year ago. Industrial production in Brazil declined 3.8 in August compared to July, negating five months of improvement. Brazils new president, Michel Temer, took over in May and brought in a new team of market-friendly leaders to steer the economy out of recession. Not everyone is convinced things are changing quickly enough. "While the government maintains a market-friendly rhetoric, the pace of reforms have been disappointing," says Dan Raghoonundon, a Latin American equity analyst at Janus Capital, a U.S. investment firm. Its also unclear how much Temer will get done with an approval rating of 14%, according to Brazilian polling firm Datafolha. Protesters are already calling for Temers resignation. Three of his cabinet officials resigned over the summer after they were accused of allegedly accepting bribes. Rousseff, the former president, was impeached for manipulating the countrys budget numbers right before an election in 2014. However, a massive bribery scandal at Brazils state-run oil company, Petrobras, largely triggered the countrys severe recession. ')
#x = indicoio.summarization('Russia was the first to order a partial mobilization of its armies on 24–25 July, and when on 28 July Austria-Hungary declared war on Serbia, Russia declared general mobilization on 30 July.[13] Germany presented an ultimatum to Russia to demobilise, and when this was refused, declared war on Russia on 1 August. Being outnumbered on the Eastern Front, Russia urged its Triple Entente ally France to open up a second front in the west. Over forty years earlier in 1870, the Franco-Prussian War had ended the Second French Empire and France had ceded the provinces of Alsace-Lorraine to a unified Germany. Bitterness over that defeat and the determination to retake Alsace-Lorraine made the acceptance of Russia\'s plea for help an easy choice, so France began full mobilisation on 1 August and, on 3 August, Germany declared war on France. The border between France and Germany was heavily fortified on both sides so, according to the Schlieffen Plan, Germany then invaded neutral Belgium and Luxembourg before moving towards France from the north, leading the United Kingdom to declare war on Germany on 4 August due to their violation of Belgian neutrality.[14][15] After the German march on Paris was halted in the Battle of the Marne, what became known as the Western Front settled into a battle of attrition, with a trench line that changed little until 1917. On the Eastern Front, the Russian army led a successful campaign against the Austro-Hungarians, but the Germans stopped its invasion of East Prussia in the battles of Tannenberg and the Masurian Lakes. In November 1914, the Ottoman Empire joined the Central Powers, opening fronts in the Caucasus, Mesopotamia and the Sinai. In 1915, Italy joined the Allies and Bulgaria joined the Central Powers; Romania joined the Allies in 1916, as did the United States in 1917.')
#print (x[0])

urls = ('/', 'index', '/textarea', 'textarea', '/otherinput', 'otherinput', '/phrase', 'phrase')

app = web.application(urls, globals(), True)

web.config.debug = True

class index:

	def __init__(self):
		self.render = web.template.render('templates/')

	def GET(self):
		user_data = web.input(id = 'https://wiki.metakgp.org/w/Code.Fun.Do')
		#data_new = web.input(name = 'none')
		x = user_data.id
		#yg = data_new.name
		#x = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
		req = requests.get(x)
		soup = BeautifulSoup(req.text, "lxml")

		



		tagh1 = soup.find_all('h1')

		tagh2 = soup.find_all('h2')

		yes = [] 

		count = 0

		for h1s in tagh1:

			if(h1s.name == 'h1'):

				yes.append(h1s.text)

		for h2s in tagh2:

			middata = []

			if(h2s.text == 'See also' or h2s.text == 'References' or h2s.text == 'See also[edit]' or h2s.text == 'References[edit]'):

				break

			if(h2s.text != 'Contents'):

				yes.append(h2s.text)

				for midpara in h2s.nextSiblingGenerator():

					if(midpara.name == 'h2'):

						break

					middata.append(midpara)

					pdata = []

				for somedata in middata:

					if(somedata.name == 'h3'):

						#newtext = ' '.join(pdata)
						#ftext = indicoio.summarization(newtext.text)
						#yes.append(ftext)
						ndata = ' '.join(pdata)
						yes.append(ndata)

						pdata = []

						yes.append(somedata.text)

						count = 1

					if(somedata.name == 'p'):

						pdata.append(somedata.text)

						ftext = '.'.join(pdata)

						newdata = indicoio.summarization(ftext)
						pdata = newdata

						#pdata = indicoio.summarization(pdata)
						#textnew = ' '.join(summnew)
						#pdata = textnew
						#pdata = '.'.join(pdata)

				if(count == 0):

					#newtext = ' '.join(pdata)
					#ftext = indicoio.summarization(newtext.text)
					mdata = ' '.join(pdata)
					yes.append(mdata)





		y = soup.find_all('p')
		o = y[0].text

		z = []


		#for i in range(0, len(yes)):
		#	z.append(indicoio.summarization(yes[i]))
		#finaltext = ' '
		#finaltext = ' '.join(yes);
		#summtext = indicoio.summarization(finaltext)
		# text = ''

		# for i in range(0, len(z)):
		# 	text = text + z[i] + '\n'

		return self.render.index(yes)

	def POST(self):
		data = web.input().textfield
		word_id = data

		url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

		r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
		#x = json.dumps(r.json())

		data2 = json.loads(r.content)
		mean = data2["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
		return (mean)

class textarea:
	def POST(self):
		data = web.input().textarea
		textf = indicoio.summarization(data)
		text = ' '.join(textf)
		return text

class otherinput:
	def POST(self):
		data = web.input().textarea
		req = requests.get(data)
		soup = BeautifulSoup(req.text, "lxml")
		tagp = soup.find_all('p')

		final = []

		for tag in tagp:
			textf = indicoio.summarization(tag.text)
			textff = ' '.join(textf)
			final.append(textff)

		return final

class phrase:
	def POST(self):
		data = web.input().textfield
		return (data + " hi")






    	
if __name__ == '__main__':app.run()

