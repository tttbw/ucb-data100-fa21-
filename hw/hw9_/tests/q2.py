test = {   'name': 'q2',
    'points': 4,
    'suites': [   {   'cases': [   {'code': ">>> x, y = part_1_data['x'], part_1_data['y'];\n>>> abs(sin_MSE([0, np.pi], x, y) - 19.49000412080223) <= 1e-5\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> x, y = part_1_data['x'], part_1_data['y'];\n>>> abs(sin_MSE_dt1([0, np.pi], x, y) - -25.376660670924529) <= 1e-5\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> x, y = part_1_data['x'], part_1_data['y'];\n>>> abs(sin_MSE_dt2([0, np.pi], x, y) - 1.9427210155296564) <= 1e-5\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
