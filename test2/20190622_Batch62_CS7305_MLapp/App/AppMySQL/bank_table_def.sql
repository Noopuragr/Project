use cust_db;
DROP TABLE IF EXISTS bank;
CREATE TABLE bank (
  customer_no int(11) NOT NULL auto_increment,
  age int(11) DEFAULT NULL,
  job varchar(250) DEFAULT NULL,
  marital varchar(250) DEFAULT NULL,
  eduation varchar(250) DEFAULT NULL,
  credit_default varchar(250) DEFAULT NULL,
  housing varchar(30) DEFAULT NULL,
  loan varchar(250) DEFAULT NULL,
  contact varchar(250) DEFAULT NULL,
  contacted_month varchar(250) DEFAULT NULL,
  day_of_week varchar(250) DEFAULT NULL,
  duration int(11) DEFAULT NULL,
  compaign varchar(250) DEFAULT NULL,
  pdays int(11) DEFAULT NULL,
  previous int(11) DEFAULT NULL,
  poutcome varchar(250) DEFAULT NULL,
  emp_var_rate float DEFAULT NULL,
  cons_price_idx float DEFAULT NULL,
  cons_conf_idx float DEFAULT NULL,
  euribor3m float DEFAULT NULL,
  nr_employees float DEFAULT NULL,
  y varchar(250) DEFAULT NULL,
  PRIMARY KEY (customer_no)
);
