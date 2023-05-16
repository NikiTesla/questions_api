CREATE TABLE IF NOT EXISTS questions(
    id serial PRIMARY KEY,
    question VARCHAR(255),
    answer VARCHAR(255),
    created_at Datetime
);