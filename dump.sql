BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY SERIAL, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2024-04-23 05:06:17.361961');
INSERT INTO django_migrations VALUES(2,'contenttypes','0002_remove_content_type_name','2024-04-23 05:06:17.385883');
INSERT INTO django_migrations VALUES(3,'auth','0001_initial','2024-04-23 05:06:17.406386');
INSERT INTO django_migrations VALUES(4,'auth','0002_alter_permission_name_max_length','2024-04-23 05:06:17.420498');
INSERT INTO django_migrations VALUES(5,'auth','0003_alter_user_email_max_length','2024-04-23 05:06:17.429522');
INSERT INTO django_migrations VALUES(6,'auth','0004_alter_user_username_opts','2024-04-23 05:06:17.439810');
INSERT INTO django_migrations VALUES(7,'auth','0005_alter_user_last_login_null','2024-04-23 05:06:17.450850');
INSERT INTO django_migrations VALUES(8,'auth','0006_require_contenttypes_0002','2024-04-23 05:06:17.456598');
INSERT INTO django_migrations VALUES(9,'auth','0007_alter_validators_add_error_messages','2024-04-23 05:06:17.482062');
INSERT INTO django_migrations VALUES(10,'auth','0008_alter_user_username_max_length','2024-04-23 05:06:17.492399');
INSERT INTO django_migrations VALUES(11,'auth','0009_alter_user_last_name_max_length','2024-04-23 05:06:17.503374');
INSERT INTO django_migrations VALUES(12,'auth','0010_alter_group_name_max_length','2024-04-23 05:06:17.512138');
INSERT INTO django_migrations VALUES(13,'auth','0011_update_proxy_permissions','2024-04-23 05:06:17.520179');
INSERT INTO django_migrations VALUES(14,'auth','0012_alter_user_first_name_max_length','2024-04-23 05:06:17.530119');
INSERT INTO django_migrations VALUES(15,'accounts','0001_initial','2024-04-23 05:06:17.547833');
INSERT INTO django_migrations VALUES(16,'admin','0001_initial','2024-04-23 05:06:17.564686');
INSERT INTO django_migrations VALUES(17,'admin','0002_logentry_remove_auto_add','2024-04-23 05:06:17.577559');
INSERT INTO django_migrations VALUES(18,'admin','0003_logentry_add_action_flag_choices','2024-04-23 05:06:17.589780');
INSERT INTO django_migrations VALUES(19,'sessions','0001_initial','2024-04-23 05:06:17.606403');
INSERT INTO django_migrations VALUES(20,'store','0001_initial','2024-04-23 05:06:17.614709');
INSERT INTO django_migrations VALUES(21,'store','0002_offrebillet_stock','2024-04-23 05:06:17.630084');
INSERT INTO django_migrations VALUES(22,'store','0003_offrebillet_slug','2024-04-23 05:06:17.638033');
INSERT INTO django_migrations VALUES(23,'store','0004_rename_thumbnail_epreuve_illustration','2024-04-23 05:06:17.646997');
INSERT INTO django_migrations VALUES(24,'store','0005_epreuve_slug','2024-04-23 05:06:17.655552');
INSERT INTO django_migrations VALUES(25,'store','0006_order','2024-04-25 04:28:09.875413');
INSERT INTO django_migrations VALUES(26,'store','0007_rename_order_achat','2024-04-25 04:47:31.914364');
INSERT INTO django_migrations VALUES(27,'store','0008_rename_ordered_achat_acheté_and_more','2024-04-25 04:59:09.378767');
INSERT INTO django_migrations VALUES(28,'store','0009_rename_produit_achat_billet','2024-04-29 17:32:20.029435');
INSERT INTO django_migrations VALUES(29,'store','0010_offrebillet_epreuve','2024-04-29 19:59:00.170044');
INSERT INTO django_migrations VALUES(30,'store','0011_achat_epreuve_alter_offrebillet_nom','2024-04-30 15:24:37.409439');
INSERT INTO django_migrations VALUES(31,'store','0012_alter_panier_utilisateur','2024-05-01 13:35:22.387175');
INSERT INTO django_migrations VALUES(32,'store','0013_remove_panier_achats_achat_panier','2024-05-02 19:42:31.746127');
INSERT INTO django_migrations VALUES(33,'store','0014_epreuve_type','2024-05-05 12:35:15.771981');
INSERT INTO django_migrations VALUES(34,'store','0015_epreuve_mention','2024-05-05 12:41:31.533924');
INSERT INTO django_migrations VALUES(35,'store','0016_transaction','2024-05-06 14:12:30.435235');
INSERT INTO django_migrations VALUES(36,'accounts','0002_customuser_nom_customuser_prenom','2024-05-06 19:12:38.340993');
INSERT INTO django_migrations VALUES(37,'store','0017_ticket','2024-05-07 19:47:20.725787');
INSERT INTO django_migrations VALUES(38,'accounts','0003_rename_nom_customuser_nom_and_more','2024-05-17 14:25:59.123552');
INSERT INTO django_migrations VALUES(39,'accounts','0004_rename_nom_customuser_nom_and_more','2024-05-17 14:27:11.046867');
INSERT INTO django_migrations VALUES(40,'accounts','0005_alter_customuser_nom_alter_customuser_prenom','2024-05-17 14:28:08.885376');
INSERT INTO django_migrations VALUES(41,'store','0018_alter_achat_panier','2024-05-20 18:39:40.394405');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY SERIAL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(5,'sessions','session');
INSERT INTO django_content_type VALUES(6,'store','epreuve');
INSERT INTO django_content_type VALUES(7,'store','offrebillet');
INSERT INTO django_content_type VALUES(8,'accounts','customuser');
INSERT INTO django_content_type VALUES(9,'store','achat');
INSERT INTO django_content_type VALUES(10,'store','panier');
INSERT INTO django_content_type VALUES(11,'store','transaction');
INSERT INTO django_content_type VALUES(12,'store','ticket');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY SERIAL, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY SERIAL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(17,5,'add_session','Can add session');
INSERT INTO auth_permission VALUES(18,5,'change_session','Can change session');
INSERT INTO auth_permission VALUES(19,5,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(20,5,'view_session','Can view session');
INSERT INTO auth_permission VALUES(21,6,'add_epreuve','Can add epreuve');
INSERT INTO auth_permission VALUES(22,6,'change_epreuve','Can change epreuve');
INSERT INTO auth_permission VALUES(23,6,'delete_epreuve','Can delete epreuve');
INSERT INTO auth_permission VALUES(24,6,'view_epreuve','Can view epreuve');
INSERT INTO auth_permission VALUES(25,7,'add_offrebillet','Can add offre billet');
INSERT INTO auth_permission VALUES(26,7,'change_offrebillet','Can change offre billet');
INSERT INTO auth_permission VALUES(27,7,'delete_offrebillet','Can delete offre billet');
INSERT INTO auth_permission VALUES(28,7,'view_offrebillet','Can view offre billet');
INSERT INTO auth_permission VALUES(29,8,'add_customuser','Can add user');
INSERT INTO auth_permission VALUES(30,8,'change_customuser','Can change user');
INSERT INTO auth_permission VALUES(31,8,'delete_customuser','Can delete user');
INSERT INTO auth_permission VALUES(32,8,'view_customuser','Can view user');
INSERT INTO auth_permission VALUES(33,9,'add_order','Can add order');
INSERT INTO auth_permission VALUES(34,9,'change_order','Can change order');
INSERT INTO auth_permission VALUES(35,9,'delete_order','Can delete order');
INSERT INTO auth_permission VALUES(36,9,'view_order','Can view order');
INSERT INTO auth_permission VALUES(37,9,'add_achat','Can add achat');
INSERT INTO auth_permission VALUES(38,9,'change_achat','Can change achat');
INSERT INTO auth_permission VALUES(39,9,'delete_achat','Can delete achat');
INSERT INTO auth_permission VALUES(40,9,'view_achat','Can view achat');
INSERT INTO auth_permission VALUES(41,10,'add_panier','Can add panier');
INSERT INTO auth_permission VALUES(42,10,'change_panier','Can change panier');
INSERT INTO auth_permission VALUES(43,10,'delete_panier','Can delete panier');
INSERT INTO auth_permission VALUES(44,10,'view_panier','Can view panier');
INSERT INTO auth_permission VALUES(45,11,'add_transaction','Can add transaction');
INSERT INTO auth_permission VALUES(46,11,'change_transaction','Can change transaction');
INSERT INTO auth_permission VALUES(47,11,'delete_transaction','Can delete transaction');
INSERT INTO auth_permission VALUES(48,11,'view_transaction','Can view transaction');
INSERT INTO auth_permission VALUES(49,12,'add_ticket','Can add ticket');
INSERT INTO auth_permission VALUES(50,12,'change_ticket','Can change ticket');
INSERT INTO auth_permission VALUES(51,12,'delete_ticket','Can delete ticket');
INSERT INTO auth_permission VALUES(52,12,'view_ticket','Can view ticket');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY SERIAL, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "accounts_customuser_groups" ("id" integer NOT NULL PRIMARY KEY SERIAL, "customuser_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "accounts_customuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY SERIAL, "customuser_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY SERIAL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO django_admin_log VALUES(55,'11',' ',1,'[{"added": {}}]',8,10,'2024-05-17 14:22:00.080641');
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('tdiull4vchciaq82tqi1pjqccsddyn4v','e30:1s0LQD:Y8XBRZyJ5scmDz10zXn8qzfVGcecxdhAuyAsADMY9Nc','2024-05-10 13:15:25.881949');
INSERT INTO django_session VALUES('l3q8e7ogx48bfs8tx2mcpdsnm1avgwpr','.eJxVjEsSgjAQBe8ya4pKQsJv6d4TqEVlkimJYkBI3FDcXVA2bLv7vRkG7R2NTaDXAPVlBnRdR6FxFmqewDtqH1y4Rsao-hEaRoof-gfLLYFGx9A2cVpPNgYcDgy1eZLfhH1of-9T0_swOky3JN3tlJ57S91pbw8HrZ7ada2lpaySFSkriGvMMSsUw6wsBErGS5RWoUGR5aWSqpQGFTNUkFCistzksHwBgrNNkg:1s29TV:Rp5R8Adm8juNnP1iaFuoyyTprASroaiQFH3BJk-Q7bE','2024-05-15 12:54:17.869138');
INSERT INTO django_session VALUES('1x6bsi659ckpfhdoer3uke59be7pvxgc','eyJwYW5pZXJfdGVtcCI6W3siYmlsbGV0X2lkIjoxLCJxdWFudGl0XHUwMGU5Ijo0LCJlcHJldXZlX2lkIjozfV19:1s2rhL:4g1cELIjp4koMZLAUlmGhibyj6a2ks64ywBqasTrwjE','2024-05-17 12:07:31.992890');
INSERT INTO django_session VALUES('50d2k8yop4m5ez9uvl5yj8mbez4fscfv','eyJwYW5pZXJfdGVtcCI6W3siYmlsbGV0X2lkIjoyLCJxdWFudGl0XHUwMGU5IjoxLCJlcHJldXZlX2lkIjoxfV19:1s3G28:GKW1hX9IbDh2JPWSvmcfBeIuHA9nHgSIM0MvnCaDf0Q','2024-05-18 14:06:36.051298');
INSERT INTO django_session VALUES('b3jikwxou0ton5iidd4md945r7rtlv0j','.eJxVjDsOwjAQBe_iGln-rT-U9JzB8npXOIAcKU4qxN0hUgpo38y8l8hlW1veBi95InEWWpx-Nyz1wX0HdC_9Nss693WZUO6KPOiQ15n4eTncv4NWRvvWxRHb5BIDGdYFPdoACm0MBp3SER0BVjTWR3AQXUVQlQMbMIl09eL9AeDbN5o:1s3XJT:wNL5apQrq_90ycMSS4tVsLEjXCGkU4qyKFh1ymEwYlg','2024-05-19 08:33:39.446186');
INSERT INTO django_session VALUES('y1qx92ckgqxjicout5ute1mnoc9ie0b9','.eJxVjEsOwjAMRO-SNYrcpokjluw5Q2XHDimgVOpnVXF3WqkLmOW8N7OZntal9OusUz-IuRo0l9-OKb20HkCeVB-jTWNdpoHtodiTzvY-ir5vp_t3UGgu-zohZMY9TY7aITAFpsitqLjI0BIrgJecMkCI4KJKIxiQvXedEzSfL_1nODA:1s4bN6:wDp40KCtLejbLt3e5S0_qbCS20__m_Xg5LiGJVCVfBc','2024-05-22 07:05:48.226632');
CREATE TABLE IF NOT EXISTS "store_epreuve" ("id" integer NOT NULL PRIMARY KEY SERIAL, "titre" varchar(200) NOT NULL, "description" text NOT NULL, "date_epreuve" date NOT NULL, "illustration" varchar(100) NULL, "slug" varchar(128) NOT NULL, "type" varchar(128) NULL, "mention" text NULL);
INSERT INTO store_epreuve VALUES(1,'Trottinette électrique de vitesse','Accomplir le plus rapidement possible 60 tours en une seule charge avec une trottinette officielle de la ville !','2024-07-10','imgbank/trottinettes1_G4vV1Ee.webp','trottinette','Individuelle','');
INSERT INTO store_epreuve VALUES(2,'Course au Rat','Une épreuve sans merci où dix athlètes courent derrière un drone revêtu d’une peau de rat. Il est même possible de tenter de l’attraper pour obtenir un score bonus','2024-06-01','imgbank/course_BOzMtko.webp','course','Individuelle','');
INSERT INTO store_epreuve VALUES(3,'Escrime à la Montante',replace(replace('Une épreuve bien connue de tout amateur de sport, l’escrime, aujourd’hui spécialement revisitée au dernier moment avec une épée qui aura marqué les esprits, la Montante !\r\nL’épreuve se déroulera à la Bastille','\r',char(13)),'\n',char(10)),'2024-07-05','imgbank/escrime2_fy4vuRo.webp','escrime','Groupe (de deux)','');
INSERT INTO store_epreuve VALUES(4,'Arts Martiaux Mixtes Mixtes','Avènement du MMA, le Pancrace des temps modernes, directement au Panthéon ! Une sélection ardue et mixte de 10 athlètes qui combattront pour la médaille d’or.','2024-07-16','imgbank/mma_Op6dQpk.webp','mma','Équipe','');
INSERT INTO store_epreuve VALUES(5,'Saut en hauteur','Une toute nouvelle mouture de l’épreuve, directement sous l’Arc de Triomphe, se passant EXACTEMENT en même temps que l’épreuve de Saut à la perche pour accroître les frissons !','2024-07-23','imgbank/saut2_J3OsqAt.webp','saut_hauteur','Individuelle ou presque','');
INSERT INTO store_epreuve VALUES(6,'Saut à la perche','Une toute nouvelle mouture de l’épreuve, directement sous l’Arc de Triomphe, se passant EXACTEMENT en même temps que l’épreuve de Saut en hauteur pour accroître les frissons !','2024-07-23','imgbank/saut1_Ono14ri.webp','saut_perche','Individuelle ou presque','');
INSERT INTO store_epreuve VALUES(7,'Tir au pigeons de Paris',replace(replace('Déroulement de l’épreuve :\r\nUne épreuve originale en partenariat avec les services vétérinaires et les sociétés de nettoyage de la ville !\r\nUn millier de pigeons peints aux couleurs des délégations relâchés en même temps sur le Trocadéro, nos dix athlètes au centre et moins de 30 secondes pour scorer un maximum à l’aide d’un fusil à pompe modifié pour le TSV ! Notez que les compétiteurs sont TOTALEMENT novices en tir, cela promet de belles actions !\r\nPas d’inquiétudes, les services efficaces de la ville auront fait évacuer les habitants et prendront en charge d’éventuelles dégradations sans taxes supplémentaires (normalement).\r\nProtection pare-balle des visiteurs non fournie','\r',char(13)),'\n',char(10)),'2024-07-31','imgbank/tir2.webp','tir','Individuelle',replace(replace('Phases : une seule phase "Winner takes all" !\r\nMentions : cette épreuve est toute neuve, le comité attends avec beaucoup d’attention les retours des athlètes et des habitants afin de prolonger ou non la présence de cette épreuve. Tout repose sur la subjectivité du ressenti, les athlètes sont invités à se surpasser (et à viser correctement si possible).','\r',char(13)),'\n',char(10)));
INSERT INTO store_epreuve VALUES(8,'Course du saumon',replace(replace('Déroulement de l’épreuve :\r\nVivez par procuration les efforts du saumon remontant avec puissance le cours d’eau !\r\nDix à douze athlètes (volontaires) surentraînés devront remonter près d’un kilomètre de Seine et si le budget le permet, ils auront un maillot spécialement étudié pour ne pas boire la tasse et attraper ce qui se fait de mieux en terme de bouillon de culture !\r\nGageons qu’il n’y ait pas de crues impromptues, sinon l’épreuve passera de dantesque à infernale.','\r',char(13)),'\n',char(10)),'2024-06-30','imgbank/natation_3sBXpbp.webp','nage','Individuelle',replace(replace('Phases : une seule phase "Winner takes all" !\r\nMentions : il y a quatre ans, l’épreuve en bassin avait laissé un goût amer, paritcipants comme spectateurs ayant trouvé la cmoptition trop aisée. Le comité s’est donc profondément creusé la tête pour proposer une mouture relevant (de loin) le niveau.\r\n\r\nDes rumeurs courrent aujourd’hui sur l’introduction d’obstacles supplémentaires pour de prochaines éditions, telle qu’une machine à vagues artificielles.','\r',char(13)),'\n',char(10)));
CREATE TABLE IF NOT EXISTS "store_achat" ("id" integer NOT NULL PRIMARY KEY SERIAL, "acheté" bool NOT NULL, "quantité" integer NOT NULL, "utilisateur_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "billet_id" bigint NOT NULL REFERENCES "store_offrebillet" ("id") DEFERRABLE INITIALLY DEFERRED, "epreuve_id" bigint NULL REFERENCES "store_epreuve" ("id") DEFERRABLE INITIALLY DEFERRED, "panier_id" bigint NULL REFERENCES "store_panier" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO store_achat VALUES(10,0,1,10,2,2,9);
INSERT INTO store_achat VALUES(11,0,1,12,1,5,10);
CREATE TABLE IF NOT EXISTS "store_offrebillet" ("id" integer NOT NULL PRIMARY KEY SERIAL, "description" text NOT NULL, "prix" decimal NOT NULL, "nombre_personnes" integer unsigned NOT NULL CHECK ("nombre_personnes" >= 0), "stock" integer NOT NULL, "slug" varchar(128) NOT NULL, "epreuve_id" bigint NULL REFERENCES "store_epreuve" ("id") DEFERRABLE INITIALLY DEFERRED, "nom" varchar(100) NULL UNIQUE);
INSERT INTO store_offrebillet VALUES(1,replace(replace('Billet Journée Solo - Accès Illimité aux Épreuves Olympiques\r\nVivez l''excitation des Jeux Olympiques avec notre Billet Solo. Ce billet vous offre un accès illimité pour une journée entière à toutes les épreuves olympiques, vous permettant de suivre les compétitions à votre rythme. Validez simplement votre QR Code à l''entrée des différentes zones de compétition et immergez-vous dans l''esprit olympique. C''est l''option parfaite pour les passionnés de sport qui désirent vivre une expérience inoubliable de manière autonome.','\r',char(13)),'\n',char(10)),30,1,15000000,'solo',NULL,'SOLO');
INSERT INTO store_offrebillet VALUES(2,'Partagez l''enthousiasme des Jeux Olympiques avec notre Billet Duo. Conçu pour deux spectateurs, ce billet assure une journée pleine d''action et d''émotion olympique. Ensemble, vous pourrez accéder à toutes les épreuves et profiter des performances athlétiques sans limite. Activez votre billet en scannant le QR Code fourni et profitez pleinement de cette journée olympique à deux.',50,2,50000000,'duo',NULL,'DUO');
INSERT INTO store_offrebillet VALUES(3,replace(replace('Billet Journée Familiale/Groupée - Accès Illimité pour Quatre aux Épreuves Olympiques\r\nEmmenez votre groupe ou votre famille aux Jeux Olympiques avec notre Billet Familial/Groupé. Ce billet permet à quatre personnes de vivre une journée remplie de passion sportive et de performances athlétiques. Pour les groupes de cinq, nous offrons la possibilité d''ajouter un membre sur demande préalable. Accédez sans restriction à toutes les épreuves dès la validation de votre QR Code et partagez ensemble l''émotion des Jeux !','\r',char(13)),'\n',char(10)),99,4,10000000,'famille',NULL,'FAMILLE');
CREATE TABLE IF NOT EXISTS "store_panier" ("id" integer NOT NULL PRIMARY KEY SERIAL, "acheté" bool NOT NULL, "date_achat" datetime NULL, "utilisateur_id" bigint NULL UNIQUE REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO store_panier VALUES(9,0,NULL,10);
INSERT INTO store_panier VALUES(10,1,'2024-05-20 18:39:53.239993',12);
CREATE TABLE IF NOT EXISTS "store_transaction" ("id" integer NOT NULL PRIMARY KEY SERIAL, "montant_total" decimal NOT NULL, "status" varchar(20) NOT NULL, "date_transaction" datetime NOT NULL, "panier_id" bigint NULL REFERENCES "store_panier" ("id") DEFERRABLE INITIALLY DEFERRED, "utilisateur_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO store_transaction VALUES(1,30,'reussi','2024-05-20 18:39:53.082808',10,12);
CREATE TABLE IF NOT EXISTS "accounts_customuser" ("id" integer NOT NULL PRIMARY KEY SERIAL, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "nom" varchar(30) NOT NULL, "prenom" varchar(30) NOT NULL);
INSERT INTO accounts_customuser VALUES(10,'pbkdf2_sha256$720000$c7vqsBVFd6SFcNZPzPnAt0$nI768SpSNRnZlsR9ipCnq96/tc2H68R0zZttfPkG9yg=','2024-05-17 14:55:56.971148',1,'Admin','','','admin@jof.fr',1,1,'2024-05-17 14:20:26.698851','','');
INSERT INTO accounts_customuser VALUES(11,'@123456789@',NULL,0,'JeanEudes','Jean','Eudes','JeanEudes@gmal.com',0,1,'2024-05-17 14:21:05','','');
INSERT INTO accounts_customuser VALUES(12,'pbkdf2_sha256$720000$u7xLqjF11VjZyBcp0yWiex$E/h8YRjDxt9+d37TJ028urSmCd96vXhLtLdnQNWtLjo=','2024-05-20 18:17:39.848083',0,'NomPrénom','Prénom','Nom','pazeboheidu-4450@yopmail.com',0,1,'2024-05-20 18:17:38.868612','','');
CREATE TABLE IF NOT EXISTS "store_ticket" ("id" integer NOT NULL PRIMARY KEY SERIAL, "montant_total" decimal NOT NULL, "date_creation" datetime NOT NULL, "qr_code" varchar(100) NULL, "transaction_id" bigint NOT NULL UNIQUE REFERENCES "store_transaction" ("id") DEFERRABLE INITIALLY DEFERRED, "utilisateur_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO store_ticket VALUES(1,30,'2024-05-20 18:39:53.094139','qr_codes/1.png',1,12);
CREATE TABLE IF NOT EXISTS "store_ticket_achats" ("id" integer NOT NULL PRIMARY KEY SERIAL, "ticket_id" bigint NOT NULL REFERENCES "store_ticket" ("id") DEFERRABLE INITIALLY DEFERRED, "achat_id" bigint NOT NULL REFERENCES "store_achat" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO store_ticket_achats VALUES(1,1,11);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',41);
INSERT INTO sqlite_sequence VALUES('django_content_type',12);
INSERT INTO sqlite_sequence VALUES('auth_permission',52);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('django_admin_log',55);
INSERT INTO sqlite_sequence VALUES('store_epreuve',8);
INSERT INTO sqlite_sequence VALUES('store_achat',11);
INSERT INTO sqlite_sequence VALUES('store_offrebillet',3);
INSERT INTO sqlite_sequence VALUES('store_panier',10);
INSERT INTO sqlite_sequence VALUES('accounts_customuser',12);
INSERT INTO sqlite_sequence VALUES('store_transaction',1);
INSERT INTO sqlite_sequence VALUES('store_ticket',1);
INSERT INTO sqlite_sequence VALUES('store_ticket_achats',1);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq" ON "accounts_customuser_groups" ("customuser_id", "group_id");
CREATE INDEX "accounts_customuser_groups_customuser_id_bc55088e" ON "accounts_customuser_groups" ("customuser_id");
CREATE INDEX "accounts_customuser_groups_group_id_86ba5f9e" ON "accounts_customuser_groups" ("group_id");
CREATE UNIQUE INDEX "accounts_customuser_user_permissions_customuser_id_permission_id_9632a709_uniq" ON "accounts_customuser_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "accounts_customuser_user_permissions_customuser_id_0deaefae" ON "accounts_customuser_user_permissions" ("customuser_id");
CREATE INDEX "accounts_customuser_user_permissions_permission_id_aea3d0e5" ON "accounts_customuser_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "store_epreuve_slug_53d39919" ON "store_epreuve" ("slug");
CREATE INDEX "store_achat_utilisateur_id_51e880eb" ON "store_achat" ("utilisateur_id");
CREATE INDEX "store_achat_billet_id_29b54c9b" ON "store_achat" ("billet_id");
CREATE INDEX "store_achat_epreuve_id_360ae2d7" ON "store_achat" ("epreuve_id");
CREATE INDEX "store_offrebillet_slug_949ab3d4" ON "store_offrebillet" ("slug");
CREATE INDEX "store_offrebillet_epreuve_id_27fddcb8" ON "store_offrebillet" ("epreuve_id");
CREATE INDEX "store_achat_panier_id_eb8993cd" ON "store_achat" ("panier_id");
CREATE INDEX "store_transaction_panier_id_07542836" ON "store_transaction" ("panier_id");
CREATE INDEX "store_transaction_utilisateur_id_e2b98a3b" ON "store_transaction" ("utilisateur_id");
CREATE INDEX "store_ticket_utilisateur_id_6c6f6d52" ON "store_ticket" ("utilisateur_id");
CREATE UNIQUE INDEX "store_ticket_achats_ticket_id_achat_id_c2047b8d_uniq" ON "store_ticket_achats" ("ticket_id", "achat_id");
CREATE INDEX "store_ticket_achats_ticket_id_218011c8" ON "store_ticket_achats" ("ticket_id");
CREATE INDEX "store_ticket_achats_achat_id_fa88067c" ON "store_ticket_achats" ("achat_id");
COMMIT;
