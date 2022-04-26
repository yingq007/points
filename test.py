import unittest
import json
import track_points



class AdderTestCase(unittest.TestCase):
    unittest.TestLoader.sortTestMethodsUsing = None

    def test_add_transaction(self):

        client=track_points.app.test_client()
        track_points.app.config['TESTING'] = True

        response = client.post('http://127.0.0.1:5000/add_points',
        data = {'payer':'DANNON','points':1000,'timestamp':'datetime.datetime(2020, 11, 02, 14, 00)'})
        self.assertEqual(response.status_code, 200)

        response = client.post('http://127.0.0.1:5000/add_points',
        data = {'payer':'UNILEVER','points':200,'timestamp':'datetime.datetime(2020, 10, 31, 11, 00)'})
        self.assertEqual(response.status_code, 200)

        response = client.post('http://127.0.0.1:5000/add_points',
        data = {'payer':'DANNON','points':-200,'timestamp':'datetime.datetime(2020, 10, 31, 15, 00)'})
        self.assertEqual(response.status_code, 200)

        response = client.post('http://127.0.0.1:5000/add_points',
        data = {'payer':'MILLER COORS','points':10000,'timestamp':'datetime.datetime(2020, 11, 01, 14, 00)'})
        self.assertEqual(response.status_code, 200)

        response = client.post('http://127.0.0.1:5000/add_points',
        data = {'payer':'DANNON','points':300,'timestamp':'datetime.datetime(2020, 10, 31, 10, 00)'})
        self.assertEqual(response.status_code, 200)

    def test_spend_points_in_account(self):
        client=track_points.app.test_client()
        response = client.post('http://127.0.0.1:5000/spend_points',
        data = {'points':"5000"})
        self.assertEqual(response.status_code, 200)

    def test_show_balance_lst(self):

        client=track_points.app.test_client()
        response = client.post('http://127.0.0.1:5000/show_balance')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    # If called like a script, run our tests
    unittest.main()