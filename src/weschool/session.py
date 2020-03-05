import requests
import json


class Session:

	def __init__(self, username: str = '', password: str = ''):
		self.username = username
		self.password = password

		self.client_id     = '2_63vhapa1xosos88o004cgs4wkg444gcos8sc4gg0gggksc8k0g'
		self.client_secret = '11o29phvsgb488gg4gsso488w480wk484oowcsk4o4cg808048'

		self.session   = requests.Session()
		self.logged_in = False
		self.bearer    = ''

		self.base_url = 'https://api.weschool.com'

	def _request(self, url: str, json = None, method: str = 'GET'):
		methods = {
			'GET'    : self.session.get,
			'POST'   : self.session.post,
			'OPTIONS': self.session.options,
			'PUT'    : self.session.put,
		}

		r = methods[method](
			url = self.base_url + url,
			json = json,
			headers = {
				'Authorization':  f'Bearer {self.bearer}'
			},
		)

		if r.text:
			return r.json()

	def login(self):
		r = self.session.post(
			url  = 'https://api.weschool.com/oauth/v2/token',
			json = {
				'scope': 'user',
				'client_id': self.client_id,
				'client_secret': self.client_secret,
				'grant_type': 'password',
				'username': self.username,
				'password': self.password,
			}
		)

		self.bearer = r.json()['access_token']

	def get_me(self):
		"""
		_=1583419959049
		"""
		return self._request(url = '/v1/users/me')

	def get_groups(self, user_id: str = ''):
		"""
		scope=list
		start=0
		max_timestamp=1583419959049
		"""
		if user_id:
			return self._request(url = f'/v1/users/{user_id}/groups')
		else:
			return self._request(url = '/v2/groups')

	def get_group_users(self, group_id):
		"""
		with_pagination=1
		offset=0
		_=1583419959049
		"""
		return self._request(url = f'/v1/groups/{group_id}/users')

	def get_boards(self, group_id):
		"""
		limit=200
		_=1583419959049
		"""
		return self._request(url = f'/v1/groups/{group_id}/boards')

	def get_board_elements(self, board_id):
		"""
		_=1583419959049
		"""
		return self._request(url = f'/v1/boards/{board_id}/')

	def track_element(self, board_id, element_id):
		"""
		_=1583419959049
		"""
		return self._request(url = f'/v1/boards/{board_id}/boardelements/{element_id}/track')

	def get_exercises(self, group_id):
		"""
		filter=ASSIGNMENTe
		group_id={group_id}
		"""
		return self._request(url = f'/v1/exercises?filter=ASSIGNMENT&group_id={group_id}')

	def get_deadlines(self, group_id):
		"""
		_=1583419959049
		"""
		return self._request(url = f'/v1/groups/{group_id}/deadlines')
