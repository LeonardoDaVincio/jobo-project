from ViewModel import StatusViewModel


# demo um es zu callen
# wie gesagt, hässlich, da nie in python garbeitet :D
# create viewmodel
vm = StatusViewModel([23.84658, 76.92383857], 30, "5s-6s", "03:45")
# create view (image) out of viewmodel
im = vm.generateStatusDisplay()
# display picture in picture viewer
im.show();


# everything zero

vm2 = StatusViewModel(agitation = "8s-8s")
im2 = vm2.generateStatusDisplay()
im2.show()
