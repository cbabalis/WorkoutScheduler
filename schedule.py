#!/usr/bin/env python

""" This module outputs a recommended schedule for my workout plans.
"""

import random


class Scheduler(object):
    """ Schedules the workouts."""

    def __init__(self):
        self.workout_choices = ['w1', 'w2', 'w3']
        self.done_workouts = []

    def plan_next_days(self, num_of_days, workout_choices, done_workouts=[]):
        """ Method to plan the next days workouts"""
        planned_workouts = []
        if not done_workouts:
            last_workout = self.get_last_workout(workout_choices)
            planned_workouts.append(last_workout)
        else:
            last_workout = self.get_last_workout(
                                workout_choices, done_workouts)
        self.schedule(last_workout, workout_choices,
                      planned_workouts, num_of_days)
        return planned_workouts

    def get_last_workout(self, workout_choices, done_workouts=[]):
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

    def schedule(self, last_workout, workout_choices,
                 planned_workouts, num_of_days):
        """ This method schedules the workouts accordingly.
        It should be run recursively.

        :param str last_workout: [mandatory] the workout done last
        :param list workout_choices: [mandatory] a list of all available
                workouts.
        :param list planned_workouts: [mandatory] the workouts already planned

        :return: next_workout

        """
        next_workout = ''
        # check if last_workout exists in the list.
        for i in range(1, num_of_days):
            # get the next workout which is NOT the last one.
            next_workout = self.get_next_workout(last_workout, workout_choices)
            # add it to planned_workouts
            planned_workouts.append(next_workout)
            # set the last_workout to the next workout
            last_workout = next_workout

    def get_next_workout(self, last_workout, workout_choices):
        possible_workout = last_workout
        while possible_workout == last_workout:
            possible_workout = random.choice(workout_choices)
        return possible_workout


def main():
    s = Scheduler()
    choices = ['w1', 'w2', 'w3']
    planned_workouts = s.plan_next_days(17, choices)
    print planned_workouts


if __name__ == '__main__':
    main()
