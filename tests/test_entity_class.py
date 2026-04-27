import unittest 
from classese.ntity_class import entity
import numpy as np
from classes.priority_queue_class import prio_q
from unittest.mock import MagicMock
import pytest

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

# --------------------- Diego Tests ----------------------
    def test_centering_pulls_entity_toward_average_position(self):
        """
        When other entities are ahead of the subject, centering should
        nudge the subject's velocity in their direction.
        """
        # Subject at origin, two neighbors both at x=10
        neighbor_a = make_entity(pos=(10, 0), velocity=(0, 0))
        neighbor_b = make_entity(pos=(10, 0), velocity=(0, 0))
        entity_list = [neighbor_a, neighbor_b]

        heap = [(0, 0), (1, 1)]  # (priority, index)
        subject = make_subject(pos=(0, 0), velocity=(0, 0), heap_entries=heap)

        factors = (0.0, 0.0, 0.5)  # only centeringfactor active
        subject.flocking_behavior(entity_list, n_humans=2, min_distance=0.5, factors=factors)

        # Velocity should now have a positive x component (moving toward x=10)
        assert subject.velocity[0] > 0, "Entity should be pulled toward neighbors"
        assert subject.velocity[1] == pytest.approx(0), "No y-movement expected"

    def test_velocity_matching_aligns_with_neighbors(self):
        """
        Neighbors all moving in the +y direction. Subject starts stationary.
        Velocity matching should give the subject a +y velocity component.
        """
        neighbor_a = make_entity(pos=(1, 0), velocity=(0, 5))
        neighbor_b = make_entity(pos=(2, 0), velocity=(0, 5))
        entity_list = [neighbor_a, neighbor_b]

        heap = [(0, 0), (1, 1)]
        subject = make_subject(pos=(0, 0), velocity=(0, 0), heap_entries=heap)

        factors = (0.0, 0.5, 0.0)  # only matchingfactor active
        subject.flocking_behavior(entity_list, n_humans=2, min_distance=0.1, factors=factors)

        assert subject.velocity[1] > 0, "Entity should match neighbors moving in +y"
        assert subject.velocity[0] == pytest.approx(0), "No y-movement expected" # no movement in x direction

    def test_separation_pushes_entity_away_from_close_neighbor(self):
        """
        A neighbor extremely close to the subject should trigger separation.
        The close vector (self.pos - other.pos) should push the subject away.
        """
        # Neighbor is just 0.1 units away — well within min_distance=1.0
        neighbor = make_entity(pos=(0.1, 0), velocity=(0, 0))
        entity_list = [neighbor]

        heap = [(0, 0)]
        subject = make_subject(pos=(0, 0), velocity=(0, 0), heap_entries=heap)

        factors = (1.0, 0.0, 0.0)  # only avoidfactor active
        subject.flocking_behavior(entity_list, n_humans=1, min_distance=1.0, factors=factors)

        # Subject at 0, neighbor at 0.1 → close vector is (0-0.1, 0) = negative x
        # So velocity should be pushed in -x direction
        assert subject.velocity[0] < 0, "Entity should be repelled from nearby neighbor"

    def test_no_velocity_change_when_perfectly_balanced(self):
        """
        If neighbors are symmetrically placed around the subject and have the
        same velocity, the net update should be zero.
        """
        # Neighbors on opposite sides cancel each other out
        neighbor_a = make_entity(pos=(-5, 0), velocity=(1, 0))
        neighbor_b = make_entity(pos=( 5, 0), velocity=(1, 0))
        entity_list = [neighbor_a, neighbor_b]

        heap = [(0, 0), (1, 1)]
        subject = make_subject(pos=(0, 0), velocity=(1, 0), heap_entries=heap)

        original_velocity = subject.velocity.copy()
        factors = (0.0, 0.5, 0.5)
        subject.flocking_behavior(entity_list, n_humans=2, min_distance=0.1, factors=factors)

        np.testing.assert_array_almost_equal(subject.velocity, original_velocity)

    def test_zombie_awareness_raises_when_same_position(self):
        subject = make_subject(pos=(5, 5), velocity=(0,0), heap_entries=[(0, 0)])
        subject.pos_alerter = np.array((5.0, 5.0))  # exact same spot
        subject.get_distance = lambda p: 0.0

        with pytest.raises(ValueError, match="EXACT same spot"):
            entity.zombie_awareness(subject)

    def test_zombie_awareness_runs_away_from_zombie(self):
        subject = make_subject(pos=(0, 0), velocity=(0,0), heap_entries=[(0, 0)])
        subject.pos_alerter = np.array((5.0, 0.0))  # zombie is to the right
        subject.get_distance = lambda p: 5.0
        subject.param_dict = {"max_speed_H": 2.0}
        subject.change_velocity = MagicMock()

        entity.zombie_awareness(subject)

        called_with = subject.change_velocity.call_args[0][0]
        assert called_with[0] < 0, "Should run in -x direction, away from zombie"
        assert called_with[1] == pytest.approx(0)

    def test_zombie_awareness_speed_equals_max_speed(self):
        subject = make_subject(pos=(0, 0), velocity=(0,0), heap_entries=[(0, 0)])
        subject.pos_alerter = np.array((3.0, 4.0))  # diagonal zombie, distance = 5
        subject.get_distance = lambda p: 5.0
        subject.param_dict = {"max_speed_H": 3.0}
        subject.change_velocity = MagicMock()

        entity.zombie_awareness(subject)

        called_with = subject.change_velocity.call_args[0][0]
        speed = np.linalg.norm(called_with)
        assert speed == pytest.approx(3.0), "Speed should equal max_speed_H exactly"

    def test_zombie_awareness_run_direction_is_unit_vector(self):
        subject = make_subject(pos=(0, 0), velocity=(0,0), heap_entries=[(0, 0)])
        subject.pos_alerter = np.array((3.0, 4.0))
        subject.get_distance = lambda p: 5.0
        subject.param_dict = {"max_speed_H": 1.0}  # scale=1 so magnitude == direction magnitude
        subject.change_velocity = MagicMock()

        entity.zombie_awareness(subject)

        called_with = subject.change_velocity.call_args[0][0]
        assert np.linalg.norm(called_with) == pytest.approx(1.0)
    
    def test_lonely_walk_calls_set_preferred_dir_when_none(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])
        subject.preferred_dir = None
        subject.set_preferred_dir = MagicMock(side_effect=lambda: setattr(subject, 'preferred_dir', np.array((1.0, 0.0))))
        subject.change_velocity = MagicMock()
        subject.param_dict = {"max_speed_H": 2.0}

        entity.lonely_walk(subject)
        subject.set_preferred_dir.assert_called_once()

    def test_lonely_walk_skips_set_preferred_dir_when_already_set(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])
        subject.preferred_dir = np.array((1.0, 0.0))  # already set
        subject.set_preferred_dir = MagicMock()
        subject.change_velocity = MagicMock()
        subject.param_dict = {"max_speed_H": 2.0}

        entity.lonely_walk(subject)

        subject.set_preferred_dir.assert_not_called()

    def test_lonely_walk_change_velocity_scaled_by_max_speed(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])
        subject.preferred_dir = np.array((1.0, 0.0))
        subject.set_preferred_dir = MagicMock()
        subject.change_velocity = MagicMock()
        subject.param_dict = {"max_speed_H": 3.0}

        entity.lonely_walk(subject)

        called_with = subject.change_velocity.call_args[0][0]
        np.testing.assert_array_almost_equal(called_with, np.array((3.0, 0.0)))
    
    def test_lonely_walk_speed_equals_max_speed(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])
        subject.preferred_dir = np.array((1/np.sqrt(2), 1/np.sqrt(2)))  # diagonal unit vector
        subject.set_preferred_dir = MagicMock()
        subject.change_velocity = MagicMock()
        subject.param_dict = {"max_speed_H": 2.0}

        entity.lonely_walk(subject)

        called_with = subject.change_velocity.call_args[0][0]
        assert np.linalg.norm(called_with) == pytest.approx(2.0) 

    def test_update_location_moves_by_velocity_times_timestep(self):
        subject = make_subject(pos=(2.0, 3.0), velocity=(1.0, 2.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 0.5,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        np.testing.assert_array_almost_equal(subject.pos, np.array((2.5, 4.0)))

    def test_update_location_wraps_upper_x_bound(self):
        subject = make_subject(pos=(99.0, 5.0), velocity=(5.0, 0.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        # 99 + 5 = 104 → wraps to 4
        assert subject.pos[0] == pytest.approx(4.0)
        assert subject.pos[1] == pytest.approx(5.0)  # y unchanged

    def test_update_location_wraps_lower_x_bound(self):
        subject = make_subject(pos=(1.0, 5.0), velocity=(-5.0, 0.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        # 1 - 5 = -4 → wraps to 96
        assert subject.pos[0] == pytest.approx(96.0)
        assert subject.pos[1] == pytest.approx(5.0)

    def test_update_location_wraps_upper_y_bound(self):
        subject = make_subject(pos=(5.0, 98.0), velocity=(0.0, 5.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        # 98 + 5 = 103 → wraps to 3
        assert subject.pos[0] == pytest.approx(5.0)
        assert subject.pos[1] == pytest.approx(3.0)

    def test_update_location_wraps_lower_y_bound(self):
        subject = make_subject(pos=(5.0, 2.0), velocity=(0.0, -5.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        # 2 - 5 = -3 → wraps to 97
        assert subject.pos[0] == pytest.approx(5.0)
        assert subject.pos[1] == pytest.approx(97.0)

    def test_update_location_no_wrapping_within_bounds(self):
        subject = make_subject(pos=(50.0, 50.0), velocity=(1.0, 1.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        np.testing.assert_array_almost_equal(subject.pos, np.array((51.0, 51.0)))

    def test_update_location_wraps_both_axes_at_once(self):
        subject = make_subject(pos=(98.0, 98.0), velocity=(5.0, 5.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        assert subject.pos[0] == pytest.approx(3.0)
        assert subject.pos[1] == pytest.approx(3.0)

    def test_update_location_exact_upper_bound_wraps(self):
        subject = make_subject(pos=(100.0, 5.0), velocity=(0.0, 0.0), heap_entries=[])
        subject.param_dict = {
            "timestep": 1.0,
            "x_bounds": (0.0, 100.0),
            "y_bounds": (0.0, 100.0)
        }

        entity.update_location(subject)

        assert subject.pos[0] == pytest.approx(0.0)  # 100 - 100 = 0


    def test_set_preferred_dir_assigns_value(self):
        subject = make_subject(pos = (0,0), velocity=(0,0), heap_entries = [])
        subject.preferred_dir = None

        entity.set_preferred_dir(subject)

        assert subject.preferred_dir is not None

    def test_set_preferred_dir_is_unit_vector(self):
        subject = make_subject(pos = (0,0), velocity=(0,0), heap_entries = [])
        subject.preferred_dir = None

        entity.set_preferred_dir(subject)

        assert np.linalg.norm(subject.preferred_dir) == pytest.approx(1.0)

    def test_set_preferred_dir_components_in_valid_range(self):
        subject = make_subject(pos = (0,0), velocity=(0,0), heap_entries = [])
        subject.preferred_dir = None

        entity.set_preferred_dir(subject)

        assert -1.<=subject.preferred_dir[0]<=1.
        assert -1.<=subject.preferred_dir[1]<=1.

    def test_set_preferred_dir_returns_2d_array(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])

        entity.set_preferred_dir(subject)

        assert isinstance(subject.preferred_dir, np.ndarray)
        assert subject.preferred_dir.shape == (2,)

    def test_set_preferred_dir_is_random(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])

        results = set()
        for _ in range(10):
            entity.set_preferred_dir(subject)
            results.add(tuple(subject.preferred_dir))

        assert len(results) > 1, "Direction should vary across calls"

    def test_set_preferred_dir_reproducible_with_seed(self):
        subject = make_subject(pos=(0,0), velocity=(0,0), heap_entries=[])

        np.random.seed(42)
        entity.set_preferred_dir(subject)
        first = subject.preferred_dir.copy()

        np.random.seed(42)
        entity.set_preferred_dir(subject)
        second = subject.preferred_dir.copy()

        np.testing.assert_array_equal(first, second)




def make_entity(pos, velocity):
    """Creates a minimal mock entity with position and velocity."""
    e = MagicMock()
    e.pos = np.array(pos, dtype=float)
    e.velocity = np.array(velocity, dtype=float)
    return e

def make_subject(pos, velocity, heap_entries):
    """
    Creates a mock 'self' entity (the one calling flocking_behavior).
    heap_entries: list of (priority, index) tuples, mimicking pq.heap
    """
    subject = make_entity(pos, velocity)
    subject.pq = MagicMock()
    subject.pq.heap = heap_entries
    # get_distance returns actual euclidean distance from subject to other entity
    subject.get_distance = lambda other_pos: np.linalg.norm(subject.pos - other_pos)
    # Bind the real method to this mock object
    subject.flocking_behavior = lambda entity_list, **kwargs: \
        entity.flocking_behavior(subject, entity_list, **kwargs)
    return subject
# ---------------------------------RUN Test--------------------------------------
if __name__ == '__main__':
    unittest.main()