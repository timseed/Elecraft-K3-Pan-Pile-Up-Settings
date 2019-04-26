# Elecraft P3 Panadapter

The P3 is Visual display of the RF spectrum, it is what the high end radio have been using for the past 20 years (IC-9000).

I am using this in conjunction with the Elecraft K3-S, their latest 100W transceiver.


# Problem

There is no problem like it does not work... it just does not work out of the box like I want it to.


## Visualisation


There is a DX Station on 14.020
You have the Centre of the spectrum as 14.020 in the K3 - it is also the same in the P3.
In the P3 you set the span to being 5Khz (that is 14.015 - 14.025)

Well 99% of all DX is positive (apart from some US/EU band stupidity).

**So What ?** you say..... I am not trying to see the place where the DX station is talking too in 50% of the screen size - with less than half the screen resolution (5Khz insitead of 2.5 Khz)


## Help
I got pointed in the right general direction by Dave (NK7Z) - but he told me the Macro's can not be strung togather.

Initially I did not believe him - but alas he seems very correct.

I think this reason is given from this extract from the Elecraft manual

### Response Time
The K3 will typically respond in less than 10 milliseconds. General worst-case latency is around 100 ms, except for commands that change bands, which can take up to 500 ms. 

At the bottom of this simple code - you will notice a time.sleep(1) This gives enough delay to allow the commands to be processed. Without this - this code will fail (you have been warned).


This code is written in Python3 - it needs 1 Module installing that module is called PySerial. You will probably need to alter the device name of your interface that is the line sp = Serial('/dev/tty.usbserial-A7004VW8', 38400, timeout=1)



# What this is trying to do

  * Assumes you are listening on the DX Station in VFO-A
  * Assumes that you want to place the DX Station in the LEFT-HAND-EDGE on the P3 Screen
  * You you can conduct a S&P type QSO


If that is the case simple run

```python
python gui.py
```

There are 2 options 

  *Set P3
  *RESET

If you want to see what is going on enter a device as **TEST** (case Sensative) - and the K3/P3 commands are displayed.

If you want to execute these command then select your device.

# Settings

Your last setting for the P3 is saved by default in the directory you run the program. It is OK to delete the .p file (Pickle) - a rather CW view of the split will be added by default.

# Testing

Tested using Mac (i5 and i7), as well as Ubuntu 14 - rig is K3-S #10678 (Feb 2016) with a P3 also from Feb 2016.

# Python Stuff

This now needs QT5 - and guidata, of these QT5 is the more tricky to install (I suggest you install it in a virtualEnv rather than as root on your machine). You will also find yourself needing

  * numpy
  * pyserial



