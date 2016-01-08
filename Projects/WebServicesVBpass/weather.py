__author__ = 'Nuno.Fernandes'

import suds
import time


url="http://10.5.2.114/kioskwebservice/kioskwebservice.asmx?singleWsdl"
client =suds.client.Client(url)
client.sd[0].service.setlocation(url)
client.set_options(port='BasicHttpBinding_VBService')
SessionKey=client.service.RequestSessionKey()
print SessionKey

it = client.factory.create(u'CaptureData')
it.enrollmentId=1000
it.sessionKey=SessionKey
it.operations.DeviceId=0
it.operations.DeviceType='Finger'
it.operations.Workflow='Default'
print it
client.service.CaptureData(it)
#print EnrollmentId

#client.service.ReleaseSessionKey(str(SessionKey))