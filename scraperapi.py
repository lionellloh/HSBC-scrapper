from urllib2 import Request, urlopen

url = 'https://www.hsbc.com.hk/gpib/channel/proxy/mortgageSvc/enqPropVal'
url2 = "https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html"

headers = {
  'Accept': 'application/json'
}

YOURAPIKEY = "2df8899c9d5addef9feb7666248f3d6f"
request = Request('http://api.scraperapi.com/?key=' + YOURAPIKEY + '&url=' + url2, headers=headers)

response_body = urlopen(request).read()
print (response_body)


curl -d 'locale=en&zoneId=33&districtId=41&estateId=1527&blockId=nil,7759,697&floor=1&flat=A' \
-X POST \
"http://api.scraperapi.com?key=2df8899c9d5addef9feb7666248f3d6f&url=https://www.hsbc.com.hk/gpib/channel/proxy/mortgageSvc/enqPropVal"


"locale":"en","zoneId":"3","districtId":"41","estateId":"1527","blockId":"nil,7759,697","floor":"1","flat":"A"


curl -i -X POST -H 'Content-Type: application/json' -d '{"locale":"en","zoneId":"3","districtId":"41","estateId":"1527","blockId":"nil,7759,697","floor":"1","flat":"A"}' https://www.hsbc.com.hk/gpib/channel/proxy/mortgageSvc/enqPropVal
