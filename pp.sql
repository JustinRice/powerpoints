CREATE DATABASE powerpoints;
\c powerpoints;


CREATE TABLE IF NOT EXISTS teams (
  id SERIAL not null, 
  school text NOT NULL,
  mascot text NOT NULL,
  class int NOT NULL,
  tracked char(1) NOT NULL,
  district text,
  confID int,
  points decimal(4,2) NOT NULL default 0.00,
  pmax decimal(4,2) NOT NULL default 0.00,
  pmin decimal(4,2) NOT NULL default 0.00,
  week1 int,
  week2 int,
  week3 int,
  week4 int,
  week5 int,
  week6 int,
  week7 int,
  week8 int,
  week9 int,
  week10 int,
  week11 int,
  week12 int,
  PRIMARY KEY(id)
);

insert into teams (school, mascot, class, tracked, district, confID) values ('xxxx', 'xx', x, 'Y', 'xxx', xx);

insert into teams (school, mascot, class, tracked, district, confID) values ('Battlefield', 'Bobcats', 6, 'Y', 'Cardinal', 8);
insert into teams (school, mascot, class, tracked, district, confID) values ('Stonewall Jackson', 'xx', 6, 'Y', 'Cardinal', 8);
insert into teams (school, mascot, class, tracked, district, confID) values ('Osbourn', 'xx', 6, 'Y', 'Cardinal', 8);
insert into teams (school, mascot, class, tracked, district, confID) values ('Osbourn Park', 'xx', 6, 'Y', 'Cardinal', 8);
insert into teams (school, mascot, class, tracked, district, confID) values ('Patriot', 'xx', 6, 'Y', 'Cardinal', 8);

insert into teams (school, mascot, class, tracked, district, confID) values ('Centreville', 'xx', 6, 'Y', 'District 5', 5);
insert into teams (school, mascot, class, tracked, district, confID) values ('Chantilly', 'xx', 6, 'Y', 'District 5', 5);
insert into teams (school, mascot, class, tracked, district, confID) values ('Herndon', 'xx', 6, 'Y', 'District 5', 5);
insert into teams (school, mascot, class, tracked, district, confID) values ('Oakton', 'xx', 6, 'Y', 'District 5', 5);
insert into teams (school, mascot, class, tracked, district, confID) values ('James Robinson', 'xx', 6, 'Y', 'District 5', 5);
insert into teams (school, mascot, class, tracked, district, confID) values ('Westfield', 'xx', 6, 'Y', 'District 5', 5);

