__author__ = 'Nuno.Fernandes'


from suds.client import Client

url = "http://10.5.2.63/kioskwebservice/kioskwebservice.asmx?singleWsdl"

client = Client(url)

client.wsdl.services.po