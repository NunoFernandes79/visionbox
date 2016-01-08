__author__ = 'Nuno.Fernandes'

from suds.client import Client

url = 'http://10.5.2.63/kioskwebservice/kioskwebservice.asmx?wsdl'

client = Client(url)

print( client.wsdl.services[0].ports[0].methods.keys())

client.service.GetCurrentHeight()
client.service.MoveRelativeHeight(5)
client.service.MoveRelativeHeight(+15)
client.service.MoveRelativeHeight(-15)



client.service.MoveAbsoluteHeight(100)


client.service.ShowScreen()

client.service.GetConfigurationParameter()
client.service.RequestEnrollmentId()
