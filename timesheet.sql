--SISTEM DE PONTARE (TIMESHEETS) 
--Modelarea unui sistem care permite angajatilor sa raporteze zilnic
--activitatile defasurate pe proiecte, grupate saptamanal in timesheeturi.
--tabelul angajati:
--contine datele angajatilor (nume, email, data angajare, activ).
--legatura prin manager_id (FK spre angajati).
--constrangeri PK, UNIQUE (email), CHECK (activ), DEFAULT (data_angajare).
--tabelul proiecte:
--listeaza proiectele disponibile.
--contine campul activ (Y/N) cu DEFAULT 'Y' pentru proiecte noi.
--tabelul activitati:
--definește tipurile de activitati (ex: Development, Training).
--include campul billable (Y/N) validat cu CHECK.
--tabelul timesheeturi:
--timesheet saptamanal per angajat.
--constrangere UNIQUE pe (id_angajat, saptamana_start).
--status implicit: 'Draft'
--tabelul pontaj_zilnic:
--raportarea zilnica a orelor lucrate pe activitate/proiect.
--contine durata_ore (0–24) cu CHECK.

---GRANTURI NECESARE PENTRU UTILIZATORUL CARE VA RULA SCRIPTUL
---GRANT CREATE TABLE, CREATE VIEW, CREATE MATERIALIZED VIEW TO timesheet_user; executate de catre SYS 

--creare tabel angajati
CREATE TABLE angajati (
    id_angajat NUMBER PRIMARY KEY,                           
    nume VARCHAR2(100) NOT NULL,                             
    email VARCHAR2(100) UNIQUE,                              
    data_angajare DATE DEFAULT SYSDATE,                      
    activ CHAR(1) CHECK (activ IN ('Y', 'N')),              
    manager_id NUMBER,
    CONSTRAINT fk_manager FOREIGN KEY (manager_id) REFERENCES angajati(id_angajat)
);

--creare tabel proiecte
CREATE TABLE proiecte (
    id_proiect NUMBER PRIMARY KEY,
    nume_proiect VARCHAR2(200) NOT NULL,
    activ CHAR(1) DEFAULT 'Y'
);

--creare tabel activitati
CREATE TABLE activitati (
    id_activitate NUMBER PRIMARY KEY,
    nume_activitate VARCHAR2(100) NOT NULL,
    billable CHAR(1) CHECK (billable IN ('Y', 'N'))
);

--creare tabel timesheeturi
CREATE TABLE timesheeturi (
    id_timesheet NUMBER PRIMARY KEY,
    id_angajat NUMBER NOT NULL,
    saptamana_start DATE NOT NULL,
    status VARCHAR2(20) DEFAULT 'Draft',
    data_submitere TIMESTAMP,
    CONSTRAINT fk_timesheet_angajat FOREIGN KEY (id_angajat) REFERENCES angajati(id_angajat),
    CONSTRAINT uq_timesheet_angajat UNIQUE (id_angajat, saptamana_start)
);

--creare tabel pontaj_zilnic
CREATE TABLE pontaj_zilnic (
    id_pontaj NUMBER PRIMARY KEY,
    id_timesheet NUMBER NOT NULL,
    data_zi DATE NOT NULL,
    id_proiect NUMBER NOT NULL,
    id_activitate NUMBER NOT NULL,
    durata_ore NUMBER(4,2) CHECK (durata_ore BETWEEN 0 AND 24),
    observatii CLOB,
    detalii_json CLOB, --coloana date semistructurate json

    CONSTRAINT fk_pontaj_timesheet FOREIGN KEY (id_timesheet) REFERENCES timesheeturi(id_timesheet),
    CONSTRAINT fk_pontaj_proiect FOREIGN KEY (id_proiect) REFERENCES proiecte(id_proiect),
    CONSTRAINT fk_pontaj_activitate FOREIGN KEY (id_activitate) REFERENCES activitati(id_activitate)
);

