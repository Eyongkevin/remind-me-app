CREATE TABLE reminder (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   label VARCHAR(100) NOT NULL,
   days VARCHAR(100) NOT NULL, -- "Mon, Tue, Wed, Thur, Fri, Sat, Sun"
   alert_type VARCHAR(100) NOT NULL, -- '{"sound": true, "popup": false}'
   alert_time TIME NOT NULL,
   active BOOL,  --DEFAULT True,
   repeat BOOL, -- DEFAULT False,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);