# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

generic_cluster_naming_prompt_keybert = """
This is a list of clusters of messages. Each cluster contains a collection of messages about the same topic. Then a name of collection is mentioned and the cluster name and the collection of messages should correlate. The name of each cluster is a short, highly-descriptive title and it should be grammatically coherent. 
---
Cluster:
Sample texts from this cluster:
- Please help me with my card. It won't activate
- I want to start using my card., How do I verify my new card?
- I tried activating my plug-in and it didn't piece of work
- I am not able to activate my card
Keywords: unable activate card
Cluster name: About Card Activation Issue
---
Cluster:
Sample texts from this cluster:
- I want to open an account for my children
- How old do you need to be to use the banks services?
- Whats the minimum age to have an account
- Can my children open an account?, How old do I need to be?
- I would like to open an account for my child
keywords: account children open
Cluster name: How to open an account for Minor
---
Cluster:
Sample texts from this cluster:
- Is there a top-up fee for transfer?
- Will there be a charge for topping up by account with a SEPA transfer?
- What are the charges for receiving a SEPA transfer?
- Is there a charge for SEPA transfers?
- Will I be charged a fee for a SEPA transfer?
Keywords: sepa transfers charged
Cluster name: About Transfer Fee
---
Cluster:
Sample texts from this cluster:
- Why do you have an identity check?
- I do not feel comfortable verifying my identity
- Why on earth do you need so much personal id info from me?
- DO you know the reason for the identity check?
- I answered so many questions about my identity. Why do you need this info?
keywords: reason identity check
Cluster name: About Reasoning Identity Check
---
Cluster:
Sample texts from this cluster:
- atm cash limits
- atm withdrawal limit
- automated teller machine cash withdrawal limit
- how much can i take out from the atm at once
- how much can i take out from the atm per day
- how much cash can be withdrawn from an atm on a daily basis
- How much cash can I get from an ATM?
keywords: cash withdrawn atm
Cluster name: About ATM Withdrawal Limit
--
"""

