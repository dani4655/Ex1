# Ex1
<b> By Segev Tzabar And Daniel Fridman<br> ID:315314609, 206760290</b>

<b>The Research That We Done For This Project </b>
1. We looked in the following articles and researches to learn about elevators utilization and optimization.<br>
A forum discussion in programming forum where the people are talking about how to optimize elevators algorithm <br>
https://www.quora.com/What-are-ways-to-optimize-the-service-algorithm-for-an-elevator<br>
A research from Columbia university that explains about elevators optimization <br>
http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf<br>
The next articale we read is an articale that discuss about offline algorithm for elevators and how to optimize the algorithm <br>
https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...<br>

<b> How The Algorithm Works</b> <br>
2.The way that the algorithm works it very simple and very effective, we made a method called "time" ⏲️,<br>
this method calculates the time it takes to an elevator to go from floor a to floor b by summing the times it takes to the elevator to open and close it doors and the times it takes to the elevator to start and stop moving plus the distance from floor a to floor b divides by the speed of the elevator.<br>
Now when we have a super simple function that calculate the times, we will run over all the calls and then over all the elevators and we check which elevator will do the call in the best time. When an elevator is chosen to take a call we add to a special counter in that we made in the class elevator that will count how many calls this elevator already took<br> 
With this information, a faster elevators will take more calls and harder calls and the slower elevators will do the simpler calls.


<b>UML Of The Project </b> <br>
3. diagram:<br>![image](https://user-images.githubusercontent.com/75334138/142442804-232330ac-fb43-4a14-a7ab-89f65418c79c.png)

<b>Tests That We Did In This Project </b><br>
4. we can use unitest to check our code and to see if it clean from bugs.
we can check if our classes fields are similar to the fields we defined.
we can check if our time function works good by calculating times and see if the output is same as we calculated. <br>
Also we will create new buildings with easy situations to calculate and then we will see in the unitest if our calculations are same like the simulator results.
