CREATE TABLE IF NOT EXISTS polls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    type TEXT,
    inst_name TEXT,
    description TEXT,
    security_key TEXT,
    secure_mode INTEGER,
    num_candidates INTEGER,
    num_voters INTEGER,
    max_approved INTEGER,
    min_threshold REAL,
    status TEXT DEFAULT 'not_started',
    date_created DATETIME DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS poll_candidate (
    poll_id INTEGER,
    candidate_id TEXT,
    name TEXT,
    faction TEXT,
    PRIMARY KEY (poll_id, candidate_id)
);

CREATE TABLE IF NOT EXISTS poll_proposal (
    poll_id INTEGER,
    proposal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    FOREIGN KEY (poll_id) REFERENCES polls(id)
    );

CREATE TABLE IF NOT EXISTS poll_result (
    poll_id INTEGER PRIMARY KEY,
    winners TEXT,
    order_cands TEXT,
    eliminated TEXT,
    referendum_result TEXT,
    FOREIGN KEY (poll_id) REFERENCES polls(id)
);

CREATE TABLE IF NOT EXISTS votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poll_id INTEGER,
    vote TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (poll_id) REFERENCES polls(id)
);