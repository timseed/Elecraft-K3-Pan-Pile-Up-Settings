#Elecraft P3 Panadapter

The P3 is Visual display of the RF spectrum, it is what the high end radio have been using for the past 20 years (IC-9000).

I am using this in conjunction with the Elecraft K3-S, their latest 100W transceiver.


#Problem

There is no problem like it does not work... it just does not work out of the box like I want it to.



##Visualisation


There is a DX Station on 14.020
You have the Centre of the spectrum as 14.020 in the K3 - it is also the same in the P3.
In the P3 you set the span to being 5Khz (that is 14.015 - 14.025)

Well 99% of all DX is positive (apart from some US/EU band stupidity).

**So What ?** you say..... I am not trying to see the place where the DX station is talking too in 50% of the screen size - with less than half the screen resolution (5Khz insitead of 2.5 Khz)


##Help
I got pointed in the right general direction by Dave (NK7Z) - but he told me the Macro's can not be strung togather.

Initially I did not believe him - but alas he seems very correct.

I think this reason is given from this extract from the Elecraft manual

###Response Time
The K3 will typically respond in less than 10 milliseconds. General worst-case latency is around 100 ms, except for commands that change bands, which can take up to 500 ms. 

At the bottom of this simple code - you will notice a time.sleep(1) This gives enough delay to allow the commands to be processed. Without this - this code will fail (you have been warned).


This code is written in Python3 - it needs 1 Module installing that module is called PySerial. You will probably need to alter the device name of your interface that is the line sp = Serial('/dev/tty.usbserial-A7004VW8', 38400, timeout=1)



#What this is trying to do

  * Assumes you are listening on the DX Station in VFO-A
  * Assumes that you want to place the DX Station in the LEFT-HAND-EDGE on the P3 Screen
  * You you can conduct a S&P type QSO


If that is the case simple run

```python
python p3_cw.py
```

To reset the Panadapter afterwards

```python
python reset.py
```

Note: You will have to edit the code to add your interface (I may fix this from the command line soon).


