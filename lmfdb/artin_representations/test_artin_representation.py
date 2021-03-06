# -*- coding: utf8 -*-
from lmfdb.base import LmfdbTest
import math
import unittest2


class ArtinRepTest(LmfdbTest):

    # All tests should pass
    #
    def test_search_deg_condrange(self):
		L = self.tc.get('/ArtinRepresentation/?dimension=3&conductor=1988-2015&group=&ramified=&unramified=&root_number=&frobenius_schur_indicator=&count=15')
		assert '41' in L.data # Only 1 result at the time this test was written, which has conductor 2009 = 7^2.41

    def test_search_gal_ram_rn_fn(self):
		L = self.tc.get('/ArtinRepresentation/?dimension=&conductor=&group=11T5&ramified=43&unramified=&root_number=1&frobenius_schur_indicator=1&count=15')
		assert '2898947' in L.data # prime divisor of one of the conductors in the result

    def test_display_page(self):
		L = self.tc.get('/ArtinRepresentation/4/3655/1/')
		assert ('Odd' in L.data) or ('odd' in L.data)

