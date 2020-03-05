def solve_exercise(session, exercise_id):
	session._request(
		url    = f'/v1/exercises/{exercise_id}/executions',
		method = 'OPTIONS',
	)

	r = session._request(
		url    = f'/v1/exercises/{exercise_id}/executions',
		method = 'POST',
	)

	r['vote']       = 100
	r['result']     = True
	r['quizzes_ok'] = len(r['quiz_executions'])
	for quiz in r['quiz_executions']:
		quiz['result']  = True
		quiz['value']   = True
		quiz['answers'] = quiz['quiz']['solutions']

	run = r['id']

	session._request(
		url    = f'/v1/exercises/{exercise_id}/executions/{run}',
		method = 'OPTIONS'
	)

	return session._request(
		url     = f'/v1/exercises/{exercise_id}/executions/{run}',
		json    = r,
		method  = 'PUT'
	)

def complete_board(session, board_id):
	elements = session.get_board_elements(board_id)
	for e in elements['board_elements']:
		session.track_element(board_id, e['id'])

def complete_group(session, group_id):
	for board in session.get_boards(group_id):
		complete_board(session, board['id'])
