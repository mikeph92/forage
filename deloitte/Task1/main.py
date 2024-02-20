import json, unittest, datetime

with open("./data-1.json", "r") as f:
  jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
  jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
  jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):

  # IMPLEMENT: Conversion From Type 1
  country, city, area, factory, section = jsonObject["location"].split("/")

  result = {
    "deviceID": jsonObject["deviceID"],
    "deviceType": jsonObject["deviceType"],
    "timestamp": jsonObject["timestamp"],
    "location": {
      "country": country,
      "city": city,
      "area": area,
      "factory": factory,
      "section": section
    },
    "data": {
      "status": jsonObject["operationStatus"],
      "temperature": jsonObject["temp"]
    }
  }
  return result


def convertFromFormat2(jsonObject):

  # IMPLEMENT: Conversion From Type 1
  timestamp = datetime.datetime.strptime(jsonObject["timestamp"],"%Y-%m-%dT%H:%M:%S.%fZ")

  result = {
    "deviceID" : jsonObject["device"]["id"],
    "deviceType" : jsonObject["device"]["type"],
    "timestamp" : datetime.datetime.timestamp(timestamp)*1000,
    "location" : {
      "country" : jsonObject["country"],
      "city" : jsonObject["city"],
      "area" : jsonObject["area"],
      "factory" : jsonObject["factory"],
      "section" : jsonObject["section"]
    },
    "data" : {
      "status" : jsonObject["data"]["status"],
      "temperature" : jsonObject["data"]["temperature"]
    }
  }
  return result


def main(jsonObject):

  result = {}

  if (jsonObject.get('device') == None):
    result = convertFromFormat1(jsonObject)
  else:
    result = convertFromFormat2(jsonObject)

  return result


class TestSolution(unittest.TestCase):

  def test_sanity(self):

    result = json.loads(json.dumps(jsonExpectedResult))
    self.assertEqual(result, jsonExpectedResult)

  def test_dataType1(self):

    result = main(jsonData1)
    self.assertEqual(result, jsonExpectedResult,
                     'Converting from Type 1 failed')

  def test_dataType2(self):

    result = main(jsonData2)
    self.assertEqual(result, jsonExpectedResult,
                     'Converting from Type 2 failed')


if __name__ == '__main__':
  unittest.main()
