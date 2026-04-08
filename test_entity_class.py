from unittest import TestCase
from entity_class import entity
import numpy as np

class test_entity(TestCase):

    #------------------------------------------------------------------------- testing keyword args und positional args 
        # make sure positional args have to be given!
        # make sure keyword args can but don't have to be given
    def test_keyword_arg_mode_not_present(self):
        with self.assertRaises(Exception):
            entity(pos = np.array([1.0,1.0]))

    def test_keyword_arg_pos_not_present(self):
        with self.assertRaises(Exception):
            entity("H")
        

    def test_positional_arg_velocity_not_present(self):
        try: entity("H", np.array((1.0,1.0)), alerted = False, pos_alerter = None, pq = None, max_speed_Z = 20.0, max_speed_H = 20.0)
        except TypeError: self.fail("raised TypeError")
            
    def test_positional_arg_alerted_not_present(self):
        try: entity("H", np.array((1.0,1.0)), velocity = np.array((1.0,1.0)), pos_alerter = None, pq = None, max_speed_Z = 20.0, max_speed_H = 20.0)
        except TypeError: self.fail("raised TypeError")
          
    def test_positional_arg_pos_alerter_not_present(self):
        try: entity("H", np.array((1.0,1.0)), velocity = np.array((1.0,1.0)), alerted = False, pq = None, max_speed_Z = 20.0, max_speed_H = 20.0)
        except TypeError: self.fail("raised TypeError")
            
    def test_positional_arg_pq_not_present(self):
        try: entity("H", np.array((1.0,1.0)), velocity = np.array((1.0,1.0)), alerted = False, pos_alerter = None, max_speed_Z = 20.0, max_speed_H = 20.0)
        except TypeError: self.fail("raised TypeError")
            
    def test_positional_arg_max_speed_Z_not_present(self):
        try: entity("H", np.array((1.0,1.0)), velocity = np.array((1.0,1.0)), alerted = False, pos_alerter = None, pq = None, max_speed_H = 20.0)
        except TypeError: self.fail("raised TypeError")
            
    def test_positional_arg_max_speed_H_not_present(self):
        try: entity("H", np.array((1.0,1.0)), velocity = np.array((1.0,1.0)), alerted = False, pos_alerter = None, pq = None, max_speed_Z = 20.0)
        except TypeError: self.fail("raised TypeError")


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
        with self.assertRaises(ValueError):
            entity.validate_vector([3.0,5.0])
    
    def test_validate_vector_not_floats(self):
        with self.assertRaises(ValueError):
            entity.validate_vector(np.array((3,5)))
    
    def test_validate_vector_array_wrong_dim(self):
        with self.assertRaises(ValueError):
            entity.validate_vector(np.array((3,5,6)))
    

    def test_validate_alerted_not_bool(self):
        with self.assertRaises(ValueError):
            entity.validate_alerted("True")

    
    def test_validate_pq_list(self):
        # testing validate_pq:
        # list not heap?? (possible?)
        # --> can be none!
        pass


    def test_validate_max_speed_not_float(self):
        with self.assertRaises(ValueError):
            entity.validate_max_speed(20)
    
    # ?? within valid range?
    
    #------------------------------------------------------------------------- testing __init__:
        # test all the variables get the value they we should be assigned through "entity(x, x1, x2, x3, ...)"
    
    def define_entitie_for_init_test(self):
        e_init = entity("Z", np.array((1.0,1.0)), np.array((1.5,1.7)), alerted = True, 
                        pos_alerter = np.array((8.3, 1.0)), pq = None, max_speed_Z = 19.0, max_speed_H = 23.0)
        return e_init
    
    def test_init_mode(self):
        e_init = self.define_entitie_for_init_test()
        self.assertEqual(e_init.mode, "Z")
    
    def test_init_pos(self):
        e_init = self.define_entitie_for_init_test()
        self.assertTrue((e_init.pos == np.array((1.0,1.0))).all())

    def test_init_velocity(self):
        e_init = self.define_entitie_for_init_test()
        self.assertTrue((e_init.velocity == np.array((1.5,1.7))).all())

    def test_init_alerted(self):
        e_init = self.define_entitie_for_init_test()
        self.assertEqual(e_init.alerted, True)

    def test_init_pos_alerter(self):
        e_init = self.define_entitie_for_init_test()
        self.assertTrue((e_init.pos_alerter == np.array((8.3, 1.0))).all())

    def test_init_pq(self):
        e_init = self.define_entitie_for_init_test()
        self.assertEqual(e_init.pq, None)

    def test_init_max_speed_Z(self):
        e_init = self.define_entitie_for_init_test()
        self.assertEqual(e_init.max_speed_Z, 19.0)

    def test_init_max_speed_H(self):
        e_init = self.define_entitie_for_init_test()
        self.assertEqual(e_init.max_speed_H, 23.0)


    #------------------------------------------------------------------------- testing __eq__:
    def test_eq_returns_NotImplemented(self):
        self.assertFalse((entity("Z", np.array((1.0,1.0))) == ["this is not an entity attribute"]))
    
    
    def define_entities_for_eq_test(self):
        e1 = entity("Z", np.array((1.0,1.0)), np.array((1.5,1.7)), alerted = True, pos_alerter = np.array((8.3, 1.0)), pq = None, max_speed_Z = 19.0, max_speed_H = 23.0)
        e2 = entity("Z", np.array((1.0,1.0)), np.array((1.5,1.7)), alerted = True, pos_alerter = np.array((8.3, 1.0)), pq = None, max_speed_Z = 19.0, max_speed_H = 23.0)
        return e1, e2
    
    def test_eq_returns_True(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertEqual(e1, e2)
        
    def test_eq_returns_False_mode(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.mode = "H"
        self.assertNotEqual(e1, e2)
        e1.mode = "Z" # change back
    
    def test_eq_returns_False_pos(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.pos = np.array((1.1,1.0))
        self.assertNotEqual(e1, e2)
        e1.pos = np.array((1.0,1.0)) # change back
    
    def test_eq_returns_False_velocity(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.velocity = np.array((1.5,9.1))
        self.assertNotEqual(e1, e2)
        e1.velocity = np.array((1.5,1.7)) # change back
    
    def test_eq_returns_False_alerted(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.alerted = False
        self.assertNotEqual(e1, e2)
        e1.alerted = True # change back
    
    def test_eq_returns_False_pos_alerter(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.pos_alerter = np.array((0.0, 1.0))
        self.assertNotEqual(e1, e2)
        e1.pos_alerter = np.array((8.3, 1.0)) # change back
    
    def test_eq_returns_False_pq(self):
        e1, e2 = self.define_entities_for_eq_test()
        pass # finish here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        e1.pq = "H"
        self.assertNotEqual(e1, e2)
        e1.pq = None # change back
    
    def test_eq_returns_False_max_speed_Z(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.max_speed_Z = 11.3
        self.assertNotEqual(e1, e2)
        e1.max_speed_Z = 19.0 # change back
    
    def test_eq_returns_False_max_speed_H(self):
        e1, e2 = self.define_entities_for_eq_test()
        e1.max_speed_Z = 25.7
        self.assertNotEqual(e1, e2)
        e1.max_speed_Z = 23.0 # change back


    #------------------------------------------------------------------------- testing get functions:
    def test_get_speed_returns_float(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertIsInstance(e1.get_speed(), float)
        
    def test_get_speed_returns_correct_speed(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertAlmostEqual(e1.get_speed(), np.linalg.norm(e1.velocity))


    def test_get_direction_returns_nparray(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertIsInstance(e1.get_direction(), np.ndarray)
    
    def test_get_direction_returns_nparray_correct_dim(self):
        e1, e2 = self.define_entities_for_eq_test()
        self.assertEqual(np.shape(e1.get_direction()), (2,))
        
    def test_get_direction_returns_correct_direction(self):
        e1, e2 = self.define_entities_for_eq_test()
        pass

    #------------------------------------------------------------------------- testing change functions:
    def test_change_mode_calls_validate_mode(self):
        e = entity("H", np.array((1.0,1.0)))
        with self.assertRaises(ValueError):
            e.change_mode("z")
    
    def test_change_mode_changes_mode(self):
        e = entity("H", np.array((1.0,1.0)))
        e.change_mode("Z")
        self.assertEqual(e.mode, "Z")

    
    def test_change_pos_calls_validate_vector(self):
        e = entity("H", np.array((1.0,1.0)))
        with self.assertRaises(ValueError):
            e.change_pos(np.array((1.0,1.0, 3.3)))
    
    def test_change_pos_changes_pos(self):
        e = entity("H", np.array((1.0,1.0)))
        e.change_pos(np.array((4.0,5.0)))
        self.assertTrue((e.pos == np.array((4.0,5.0))).all())
        

    def test_change_alerted_calls_validate_alerted(self):
        e = entity("H", np.array((1.0,1.0)), alerted = True)
        with self.assertRaises(ValueError):
            e.change_alerted("blabla")
    
    def test_change_alerted_changes_alerted(self):
        e = entity("H", np.array((1.0,1.0)), alerted = True)
        e.change_alerted(False)
        self.assertFalse(e.alerted)


    def test_change_pos_alerter_calls_validate_vector(self):
        e = entity("H", np.array((1.0,1.0)), pos_alerter = np.array((4.0,1.0)))
        with self.assertRaises(ValueError):
            e.change_pos_alerter(np.array((1.0, 1.0, 3.3)))
    
    def test_change_pos_alerter_changes_pos_alerter(self):
        e = entity("H", np.array((1.0,1.0)), pos_alerter = np.array((4.0,1.0)))
        e.change_pos_alerter(np.array((4.0,5.0)))
        self.assertTrue((e.pos_alerter == np.array((4.0,5.0))).all())
    

    def test_change_pq_calls_validate_pq(self):
        pass
    
    def test_change_pq_changes_pq(self):
        pass