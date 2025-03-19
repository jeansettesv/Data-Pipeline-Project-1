--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    id integer NOT NULL,
    nome text NOT NULL,
    email text NOT NULL,
    cidade text,
    data_cadastro timestamp without time zone DEFAULT now()
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_seq OWNER TO postgres;

--
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (id, nome, email, cidade, data_cadastro) FROM stdin;
38	Mark Valencia MD	ufry@example.net	Janetton	2021-11-24 00:00:00
79	Benjamin Archer	guerrerojustin@example.org	New Derekmouth	2020-07-05 00:00:00
18	Nicole Cook	susanvasquez@example.org	East Christopherbury	2024-08-26 00:00:00
54	Brenda Flores	ugonzales@example.com	New Edwin	2024-10-30 00:00:00
75	Mr. Larry Morris MD	samuel21@example.net	Joshuaport	2023-10-28 00:00:00
88	Mr. Anthony Perez	wrightmartin@example.com	Lake Markfort	2020-10-08 00:00:00
72	Laura Ford	brownchelsea@example.com	Sherryland	2022-02-25 00:00:00
70	David Lee	joseph62@example.org	Williamsland	2024-11-12 00:00:00
67	Angela Todd	dickersonpeggy@example.net	West Davidtown	2021-01-20 00:00:00
62	Nicholas Terry	brett71@example.net	South Chad	2023-06-19 00:00:00
86	Cameron Gonzalez	dmays@example.com	Haleychester	2023-11-28 00:00:00
82	Andrew Vance	rosscynthia@example.net	North Veronicaton	2021-09-20 00:00:00
4	Jennifer Lyons	costachristine@example.net	Salazarland	2024-11-20 00:00:00
41	Cassandra Miranda	derrick87@example.com	West Joshuaside	2021-09-25 00:00:00
96	David Jackson	htaylor@example.com	Lake Teresaville	2021-04-25 00:00:00
53	Michelle Hanson	nicholsonwilliam@example.com	Markmouth	2022-06-06 00:00:00
6	David Powell	nicholas12@example.net	Turnermouth	2023-09-14 00:00:00
80	Matthew Lee	dberry@example.net	Guerrerotown	2023-06-10 00:00:00
99	Ashley Kelley	williamsbrett@example.net	Brownhaven	2024-07-24 00:00:00
58	Kathy Ali	gonzalezlouis@example.net	South Theresaville	2021-05-11 00:00:00
8	Michael Herrera	wsims@example.org	Stevestad	2021-10-19 00:00:00
65	Rhonda Mckay	rhodesjames@example.com	Sandovalland	2022-06-24 00:00:00
26	Jorge Branch	marcus70@example.org	East Ashleyview	2024-02-09 00:00:00
85	Mr. Nicholas Griffin Jr.	xmendoza@example.com	North John	2023-10-20 00:00:00
68	Stephanie Schroeder	twoods@example.com	North Kathleen	2024-03-13 00:00:00
34	Micheal West	lesliebrock@example.org	West Hector	2023-07-28 00:00:00
60	Stephen Fisher	tnichols@example.com	New Lauramouth	2022-10-14 00:00:00
55	Sergio Harrison	jameschang@example.com	Lutzstad	2023-11-10 00:00:00
71	Pedro Mcpherson	gmiller@example.net	Lake Timothystad	2023-01-26 00:00:00
16	David Johnson	fwilson@example.org	Matthewside	2023-08-08 00:00:00
66	Mr. Victor Sanders	calhounrobin@example.com	Ericshire	2023-09-24 00:00:00
12	Christopher Roy	saundersrichard@example.org	New Mary	2020-05-03 00:00:00
61	Vicki Vang	zball@example.net	Port Elizabeth	2020-01-03 00:00:00
98	Jessica Lopez	chelseacole@example.com	South Andrew	2020-11-29 00:00:00
49	Christopher Adams	jesuscastillo@example.com	West Michaelfort	2024-04-23 00:00:00
74	Jeffery Schultz	usuarez@example.org	Port Codyberg	2024-07-28 00:00:00
19	Kelsey Davis	elizabeth31@example.org	Port Randy	2023-04-23 00:00:00
36	David Brady	christina12@example.com	South Wandashire	2024-03-04 00:00:00
51	Michael Morrison	jgarrett@example.net	Port Andrea	2020-01-25 00:00:00
27	Rebecca Molina	ashleyfrancis@example.org	Garrettchester	2021-05-05 00:00:00
32	Edwin Rivas	eric29@example.com	Davidview	2021-08-22 00:00:00
13	Mark Wilson	pricebrenda@example.net	New Lawrence	2024-06-04 00:00:00
94	Dr. Margaret Jones DDS	suzannesummers@example.net	East Christopherview	2021-04-17 00:00:00
91	Aaron Evans	adam36@example.org	New Nathan	2021-11-01 00:00:00
21	Raymond Warren	ibarrera@example.com	North Rodney	2021-02-06 00:00:00
77	Lori Coleman	melissa26@example.org	Clarkville	2024-12-08 00:00:00
73	Jason Rodriguez	michaelpeterson@example.com	Codyshire	2024-05-18 00:00:00
97	Luis Rivera	asnow@example.com	Johnsonside	2020-08-12 00:00:00
92	Diane Palmer	bpeterson@example.net	Nicoleshire	2021-03-05 00:00:00
31	Spencer Nolan	alicewilson@example.org	Stephenview	2021-10-17 00:00:00
44	Nathaniel Meyers	torresstanley@example.net	New Michael	2021-03-24 00:00:00
10	Michael Malone	wallacedeborah@example.com	North Christinaville	2023-10-01 00:00:00
1	Marc Daniels	ninarios@example.org	Port William	2021-08-15 00:00:00
56	Ashley Ortiz MD	anthonyfoster@example.net	Denisemouth	2023-06-30 00:00:00
52	Ellen Silva	gutierrezbrent@example.net	Randolphstad	2020-06-01 00:00:00
25	Samantha Hale	lowekelly@example.org	Bensonstad	2020-02-25 00:00:00
93	Jennifer King	ujohnson@example.net	Moralesland	2022-10-14 00:00:00
64	Melanie Richardson	matthew84@example.net	North Paul	2023-06-22 00:00:00
89	Ashley Hampton	thomasadam@example.com	Archerland	2021-04-26 00:00:00
29	David Bean	wking@example.org	Jenniferfurt	2020-12-28 00:00:00
90	Brian Ward	brittany65@example.net	Lake Williammouth	2022-09-21 00:00:00
42	Alison Smith	davisstephen@example.org	Marquezmouth	2024-07-04 00:00:00
24	Gregory Foster	yestrada@example.org	Emilyview	2025-01-22 00:00:00
28	Gloria Tucker	lancehester@example.net	Loweside	2022-02-12 00:00:00
9	Robert Gutierrez	thompsontracy@example.org	West Terrifurt	2023-07-26 00:00:00
84	Jeremy Ali	dominguezjenna@example.com	Lake Whitneyton	2021-08-11 00:00:00
47	Kenneth Hicks	melanie08@example.org	East Johnside	2021-08-09 00:00:00
57	Rachel Allen	wmurray@example.com	Marilynport	2020-10-16 00:00:00
14	Jenny Green	moorejay@example.net	West Thomas	2020-02-05 00:00:00
81	Ashley Mccarthy	jimmy34@example.com	Audreyport	2022-09-25 00:00:00
63	Kimberly Bishop	castroamy@example.net	South Colleen	2024-11-15 00:00:00
43	Troy Hawkins	anthony22@example.net	Jamestown	2021-12-14 00:00:00
100	Paula Wilson	brett57@example.org	North Brandon	2024-10-12 00:00:00
59	Eric Davis	amber79@example.org	East William	2021-12-04 00:00:00
48	Cynthia Rodriguez	ccarr@example.com	Aliciaton	2023-04-29 00:00:00
20	Mark Ryan	christine92@example.org	Port Cheyenne	2022-08-29 00:00:00
50	Ashley Jensen	gregory08@example.org	Rothberg	2021-05-26 00:00:00
83	Joshua Johnson	robertmonroe@example.org	Gregoryberg	2024-10-25 00:00:00
15	Allison Sparks	wperkins@example.com	Lake Robyn	2025-03-10 00:00:00
22	Brian Olsen	jamiethompson@example.net	North Angelaland	2024-02-08 00:00:00
30	Jonathan Brooks	andrea76@example.org	Weberburgh	2022-02-16 00:00:00
46	Stephen Wilson	rpena@example.com	Warrenberg	2020-01-06 00:00:00
78	Michael Mathews	allison98@example.com	Riceland	2024-10-29 00:00:00
17	Aaron Walker	wendywhite@example.com	Kennedyview	2020-02-26 00:00:00
87	Victoria Welch	brittanygallegos@example.org	New Lance	2023-06-30 00:00:00
11	Jared Manning	james79@example.net	New Christopher	2020-09-15 00:00:00
2	Scott Smith	ryan29@example.org	Brendashire	2023-12-19 00:00:00
7	Nathaniel Rodriguez	jeffrey84@example.com	North Michael	2023-09-03 00:00:00
37	Marco Taylor	isimpson@example.net	East Tara	2023-11-17 00:00:00
40	Carrie Baldwin	lauralewis@example.org	Lake Lauraside	2022-05-06 00:00:00
69	Jim Anderson	kathrynramos@example.net	West Tabithahaven	2020-01-31 00:00:00
5	Chad Harris	ctaylor@example.net	Port Amandatown	2023-03-06 00:00:00
33	Martin Jenkins	benjamin21@example.org	New Bonnieborough	2021-07-18 00:00:00
35	Claudia Martin	sgraham@example.com	Port Denise	2021-12-17 00:00:00
76	Jason Baker	barnesdebra@example.org	Johnsontown	2024-03-21 00:00:00
95	Elaine Howard	graybrandon@example.com	New James	2020-04-16 00:00:00
3	Tracey Torres	mroach@example.com	West Kerri	2020-02-09 00:00:00
23	Amber Powers	stephanie68@example.com	Campbellmouth	2024-07-29 00:00:00
39	Robert Simmons	michael05@example.com	Lake Markside	2024-05-30 00:00:00
45	Tony Donovan	jasminewebb@example.org	Port Roseview	2020-10-12 00:00:00
\.


--
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clientes_id_seq', 1, false);


--
-- Name: clientes clientes_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_email_key UNIQUE (email);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

