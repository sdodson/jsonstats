import yaml
import commands
import json

class Facter(object):
    def __init__(self):
        (ret, output) = commands.getstatusoutput('facter' + ' -p' + ' --yaml')
        self.result = yaml.load(output)

    def dump_json(self, key=None):
        if not key:
            return json.dumps(self.result)
        elif key in self.result:
            return json.dumps(self.result[key])
        else:
            raise "wtf are you doing"


# USAGE
#
# import FetchStats.Facter
#
# f = FetchStats.Facter()
# print f.dump_json()
# print f.dump_json('selinux')