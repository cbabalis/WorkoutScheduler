#!/usr/bin/env python

""" This module outputs a recommended schedule for my workout plans.
"""


class Scheduler(object):
    """ Schedules the workouts."""

    def __init__(self_):
        self.workout_choices = ['w1', 'w2', 'w3']
        self.done_workouts = []

    def plan_next_days(self, num_of_days, workout_choices, done_workouts):
        """ Method to plan the next days workouts"""
        if not done_workouts:
            last_workout = self.get_last_workout(workout_choices)
            planned_workouts.append(last_workout)
        else:
            last_workout = self.get_last_workout(workout_choices, done_workouts)
        for i in range(1, num_of_days):
            planned_workouts.append(self.schedule(last_workout, workout_choices, planned_workouts))

    def get_last_workout(workout_choices, done_workouts=[]):
        """ Method to get the last workout.
        If no workout has been done yet, then return an element of the
        possible choices and set this as the last workout.

        :param list workout_choices: is a list of all workout choices.
        :param list done_workouts: is the list of all done workouts.

        :return: the last workout done.
        """
        if not done_workouts:
            return workout_choices[1]
        else:
            return done_workouts[-1]


    def schedule(self, last_workout, workout_choices, planned_workouts):
        """ This method schedules the workouts accordingly.
        It should be run recursively.

        :param str last_workout: [mandatory] the workout done last
        :param list workout_choices: [mandatory] a list of all available workouts
        :param list planned_workouts: [mandatory] the workouts already planned

        :return: next_workout

        """
        next_workout = ''
        workouts = iter(workout_choices)
        # check if last_workout exists in the list.
        if last_workout in workout_choices:
            # if it is, then take the next one.
            next_workout = workouts.next()
            # add it to planned_workouts and
            planned_workouts.append(next_workout)
            # set it as the last_workout
            return next_workout


