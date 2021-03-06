import sensiball
import time

class Handler(object):
    def handle_positions(self, positions):
        """
        This function is called every 20ms.
        positions = (
            pulses,  # goalie translation
            maximum_pulses, # goalie translation
            pulses, # goalie rotation
            maximum_pulses, # goalie rotation
            pulses, # defender translation
            maximum_pulses, # defender translation
            pulses, # defender rotation
            maximum_pulses, # defender rotation
            pulses, # midfield translation
            maximum_pulses, # midfield translation
            pulses, # midfield rotation
            maximum_pulses, # midfield rotation
            pulses, # forward translation
            maximum_pulses, # forward translation
            pulses, # forward rotation
            maximum_pulses, # forward rotation
        )
        For translations, `pulses == 0` means the shaft reached the inner limit,
            and `pulses == maximum_pulses - 1` means it reached the outer one.
        For rotations, `maximum_pulses` is always `980`.
            `pulses == 0` means vertical (default player position).
        """
        print(positions)

table = sensiball.Table(device='/dev/cu.usbmodemFA131')
handler = Handler()
table.add_handler(handler)

time.sleep(2)
table.set_speeds((120, 120, 0, 0, 0, 0, 0, 0))
time.sleep(1)
table.set_speeds((-120, -120, 0, 0, 0, 0, 0, 0))
time.sleep(1)
table.set_speeds((0, 0, 0, 0, 0, 0, 0, 0))
table.calibrate()
table.close()
