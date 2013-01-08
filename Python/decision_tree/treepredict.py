# vim: fileencoding=utf-8

my_data = [line.split('\t') for line in file('./decision_tree_example.txt')]

class decisionnode:
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None):
        self.col=col
        self.value=value
        self.results=result
        self.tb=tb
        self.fb=fb
        
def divideset(rows, column, value):
    split_function=None

    # decide the function by value type
    if isinstance(value, int) or isinstance(value, float):
        split_function = lambda row:row[column] >= value
    else:
        split_function = lambda row:row[column] == value


    # divide row
    set1=[row for row in rows if split_function(row)]
    set2=[row for row in rows if not split_function(row)]

    return (set1, set2)

def uniquecounts(rows):
    results={}
    for row in rows:
        r=row[len(row)-1]
        if r not in results: results[r] = 0
        results[r] += 1
    return results
