CREATE TABLE IF NOT EXISTS analysis_history (
    id SERIAL PRIMARY KEY,
    word_count INT NOT NULL,
    mode VARCHAR(50) NOT NULL,
    read_time_minutes INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
