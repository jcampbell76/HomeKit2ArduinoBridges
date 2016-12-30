# HomeKit2ArduinoBridges
Jacob Campbell - 2016

Collection of custom HomeKit Accessory Java Scripts which talk to a python based bridge / server which manages several 
custom "internet of things"

One trick is to create several HomeKit Accessories with similar names to operate on one device, (e.g. you could add features to
string of addressable LED's by having several "HomeKit accessories" operate on the function of the one string of LED's - the
python bridge/server manages how the "HomeKit accessory" devices operate on the arduino controlled string of LED's

