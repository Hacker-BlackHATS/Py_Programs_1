"""
Sammy runs a famous burger shop where he prepares one burger at a time since it has a secret
ingredient. In a normal shop the customers are served by first come first serve policy. Sammy
thought though this is fair to customer but he wanted to maximize his profits so he devised an
alternative mechanism. There were hundreds of burger in his catalog, all of which took
different amount of time to cook because of different cooking style. He wanted to reduce the
time which a customer spends waiting on an average. So, if he has some pool of orders at any
point of time then he can choose any order to serve provided he meets his goal of reducing the
amount of time customer is waiting. The waiting time starts as soon as customer places an order
and the time at which he receives his order. Since the customer uses in store app to place the
order hence two customers can also place the order at the same time. Let's say we have three
customers who come at time t=0, t=1, & t=2 respectively, and the time needed to cook their
burgers is 3, 9 and 6 respectively. If Sammy applies first-come, first-served rule, then the
waiting time of three customers is 3, 11, & 16 respectively. The average waiting time in this
case is (3 + 11 + 16) / 3 = 10. This is not an optimized solution. After serving the first
customer at time t=4, Sammy can choose to serve the third customer. In that case, the waiting
time will be 3, 7, & 17 respectively. Hence the average waiting time is (3 + 7 + 17) / 3 = 9.

Input Format :
    The first line contains an integer N, which is the number of customers.
    In the next N lines, the ith line contains two space separated numbers Ti and Li.
    Ti is the time when ith customer order a burger, and Li is the time required to cook
    that burger.
    The ith customer is not the customer arriving at the arrival time.
    The order of entry can be in any order i.e. entry of t5 can be before t1.

Constraints :
    1 ≤ N ≤ 10^5 0 ≤ Ti ≤ 10^9 1 ≤ Li ≤ 10^9
"""