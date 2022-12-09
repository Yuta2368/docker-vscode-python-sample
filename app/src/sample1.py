# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,100,0.5)
# Hz = 5.
# y = np.sin(2.0 * np.pi * (x * Hz) / 100)

# plt.plot(x,y)
# plt.savefig('test.png')

import sys
import time
import json
from simple_salesforce import Salesforce

def do_sf_api():
  sf = Salesforce(instance_url='https://akamai.my.salesforce.com', username='yozaki@akamai.com', password='Ss982368#ccc', security_token='5yy6i2OxYSO7wpM34ZBMm95K')
  query_str = "SELECT Case.AKAM_Case_ID__c FROM CaseMilestone WHERE IsCompleted = false AND Case.IsClosed = false AND Case.Case_Owner_Email_address__c = " + "'yozaki@akamai.com' LIMIT 10"
  api_res = sf.query(query_str)
  # json_str_res = json.dumps(api_res)
  # json_dict = json.loads(json_str_res.replace('\\r\\n', '').replace('\\n', ''))
  # target_dicts = json_dict['records']
  # for i in range(len(target_dicts)):
  #   try:
  #     del target_dicts[i]['attributes']
  #   except KeyError:
  #     pass
  print(type(api_res))
  print(api_res)


if __name__ == "__main__":
  start = time.time()
  try:
    res = do_sf_api()
  except Exception as e:
    print('do_sf_api error: ' + e)
    sys.exit(1)
  elapsed_time = time.time() - start
  print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
  sys.exit(0)
