# Lab 2: Closed Loop Controller Test System

This lab utilizes a motor and encoder to create a clossed loop controller. 

---

### Step Response of System with Gain of 0.05

![IdealGainResponse](/docs/kP_05.png)

This is the step response obtained when using a gain of kP = 0.05.
This gain gives the best balance of time to reach position vs reduced overshoot.

---
### Step Response of System with Gain of 0.15

![NonIdealGainResponse](/docs/kP_15.png)

This is the step response obtained when using a gain of kP = 0.15.
This gain leads to an increase in overshoot over kP = 0.05.

---
### Step Response of System with Gain of 0.03

![NonIdealGainResponse2](/docs/kP_03.png)

This is the step response obtained when using a gain of kP = 0.03.
The time to reach the final position is much longer than with gaine kP = 0.05.

---
