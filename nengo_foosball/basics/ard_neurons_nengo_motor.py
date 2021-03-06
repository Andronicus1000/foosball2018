#
# use nano_neurons code on arduino
# reset motor, wait for callibration to stop; refresh nengo
# hit play (serial should connect after a bit)
#
import serial
import nengo
import struct
import timeit
import time

ser = None
last_write_time = None

def on_start(sim):
    global ser
    ser = serial.Serial('COM8', 9600)
    ser.isOpen()
    time.sleep(15)

def ard_output(t,x):
    global last_write_time
    cur_time = timeit.default_timer()
    if last_write_time is None or cur_time > (last_write_time+.01):
        x = int(x*255) # max 255 pwm
        dir = 0
        if x<0:
            x = -x
            dir = 1
        if x> 255: x = 255
        a = struct.pack('BB', x, dir)
        ser.write(a)
        last_write_time = cur_time

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    ens = nengo.Ensemble(100, 1)
    motor = nengo.Node(ard_output, size_in=1, size_out=0)
    nengo.Connection(stim, ens, synapse=None)
    nengo.Connection(ens, motor, synapse = 0.01)
