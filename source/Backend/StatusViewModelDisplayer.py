from ViewModel import StatusViewModel, SetTemperatureViewModel, MenuViewModel


# demo um es zu callen
# wie gesagt, hässlich, da nie in python garbeitet :D
# create viewmodel
vm = StatusViewModel([23.84658, 76.92383857], 30, "5s-6s", "03:45")
# create view (image) out of viewmodel
im = vm.generateView()
# display picture in picture viewer
im.show();


# everything zero

vm2 = StatusViewModel(agitation = "8s-8s")
im2 = vm2.generateView()
im2.show()

# Temperature ViewModel (intended when turning knob)
vm3 = SetTemperatureViewModel()
vm3.increase()
vm3.increase()
vm3.increase()
im3 = vm3.generateView()
im3.show()

items = ["Start", "Set Agitation", "Set Temperature"]
vm4 = MenuViewModel(items)
vm4.next()
im4 = vm4.generateView()
im4.show()

im.save("StatusDisplay.bmp")
im3.save("SetTemperature.bmp")
im4.save("Menu.bmp")