import unittest 

from heapq import *
from priority_queue_class import prio_q

class pq_test(unittest.TestCase):
    
    # test __init__()
    def test_init(self):
        try:
            prio_q()
        except Exception:
            self.fail("Initialization of pq class failed")
    
    def test_init_heap_empty_list(self):
        pq1 = prio_q()
        self.assertEqual(pq1.heap, [])
        

    # test validate_heappush_item()
    def test_validate_heappush_item_not_tuple(self):
        with self.assertRaises(TypeError):
            prio_q.validate_push_item([3.3, 1])
    
    def test_validate_heappush_item_is_tuple(self):
        try:
            prio_q.validate_push_item((3.3, 1))
        except TypeError:
            self.fail("validate_push_item falsely raised TypeError")

    def test_validate_heappush_item0_not_float(self):
        with self.assertRaises(TypeError):
            prio_q.validate_push_item((3, 1))
    
    def test_validate_heappush_item0_is_float(self):
        try:
            prio_q.validate_push_item((3.3, 4))
        except TypeError:
            self.fail("validate_push_item falsely raised TypeError")
    
    def test_validate_heappush_item0_not_larger_0(self):
        with self.assertRaises(ValueError):
            prio_q.validate_push_item((-1.3, 4))

    def test_validate_heappush_item1_not_int(self):
        with self.assertRaises(TypeError):
            prio_q.validate_push_item((3.3, 1.5))

    def test_validate_heappush_item1_is_int(self):
        try:
            prio_q.validate_push_item((3.3, 5))
        except TypeError:
            self.fail("validate_push_item falsely raised TypeError")

    # test heap_push()
    def test_heap_push_calls_validate_item(self):
        with self.assertRaises(TypeError):
            pq1 = prio_q()
            pq1.push([3.3, 2])
    
    def test_heap_push_item_changes_heap(self):
        pq1 = prio_q()
        pq1.push((3.3, 2))
        self.assertEqual(pq1.heap[0], (3.3, 2))

  
    # test key()
    def test_key_returns_smallest_dist2(self):
        pass


    # test __eq__
    def test_eq_NotImplemented_for_other_not_pq(self):
        self.assertFalse(prio_q() == "some_rdm_str")
    
    def eq_test_example_pqs(self):
        pq1 = prio_q()
        pq2 = prio_q()
        for i in [(4.4, 3), (3.2, 8), (11.4, 1)]:
            heappush(pq1.heap, i)
            heappush(pq2.heap, i)
        return pq1, pq2

    def test_eq_returns_True(self):
        pq1, pq2 = self.eq_test_example_pqs()
        self.assertTrue(pq1==pq2)

    def test_eq_returns_False(self):
        pq1, pq2 = self.eq_test_example_pqs()
        pq2.heap[2] = (11.4, 13)
        self.assertFalse(pq1==pq2)




# ---------------------------------RUN Test--------------------------------------
# if __name__ == '__main__':
#     unittest.main()