--creare index suplimentar
CREATE INDEX idx_pontaj_data ON pontaj_zilnic(data_zi);
--inseram valori in tabelul angajati – 3 persoane, una este managerul celorlalti, adica prima persoana
INSERT INTO angajati (id_angajat, nume, email, data_angajare, activ, manager_id)
VALUES (1, 'Popescu Ana', 'ana.popescu@endava.com', TO_DATE('2022-05-09', 'YYYY-MM-DD'), 'Y', NULL);
INSERT INTO angajati (id_angajat, nume, email, data_angajare, activ, manager_id)
VALUES (2, 'Ionescu Mihai', 'mihai.ionescu@endava.com', TO_DATE('2023-03-01', 'YYYY-MM-DD'), 'Y', 1);
INSERT INTO angajati (id_angajat, nume, email, data_angajare, activ, manager_id)
VALUES (3, 'Dumitru Elena', 'elena.dumitru@endava.com', TO_DATE('2024-11-20', 'YYYY-MM-DD'), 'Y', 1);

--inseram valori in tabelul proiecte - 2 active, 1 inchis
INSERT INTO proiecte (id_proiect, nume_proiect, activ) VALUES (10, 'Apollo CRM rollout', 'Y');
INSERT INTO proiecte (id_proiect, nume_proiect, activ) VALUES (11, 'Mobile Banking v3',  'Y');
INSERT INTO proiecte (id_proiect, nume_proiect, activ) VALUES (12, 'Legacy SAP sunset',  'N');

--am pus acest define off pentru ca mi se lua primul insert ca si variabila de substituie si nu am nevoie
SET DEFINE OFF;
--inseram valori in tabelul activitati
INSERT INTO activitati (id_activitate, nume_activitate, billable) VALUES (100, 'Analysis & Design', 'Y');
INSERT INTO activitati (id_activitate, nume_activitate, billable) VALUES (101, 'Development',       'Y');
INSERT INTO activitati (id_activitate, nume_activitate, billable) VALUES (102, 'Code Review',       'Y');
INSERT INTO activitati (id_activitate, nume_activitate, billable) VALUES (103, 'Internal Training', 'N');
INSERT INTO activitati (id_activitate, nume_activitate, billable) VALUES (104, 'Pre-sales support', 'N');

--inseram valori in tabelul timesheeturi- cate unul pe saptamana/angajat
INSERT INTO timesheeturi (id_timesheet, id_angajat, saptamana_start, status, data_submitere)
VALUES (1000, 2, TO_DATE('2025-06-02', 'YYYY-MM-DD'), 'Submitted', SYSTIMESTAMP);
INSERT INTO timesheeturi (id_timesheet, id_angajat, saptamana_start, status, data_submitere)
VALUES (1001, 3, TO_DATE('2025-06-02', 'YYYY-MM-DD'), 'Submitted', SYSTIMESTAMP);
INSERT INTO timesheeturi (id_timesheet, id_angajat, saptamana_start, status, data_submitere)
VALUES (1002, 2, TO_DATE('2025-05-26', 'YYYY-MM-DD'), 'Approved', SYSTIMESTAMP - 8);
INSERT INTO timesheeturi (id_timesheet, id_angajat, saptamana_start, status, data_submitere)
VALUES (1003, 3, TO_DATE('2025-05-26', 'YYYY-MM-DD'), 'Approved', SYSTIMESTAMP - 8);

