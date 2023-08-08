# fetch votes for a given poll and calculate its result
from backend.approval import calculate_approval
from backend.db.Database import Database
from backend.fptp import calculate_fptp
from backend.runoff import calculate_runoff


def calculate_result(poll_id):
    db = Database.get_instance()
    print('DB called')
    poll = db.get_poll(id=poll_id)
    if not poll:
        raise Exception('poll not found')
    votes = db.get_poll_votes(poll_id, only_values=True)
    candidates = db.get_poll_candidates(poll_id)
    candidate_ids = [c['candidate_id'] for c in candidates]
    if poll['type'] == 'fptp':
        return calculate_fptp(votes, candidate_ids)
    elif poll['type'] == 'runoff':
        return calculate_runoff(votes, candidate_ids)
    elif poll['type'] == 'approval':
        return calculate_approval(votes, candidate_ids, max_approved=poll['max_approved'], min_threshold=poll['min_threshold'])