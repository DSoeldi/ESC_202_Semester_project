import unittest 
from entity_class import entity
import numpy as np
from priority_queue_class import prio_q

class test_entity(unittest.TestCase):

    #------------------------------------------------------------------------- testing keyword args und positional args 
        # make sure positional args have to be given!
        # make sure keyword args can but don't have to be given
    def test_keyword_arg_mode_not_present(self):
        with self.assertRaises(Exception):
            entity(np.array([1.0,1.0]), {"some_key": "some_value"}, 3)

    def test_keyword_arg_pos_not_present(self):
        with self.assertRaises(Exception):
            entity("H", {"some_key": "some_value"}, 3)

    def test_keyword_arg_param_dict_not_present(self):
        with self.assertRaises(Exception):
            entity("H", np.array([1.0,1.0]), 3)
    
    def test_keyword_idx_all_ents_not_present(self):
        with self.assertRaises(Exception):
            entity("H", np.array([1.0,1.0]), {"some_key": "some_value"})
        

    def test_positional_arg_velocity_not_present(self):
        try: entity("H", np.array([1.0,1.0]), {"some_key": "some_value"}, 3, alerted = False, 
                    pos_alerter = None)
        except Exception: self.fail("raised TypeError")
            
    def test_positional_arg_alerted_not_present(self):
        try: entity("H", np.array([1.0,1.0]), {"some_key": "some_value"}, 3, velocity = np.array((1.0,1.0)), 
                    pos_alerter = None)
        except Exception: self.fail("raised TypeError")
          
    def test_positional_arg_pos_alerter_not_present(self):
        try: entity("H", np.array([1.0,1.0]), {"some_key": "some_value"}, 3, velocity = np.array((1.0,1.0)), 
                    alerted = False)
        except Exception: self.fail("raised TypeError")
            
    def test_positional_arg_pq_not_present(self):
        try: entity("H", np.array([1.0,1.0]), {"some_key": "some_value"}, 3, velocity = np.array((1.0,1.0)), 
                    alerted = False, pos_alerter = None)
        except Exception: self.fail("raised TypeError")


    #------------------------------------------------------------------------- testing validate functions

    def test_validate_mode_non_str(self):
        with self.assertRaises(ValueError):
            entity.validate_mode(3)
    
    def test_validate_mode_lowercase_str(self):
        with self.assertRaises(ValueError):
            entity.validate_mode("h")
        with self.assertRaises(ValueError):
            entity.validate_mode("z")
    
    def test_validate_mode_correct_1(self):
        try: entity.validate_mode("H")
        except ValueError: self.fail("raised ValueError")
    
    def test_validate_mode_correct_2(self):
        try: entity.validate_mode("Z")
        except ValueError: self.fail("raised ValueError")


    def test_validate_vector_not_ndarray(self):
        with self.assertRaises(TypeError):
            entity.validate_vector([3.0,5.0])
    
    def test_validate_vector_not_floats(self):
        with self.assertRaises(TypeError):
            entity.validate_vector(np.array((3,5)))
    
    def test_validate_vector_array_wrong_dim(self):
        with self.assertRaises(ValueError):
            entity.validate_vector(np.array((3.0,5.0,6.0)))
    

    def test_validate_param_dict_not_dict(self):
        with self.assertRaises(TypeError):
            entity.validate_param_dict({2,3,4})
    
    def test_validate_param_dict_correct(self):
        try: entity.validate_param_dict({"hello": 3})
        except Exception: self.fail("raised Exception")


    def test_validate_idx_all_ents_not_int(self):
        with self.assertRaises(TypeError):
            entity.validate_idx_all_ents(3.3)
    
    def test_validate_idx_all_ents_negative_int(self):
        with self.assertRaises(ValueError):
            entity.validate_idx_all_ents(-1)
    
    def test_validate_idx_all_ents_correct(self):
        try: entity.validate_idx_all_ents(0)
        except Exception: self.fail("raised Exception")
    

    def test_validate_alerted_not_bool(self):
        with self.assertRaises(TypeError):
            entity.validate_alerted("True")
    
    def test_validate_alerted_correct(self):
        try: entity.validate_alerted(True)
        except Exception: self.fail("raised Exception")


    def test_validate_pq_heap_not_list(self):
        pq1 = prio_q()
        pq1.heap = "not a list"
        with self.assertRaises(TypeError):
            entity.validate_pq(pq1)
    
    def test_validate_pq_not_prio_q(self):
        pq1 = "not_prio_q"
        with self.assertRaises(TypeError):
            entity.validate_pq(pq1)

    def test_validate_pq_correct(self):
        try: entity.validate_pq(prio_q())
        except Exception: self.fail("raised Exception")
    
    #------------------------------------------------------------------------- testing __init__:
        # test all the variables get the value they we should be assigned through "entity(x, x1, x2, x3, ...)"
    
    def define_entity_for_init_test(self):
        e_init = entity("Z", np.array((1.0,1.0)), {"some_key": "some_value"}, 3, velocity = np.array((1.5,1.7)), 
                        alerted = True, pos_alerter = np.array((8.3, 1.0)))
        return e_init
    
    def test_init_mode(self):
        e_init = self.define_entity_for_init_test()
        self.assertEqual(e_init.mode, "Z")
    
    def test_init_pos(self):
        e_init = self.define_entity_for_init_test()
        self.assertTrue((e_init.pos == np.array((1.0,1.0))).all())

    def test_init_param_dict(self):
        e_init = self.define_entity_for_init_test()
        self.assertTrue(e_init.param_dict == {"some_key": "some_value"})
    
    def test_init_idx_all_ents(self):
        e_init = self.define_entity_for_init_test()
        self.assertTrue(e_init.idx_all_ents == 3)

    def test_init_velocity(self):
        e_init = self.define_entity_for_init_test()
        self.assertTrue((e_init.velocity == np.array((1.5,1.7))).all())

    def test_init_alerted(self):
        e_init = self.define_entity_for_init_test()
        self.assertEqual(e_init.alerted, True)

    def test_init_pos_alerter(self):
        e_init = self.define_entity_for_init_test()
        self.assertTrue((e_init.pos_alerter == np.array((8.3, 1.0))).all())

    #------------------------------------------------------------------------- testing __eq__:
    def test_eq_returns_NotImplemented(self):
        self.assertFalse(entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3) == ["this is not an entity attribute"])
    
    
    def define_entities_for_eq_test(self):
        e1 = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3, np.array((1.5,1.7)), alerted = True, pos_alerter = np.array((8.3, 1.0)))
        e2 = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3, np.array((1.5,1.7)), alerted = True, pos_alerter = np.array((8.3, 1.0)))
        return e1, e2
    
    def test_eq_returns_True(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertEqual(e1, e2)
        
    def test_eq_returns_False_mode(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.mode = "H"
        self.assertNotEqual(e1, e2)
    
    def test_eq_returns_False_pos(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.pos = np.array((1.1,1.0))
        self.assertNotEqual(e1, e2)
        e1.pos = np.array((1.0,1.0)) # change back
    
    def test_eq_returns_False_idx_all_ents(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.idx_all_ents = 5
        self.assertNotEqual(e1, e2)
    
    def test_eq_returns_False_velocity(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.velocity = np.array((1.5,9.1))
        self.assertNotEqual(e1, e2)
    
    def test_eq_returns_False_alerted(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.alerted = False
        self.assertNotEqual(e1, e2)
    
    def test_eq_returns_False_pos_alerter(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.pos_alerter = np.array((0.0, 1.0))
        self.assertNotEqual(e1, e2)

    #------------------------------------------------------------------------- testing get functions:
    def test_get_speed_returns_float(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertIsInstance(e1.get_speed(), float)
        
    def test_get_speed_returns_correct_speed(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertAlmostEqual(e1.get_speed(), np.linalg.norm(e1.velocity))

    #------------------------------------------------------------------------- testing change functions:
    def test_change_mode_calls_validate_mode(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3)
        with self.assertRaises(ValueError):
            e.change_mode("z")
    
    def test_change_mode_changes_mode(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3)
        e.change_mode("Z")
        self.assertEqual(e.mode, "Z")

    
    def test_change_pos_calls_validate_vector(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3)
        with self.assertRaises(ValueError):
            e.change_pos(np.array((1.0,1.0, 3.3)))
    
    def test_change_pos_changes_pos(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3)
        e.change_pos(np.array((4.0,5.0)))
        self.assertTrue((e.pos == np.array((4.0,5.0))).all())
        

    def test_change_alerted_calls_validate_alerted(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3, alerted = True)
        with self.assertRaises(TypeError):
            e.change_alerted("blabla")
    
    def test_change_alerted_changes_alerted(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3, alerted = True)
        e.change_alerted(False)
        self.assertFalse(e.alerted)


    def test_change_pos_alerter_calls_validate_vector(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3, pos_alerter = np.array((4.0,1.0)))
        with self.assertRaises(ValueError):
            e.change_pos_alerter(np.array((1.0, 1.0, 3.3)))
    
    def test_change_pos_alerter_changes_pos_alerter(self):
        e = entity("Z", np.array((1.0,1.0)), {"key": "value"}, 3, pos_alerter = np.array((4.0,1.0)))
        e.change_pos_alerter(np.array((4.0,5.0)))
        self.assertTrue((e.pos_alerter == np.array((4.0,5.0))).all())
    

    def test_change_pq_calls_validate_pq(self):
        pass
    
    def test_change_pq_changes_pq(self):
        pass



# ---------------------------------RUN Test--------------------------------------
if __name__ == '__main__':
    unittest.main()