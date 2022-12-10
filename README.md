# Drunkards going home
### Backend dev task 2022Q1

## The story...
Loads of people are waiting for 代行 coming to pick them up, waiting sometimes for more than two hours despite there being available drivers where they don't know... And there's too many phone numbers to call while drunk! Help everyone get help quicker!
## Description
In Takamatsu City there's a lot of 代行 but it's a pain to call all of them while being drunk so there's more and more people asking for some common solution where you can check all companies availability at the same time and request a driver to a certain spot.

The platform needs to be highly scalable and performant. There's also a need to easily develop new features no matter what development environment you are using.  

For performance reasons the leads have decided that they want the platform to use the flashy gRPC framework for client-server communication for the web app.  

The platform must enable the customers to
1. Request a driver to a specific location immediately or at a specific time
    - With it provide necessary from and to locations
    - Register personal information
The platform might enable the customers to
2. Cancel a performed request for a driver
3. See a list of historical requests made
4. See how much time is left until the driver comes or if it's going to be delayed in real time
## So basically...
This task is focused on the architectural part but you also need to implement this platform. How you do it is up to you. Remember that there's a must and might - meaning that must is something you have to support but might is something you may do if you have time & energy. You decide yourself how you want to approach this problem and what tools & design patterns you use.

But I want you to use Git so that I can see how you step by step build your code (one commit for everything is a big no-no).

Don't put time into the visual design.
I care more about your structure, way of thinking than the rest.