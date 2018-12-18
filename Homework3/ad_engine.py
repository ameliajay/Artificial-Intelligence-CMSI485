'''
ad_engine.py

CMSI 485 HW 3: Advertisement engine that selects from two
ad traits to maximize expected utility of converting a sale
for the Forney Industries Protectron 3001
'''

import itertools
import unittest
import math
import numpy as np
from pomegranate import *

class AdEngine:

    def __init__(self, data_file, structure, dec_vars, util_map):
        """
        Responsible for initializing the Decision Network of the
        AdEngine from the structure discovered by Tetrad
        """

        self.data_file = data_file
        self.structure = structure
        self.dec_vars = dec_vars
        self.util_map = util_map

        X = np.genfromtxt(data_file, dtype = 'int', delimiter = ',', names = True)
        self.state_names = X.dtype.names
        self.model = BayesianNetwork.from_structure(X = X.view((int, len(self.state_names))), structure = structure, state_names = self.state_names)

    def decide(self, evidence):
        """
        Given some observed demographic "evidence" about a potential
        consumer, selects the ad content that maximizes expected utility
        and returns a dictionary over any decision variables and their
        best values

        :param dict evidence: dict mapping network variables to their
        observed values, of the format: {"Obs1": val1, "Obs2": val2, ...}
        :return: dict of format: {"DecVar1": val1, "DecVar2": val2, ...}
        """
        best_combo, best_util = None, -math.inf

        key = list(self.util_map.keys())[0]
        for i in range(len(self.state_names)):
            if self.state_names[i] is key:
                util_index = i

        combos = []
        dec_vals = (0, 1)
        for pair in list(itertools.product(dec_vals, repeat = len(self.dec_vars))):
            combo = {}
            for i in range(len(self.dec_vars)):
                combo[self.dec_vars[i]] = pair[i]
            combos.append(combo)

        dict = {}
        for combo in combos:
            evidence.update(combo)
            eu = 0
            for i in range(len(self.util_map[key])):
                eu += self.model.predict_proba(evidence)[util_index].parameters[0][i] * self.util_map[key][i]
            dict[eu] = combo
        best_util = max(list(dict.keys()))
        best_combo = dict[best_util]

        return best_combo

class AdEngineTests(unittest.TestCase):

    def test_defendotron_ad_engine_t1(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1", "Ad2"],
            structure = ((), (), (0, 9), (6,), (9, 1), (1, 8, 0), (1,), (5, 2), (), ()),
            util_map = {"S": {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({"T": 1}), {"Ad1": 0, "Ad2": 1})
        self.assertIn(engine.decide({"F": 1}), [{"Ad1": 1, "Ad2": 0},{"Ad1": 1, "Ad2": 1}])
        self.assertEqual(engine.decide({"G": 1, "T": 0}), {"Ad1": 1, "Ad2": 1})


    def test_defendotron_ad_engine_t2(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1"],
            structure = ((), (), (0, 9), (6,), (9, 1), (1, 8, 0), (1,), (5, 2), (), ()),
            util_map = {"S": {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({"A": 1}), {"Ad1": 0})
        self.assertEqual(engine.decide({"P": 1, "A": 0}), {"Ad1": 1})
        self.assertIn(engine.decide({"A": 1, "G": 0, "T": 1}), [{"Ad1": 0}, {"Ad1": 1}])

if __name__ == "__main__":
    unittest.main()
