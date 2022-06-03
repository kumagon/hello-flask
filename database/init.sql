CREATE TABLE item (
  id INT AUTO_INCREMENT,
  title VARCHAR(50),
  description VARCHAR(255),
  userId INT(11),
  createdAt DATETIME,
  updatedAt DATETIME,
  PRIMARY KEY (id)
);

INSERT INTO item (title, description, userId, createdAt, updatedAt) VALUE ('test', 'test', 1, NOW(), NOW());

