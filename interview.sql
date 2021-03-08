
/* Question 1 */

/* Part 1 */
SELECT COUNT(blockchain)
FROM ethereum_transactions
BETWEEN DATE NOW() and NOW() - INTERVAL '1 DAY';


/* Part 2 */

SELECT DISTINCT
    address_from,
    COUNT(address_from) as mycount,
FROM
   etherium_transactions
    
BETWEEN DATE NOW() and NOW() - INTERVAL '1 DAY';


/* Question 2 */

SELECT * FROM ethereum_transactions JOIN address_labels USING(label) WHERE label = 'Coinbase';


/* Question 3 */

SELECT SUM (amount) AS total
FROM ethereum_transations
  


/* Question 4 */
SELECT DISTINCT
    address_from,
    COUNT(address_from) as mycount,
FROM
   ethereum_transactions

ORDER BY 
    mycount DESC

FETCH FIRST 10 ROW ONLY;



    