import uuid as _uuid

from api import TestApi
from assertions import TestAssertions
from interface import TestInterface

"""
Tests the SIMON microservice
"""


class TestSimon(TestAssertions):
    """
    Tests the SIMON microservice
    """

    def test_secure_sum(self):
        """tests the SecureSum microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='SecureSum',
            data_alice=123.456789,
            data_bob=1234.56789,
            correct={'sum': 1358.024679})

    def test_secure_sum_3p(self):
        """tests the SecureSum microprotocol for three parties"""
        self.run_three_party_test(
            microprotocol='SecureSum',
            data_alice=123.456789,
            data_bob=1234.56789,
            data_charlie=12345.6789,
            correct={'sum': 13703.703579})

    def test_secure_matrix_multiplication(self):
        """tests the SecureMatrixMultiplication
        microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='SecureMatrixMultiplication',
            data_alice=[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            data_bob=[[[-1, 4, 7], [2, -5, 3], [0, 1, -5]]],
            correct={'product': [[3, -3, -2], [6, -3, 13], [9, -3, 28]]})

    def test_secure_median(self):
        """tests the SecureMedian microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='SecureMedian',
            data_alice=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            data_bob=[10, 11, 12, 13, 14, 15, 16, 17, 18],
            correct={'median': 9.5})

        self.run_two_party_test(
            microprotocol='SecureMedian',
            data_alice=[-970, 138, 636, 626, -75, 449, -300, 100, 352, -168,
                        -918, -23, 434],
            data_bob=[748, 672, -221, 911, 309, 108, -235, 185,
                      -308, -477, 236, 537, -778, 168, 864, 372,
                      449, -267, 101, 48, -83, -861, -39, -25,
                      786, 11, -486, 375, 294, 678, -282, -591, -530],
            correct={'median': 100.5})

        self.run_two_party_test(
            microprotocol='SecureMedian',
            data_alice=[-97, -887, 621, -349, 280, 982, -996, 445, 259, -744,
                        17, 232, 184, -171, 159, 698, 981, 840, -257, 407, -14,
                        -360, 858, -804, -833, 440, 952, 231, 911, -802, 730,
                        373, -149, -836, 809, 663, 881],
            data_bob=[-626, 510, -913, -878, 982, 535, -671, -231, -246],
            correct={'median': 207.5})

        self.run_two_party_test(
            microprotocol='SecureMedian',
            data_alice=[0.831716252, 0.126745429, 0.710476552, 0.719059441,
                        0.244178834, 0.024707453, 0.799845091, 0.595732707,
                        0.603235169],
            data_bob=[0.289322013, 0.123191087, 0.309589152, 0.401435888,
                      0.149810757, 0.710600217, 0.565250515, 0.605866414,
                      0.86703249,  0.399420031, 0.707189188, 0.128262609,
                      0.275647641, 0.902004041, 0.840246023, 0.44665615,
                      0.686489818, 0.505423716, 0.327261739, 0.641869952,
                      0.905716932, 0.71225097, 0.759316815, 0.842361933,
                      0.541164596, 0.597520199, 0.831365555, 0.401612055,
                      0.803858239, 0.377603516, 0.254109827, 0.090941054,
                      0.874912006, 0.066641412, 0.510510482, 0.671451831,
                      0.206979523],
            correct={'median': 0.580491611})

        self.run_two_party_test(
            microprotocol='SecureMedian',
            data_alice=[0.244342052551627,
                        0.830993512950289,
                        0.988275104137248,
                        0.220365083595427,
                        0.0477064964715441,
                        0.556520465326501,
                        0.287127587416642,
                        0.269356192310966,
                        0.74221191178885,
                        0.177389344090634,
                        0.227844199258586,
                        0.0730977531011668,
                        0.0701792403022937],
            data_bob=[0.383569250689215,
                      0.0831464384553564,
                      0.265322907204646,
                      0.338980363838168,
                      0.825095098622235,
                      0.721926945820403,
                      0.729013248911152,
                      0.379865164972118,
                      0.214929476049738,
                      0.251763948992772,
                      0.664381280285514,
                      0.789271141741488,
                      0.309799243491765,
                      0.416014336098567,
                      0.692848622753307,
                      0.141920951834456,
                      0.649978547801793,
                      0.903360320852501,
                      0.353194880037834,
                      0.203657535886452,
                      0.861417440983921],
            correct={'median': 0.346087621938001})

    def test_set_intersection(self):
        """tests the SetIntersection microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='SetIntersection',
            data_alice=[['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                        ['E', 'C', 'B', 'A', 'D']],
            data_bob=[['C', 'F', 'A'], ['C', 'F', 'A', 'D']],
            correct={'size_intersection': 2,
                     'intersection': ['A', 'C']})

    def test_set_intersection_size(self):
        """tests the SetIntersectionSize microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='SetIntersectionSize',
            data_alice=[['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                        ['E', 'C', 'B', 'A', 'D']],
            data_bob=[['C', 'F', 'A'], ['C', 'F', 'A', 'D']],
            correct={'size_intersection': 2})

    def test_statistics_bivariate(self):
        """tests the StatisticsBivariate microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='StatisticsBivariate',
            data_alice=[(1.0, 2.0)],
            data_bob=[(2.0, 3.0)],
            correct={'samples': 2,
                     'covariance_mle': 0.25,
                     'covariance': 0.5,
                     'correlation_coefficient': 1.0,
                     'regression_slope': 1.0,
                     'regression_interceipt': 1.0,
                     'regression_slope_only': 1.6})

    def test_statistics_frequency(self):
        """tests the StatisticsFrequency microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='StatisticsFrequency',
            data_alice=['A', 'A', 'B', 'C', 'C', 'C'],
            data_bob=['A', 'B', 'C', 'B', 'C', 'B', 'B', 'C', 'C'],
            correct={'mode': 'C',
                     'histogram': {'A': 3, 'B': 5, 'C': 7}})

    def test_statistics_contingency(self):
        """tests the StatisticsContingency microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='StatisticsContingency',
            data_alice=[('smoker', 'male'), ('non-smoker', 'female'),
                        ('smoker', 'female'), ('non-smoker', 'female'),
                        ('smoker', 'male'), ('smoker', 'male')],
            data_bob=[('non-smoker', 'female'), ('smoker', 'female'),
                      ('smoker', 'male'), ('non-smoker', 'female'),
                      ('non-smoker', 'female'), ('non-smoker', 'male')],
            correct={'mode': ('non-smoker', 'female'),
                     'table': {'non-smoker': {'male': 1, 'female': 5},
                               'smoker': {'male': 4, 'female': 2}}})

    def test_statistics_contingency_vertical(self):
        """tests the StatisticsContingencyVertical microprotocol
        for two parties"""
        self.run_two_party_test(
            microprotocol='StatisticsContingencyVertical',
            data_alice=[('A', 'male'), ('B', 'female'), ('C', 'male'),
                        ('D', 'female'), ('E', 'male'), ('F', 'male')],
            data_bob=[('A', 'non-smoker'), ('B', 'smoker'), ('C', 'smoker'),
                      ('D', 'non-smoker'), ('E', 'non-smoker'),
                      ('G', 'non-smoker')],
            correct={'mode': ('male', 'non-smoker'),
                     'table': {'male': {'non-smoker': 2, 'smoker': 1},
                               'female': {'non-smoker': 1, 'smoker': 1}}})

    def test_statistics_univariate(self):
        """tests the StatisticsUnivariate microprotocol for two parties"""
        self.run_two_party_test(
            microprotocol='StatisticsUnivariate',
            data_alice=[1.0, 2.0, 3.0, 4.0, 5.0],
            data_bob=[6.0, 7.0, 8.0, 9.0, 10.0],
            correct={'samples': 10,
                     'minimum': 1.0,
                     'maximum': 10.0,
                     'sum': 55.0,
                     'mean': 5.5,
                     'harmonic_mean': 3.4141715214740550061,
                     'geometric_mean': 4.5287286881167647622,
                     'variance': 9.1666666666666666667,
                     'variance_mle': 8.25,
                     'variance_of_sample_mean': 0.91666666666666666667,
                     'standard_deviation': 3.0276503540974916654,
                     'standard_deviation_mle': 2.8722813232690143299,
                     'standard_error_of_sample_mean': 0.95742710775633810998,
                     'coefficient_of_variation': 0.55048188256318030280,
                     'coefficient_of_variation_mle': 0.52223296786709351453,
                     'root_mean_square': 6.2048368229954282981,
                     'root_mean_square_deviation': 2.8722813232690143299,
                     'skewness': 0.0,
                     'kurtosis': 1.7757575757575757576,
                     'kurtosis_excess': -1.2242424242424242424,
                     'hyper_skewness': 0.0,
                     'hyper_flatness': 3.7033976124885215794})

    def test_statistics_regression_OLS_vertical(self):
        """tests the StatisticsRegressionOLSVertical microprotocol
        for two parties"""
        self.run_two_party_test(
            microprotocol='StatisticsRegressionOLSVertical',
            data_alice=[[[1.0, 2.0, 0.0], [2.0, 1.0, 1.0], [0.0, 4.0, 3.0]]],
            data_bob=[[17.0, 23.0, 45.0]],
            correct={'mle': [[5.0, 6.0, 7.0]]})

    def run_two_party_test(self, microprotocol, data_alice, data_bob, correct):

        """creates two local busses on a synthetic interface
        and runs two-party computation"""

        interface_a = TestInterface()
        interface_b = TestInterface()
        interface_sync = TestInterface()

        network_a = {'nodes': [interface_a, interface_b], 'myself': 0}
        network_b = {'nodes': [interface_a, interface_b], 'myself': 1}

        api_a = TestApi(interface=interface_a)
        api_b = TestApi(interface=interface_b)
        api_sync = TestApi(interface=interface_sync)

        microservice_a = api_a.create(protocol="Simon")
        microservice_b = api_b.create(protocol="Simon")

        task_a = microservice_a.create_task(microprotocol=microprotocol,
                                            network=network_a)

        invitation_a = api_a.download(task_a.invite())

        uuid = str(_uuid.uuid4())
        api_sync.send_broadcast(invitation_a, uuid)

        invitation_b = api_sync.receive_broadcast(uuid)
        task_b = microservice_b.join_task(invitation=invitation_b,
                                          network=network_b)

        task_a.input(data=data_alice)
        task_b.input(data=data_bob)

        task_a.start()
        task_b.start()

        repr_res_a = None
        while repr_res_a is None:
            repr_res_a = task_a.result()
        result_a = api_a.download(repr_res_a)
        self.assertEqual(result_a['inputs'], 2)
        for key in correct:
            self.outer_assertion(correct[key], result_a['result'][key], key)
        for key in result_a['result']:
            self.outer_assertion(correct[key], result_a['result'][key], key)

    def run_three_party_test(self, microprotocol, data_alice, data_bob,
                             data_charlie, correct):

        """creates three local busses on a synthetic interface
        and runs three-party computation"""

        interface_a = TestInterface()
        interface_b = TestInterface()
        interface_c = TestInterface()
        interface_sync = TestInterface()

        network_a = {'nodes': [interface_a, interface_b, interface_c],
                     'myself': 0}
        network_b = {'nodes': [interface_a, interface_b, interface_c],
                     'myself': 1}
        network_c = {'nodes': [interface_a, interface_b, interface_c],
                     'myself': 2}

        api_a = TestApi(interface=interface_a)
        api_b = TestApi(interface=interface_b)
        api_c = TestApi(interface=interface_c)
        api_sync = TestApi(interface=interface_sync)

        microservice_a = api_a.create(protocol="Simon")
        microservice_b = api_b.create(protocol="Simon")
        microservice_c = api_c.create(protocol="Simon")

        task_a = microservice_a.create_task(microprotocol=microprotocol,
                                            network=network_a)

        invitation_a = api_a.download(task_a.invite())

        uuid = str(_uuid.uuid4())
        api_sync.send_broadcast(invitation_a, uuid)

        invitation_b = api_sync.receive_broadcast(uuid)
        task_b = microservice_b.join_task(invitation=invitation_b,
                                          network=network_b)

        invitation_c = api_sync.receive_broadcast(uuid)
        task_c = microservice_c.join_task(invitation=invitation_c,
                                          network=network_c)

        task_a.input(data=data_alice)
        task_b.input(data=data_bob)
        task_c.input(data=data_charlie)

        task_a.start()
        task_b.start()
        task_c.start()

        repr_res_a = None
        while repr_res_a is None:
            repr_res_a = task_a.result()
        result_a = api_a.download(repr_res_a)
        self.assertEqual(result_a['inputs'], 3)
        for key in correct:
            self.outer_assertion(correct[key], result_a['result'][key], key)
        for key in result_a['result']:
            self.outer_assertion(correct[key], result_a['result'][key], key)
