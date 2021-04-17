from itertools import combinations
from collections import defaultdict
from operator import itemgetter


class Apriori:
    def __init__(self,data,threshold,mincount):
        '''
        Initializing Apriori class
        '''
        self.data = data
        self.threshold = threshold
        self.mincount = mincount


    def update_pair_counts(self, pair_counts, itemset):
        '''
        Updates a dictionary of pair counts for
        all pairs of items in a given itemset.
        '''

        for (a,b) in combinations(itemset, 2):
            pair_counts[(a,b)] += 1
            pair_counts[(b,a)] += 1
    

    def update_item_counts(self, item_counts, itemset):
        '''
        Updates a dictionary of item counts for
        all items in a given itemset.
        '''
        for i in itemset:
            item_counts[i] += 1
    
    def filter_rules_by_conf(self, pair_counts, item_counts):
        '''
        Find confidence for each pair in pair_counts and 
        filter according to threshold
        '''
        rules = {} 
        for (a,b) in pair_counts:
            conf = pair_counts[(a,b)]/item_counts[a]
            if conf>=self.threshold and item_counts[a]>=self.mincount and item_counts[b]>=self.mincount:
                rules[(a,b)] = conf
        return rules

    def print_rules(self, rules):
        '''
        Format and print each rule
        '''
        if type(rules) is dict or type(rules) is defaultdict:
            ordered_rules = sorted(rules.items(), key=itemgetter(1), reverse=True)
        else: 
            ordered_rules = [((a,b), None) for a,b in rules]

        for (a,b), conf_ab in ordered_rules:
            text = "{} => {}".format(a, b)
            if conf_ab:
                text = "conf(" + text + ") = {:.3f}".format(conf_ab)
                print(text)

    def find_assoc_rules(self):
        '''
        Run the algorithm for finding pair rules
        '''

        pc = defaultdict(int)
        ic = defaultdict(int)

        for itemset in self.data:
            self.update_pair_counts(pc,itemset)
            self.update_item_counts(ic,itemset)

        rules = self.filter_rules_by_conf(pc,ic)

        return rules