        
CREATE DATABASE IF NOT EXISTS Agenda;

use Agenda;

CREATE TABLE users(
    id           int(25) auto_increment not null,
    name         varchar(100),
    LastName     varchar(255),
    email        varchar(255) not null,
    password     varchar(255) not null,
    date         date not null,
    CONSTRAINT   pk_users PRIMARY KEY(id),
    CONSTRAINT   uq_email UNIQUE(email)
) ENGINE = InnoDB;


CREATE TABLE Notes(
    id          int(25) auto_increment not null,
    user_id     int(25) not null,
    title       varchar(255) not null,
    descriptio  MEDIUMTEXT,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(user_id) REFERENCES users(id)
) ENGINE = InnoDB;

