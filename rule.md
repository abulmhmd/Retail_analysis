**min_support**: support refers to the popularity of item and can be calculated by finding the number of transactions containing a particular item divided by the total number of transactions.

Support(diaper) = (Transactions containing (diaper))/(Total Transactions)

Support(diaper) = 150 / 1000 = 15 %

**min_confidence**: Confidence refers to the likelihood that an item B is also bought if item A is bought. It can be calculated by finding the number of transactions where A and B are bought together, divided by the total number of transactions where A is bought. Mathematically, it can be represented as:

Confidence(A -> B) = (Transactions containing both (A and B))/(Transactions containing A)

The confidence of likelihood of purchasing a diaper if a customer purchase milk.

Confidence(milk -> diaper) = (Transactions containing both (milk and diaper))/(Transactions containing milk)

Confidence(milk -> diaper) =30 / 120 = 25 %

Confidence is similar to Naive Based Algorithm.

**min_lift**: Lift refers to the increase in the ratio of the sale of B when A is sold. 

Lift(A -> B) can be calculated by dividing Confidence(A -> B) divided by Support(B). 
Mathematically it can be represented as:
Lift(A -> B) = (Confidence (A -> B))/(Support (B))

Lift(milk -> diaper) = (Confidence (milk -> diaper))/(Support (diaper))

Lift(milk -> diaper) = 25 / 15 = 1.66

So by Lift theory, there is 1.66 times more chance of buying milk and diaper together than just buying diaper alone.

**min_length**:  How many Items do we want to associate in our rules.

**RULES FOR APRIORI ALGORITHM:**

#### 1. Set a minimum value for support and confidence. This means that we are only interested in finding rules for the items that have certain default existence (e.g. support) and have a minimum value           for co-occurrence with other items (e.g. confidence).

#### 2. Extract all the subsets having a higher value of support than a minimum threshold.

#### 3. Select all the rules from the subsets with confidence value higher than the minimum threshold.

#### 4. Order the rules by descending order of Lift.