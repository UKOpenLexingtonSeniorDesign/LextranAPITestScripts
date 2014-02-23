import urllib2
import xml.etree.ElementTree as XML


def get_route_stops(route=10):
	route_xml_api_url = 'http://realtime.lextran.com/InfoPoint/map/GetRouteXml.ashx?'
	route_id = "RouteId=" + str(route)
	response = urllib2.urlopen(route_xml_api_url+route_id)
	html = response.read()
	route_xml = XML.fromstring(html)
	stops = []
	for child in route_xml:
		if child.tag == 'stops':
			for stop in child:
				stops.append([stop.attrib["label"],stop.attrib["lat"],stop.attrib["lng"]])
	return stops

def get_bus_on_route(route=10):
	route_xml_api_url = 'http://realtime.lextran.com/InfoPoint/map/GetVehicleXml.ashx?'
	route_id = 'RouteId='+str(route)
	response = urllib2.urlopen(route_xml_api_url+route_id)
	html = response.read()
	bus_xml = XML.fromstring(html)
	buses = []
	for bus in bus_xml:
		buses.append([bus.attrib['name'],bus.attrib['lat'],bus.attrib['lng']])
	return buses

if __name__ == "__main__":
	for a in get_route_stops():
		print a
	for b in get_bus_on_route():
		print b