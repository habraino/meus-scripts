import json

from datetime import datetime

data = {'datetime': datetime(2020, 5, 24, 14, 6, 33)}
#print(json.dumps(data))

class DateTimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.isoformat()
        except AttributeError:
            return super(DateTimeJSONEncoder, self).default(obj)

encoder = DateTimeJSONEncoder()
print(encoder.encode(data))

