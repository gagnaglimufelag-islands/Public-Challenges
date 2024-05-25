DROP TABLE IF EXISTS users;

CREATE TABLE users (
    username VARCHAR(20),
    password VARCHAR(32),
    is_admin boolean
);

INSERT INTO users (username, password, is_admin) VALUES ('Bob', 'bdc87b9c894da5168059e00ebffb9077', False);
INSERT INTO users (username, password, is_admin) VALUES ('Alice', 'd8578edf8458ce06fbc5bb76a58c5ca4', False);
INSERT INTO users (username, password, is_admin) VALUES ('Eve', 'c3712025edec7b1cd46241bfde3d0229', True);
INSERT INTO users (username, password, is_admin) VALUES ('Joe', 'd0763edaa9d9bd2a9516280e9044d885', False);
INSERT INTO users (username, password, is_admin) VALUES ('Rob', '5fcfd41e547a12215b173ff47fdd3739', False);
INSERT INTO users (username, password, is_admin) VALUES ('Jane', '5d41402abc4b2a76b9719d911017c592', False);
INSERT INTO users (username, password, is_admin) VALUES ('Suse', '25f9e794323b453885f5181f1b624d0b', False);


CREATE USER postgres_read WITH PASSWORD 'fmkdlaojkl45F';
GRANT CONNECT ON DATABASE postgres TO postgres_read;
GRANT USAGE ON SCHEMA public TO postgres_read;
GRANT SELECT ON users TO postgres_read;