import pymel.core as pm

bifrost_grapht = pm.ls('bifrostGraphShape1')[0]

for each in range(50):
    new_space_locator = pm.spaceLocator()
    bifrost_grapht.sine[each] >> new_space_locator.translateY
    new_space_locator.translateX.set(each)
