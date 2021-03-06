#!/usr/bin/python
import gc
import unittest

class GcTests(unittest.TestCase):
    def test_the_simplest(self):
        pass
if __name__ == '__main__':
    unittest.main()

def test_gc(self):
    self.assertEqual(gc('ACTG'), 0.5)

def test_long(self):
    self.assertAlmostEqual(gc('ACTGCAGATCTGAAATTCAGTAAGGG'), 0.4230769)

def test_empty(self):
    self.assertRaises(TypeError, gc, )


def gc(sequence):
    gc_count = 0
    valid_nucleotides = ['A','C','T','U','G','N']
    for nuc in sequence:
        nuc = nuc.upper()
        if nuc not in valid_nucleotides:
            raise Exception(nuc + ' is not a valid nucleotide.')
        if nuc == 'G':
            gc_count += 1
        if nuc == 'C':
            gc_count += 1
    if len(sequence)==0:
        return 0 
    return (float(gc_count) / len(sequence))

def test_lowercase(self):
    self.assertEqual(gc('AcTg'), 0.5)

def test_random(self):
    self.assertRaises(Exception, gc, 'This is just a random sentence, but we still get a gc content back.')

def test_empty_string(self):
    self.assertEqual(gc(''), 0)
