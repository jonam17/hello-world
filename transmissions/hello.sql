-- TRANSMISSION 04 // SQL — every workflow ends up in a table eventually.

CREATE TABLE IF NOT EXISTS transmissions (
    id          SERIAL PRIMARY KEY,
    node        TEXT NOT NULL DEFAULT '00',
    payload     TEXT NOT NULL,
    sent_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO transmissions (payload) VALUES ('Hello, World');

SELECT '[NODE ' || node || '] ' || payload AS signal FROM transmissions;
