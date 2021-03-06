DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    item_count INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL
);