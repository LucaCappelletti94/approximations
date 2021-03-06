approximations
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Python package containing approximations of various NP problems.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install approximations

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Available approximations
--------------------------------------------------------------

Knapsack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Knapsack is approximated using a FPTAS, with arbitrarily good approximation. The computing cost increases up to becoming NP as the approximation approaches 0.

.. code:: python

    from approximations import knapsack

    total_weight, total_value, selected_objects = knapsack(
        weights=[1,2,3,4, 1, 2, 2, 2, 2, 2],
        values=[3,2,1,2,  1, 2, 2, 2, 2, 56],
        capacity=20,
        approximation=0.1
    ) # (18, 72, [0, 1, 3, 4, 5, 6, 7, 8, 9])


Load Balancing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Load Balancing is approximated using a 1.5-approximation greedy algorithm.

.. code:: python

    from approximations import load_balancing

    assignment, makespans = load_balancing([1,2,3,4,5,6], 3) # ([[5, 0], [4, 1], [3, 2]], [7, 7, 7])

Set Cover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set Cover is approximated using a greedy algorithm.

.. code:: python

    from approximations image set_cover

    cover = set_cover(
        {1, 2, 3, 4, 5},
        [{1, 2}, {3}, {1, 2, 3, 4}, {1, 3, 5}],
        [1, 2, 3, 4]
    ) # [0, 2, 3]

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/approximations.png
   :target: https://travis-ci.org/LucaCappelletti94/approximations
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_approximations&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_approximations
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_approximations&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_approximations
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_approximations&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_approximations
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/approximations/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/approximations?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/approximations.svg
    :target: https://badge.fury.io/py/approximations
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/approximations
    :target: https://pepy.tech/badge/approximations
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/5fe5e0229af449d9863f06682189e880
    :target: https://www.codacy.com/manual/LucaCappelletti94/approximations?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/approximations&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/fa6c757264e228633237/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/approximations/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/fa6c757264e228633237/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/approximations/test_coverage
    :alt: Code Climate Coverate