--inseram valori in tabela pontaj_zilnic - cateva intrari pe aceeasi saptamana(totalul pe zi nu depaseste 24 h; FK-urile leaga totul)
INSERT INTO pontaj_zilnic (id_pontaj, id_timesheet, data_zi, id_proiect, id_activitate, durata_ore, observatii, detalii_json)
VALUES (2001, 1000, TO_DATE('2025-06-02', 'YYYY-MM-DD'), 10, 101, 8, 'Sprint backlog', NULL);
INSERT INTO pontaj_zilnic VALUES (2002, 1000, TO_DATE('2025-06-03', 'YYYY-MM-DD'), 10, 101, 7.5, 'Implementare API', NULL);
INSERT INTO pontaj_zilnic VALUES (2003, 1000, TO_DATE('2025-06-03', 'YYYY-MM-DD'), 10, 102, 0.5, 'Peer review', NULL);
INSERT INTO pontaj_zilnic VALUES (2004, 1000, TO_DATE('2025-06-04', 'YYYY-MM-DD'), 11, 100, 8, 'Workshop design', NULL);
INSERT INTO pontaj_zilnic VALUES (2005, 1001, TO_DATE('2025-06-02', 'YYYY-MM-DD'), 11, 101, 8, NULL, '{"jira":"MB-231","notes":"login flow"}');
INSERT INTO pontaj_zilnic VALUES (2006, 1001, TO_DATE('2025-06-03', 'YYYY-MM-DD'), 11, 101, 8, NULL, NULL);
INSERT INTO pontaj_zilnic VALUES (2007, 1001, TO_DATE('2025-06-04', 'YYYY-MM-DD'), 11, 103, 2, 'Kotlin course', NULL);
INSERT INTO pontaj_zilnic VALUES (2008, 1001, TO_DATE('2025-06-04', 'YYYY-MM-DD'), 11, 101, 6, NULL, NULL);
INSERT INTO pontaj_zilnic VALUES (2009, 1002, TO_DATE('2025-05-27', 'YYYY-MM-DD'), 10, 101, 8, NULL, NULL);
INSERT INTO pontaj_zilnic VALUES (2010, 1003, TO_DATE('2025-05-27', 'YYYY-MM-DD'), 11, 101, 8, NULL, NULL);

--view simplu: Ore raportate per angajat per saptamana

CREATE OR REPLACE VIEW vw_raport_saptamanal AS
SELECT
    a.nume,
    t.saptamana_start,
    SUM(p.durata_ore) AS total_ore
FROM angajati a
JOIN timesheeturi t ON a.id_angajat = t.id_angajat
JOIN pontaj_zilnic p ON p.id_timesheet = t.id_timesheet
GROUP BY a.nume, t.saptamana_start;

--materialized view: Total ore per proiect

CREATE MATERIALIZED VIEW mv_ore_per_proiect
BUILD IMMEDIATE
REFRESH ON DEMAND
AS
SELECT 
    p.id_proiect,
    pr.nume_proiect,
    SUM(p.durata_ore) AS total_ore
FROM pontaj_zilnic p
JOIN proiecte pr ON p.id_proiect = pr.id_proiect
GROUP BY p.id_proiect, pr.nume_proiect;

--acest slect calculeaza numarul total de ore raportate per zi
SELECT data_zi, SUM(durata_ore) AS total_ore
FROM pontaj_zilnic
GROUP BY data_zi;

--acest select listeaza toti angajatii si totalul orelor raportate(daca exista)
SELECT a.nume, SUM(p.durata_ore) AS total_ore
FROM angajati a
LEFT JOIN timesheeturi t ON a.id_angajat = t.id_angajat
LEFT JOIN pontaj_zilnic p ON p.id_timesheet = t.id_timesheet
GROUP BY a.nume;

--acest select afiseaza orele raportate de fiecare angajat in fiecare zi,
--impreuna cu media orelor raportate de acel angajat pana in ziua curenta.
SELECT 
    a.nume,
    p.data_zi,
    p.durata_ore,
    AVG(p.durata_ore) OVER (
        PARTITION BY a.id_angajat
        ORDER BY p.data_zi
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS media_ore
FROM angajati a
JOIN timesheeturi t ON t.id_angajat = a.id_angajat
JOIN pontaj_zilnic p ON p.id_timesheet = t.id_timesheet
ORDER BY a.nume, p.data_zi;

--modificam statusul unui timesheet din 'Approved' in 'Draft'
UPDATE timesheeturi
SET status = 'Draft'
WHERE id_timesheet = 1002;



