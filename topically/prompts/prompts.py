# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

generic_cluster_naming_prompt = """
This is a list of clusters of messages . Each cluster contains a collection of messages about the same topic. Then a name of collection is mentioned. The name of each cluster is a short, highly-descriptive title
---
Cluster:
Sample texts from this cluster:
- Yosemite - Merced River
- Just before jump into the Merced River wallpaper
- silvermirage: First Snow on the Merced River [Photographer: Chris Cabot]
- Three Brothers - Merced River - Yosemite - 2010
- Merced River in Winter

Cluster name: Merced River
---
Cluster:
Sample texts from this cluster:
- Sara Coolidge - Half Dome Sunset
- Orange Shades over Half Dome
- Descent from Mt Hoffman, vew of Half Dome at sunset
- Half_Dome_at_Sunset_Sentinel_Bridge_3691
- Gary Hart Photography: Last Light, Half Dome, Yosemite

Cluster name: Half Dome at sunset
---
Cluster:
Sample texts from this cluster:
- The Domes of the Yosemite: 1870 by Albert Bierstadt (Amon Carter Museum of American Art, Fort Worth, TX) - Hudson River School
- Valley of the Yosemite by Albert Bierstadt
- ""Domes of Yosemite" by Albert Bierstadt - Uploaded by Vermont Humanities"
- Albert Bierstadt - Domes of the Yosemite
- Valley of the Yosemite (1864), Albert Bierstadt

Cluster name: The Domes of the Yosemite
---
Cluster:
Sample texts from this cluster:
- Hi I need your assistance - client ordered the wrong bathroom hardware and I'm trying to return it - it says beyond the return time but we'd appreciate it (unopened)
- ordered a JBL CHARGE3 on Black Friday. Unplugged it the first time it does this help! maybe you can help too? I don't want a return just a new cord.
- I just wanted to know what do you mean by "working condition" for old phone exchange??
- Hi I have a defective product and the seller is being astonishingly unhelpful, please could you advise?
- How do I report a missing item? Like not in the box with everything else. Your site is useless for this. Thanks!

Cluster name: Returns and exchanges of defective, damaged, or missing products
---
Cluster:
Sample texts from this cluster:
- I paid extra for Next day delivery (to be delivered today: saturday) however on the delivery tracking timeline it says expected delivery Monday. Can you look into why this is the case please? And when it actually will arrive so I can make sure I'm home.
- isn't prime two day shipping supposed to be guaranteed? what happens when its late?
- what do you mean by 2-day shipping? customer care executive is saying that 2-day shipping means we can ship anytime and 2 days are counted after shipping. why is he fooling ?
- the products in my cart have free shipping. Does this mean there is free shipping to all countries? (That are available for shipping ofc)

Cluster name: Shipping and delivery issues
---
"""

customer_service_tweets_prompt = """
This is a list of clusters of messages sent by customers to the customer service department of ecommerce company. Each cluster contains a collection of messages about the same topic. In addition to a sample of the messages, a list of keywords describing the collection is mentioned in addition to the name of the collection. The name of each cluster is a short, highly-descriptive title
---
Cluster #0
Sample messages from this cluster:
- I paid extra for Next day delivery (to be delivered today: saturday) however on the delivery tracking timeline it says expected delivery Monday. Can you look into why this is the case please? And when it actually will arrive so I can make sure I'm home.
- isn't prime two day shipping supposed to be guaranteed? what happens when its late?
- what do you mean by 2-day shipping? customer care executive is saying that 2-day shipping means we can ship anytime and 2 days are counted after shipping. why is he fooling ?
- the products in my cart have free shipping. Does this mean there is free shipping to all countries? (That are available for shipping ofc)

Keywords for messages in this cluster: ups, late, monday, tomorrow, paid day, extra, arrive, delivered, day delivery, day shipping
Cluster name: Shipping and delivery issues

---
Cluster #1
Sample messages from this cluster:
- I filled the form and submitted. I hope you solve my issue as I spent 40k and got nothing in return
- Who can I contact with a complaint. I've used Chat and been offered an unsatisfactory resolution.
- I have called 4 times and each time I am told the investigation is ongoing - seems to be no sense of urgency
- hey folks.. My Icoffee that I bought died on me and I want to get it fixed but website is down and nobody answers the phone
- I contacted you last week and filled in a form as requested but i still haven't had anybody contact me to resolve the issue. please can somebody contact me ASAP

Keywords for messages in the cluster: mail address, blocked, reply, email address, speak, response, mail, fax, fraud, complaint
Cluster name: New and unresolved complaints
---
Cluster #2
Sample messages from this cluster:
- Hi I need your assistance - client ordered the wrong bathroom hardware and I'm trying to return it - it says beyond the return time but we'd appreciate it (unopened)
- ordered a JBL CHARGE3 on Black Friday. Unplugged it the first time it does this help! maybe you can help too? I don't want a return just a new cord.
- I just wanted to know what do you mean by "working condition" for old phone exchange??
- Hi I have a defective product and the seller is being astonishingly unhelpful, please could you advise?
- How do I report a missing item? Like not in the box with everything else. Your site is useless for this. Thanks!
Keywords for messages in the cluster: warranty, returned, exchange, return item, label, defective, refund, replacement, damaged, return
Cluster name: Returns and exchanges of defective, damaged, or missing products
---"""

news_article_headlines_prompt = """
This is a list of clusters of news article headlines. Each cluster contains a collection of headlines about the same topic. In addition to a sample of the headlines, the name of the cluster is mentioned. The name of each cluster is a short, highly-descriptive title.
---
Cluster #0
Sample headlines from this cluster:
- 

Cluster name:

---
Cluster #1
Sample headlines from this cluster:
- 

Cluster name:

---
Cluster #2
Sample headlines from this cluster:
- 

Cluster name:

---
"""
