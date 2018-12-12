# > scrapy shell 'http://lemonde.fr'
# > response.css('title')
# > response.css('title::text')
# > response.urljoin(response.css('a::attr(href)').extract()[8])
# > [response.urljoin(response.css('a::attr(href)').extract()[i]) for i in range(0, len(response.css('a::attr(href)').extract()))]

# Exercice : Utiliser une liste compréhension pour transformer les 10 premiers liens relatifs
# récupérés par la méthode extract() en liens absolus.
# > [response.urljoin(response.css('a::attr(href)').extract()[i]) for i in range(0, 10)] 


# > 
# > 
# > 