insert into teams (school, mascot, class, tracked, district, confID) values ('Fairfax', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('Hayfield', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('Langley', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('James Madison', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('McLean', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('South Lakes', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('Washington-Lee', 'xx', 6, 'Y', 'District 6', 6);
insert into teams (school, mascot, class, tracked, district, confID) values ('Yorktown', 'xx', 6, 'Y', 'District 6', 6);

insert into teams (school, mascot, class, tracked, district, confID) values ('Annandale', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lake Braddock', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('Mount Vernon', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('South County', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('West Potomac', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('West Springfield', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('T.C. Williams', 'xx', 6, 'Y', 'District 7', 7);
insert into teams (school, mascot, class, tracked, district, confID) values ('W.T. Woodson', 'xx', 6, 'Y', 'District 7', 7);

insert into teams (school, mascot, class, tracked, district, confID) values ('Bayside', 'xx', 6, 'Y', 'Beach', 1);
insert into teams (school, mascot, class, tracked, district, confID) values ('Cox', 'xx', 6, 'Y', 'Beach', 1);
insert into teams (school, mascot, class, tracked, district, confID) values ('First Colonial', 'xx', 6, 'Y', 'Beach', 1);
insert into teams (school, mascot, class, tracked, district, confID) values ('Kellam', 'xx', 6, 'Y', 'Beach', 1);
insert into teams (school, mascot, class, tracked, district, confID) values ('Landstown', 'xx', 6, 'Y', 'Beach', 1);
insert into teams (school, mascot, class, tracked, district, confID) values ('Ocean Lakes', 'xx', 6, 'Y', 'Beach', 1);
insert into teams (school, mascot, class, tracked, district, confID) values ('Tallwood', 'xx', 6, 'Y', 'Beach', 1);

insert into teams (school, mascot, class, tracked, district, confID) values ('Forest Park', 'Bruins', 6, 'Y', 'Cardinal', 4);
insert into teams (school, mascot, class, tracked, district, confID) values ('Freedom (PW)', 'Eagles', 6, 'Y', 'Cardinal', 4);
insert into teams (school, mascot, class, tracked, district, confID) values ('Gar-Field', 'Indians', 6, 'Y', 'Cardinal', 4);
insert into teams (school, mascot, class, tracked, district, confID) values ('Hylton', 'Bulldogs', 6, 'Y', 'Cardinal', 4);
insert into teams (school, mascot, class, tracked, district, confID) values ('Woodbridge', 'Vikings', 6, 'Y', 'Cardinal', 4);

insert into teams (school, mascot, class, tracked, district, confID) values ('Thomas Dale', 'xx', 6, 'Y', 'Central', 3);

insert into teams (school, mascot, class, tracked, district, confID) values ('Colonial Forge', 'Eagles', 6, 'Y', 'Commonwealth', 4);
insert into teams (school, mascot, class, tracked, district, confID) values ('Riverbend', 'Bears', 6, 'Y', 'Commonwealth', 4);

insert into teams (school, mascot, class, tracked, district, confID) values ('Clover Hill', 'xx', 6, 'Y', 'Dominion', 3);
insert into teams (school, mascot, class, tracked, district, confID) values ('Cosby', 'xx', 6, 'Y', 'Dominion', 3);
insert into teams (school, mascot, class, tracked, district, confID) values ('James River (Ch)', 'xx', 6, 'Y', 'Dominion', 3);
insert into teams (school, mascot, class, tracked, district, confID) values ('Manchester', 'xx', 6, 'Y', 'Dominion', 3);

insert into teams (school, mascot, class, tracked, district, confID) values ('Granby', 'xx', 6, 'Y', 'Eastern', 2);

insert into teams (school, mascot, class, tracked, district, confID) values ('Woodside', 'xx', 6, 'Y', 'Peninsula', 2);

insert into teams (school, mascot, class, tracked, district, confID) values ('Franklin Co.', 'xx', 6, 'Y', 'Piedmont', 3);

insert into teams (school, mascot, class, tracked, district, confID) values ('Grassfield', 'xx', 6, 'Y', 'Southeastern', 2);
insert into teams (school, mascot, class, tracked, district, confID) values ('Oscar Smith', 'xx', 6, 'Y', 'Southeastern', 2);
insert into teams (school, mascot, class, tracked, district, confID) values ('Western Branch', 'xx', 6, 'Y', 'Southeastern', 2);

insert into teams (school, mascot, class, tracked) values ('Athens (NC)', 'xx', 6, 'N');
insert into teams (school, mascot, class, tracked) values ('Northwestern (SC)', 'xx', 6, 'N');

insert into teams (school, mascot, class, tracked, district, confID) values ('Atlee', 'xx', 5, 'Y', 'Capital', 16);
insert into teams (school, mascot, class, tracked, district, confID) values ('Patrick Henry (Ash)', 'xx', 5, 'Y', 'Capitals', 16);

insert into teams (school, mascot, class, tracked, district, confID) values ('Potomac', 'Panthers', 5, 'Y', 'Cardinal', 15);

insert into teams (school, mascot, class, tracked, district, confID) values ('Brooke Point', 'Black-Hawks', 5, 'Y', 'Commonwealth', 15);
insert into teams (school, mascot, class, tracked, district, confID) values ('Massaponax', 'Panthers', 5, 'Y', 'Commonwealth', 15);
insert into teams (school, mascot, class, tracked, district, confID) values ('Mountain View', 'Wildcats', 5, 'Y', 'Commonwealth', 15);
insert into teams (school, mascot, class, tracked, district, confID) values ('North Stafford', 'Wolverines', 5, 'Y', 'Commonwealth', 15);
insert into teams (school, mascot, class, tracked, district, confID) values ('Stafford', 'Indians', 5, 'Y', 'Commonwealth', 15);

insert into teams (school, mascot, class, tracked, district, confID) values ('Thomas Edison', 'xx', 5, 'Y', 'District 13', 13);
insert into teams (school, mascot, class, tracked, district, confID) values ('Falls Church', 'xx', 5, 'Y', 'District 13', 13);
insert into teams (school, mascot, class, tracked, district, confID) values ('T. Jefferson (Ale)', 'xx', 5, 'Y', 'District 13', 13);
insert into teams (school, mascot, class, tracked, district, confID) values ('R.E. Lee (Spr)', 'xx', 5, 'Y', 'District 13', 13);
insert into teams (school, mascot, class, tracked, district, confID) values ('George Marshall', 'xx', 5, 'Y', 'District 13', 13);
insert into teams (school, mascot, class, tracked, district, confID) values ('JEB Stuart', 'xx', 5, 'Y', 'District 13', 13);
insert into teams (school, mascot, class, tracked, district, confID) values ('Wakefield', 'xx', 5, 'Y', 'District 13', 13);

insert into teams (school, mascot, class, tracked, district, confID) values ('Albemarle', 'Patriot', 5, 'Y', 'Jefferson', 16);
insert into teams (school, mascot, class, tracked, district, confID) values ('Orange', 'Hornets', 5, 'Y', 'Jefferson', 16);

insert into teams (school, mascot, class, tracked, district, confID) values ('Halifax Co.', 'xx', 5, 'Y', 'Piedmont', 16);

insert into teams (school, mascot, class, tracked, district, confID) values ('Briar Woods', 'xx', 5, 'Y', 'Potomac', 14);
insert into teams (school, mascot, class, tracked, district, confID) values ('Broad Run', 'xx', 5, 'Y', 'Potomac', 14);
insert into teams (school, mascot, class, tracked, district, confID) values ('Potomac Falls', 'xx', 5, 'Y', 'Potomac', 14);
insert into teams (school, mascot, class, tracked, district, confID) values ('Stone Bridge', 'xx', 5, 'Y', 'Potomac', 14);
insert into teams (school, mascot, class, tracked, district, confID) values ('Tuscarora', 'xx', 5, 'Y', 'Potomac', 14);

insert into teams (school, mascot, class, tracked, district, confID) values ('Patrick Henry (Roa)', 'xx', 5, 'Y', 'River Ridge', 16);

insert into teams (school, mascot, class, tracked, district, confID) values ('Green Run', 'xx', 5, 'Y', 'Beach', 9);
insert into teams (school, mascot, class, tracked, district, confID) values ('Kempsville', 'xx', 5, 'Y', 'Beach', 9);
insert into teams (school, mascot, class, tracked, district, confID) values ('Princess Anne', 'xx', 5, 'Y', 'Beach', 9);
insert into teams (school, mascot, class, tracked, district, confID) values ('Salem (VB)', 'xx', 5, 'Y', 'Beach', 9);

insert into teams (school, mascot, class, tracked, district, confID) values ('Henrico', 'xx', 5, 'Y', 'Capital', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('Highland Springs', 'xx', 5, 'Y', 'Capital', 12);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lee-Davis', 'xx', 5, 'Y', 'Capital', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('Varina', 'xx', 5, 'Y', 'Capital', 12);

insert into teams (school, mascot, class, tracked, district, confID) values ('Matoaca', 'xx', 5, 'Y', 'Central', 12);
insert into teams (school, mascot, class, tracked, district, confID) values ('Meadowbrook', 'xx', 5, 'Y', 'Central', 12);
insert into teams (school, mascot, class, tracked, district, confID) values ('Prince George', 'xx', 5, 'Y', 'Central', 12);

insert into teams (school, mascot, class, tracked, district, confID) values ('Deep Run', 'xx', 5, 'Y', 'Colonial', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('Douglas Freeman', 'xx', 5, 'Y', 'Colonial', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('Glen Allen', 'xx', 5, 'Y', 'Colonial', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('Mills Godwin', 'xx', 5, 'Y', 'Colonial', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('Hermitage', 'xx', 5, 'Y', 'Colonial', 11);
insert into teams (school, mascot, class, tracked, district, confID) values ('J.R. Tucker', 'xx', 5, 'Y', 'Colonial', 11);

insert into teams (school, mascot, class, tracked, district, confID) values ('L.C. Bird', 'xx', 5, 'Y', 'Dominion', 12);

insert into teams (school, mascot, class, tracked, district, confID) values ('Maury', 'xx', 5, 'Y', 'Eastern', 9);
insert into teams (school, mascot, class, tracked, district, confID) values ('Norview', 'xx', 5, 'Y', 'Eastern', 9);

insert into teams (school, mascot, class, tracked, district, confID) values ('Bethel', 'xx', 5, 'Y', 'Peninsula', 10);
insert into teams (school, mascot, class, tracked, district, confID) values ('Gloucester', 'xx', 5, 'Y', 'Peninsula', 10);
insert into teams (school, mascot, class, tracked, district, confID) values ('Hampton', 'xx', 5, 'Y', 'Peninsula', 10);
insert into teams (school, mascot, class, tracked, district, confID) values ('Kecoughtan', 'xx', 5, 'Y', 'Peninsula', 10);
insert into teams (school, mascot, class, tracked, district, confID) values ('Menchville', 'xx', 5, 'Y', 'Peninsula', 10);
insert into teams (school, mascot, class, tracked, district, confID) values ('Warwick', 'xx', 5, 'Y', 'Peninsula', 10);

insert into teams (school, mascot, class, tracked, district, confID) values ('Hickory', 'xx', 5, 'Y', 'Southeastern', 9);
insert into teams (school, mascot, class, tracked, district, confID) values ('Indian River', 'xx', 5, 'Y', 'Southeastern', 9);
insert into teams (school, mascot, class, tracked, district, confID) values ('Nansemond River', 'xx', 5, 'Y', 'Southeastern', 10);

insert into teams (school, mascot, class, tracked) values ('Hillside (NC)', 'xx', 5, 'N');
insert into teams (school, mascot, class, tracked) values ('Okeechobee (Fl)', 'xx', 5, 'N');
insert into teams (school, mascot, class, tracked) values ('Vance (NC)', 'xx', 5, 'N');
insert into teams (school, mascot, class, tracked) values ('Woodrow Wilson (DC)', 'xx', 5, 'N');

insert into teams (school, mascot, class, tracked, district, confID) values ('Caroline', 'Cavaliers', 4, 'Y', 'Battlefield', 19);
insert into teams (school, mascot, class, tracked, district, confID) values ('Chancellor', 'Chargers', 4, 'Y', 'Battlefield', 19);
insert into teams (school, mascot, class, tracked, district, confID) values ('Courtland', 'Cougars', 4, 'Y', 'Battlefield', 19);
insert into teams (school, mascot, class, tracked, district, confID) values ('King George', 'Foxes', 4, 'Y', 'Battlefield', 19);

insert into teams (school, mascot, class, tracked, district, confID) values ('Grafton', 'xx', 4, 'Y', 'Bay Rivers', 18);
insert into teams (school, mascot, class, tracked, district, confID) values ('Jamestown', 'xx', 4, 'Y', 'Bay Rivers', 18);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lafayette', 'xx', 4, 'Y', 'Bay Rivers', 18);
insert into teams (school, mascot, class, tracked, district, confID) values ('Smithfield', 'xx', 4, 'Y', 'Bay Rivers', 18);

insert into teams (school, mascot, class, tracked, district, confID) values ('Hanover', 'xx', 4, 'Y', 'Capital', 20);

insert into teams (school, mascot, class, tracked, district, confID) values ('Dinwiddie', 'xx', 4, 'Y', 'Central', 20);

insert into teams (school, mascot, class, tracked, district, confID) values ('Huguenot', 'xx', 4, 'Y', 'Dominion', 20);
insert into teams (school, mascot, class, tracked, district, confID) values ('Midlothian', 'xx', 4, 'Y', 'Dominion', 20);
insert into teams (school, mascot, class, tracked, district, confID) values ('Monacan', 'xx', 4, 'Y', 'Dominion', 20);

insert into teams (school, mascot, class, tracked, district, confID) values ('Churchland', 'xx', 4, 'Y', 'Eastern', 17);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lake Taylor', 'xx', 4, 'Y', 'Eastern', 17);
insert into teams (school, mascot, class, tracked, district, confID) values ('Woodrow Wilson', 'xx', 4, 'Y', 'Eastern', 17);

insert into teams (school, mascot, class, tracked, district, confID) values ('Eastern View', 'Cyclones', 4, 'Y', 'Evergreen', 19);

insert into teams (school, mascot, class, tracked, district, confID) values ('Louisa', 'Lions', 4, 'Y', 'Jefferson', 19);
insert into teams (school, mascot, class, tracked, district, confID) values ('Powhatan', 'Indians', 4, 'Y', 'Jefferson', 20);

insert into teams (school, mascot, class, tracked, district, confID) values ('Denbigh', 'xx', 4, 'Y', 'Peninsula', 18);
insert into teams (school, mascot, class, tracked, district, confID) values ('Heritage (NN)', 'xx', 4, 'Y', 'Peninsula', 18);

insert into teams (school, mascot, class, tracked, district, confID) values ('Deep Creek', 'xx', 4, 'Y', 'Southeastern', 17);
insert into teams (school, mascot, class, tracked, district, confID) values ('Great Bridge', 'xx', 4, 'Y', 'Southeastern', 17);
insert into teams (school, mascot, class, tracked, district, confID) values ('Kings Fork', 'xx', 4, 'Y', 'Southeastern', 17);

insert into teams (school, mascot, class, tracked, district, confID) values ('William Byrd', 'xx', 4, 'Y', 'Blue Ridge', 24);
insert into teams (school, mascot, class, tracked, district, confID) values ('William Fleming', 'xx', 4, 'Y', 'Blue Ridge', 24);

insert into teams (school, mascot, class, tracked, district, confID) values ('John Champe', 'xx', 4, 'Y', 'Dulles', 22);
insert into teams (school, mascot, class, tracked, district, confID) values ('Dominion', 'xx', 4, 'Y', 'Dulles', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Freedom (LC)', 'xx', 4, 'Y', 'Dulles', 22);
insert into teams (school, mascot, class, tracked, district, confID) values ('Heritage (LC)', 'xx', 4, 'Y', 'Dulles', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Loudoun Co.', 'xx', 4, 'Y', 'Dulles', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Loudoun Valley', 'xx', 4, 'Y', 'Dulles', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Park View (St)', 'xx', 4, 'Y', 'Dulles', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Rock Ridge', 'xx', 4, 'Y', 'Dulles', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Woodgrove', 'xx', 4, 'Y', 'Dulles', 21);

insert into teams (school, mascot, class, tracked, district, confID) values ('Fauquier', 'Falcons', 4, 'Y', 'Evergreen', 22);
insert into teams (school, mascot, class, tracked, district, confID) values ('Kettle Run', 'xx', 4, 'Y', 'Evergreen', 22);
insert into teams (school, mascot, class, tracked, district, confID) values ('Liberty (Beal)', 'Eagles', 4, 'Y', 'Evergreen', 22);

insert into teams (school, mascot, class, tracked, district, confID) values ('Charlottesville', 'Black Knights', 4, 'Y', 'Jefferson', 23);

insert into teams (school, mascot, class, tracked, district, confID) values ('Handley', 'xx', 4, 'Y', 'Northwestern', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Millbrook', 'xx', 4, 'Y', 'Northwestern', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('Sherando', 'xx', 4, 'Y', 'Northwestern', 21);
insert into teams (school, mascot, class, tracked, district, confID) values ('James Wood', 'xx', 4, 'Y', 'Northwestern', 21);

insert into teams (school, mascot, class, tracked, district, confID) values ('Bassett', 'xx', 4, 'Y', 'Piedmont', 24);
insert into teams (school, mascot, class, tracked, district, confID) values ('George Washington', 'xx', 4, 'Y', 'Piedmont', 23);

insert into teams (school, mascot, class, tracked, district, confID) values ('Pulaski Co.', 'xx', 4, 'Y', 'River Ridge', 24);
insert into teams (school, mascot, class, tracked, district, confID) values ('Salem (Sa)', 'xx', 4, 'Y', 'River Ridge', 24);
insert into teams (school, mascot, class, tracked, district, confID) values ('Carroll Co.', 'xx', 4, 'Y', 'River Ridge', 24);

insert into teams (school, mascot, class, tracked, district, confID) values ('Amherst Co.', 'xx', 4, 'Y', 'Seminole', 23);
insert into teams (school, mascot, class, tracked, district, confID) values ('E.C. Glass', 'xx', 4, 'Y', 'Seminole', 23);
insert into teams (school, mascot, class, tracked, district, confID) values ('Jefferson Forest', 'xx', 4, 'Y', 'Seminole', 23);
insert into teams (school, mascot, class, tracked, district, confID) values ('Liberty Christian', 'xx', 4, 'Y', 'Seminole', 23);

insert into teams (school, mascot, class, tracked, district, confID) values ('Harrisonburg', 'xx', 4, 'Y', 'Valley', 21);

insert into teams (school, mascot, class, tracked) values ('J.M. Bennett (MD)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Bishop McNamara', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('David Crockett (TN)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Hedgesville (WV)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Jefferson Co. (WV)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Martinsburg (WV)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Person (NC)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Tennessee (TN)', 'xx', 4, 'N');
insert into teams (school, mascot, class, tracked) values ('Washington (WV)', 'xx', 4, 'N');

insert into teams (school, mascot, class, tracked, district, confID) values ('James Monroe', 'Yellow Jackets', 3, 'Y', 'Battlefield', 28);
insert into teams (school, mascot, class, tracked, district, confID) values ('Spotsylvania', 'Knights', 3, 'Y', 'Battlefield', 26);

insert into teams (school, mascot, class, tracked, district, confID) values ('New Kent', 'xx', 3, 'Y', 'Bay Rivers', 25);
insert into teams (school, mascot, class, tracked, district, confID) values ('Poquoson', 'xx', 3, 'Y', 'Bay Rivers', 25);
insert into teams (school, mascot, class, tracked, district, confID) values ('Tabb', 'xx', 3, 'Y', 'Bay Rivers', 27);
insert into teams (school, mascot, class, tracked, district, confID) values ('Warhill', 'xx', 3, 'Y', 'Bay Rivers', 25);
insert into teams (school, mascot, class, tracked, district, confID) values ('York', 'xx', 3, 'Y', 'Bay Rivers', 27);

insert into teams (school, mascot, class, tracked, district, confID) values ('William Monroe', 'xx', 3, 'Y', 'Bull Run', 28);
insert into teams (school, mascot, class, tracked, district, confID) values ('Warren Co.', 'xx', 3, 'Y', 'Bull Run', 28);

insert into teams (school, mascot, class, tracked, district, confID) values ('Armstrong', 'xx', 3, 'Y', 'Capital', 26);

insert into teams (school, mascot, class, tracked, district, confID) values ('Hopewell', 'xx', 3, 'Y', 'Central', 26);
insert into teams (school, mascot, class, tracked, district, confID) values ('Petersburg', 'xx', 3, 'Y', 'Central', 26);

insert into teams (school, mascot, class, tracked, district, confID) values ('T. Jefferson (Ri)', 'xx', 3, 'Y', 'Colonial', 26);
insert into teams (school, mascot, class, tracked, district, confID) values ('John Marshall', 'xx', 3, 'Y', 'Colonial', 26);

insert into teams (school, mascot, class, tracked, district, confID) values ('George Wythe (Ri)', 'xx', 3, 'Y', 'Dominion', 26);

insert into teams (school, mascot, class, tracked, district, confID) values ('Riverside', 'xx', 3, 'Y', 'Dulles', 28);

insert into teams (school, mascot, class, tracked, district, confID) values ('I.C. Norcom', 'xx', 3, 'Y', 'Eastern', 27);
insert into teams (school, mascot, class, tracked, district, confID) values ('B.T. Washington', 'xx', 3, 'Y', 'Eastern', 27);

insert into teams (school, mascot, class, tracked, district, confID) values ('Brentsville', 'xx', 3, 'Y', 'Evergreen', 28);
insert into teams (school, mascot, class, tracked, district, confID) values ('Culpeper', 'Blue Devils', 3, 'Y', 'Evergreen', 28);
insert into teams (school, mascot, class, tracked, district, confID) values ('Manassas Park', 'xx', 3, 'Y', 'Evergreen', 28);

insert into teams (school, mascot, class, tracked, district, confID) values ('Skyline', 'xx', 3, 'Y', 'Northwestern', 28);

insert into teams (school, mascot, class, tracked, district, confID) values ('Phoebus', 'xx', 3, 'Y', 'Peninsula', 27);

insert into teams (school, mascot, class, tracked, district, confID) values ('Lakeland', 'xx', 3, 'Y', 'Southeastern', 27);

insert into teams (school, mascot, class, tracked, district, confID) values ('Park View (SH)', 'xx', 3, 'Y', 'Tri-Rivers', 25);
insert into teams (school, mascot, class, tracked, district, confID) values ('Southampton', 'xx', 3, 'Y', 'Tri-Rivers', 25);

insert into teams (school, mascot, class, tracked, district, confID) values ('Alleghany', 'xx', 3, 'Y', 'Blue Ridge', 31);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lord Botetourt', 'xx', 3, 'Y', 'Blue Ridge', 31);
insert into teams (school, mascot, class, tracked, district, confID) values ('Northside', 'xx', 3, 'Y', 'Blue Ridge', 31);
insert into teams (school, mascot, class, tracked, district, confID) values ('Rockbridge Co.', 'xx', 3, 'Y', 'Blue Ridge', 31);
insert into teams (school, mascot, class, tracked, district, confID) values ('Staunton River', 'xx', 3, 'Y', 'Blue Ridge', 31);

insert into teams (school, mascot, class, tracked, district, confID) values ('Fluvanna', 'Flucos', 3, 'Y', 'Jefferson', 29);
insert into teams (school, mascot, class, tracked, district, confID) values ('Monticello', 'xx', 3, 'Y', 'Jefferson', 29);
insert into teams (school, mascot, class, tracked, district, confID) values ('Western Albemarle', 'xx', 3, 'Y', 'Jefferson', 29);

insert into teams (school, mascot, class, tracked, district, confID) values ('Patrick Co.', 'xx', 3, 'Y', 'Piedmont', 32);
insert into teams (school, mascot, class, tracked, district, confID) values ('Tunstall', 'xx', 3, 'Y', 'Piedmont', 30);
insert into teams (school, mascot, class, tracked, district, confID) values ('Magna Vista', 'xx', 3, 'Y', 'Piedmont', 31);

insert into teams (school, mascot, class, tracked, district, confID) values ('Blacksburg', 'xx', 3, 'Y', 'River Ridge', 32);
insert into teams (school, mascot, class, tracked, district, confID) values ('Cave Spring', 'xx', 3, 'Y', 'River Ridge', 32);
insert into teams (school, mascot, class, tracked, district, confID) values ('Christiansburg', 'xx', 3, 'Y', 'River Ridge', 32);
insert into teams (school, mascot, class, tracked, district, confID) values ('Hidden Valley', 'xx', 3, 'Y', 'River Ridge', 32);

insert into teams (school, mascot, class, tracked, district, confID) values ('Brookville', 'xx', 3, 'Y', 'Seminole', 30);
insert into teams (school, mascot, class, tracked, district, confID) values ('Heritage (Ly)', 'xx', 3, 'Y', 'Seminole', 30);
insert into teams (school, mascot, class, tracked, district, confID) values ('Liberty (Bed)', 'xx', 3, 'Y', 'Seminole', 30);
insert into teams (school, mascot, class, tracked, district, confID) values ('Rustburg', 'xx', 3, 'Y', 'Seminole', 30);

insert into teams (school, mascot, class, tracked, district, confID) values ('Abingdon', 'xx', 3, 'Y', 'Southwest', 32);

insert into teams (school, mascot, class, tracked, district, confID) values ('Broadway', 'xx', 3, 'Y', 'Valley', 29);
insert into teams (school, mascot, class, tracked, district, confID) values ('Fort Defiance', 'xx', 3, 'Y', 'Valley', 29);
insert into teams (school, mascot, class, tracked, district, confID) values ('Spotswood', 'xx', 3, 'Y', 'Valley', 29);
insert into teams (school, mascot, class, tracked, district, confID) values ('Turner Ashby', 'xx', 3, 'Y', 'Valley', 29);
insert into teams (school, mascot, class, tracked, district, confID) values ('Waynesboro', 'xx', 3, 'Y', 'Valley', 29);


insert into teams (school, mascot, class, tracked) values ('Bartlett Yancey (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Cambridge/S.Dorchester (MD)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Cocoa (Fl)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Currituck (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Eastern (DC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('First Flight (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Letcher Co. (KY)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('McMichael (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Morehead (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Northeastern (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Potomac (MD)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Roanoke Rapids (NC)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Spring Mills (WV)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Sullivan South (TN)', 'xx', 3, 'N');
insert into teams (school, mascot, class, tracked) values ('Woodberry Forest', 'xx', 3, 'N');

insert into teams (school, mascot, class, tracked, district, confID) values ('Bruton', 'xx', 2, 'Y', 'Bay Rivers', 33);

insert into teams (school, mascot, class, tracked, district, confID) values ('Central (Wo)', 'xx', 2, 'Y', 'Bull Run', 35);
insert into teams (school, mascot, class, tracked, district, confID) values ('Clarke Co.', 'xx', 2, 'Y', 'Bull Run', 35);
insert into teams (school, mascot, class, tracked, district, confID) values ('Madison Co.', 'xx', 2, 'Y', 'Bull Run', 35);
insert into teams (school, mascot, class, tracked, district, confID) values ('George Mason', 'xx', 2, 'Y', 'Bull Run', 35);
insert into teams (school, mascot, class, tracked, district, confID) values ('Strasburg', 'xx', 2, 'Y', 'Bull Run', 35);

insert into teams (school, mascot, class, tracked, district, confID) values ('Nelson Co.', 'xx', 2, 'Y', 'Dogwood', 36);

insert into teams (school, mascot, class, tracked, district, confID) values ('Arcadia', 'xx', 2, 'Y', 'Eastern Shore', 33);
insert into teams (school, mascot, class, tracked, district, confID) values ('Nandua', 'xx', 2, 'Y', 'Eastern Shore', 33);

insert into teams (school, mascot, class, tracked, district, confID) values ('Amelia Co.', 'xx', 2, 'Y', 'James River', 34);
insert into teams (school, mascot, class, tracked, district, confID) values ('Bluestone', 'xx', 2, 'Y', 'James River', 34);
insert into teams (school, mascot, class, tracked, district, confID) values ('Goochland', 'xx', 2, 'Y', 'James River', 34);
insert into teams (school, mascot, class, tracked, district, confID) values ('Nottoway', 'xx', 2, 'Y', 'James River', 34);
insert into teams (school, mascot, class, tracked, district, confID) values ('Prince Edward', 'xx', 2, 'Y', 'James River', 34);

insert into teams (school, mascot, class, tracked, district, confID) values ('Washington & Lee', 'xx', 2, 'Y', 'Northern Neck', 33);

insert into teams (school, mascot, class, tracked, district, confID) values ('Buffalo Gap', 'xx', 2, 'Y', 'Shenandoah', 36);
insert into teams (school, mascot, class, tracked, district, confID) values ('East Rockingham', 'xx', 2, 'Y', 'Shenandoah', 36);
insert into teams (school, mascot, class, tracked, district, confID) values ('Page Co.', 'xx', 2, 'Y', 'Shenandoah', 36);
insert into teams (school, mascot, class, tracked, district, confID) values ('Stuarts Draft', 'xx', 2, 'Y', 'Shenandoah', 36);
insert into teams (school, mascot, class, tracked, district, confID) values ('Wilson Memorial', 'xx', 2, 'Y', 'Shenandoah', 36);

insert into teams (school, mascot, class, tracked, district, confID) values ('King William', 'xx', 2, 'Y', 'Tidewater', 33);

insert into teams (school, mascot, class, tracked, district, confID) values ('Brunswick', 'xx', 2, 'Y', 'Tri-Rivers', 34);
insert into teams (school, mascot, class, tracked, district, confID) values ('Greensville', 'xx', 2, 'Y', 'Tri-Rivers', 34);

insert into teams (school, mascot, class, tracked, district, confID) values ('R.E. Lee (St)', 'xx', 2, 'Y', 'Valley', 36);

insert into teams (school, mascot, class, tracked, district, confID) values ('Grundy', 'xx', 2, 'Y', 'Black Diamond', 39);

insert into teams (school, mascot, class, tracked, district, confID) values ('Appomattox', 'xx', 2, 'Y', 'Dogwood', 37);
insert into teams (school, mascot, class, tracked, district, confID) values ('Chatham', 'xx', 2, 'Y', 'Dogwood', 37);
insert into teams (school, mascot, class, tracked, district, confID) values ('Dan River', 'xx', 2, 'Y', 'Dogwood', 37);
insert into teams (school, mascot, class, tracked, district, confID) values ('Gretna', 'xx', 2, 'Y', 'Dogwood', 37);

insert into teams (school, mascot, class, tracked, district, confID) values ('Marion', 'xx', 2, 'Y', 'Hogoheegee', 39);

insert into teams (school, mascot, class, tracked, district, confID) values ('Buckingham Co.', 'xx', 2, 'Y', 'James River', 37);
insert into teams (school, mascot, class, tracked, district, confID) values ('Randolph-Henry', 'xx', 2, 'Y', 'James River', 37);

insert into teams (school, mascot, class, tracked, district, confID) values ('John Battle', 'xx', 2, 'Y', 'Mountain', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Central-Wise', 'xx', 2, 'Y', 'Mountain', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Gate City', 'xx', 2, 'Y', 'Mountain', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lee', 'xx', 2, 'Y', 'Mountain', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Ridgeview', 'xx', 2, 'Y', 'Mountain', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Union', 'xx', 2, 'Y', 'Mountain', 40);

insert into teams (school, mascot, class, tracked, district, confID) values ('Graham', 'xx', 2, 'Y', 'Mountain Empire', 39);
insert into teams (school, mascot, class, tracked, district, confID) values ('Grayson Co.', 'xx', 2, 'Y', 'Mountain Empire', 39);

insert into teams (school, mascot, class, tracked, district, confID) values ('Martinsville', 'xx', 2, 'Y', 'Piedmont', 38);
insert into teams (school, mascot, class, tracked, district, confID) values ('James River (Bu)', 'xx', 2, 'Y', 'Pioneer', 38);

insert into teams (school, mascot, class, tracked, district, confID) values ('Lebanon', 'xx', 2, 'Y', 'Southwest', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Richlands', 'xx', 2, 'Y', 'Southwest', 39);
insert into teams (school, mascot, class, tracked, district, confID) values ('Tazewell', 'xx', 2, 'Y', 'Southwest', 39);
insert into teams (school, mascot, class, tracked, district, confID) values ('Virginia', 'xx', 2, 'Y', 'Southwest', 39);

insert into teams (school, mascot, class, tracked, district, confID) values ('Gate City', 'xx', 2, 'Y', 'Three Rivers', 40);
insert into teams (school, mascot, class, tracked, district, confID) values ('Giles', 'xx', 2, 'Y', 'Three Rivers', 38);
insert into teams (school, mascot, class, tracked, district, confID) values ('Glenvar', 'xx', 2, 'Y', 'Three Rivers', 38);

insert into teams (school, mascot, class, tracked) values ('Bluefield (WV)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('East Ridge (KY)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Fort Hill (MD)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Holmes (NC)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Kent (MD)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('McCreary Central (KY)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('River View (WV)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Shelby Valley (KY)', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Benedictine', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Fork Union', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('Saint John Paul', 'xx', 2, 'N');
insert into teams (school, mascot, class, tracked) values ('St. Christophers', 'xx', 2, 'N');

insert into teams (school, mascot, class, tracked) values ('Rappahannock Co.', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Chincoteague', 'xx', 1, 'N');

insert into teams (school, mascot, class, tracked, district, confID) values ('Altavista', 'xx', 1, 'Y', 'Dogwood', 44);
insert into teams (school, mascot, class, tracked, district, confID) values ('William Campbell', 'xx', 1, 'Y', 'Dogwood', 44);

insert into teams (school, mascot, class, tracked, district, confID) values ('Northampton', 'xx', 1, 'Y', 'Eastern Shore', 43);

insert into teams (school, mascot, class, tracked, district, confID) values ('Central (Lun)', 'xx', 1, 'Y', 'James River', 42);
insert into teams (school, mascot, class, tracked, district, confID) values ('Cumberland', 'xx', 1, 'Y', 'James River', 42);

insert into teams (school, mascot, class, tracked, district, confID) values ('Coloinal Beach', 'xx', 1, 'Y', 'Northern Neck', 43);
insert into teams (school, mascot, class, tracked, district, confID) values ('Essex', 'xx', 1, 'Y', 'Northern Neck', 43);
insert into teams (school, mascot, class, tracked, district, confID) values ('Lancaster', 'xx', 1, 'Y', 'Northern Neck', 43);
insert into teams (school, mascot, class, tracked, district, confID) values ('Northumberland', 'xx', 1, 'Y', 'Northern Neck', 43);
insert into teams (school, mascot, class, tracked, district, confID) values ('Rappahnannock', 'xx', 1, 'Y', 'Northern Neck', 43);

insert into teams (school, mascot, class, tracked, district, confID) values ('Stonewall Jackson (Qui)', 'xx', 1, 'Y', 'Shenandoah', 44);
insert into teams (school, mascot, class, tracked, district, confID) values ('Luray', 'xx', 1, 'Y', 'Shenandoah', 44);

insert into teams (school, mascot, class, tracked, district, confID) values ('Charles City', 'xx', 1, 'Y', 'Tidewater', 42);
insert into teams (school, mascot, class, tracked, district, confID) values ('King & Queen', 'xx', 1, 'Y', 'Tidewater', 42);
insert into teams (school, mascot, class, tracked, district, confID) values ('Mathews', 'xx', 1, 'Y', 'Tidewater', 42);
insert into teams (school, mascot, class, tracked, district, confID) values ('Middlesex', 'xx', 1, 'Y', 'Tidewater', 42);
insert into teams (school, mascot, class, tracked, district, confID) values ('West Point', 'Pointers', 1, 'Y', 'Tidewater', 42);

insert into teams (school, mascot, class, tracked, district, confID) values ('Franklin', 'xx', 1, 'Y', 'Tri-Rivers', 41);
insert into teams (school, mascot, class, tracked, district, confID) values ('Surry', 'xx', 1, 'Y', 'Tri-Rivers', 41);
insert into teams (school, mascot, class, tracked, district, confID) values ('Sussex', 'xx', 1, 'Y', 'Tri-Rivers', 41);
insert into teams (school, mascot, class, tracked, district, confID) values ('Windsor', 'xx', 1, 'Y', 'Tri-Rivers', 41);

insert into teams (school, mascot, class, tracked, district, confID) values ('Honaker', 'xx', 1, 'Y', 'Black Diamond', 47);
insert into teams (school, mascot, class, tracked, district, confID) values ('Hurley', 'xx', 1, 'Y', 'Black Diamond', 47);
insert into teams (school, mascot, class, tracked, district, confID) values ('Twin Valley', 'xx', 1, 'Y', 'Black Diamond', 47);

insert into teams (school, mascot, class, tracked, district, confID) values ('J.I. Burton', 'xx', 1, 'Y', 'Cumberland', 48);
insert into teams (school, mascot, class, tracked, district, confID) values ('Castlewood', 'xx', 1, 'Y', 'Cumberland', 48);
insert into teams (school, mascot, class, tracked, district, confID) values ('Eastside', 'xx', 1, 'Y', 'Cumberland', 48);
insert into teams (school, mascot, class, tracked, district, confID) values ('Rye Cove', 'xx', 1, 'Y', 'Cumberland', 48);
insert into teams (school, mascot, class, tracked, district, confID) values ('Twin Springs', 'xx', 1, 'Y', 'Cumberland', 48);
insert into teams (school, mascot, class, tracked, district, confID) values ('Thomas Walker', 'xx', 1, 'Y', 'Cumberland', 48);

insert into teams (school, mascot, class, tracked, district, confID) values ('Chilhowie', 'xx', 1, 'Y', 'Hogoheegee', 46);
insert into teams (school, mascot, class, tracked, district, confID) values ('Patrick Henry (GS', 'xx', 1, 'Y', 'Hogoheegee', 47);
insert into teams (school, mascot, class, tracked, district, confID) values ('Holston', 'xx', 1, 'Y', 'Hogoheegee', 47);
insert into teams (school, mascot, class, tracked, district, confID) values ('Northwood', 'xx', 1, 'Y', 'Hogoheegee', 47);
insert into teams (school, mascot, class, tracked, district, confID) values ('Rural Retreat', 'xx', 1, 'Y', 'Hogoheegee', 46);
insert into teams (school, mascot, class, tracked, district, confID) values ('George Wythe (Wy)', 'xx', 1, 'Y', 'Hogoheegee', 46);

insert into teams (school, mascot, class, tracked, district, confID) values ('Bland Co.', 'xx', 1, 'Y', 'Mountain Empire', 46);
insert into teams (school, mascot, class, tracked, district, confID) values ('Fort Chiswell', 'xx', 1, 'Y', 'Mountain Empire', 46);
insert into teams (school, mascot, class, tracked, district, confID) values ('Galax', 'xx', 1, 'Y', 'Mountain Empire', 46);
insert into teams (school, mascot, class, tracked, district, confID) values ('Narrows', 'xx', 1, 'Y', 'Mountain Empire', 45);

insert into teams (school, mascot, class, tracked, district, confID) values ('Bath Co.', 'xx', 1, 'Y', 'Pioneer', 45);
insert into teams (school, mascot, class, tracked, district, confID) values ('Covington', 'xx', 1, 'Y', 'Pioneer', 45);
insert into teams (school, mascot, class, tracked, district, confID) values ('Craig Co.', 'xx', 1, 'Y', 'Pioneer', 45);
insert into teams (school, mascot, class, tracked, district, confID) values ('Parry McCluer', 'xx', 1, 'Y', 'Pioneer', 45);

insert into teams (school, mascot, class, tracked, district, confID) values ('Auburn', 'xx', 1, 'Y', 'Three Rivers', 45);
insert into teams (school, mascot, class, tracked, district, confID) values ('Eastern Montgomery', 'xx', 1, 'Y', 'Three Rivers', 45);
insert into teams (school, mascot, class, tracked, district, confID) values ('Radford', 'xx', 1, 'Y', 'Three Rivers', 45);


insert into teams (school, mascot, class, tracked) values ('Alleghany (NC)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Avalon (MD)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Col. Richardson', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('East Hardy (WV)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Greenbrier West (WV)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Hancock Co. (TN)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Harlan Independent (KY)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Jenkins (KY)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Montcalm (WV)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('North Stokes (NC)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Paintsville (KY)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Pendleton Co. (WV)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Phelps (KY)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Pocahontas (WV)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Snow Hill (MD)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('South Floyd (KY)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Unaka (TN)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Van (WV)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Weldon (NC)', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Broadwater Acad.', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Charlotte Christian', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Grace Christian', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Greenbriar Acad.', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Kenston Forest', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Portsmouth Christian', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Quantico', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Roanoke Catholic', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Trinity Episcopal', 'xx', 1, 'N');
insert into teams (school, mascot, class, tracked) values ('Word of God', 'xx', 1, 'N');
