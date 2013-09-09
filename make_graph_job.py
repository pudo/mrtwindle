#!usr/bin/python2.6
import json
import os
from pprint import pprint
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol, JSONProtocol


class LineProtocol(JSONProtocol):

    def read(self, line):
        print "ATTEMPTING TO LOAD LINE", len(line)
        return None, json.loads(line)


class MRMakeGraph(MRJob):
    INPUT_PROTOCOL = LineProtocol
    INTERNAL_PROTOCOL = JSONProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, line):
        print "GOT DATA", len(line)
        yield "bar", 1
        #for status in json.loads(line):
            #status_user = status['user']['screen_name']
            #mentions = status.get('entities', {}).get('user_mentions', [])
            #for mention in mentions:
            #    yield {'user': status_user, 'mentions': mention.get('screen_name')}, 1

    def reducer(self, users, occurrences):
        #users['weight'] = sum(occurrences)
        #yield None, users
        yield None, {'name': users, 'val': sum(occurrences)}

if __name__ == '__main__':
    MRMakeGraph.run()

