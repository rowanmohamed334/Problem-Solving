# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # print('try to see elems:', self.elems)
            # use reverse order, because we append strings to the end
            if self.elems.get(query.ind):
                self.write_chain(reversed(self.elems[query.ind]))
            else:
                self.write_chain([])
        else:
            try:
                dickey = self._hash_func(query.s)
                ind = self.elems[dickey].index(query.s)
                # print("ind: ", ind)
            except ValueError:
                ind = -1
            except KeyError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if self.elems.get(self._hash_func(query.s)) and ind == -1:
                    self.elems[self._hash_func(query.s)].append(query.s)
                elif ind == -1:
                    self.elems[self._hash_func(query.s)] = [query.s]
            else:
                if ind != -1:
                    self.elems[self._hash_func(query.s)].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
