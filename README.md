# Holiday Oracle Python bindings

[![Build Status](https://travis-ci.com/OffChainData/holiday-oracle-python.svg?branch=master)](https://travis-ci.com/OffChainData/holiday-oracle-python)
[![License](https://offchaindata.com/images/license.svg)](https://github.com/OffChainData/holiday-oracle-python/blob/master/LICENSE)
[![pypi](https://img.shields.io/badge/pypi-v0.1.2-orange)](https://pypi.org/project/holiday-oracle/)


The Holiday Oracle Python library provides convenient access to the global holiday API provided by [Off Chain Data](https://holidayoracle.io/docs/index.html) from applications written in the Python language. 

## Requirements

* An API token from [Holiday Oracle](https://holidayoracle.io)
* Python 3.4+

## Installation 

Install with pip:

```pip install --upgrade holiday-oracle```

Install from source with:

```pip install --editable .```

## Calling the API

Calling the API is straight-forward:

```python
from offchain.api import HolidayOracleApi

api = HolidayOracleApi( token )
resp = api.me()
print( resp.json )
```

If no token is provided, the library will look for a `OCD_TOKEN` environment variable.

The HTTP response code, headers and raw response data are also provided in the response object.

Some API endpoints have mandatory parameters e.g.
```python
resp = api.date( country="AU", date="2020-01-01" )
```
Optional parameters can also be provided in the same way e.g.
```python
resp = api.date( country="AU", date="2020-01-01", subdivision="NSW" )
```

## Handling errors

If an error occurs, an `ApiError` exception will be thrown e.g.
```python
try:
    resp = api.me()
except ApiError as ex:
    print( "ERROR:", ex.message )
```

## Supported Locations

The following is a list of locations supported by the API.
Where a country has no subdivisions, holidays are returned for the entire country.
Where subdivisions are defined, you can query for holidays a both the country and subdivisions level.

You can also query the API [https://offchaindata.com/docs/index.html#locations](https://offchaindata.com/docs/index.html#locations) for a list of currently supported locations.

| Country &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| Subdivision |
|---------|-------------|
| Andorra (AD) |  Andorra la Vella (07) | 
| United Arab Emirates (AE) |  Entire Country | 
| Antigua and Barbuda (AG) |  Barbuda (10) | 
| Anguilla (AI) |  Entire Country | 
| Albania (AL) |  Entire Country | 
| Armenia (AM) |  Entire Country | 
| Angola (AO) |  Entire Country | 
| Argentina (AR) |  Entire Country | 
| American Samoa (AS) |  Entire Country | 
| Austria (AT) |  Burgenland (1),  Kärnten (2),  Niederösterreich (3),  Oberösterreich (4),  Salzburg (5),  Steiermark (6),  Tirol (7),  Vorarlberg (8),  Wien (9) | 
| Australia (AU) |  Australian Capital Territory (ACT),  New South Wales (NSW),  Northern Territory (NT),  Queensland (QLD),  South Australia (SA),  Tasmania (TAS),  Victoria (VIC),  Western Australia (WA) | 
| Aruba (AW) |  Entire Country | 
| Åland Islands (AX) |  Entire Country | 
| Azerbaijan (AZ) |  Entire Country | 
| Bosnia and Herzegovina (BA) |  Federacija Bosne i Hercegovine (BIH),  Brčko distrikt (BRC),  Republika Srpska (SRP) | 
| Barbados (BB) |  Entire Country | 
| Bangladesh (BD) |  Entire Country | 
| Belgium (BE) |  Brussels Hoofdstedelijk Gewest (BRU),  Vlaams Gewest (VLG),  wallonne, Région (WAL) | 
| Burkina Faso (BF) |  Entire Country | 
| Bulgaria (BG) |  Entire Country | 
| Bahrain (BH) |  Entire Country | 
| Burundi (BI) |  Entire Country | 
| Benin (BJ) |  Entire Country | 
| Saint Barthélemy (BL) |  Entire Country | 
| Bermuda (BM) |  Entire Country | 
| Brunei Darussalam (BN) |  Entire Country | 
| Bolivia (Plurinational State of) (BO) |  Entire Country | 
| Bonaire, Sint Eustatius and Saba (BQ) |  Boneiru (BO),  Saba (SA),  Sint Eustatius (SE) | 
| Brazil (BR) |  Acre (AC),  Alagoas (AL),  Amazonas (AM),  Amapá (AP),  Bahia (BA),  Ceará (CE),  Distrito Federal (DF),  Espírito Santo (ES),  Goiás (GO),  Maranhão (MA),  Minas Gerais (MG),  Mato Grosso do Sul (MS),  Mato Grosso (MT),  Pará (PA),  Paraíba (PB),  Pernambuco (PE),  Piauí (PI),  Paraná (PR),  Rio de Janeiro (RJ),  Rio Grande do Norte (RN),  Rondônia (RO),  Roraima (RR),  Rio Grande do Sul (RS),  Santa Catarina (SC),  Sergipe (SE),  São Paulo (SP),  Tocantins (TO) | 
| Bahamas (BS) |  Entire Country | 
| Botswana (BW) |  Entire Country | 
| Belarus (BY) |  Entire Country | 
| Belize (BZ) |  Entire Country | 
| Canada (CA) |  Alberta (AB),  Colombie-Britannique (BC),  Manitoba (MB),  Nouveau-Brunswick (NB),  Terre-Neuve-et-Labrador (NL),  Nouvelle-Écosse (NS),  Territoires du Nord-Ouest (NT),  Nunavut (NU),  Ontario (ON),  Île-du-Prince-Édouard (PE),  Québec (QC),  Saskatchewan (SK),  Yukon (YT) | 
| Cocos (Keeling) Islands (CC) |  Entire Country | 
| Congo, Democratic Republic of the (CD) |  Entire Country | 
| Central African Republic (CF) |  Entire Country | 
| Congo (CG) |  Entire Country | 
| Switzerland (CH) |  Aargau (AG),  Appenzell Innerrhoden (AI),  Appenzell Ausserrhoden (AR),  Berne (BE),  Basel-Landschaft (BL),  Basel-Stadt (BS),  Fribourg (FR),  Genève (GE),  Glarus (GL),  Grischun (GR),  Jura (JU),  Luzern (LU),  Neuchâtel (NE),  Nidwalden (NW),  Obwalden (OW),  Sankt Gallen (SG),  Schaffhausen (SH),  Solothurn (SO),  Schwyz (SZ),  Thurgau (TG),  Ticino (TI),  Uri (UR),  Vaud (VD),  Valais (VS),  Zug (ZG),  Zürich (ZH) | 
| Côte d'Ivoire (CI) |  Entire Country | 
| Chile (CL) |  Arica y Parinacota (AP),  Atacama (AT),  Biobío (BI),  Coquimbo (CO),  Los Ríos (LR),  Magallanes (MA),  Tarapacá (TA) | 
| Cameroon (CM) |  Entire Country | 
| China (CN) |  Entire Country | 
| Colombia (CO) |  Entire Country | 
| Costa Rica (CR) |  Entire Country | 
| Cuba (CU) |  Entire Country | 
| Cabo Verde (CV) |  Ilhas de Sotavento (S) | 
| Curaçao (CW) |  Entire Country | 
| Christmas Island (CX) |  Entire Country | 
| Cyprus (CY) |  Entire Country | 
| Czechia (CZ) |  Entire Country | 
| Germany (DE) |  Brandenburg (BB),  Berlin (BE),  Baden-Württemberg (BW),  Bayern (BY),  Bremen (HB),  Hessen (HE),  Hamburg (HH),  Mecklenburg-Vorpommern (MV),  Niedersachsen (NI),  Nordrhein-Westfalen (NW),  Rheinland-Pfalz (RP),  Schleswig-Holstein (SH),  Saarland (SL),  Sachsen (SN),  Sachsen-Anhalt (ST),  Thüringen (TH) | 
| Denmark (DK) |  Entire Country | 
| Dominica (DM) |  Entire Country | 
| Dominican Republic (DO) |  Entire Country | 
| Algeria (DZ) |  Entire Country | 
| Ecuador (EC) |  Pichincha (P) | 
| Estonia (EE) |  Entire Country | 
| Egypt (EG) |  Entire Country | 
| Spain (ES) |  Andalucía (AN),  Aragón (AR),  Asturias, Principado de (AS),  Cantabria (CB),  Ceuta (CE),  Castilla y León (CL),  Castilla-La Mancha (CM),  Canarias (CN),  Catalunya (CT),  Extremadura (EX),  Galicia (GA),  Illes Balears (IB),  La Rioja (LO),  Madrid (M),  Murcia, Región de (MC),  Madrid, Comunidad de (MD),  Melilla (ML),  Murcia (MU),  Navarra (NA),  Navarra, Comunidad Foral de (NC),  Asturias (O),  País Vasco (PV),  La Rioja (RI),  Valenciana, Comunidad (VC) | 
| Ethiopia (ET) |  Entire Country | 
| Finland (FI) |  Entire Country | 
| Micronesia (Federated States of) (FM) |  Entire Country | 
| Faroe Islands (FO) |  Entire Country | 
| France (FR) |  Moselle (57),  Bas-Rhin (67),  Haut-Rhin (68),  Saint-Barthélemy (BL),  Guyane (GF),  Guadeloupe (GP),  Guadeloupe (GUA),  La Réunion (LRE),  Mayotte (MAY),  Saint-Martin (MF),  Martinique (MQ),  Nouvelle-Calédonie (NC),  Polynésie française (PF),  La Réunion (RE),  Wallis-et-Futuna (WF),  Mayotte (YT) | 
| Gabon (GA) |  Entire Country | 
| United Kingdom of Great Britain and Northern Ireland (GB) |  England (ENG),  Northern Ireland (NIR),  Scotland (SCT),  Wales (WLS) | 
| Grenada (GD) |  Entire Country | 
| French Guiana (GF) |  Entire Country | 
| Guernsey (GG) |  Entire Country | 
| Gibraltar (GI) |  Entire Country | 
| Greenland (GL) |  Entire Country | 
| Gambia (GM) |  Entire Country | 
| Guadeloupe (GP) |  Entire Country | 
| Equatorial Guinea (GQ) |  Entire Country | 
| Greece (GR) |  Entire Country | 
| Guatemala (GT) |  Entire Country | 
| Guam (GU) |  Entire Country | 
| Guyana (GY) |  Entire Country | 
| Hong Kong (HK) |  Entire Country | 
| Honduras (HN) |  Entire Country | 
| Croatia (HR) |  Splitsko-dalmatinska županija (17),  Dubrovačko-neretvanska županija (19) | 
| Haiti (HT) |  Entire Country | 
| Hungary (HU) |  Entire Country | 
| Indonesia (ID) |  Entire Country | 
| Ireland (IE) |  Entire Country | 
| Israel (IL) |  Entire Country | 
| Isle of Man (IM) |  Entire Country | 
| India (IN) |  Andhra Pradesh (AP),  Assam (AS),  Bihar (BR),  Gujarat (GJ),  Haryana (HR),  Karnataka (KA),  Kerala (KL),  Maharashtra (MH),  Madhya Pradesh (MP),  Rajasthan (RJ),  Sikkim (SK),  Tamil Nadu (TN),  Uttar Pradesh (UP),  West Bengal (WB) | 
| Iceland (IS) |  Entire Country | 
| Italy (IT) |  Valle d'Aosta (23),  Trentino-Alto Adige (32),  Ancona (AN),  Bari (BA),  Belluno (BL),  Bologna (BO),  Brescia (BS),  Bolzano (BZ),  Campobasso (CB),  Chieti (CH),  Cosenza (CS),  Catania (CT),  Enna (EN),  Forlì-Cesena (FC),  Ferrara (FE),  Firenze (FI),  Frosinone (FR),  Genova (GE),  Isernia (IS),  Crotone (KR),  Latina (LT),  Monza e Brianza (MB),  Milano (MI),  Mantova (MN),  Modena (MO),  Massa-Carrara (MS),  Napoli (NA),  Palermo (PA),  Piacenza (PC),  Padova (PD),  Pescara (PE),  Perugia (PG),  Pisa (PI),  Parma (PR),  Pistoia (PT),  Pesaro e Urbino (PU),  Ravenna (RA),  Reggio Emilia (RE),  Rieti (RI),  Roma (RM),  Rimini (RN),  Rovigo (RO),  Salerno (SA),  La Spezia (SP),  Siracusa (SR),  Teramo (TE),  Torino (TO),  Vercelli (VC),  Venezia (VE),  Vicenza (VI) | 
| Jersey (JE) |  Entire Country | 
| Jamaica (JM) |  Entire Country | 
| Japan (JP) |  Entire Country | 
| Kenya (KE) |  Entire Country | 
| Korea, Republic of (KR) |  Entire Country | 
| Cayman Islands (KY) |  Entire Country | 
| Liechtenstein (LI) |  Entire Country | 
| Lesotho (LS) |  Entire Country | 
| Lithuania (LT) |  Entire Country | 
| Luxembourg (LU) |  Entire Country | 
| Latvia (LV) |  Entire Country | 
| Morocco (MA) |  Entire Country | 
| Monaco (MC) |  Entire Country | 
| Moldova, Republic of (MD) |  Cahul (CA),  Chișinău (CU) | 
| Montenegro (ME) |  Entire Country | 
| Madagascar (MG) |  Entire Country | 
| Marshall Islands (MH) |  Entire Country | 
| North Macedonia (MK) |  Entire Country | 
| Mongolia (MN) |  Entire Country | 
| Northern Mariana Islands (MP) |  Entire Country | 
| Martinique (MQ) |  Entire Country | 
| Malta (MT) |  Entire Country | 
| Malawi (MW) |  Entire Country | 
| Mexico (MX) |  Entire Country | 
| Malaysia (MY) |  Entire Country | 
| Mozambique (MZ) |  Entire Country | 
| Namibia (NA) |  Entire Country | 
| Niger (NE) |  Entire Country | 
| Nicaragua (NI) |  Entire Country | 
| Netherlands (NL) |  Entire Country | 
| Norway (NO) |  Entire Country | 
| New Zealand (NZ) |  Tāmaki-makau-rau (AUK),  Te Moana a Toi Te Huatahi (BOP),  Waitaha (CAN),  Wharekauri (CIT),  Tūranga nui a Kiwa (GIS),  Te Matau a Māui (HKB),  Marlborough (MBH),  Manawatu Whanganui (MWT),  Whakatū (NSN),  Te Tai tokerau (NTL),  Ō Tākou (OTA),  Murihiku (STL),  Tasman (TAS),  Taranaki (TKI),  Te Whanga-nui-a-Tara (WGN),  Waikato (WKO),  Te Taihau ā uru (WTC) | 
| Panama (PA) |  Entire Country | 
| Peru (PE) |  Cusco (CUS) | 
| Philippines (PH) |  Entire Country | 
| Poland (PL) |  Entire Country | 
| Puerto Rico (PR) |  Entire Country | 
| Portugal (PT) |  Região Autónoma dos Açores (20),  Região Autónoma da Madeira (30) | 
| Palau (PW) |  Entire Country | 
| Paraguay (PY) |  Entire Country | 
| Qatar (QA) |  Entire Country | 
| Réunion (RE) |  Entire Country | 
| Romania (RO) |  Entire Country | 
| Serbia (RS) |  Entire Country | 
| Russian Federation (RU) |  Entire Country | 
| Rwanda (RW) |  Entire Country | 
| Sweden (SE) |  Entire Country | 
| Singapore (SG) |  Entire Country | 
| Saint Helena, Ascension and Tristan da Cunha (SH) |  Ascension (AC),  Saint Helena (HL),  Tristan da Cunha (TA) | 
| Slovenia (SI) |  Entire Country | 
| Svalbard and Jan Mayen (SJ) |  Entire Country | 
| Slovakia (SK) |  Banskobystrický kraj (BC),  Bratislavský kraj (BL),  Košický kraj (KI),  Nitriansky kraj (NI),  Prešovský kraj (PV),  Trnavský kraj (TA),  Trenčiansky kraj (TC),  Žilinský kraj (ZI) | 
| San Marino (SM) |  Entire Country | 
| Somalia (SO) |  Awdal (AW),  Sanaag (SA),  Sool (SO),  Togdheer (TO),  Woqooyi Galbeed (WO) | 
| Suriname (SR) |  Entire Country | 
| South Sudan (SS) |  Entire Country | 
| Sao Tome and Principe (ST) |  Entire Country | 
| El Salvador (SV) |  San Salvador (SS) | 
| Togo (TG) |  Entire Country | 
| Tunisia (TN) |  Entire Country | 
| Tonga (TO) |  Entire Country | 
| Turkey (TR) |  Entire Country | 
| Taiwan, Province of China (TW) |  Entire Country | 
| Tanzania, United Republic of (TZ) |  Entire Country | 
| Ukraine (UA) |  Entire Country | 
| Uganda (UG) |  Entire Country | 
| United States of America (US) |  Alaska (AK),  Alabama (AL),  Arkansas (AR),  American Samoa (AS),  Arizona (AZ),  California (CA),  Colorado (CO),  Connecticut (CT),  District of Columbia (DC),  Delaware (DE),  Florida (FL),  Georgia (GA),  Guam (GU),  Hawaii (HI),  Iowa (IA),  Idaho (ID),  Illinois (IL),  Indiana (IN),  Kansas (KS),  Kentucky (KY),  Louisiana (LA),  Massachusetts (MA),  Maryland (MD),  Maine (ME),  Michigan (MI),  Minnesota (MN),  Missouri (MO),  Northern Mariana Islands (MP),  Mississippi (MS),  Montana (MT),  North Carolina (NC),  North Dakota (ND),  Nebraska (NE),  New Hampshire (NH),  New Jersey (NJ),  New Mexico (NM),  Nevada (NV),  New York (NY),  Ohio (OH),  Oklahoma (OK),  Oregon (OR),  Pennsylvania (PA),  Puerto Rico (PR),  Rhode Island (RI),  South Carolina (SC),  South Dakota (SD),  Tennessee (TN),  Texas (TX),  Utah (UT),  Virginia (VA),  Virgin Islands, U.S. (VI),  Vermont (VT),  Washington (WA),  Wisconsin (WI),  West Virginia (WV),  Wyoming (WY) | 
| Uruguay (UY) |  Entire Country | 
| Holy See (VA) |  Entire Country | 
| Venezuela (Bolivarian Republic of) (VE) |  Anzoátegui (B),  Carabobo (G),  Lara (K),  Miranda (M),  Monagas (N),  Táchira (S),  Zulia (V) | 
| Virgin Islands (U.S.) (VI) |  Entire Country | 
| Viet Nam (VN) |  Entire Country | 
| Mayotte (YT) |  Entire Country | 
| South Africa (ZA) |  Entire Country | 
| Zambia (ZM) |  Entire Country | 
| Zimbabwe (ZW) |  Entire Country |
