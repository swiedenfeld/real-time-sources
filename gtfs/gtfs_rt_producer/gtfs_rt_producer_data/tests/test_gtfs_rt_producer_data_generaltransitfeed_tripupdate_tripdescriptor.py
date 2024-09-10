"""
Test case for TripDescriptor
"""

import os
import sys
import unittest

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../src'.replace('/', os.sep))))

from gtfs_rt_producer_data.generaltransitfeed.tripupdate.tripdescriptor import TripDescriptor
from test_gtfs_rt_producer_data_generaltransitfeed_tripupdate_tripdescriptor_types_schedulerelationship import Test_ScheduleRelationship

class Test_TripDescriptor(unittest.TestCase):
    """
    Test case for TripDescriptor
    """

    def setUp(self):
        """
        Set up test case
        """
        self.instance = Test_TripDescriptor.create_instance()

    @staticmethod
    def create_instance():
        """
        Create instance of TripDescriptor for testing
        """
        instance = TripDescriptor(
            trip_id='vulkmdyazsnjfrzqclyg',
            route_id='xinpotkvcnrikpnknvna',
            direction_id=int(98),
            start_time='sdjjxoebwzbscceibpss',
            start_date='tswyprpyveptoevnubmh',
            schedule_relationship=Test_ScheduleRelationship.create_instance()
        )
        return instance

    
    def test_trip_id_property(self):
        """
        Test trip_id property
        """
        test_value = 'vulkmdyazsnjfrzqclyg'
        self.instance.trip_id = test_value
        self.assertEqual(self.instance.trip_id, test_value)
    
    def test_route_id_property(self):
        """
        Test route_id property
        """
        test_value = 'xinpotkvcnrikpnknvna'
        self.instance.route_id = test_value
        self.assertEqual(self.instance.route_id, test_value)
    
    def test_direction_id_property(self):
        """
        Test direction_id property
        """
        test_value = int(98)
        self.instance.direction_id = test_value
        self.assertEqual(self.instance.direction_id, test_value)
    
    def test_start_time_property(self):
        """
        Test start_time property
        """
        test_value = 'sdjjxoebwzbscceibpss'
        self.instance.start_time = test_value
        self.assertEqual(self.instance.start_time, test_value)
    
    def test_start_date_property(self):
        """
        Test start_date property
        """
        test_value = 'tswyprpyveptoevnubmh'
        self.instance.start_date = test_value
        self.assertEqual(self.instance.start_date, test_value)
    
    def test_schedule_relationship_property(self):
        """
        Test schedule_relationship property
        """
        test_value = Test_ScheduleRelationship.create_instance()
        self.instance.schedule_relationship = test_value
        self.assertEqual(self.instance.schedule_relationship, test_value)
    
