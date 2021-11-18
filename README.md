# Ex1

<b>The Research That We Done For This Project </b>
1. We looked in the following articles and researches to learn about elevators utilization and optimization.<br>
A forum discussion in programming forum where the people are talking about how to optimize elevators algorithm <br>
https://www.quora.com/What-are-ways-to-optimize-the-service-algorithm-for-an-elevator<br>
A research from Columbia university that explains about elevators optimization <br>
http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf<br>
The next articale we read is an articale that discuss about offline algorithm for elevators and how to optimize the algorithm <br>
https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...<br>

<b> How The Algorithm Works</b> <br>
2. The algorithm will work mainly on times, to decide which elevator will be assigned to a call we will check varies of things
to optimize avrerage time and to complete many calls as we can.
An elevator will use a function called time that calculate how long will it take to the elevator to complete it calls, then with this information we will check out if the optimized route it by sending faster elevator to more calls or to send it to the bigger interval of floors (e.g the fast elevator should take floor 0 to 100 and the slower will do floors (1,2,3,4,5,6,7,8 to 10) the slower elevator will do it slow but even slower if it goes from floor 0 to 100).

<b>UML Of The Project </b> <br>
3. diagram:<br>![image](https://user-images.githubusercontent.com/75334138/141819802-ecdafdc1-78ec-451e-959c-f86e764e8291.png)

<b>Tests That We Did In This Project </b><br>
4. we can use unitest to check our code and to see if it clean from bugs.
we can check if our classes fields are similar to the fields we defined.
we can check if our time function works good by calculating times and see if the output is same as we calculated
