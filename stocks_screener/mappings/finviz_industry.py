
def stock_dict_code():

    data = """
    A/ Agilent Technologies Inc./ Healthcare/ Diagnostics & Research
AA/ Alcoa Corp/ Basic Materials/ Aluminum
AAL/ American Airlines Group Inc/ Industrials/ Airlines
AAON/ AAON Inc./ Industrials/ Building Products & Equipment
AAP/ Advance Auto Parts Inc/ Consumer Cyclical/ Specialty Retail
AAPL/ Apple Inc/ Technology/ Consumer Electronics
AAT/ American Assets Trust Inc/ Real Estate/ REIT - Diversified
AB/ AllianceBernstein Holding Lp/ Financial/ Asset Management
ABBV/ Abbvie Inc/ Healthcare/ Drug Manufacturers - General
ABCB/ Ameris Bancorp/ Financial/ Banks - Regional
ABCL/ AbCellera Biologics Inc/ Healthcare/ Biotechnology
ABG/ Asbury Automotive Group Inc/ Consumer Cyclical/ Auto & Truck Dealerships
ABM/ ABM Industries Inc./ Industrials/ Specialty Business Services
ABNB/ Airbnb Inc/ Consumer Cyclical/ Travel Services
ABR/ Arbor Realty Trust Inc./ Real Estate/ REIT - Mortgage
ABT/ Abbott Laboratories/ Healthcare/ Medical Devices
ACA/ Arcosa Inc/ Industrials/ Engineering & Construction
ACAD/ Acadia Pharmaceuticals Inc/ Healthcare/ Biotechnology
ACCD/ Accolade Inc/ Healthcare/ Health Information Services
ACDC/ ProFrac Holding Corp/ Energy/ Oil & Gas Equipment & Services
ACHC/ Acadia Healthcare Company Inc/ Healthcare/ Medical Care Facilities
ACHR/ Archer Aviation Inc/ Industrials/ Aerospace & Defense
ACI/ Albertsons Companies Inc/ Consumer Defensive/ Grocery Stores
ACIW/ ACI Worldwide Inc/ Technology/ Software - Infrastructure
ACLS/ Axcelis Technologies Inc/ Technology/ Semiconductor Equipment & Materials
ACLX/ Arcellx Inc/ Healthcare/ Biotechnology
ACM/ AECOM/ Industrials/ Engineering & Construction
ACMR/ ACM Research Inc/ Technology/ Semiconductor Equipment & Materials
ACN/ Accenture plc/ Technology/ Information Technology Services
ACT/ Enact Holdings Inc/ Financial/ Insurance - Specialty
ACVA/ ACV Auctions Inc/ Consumer Cyclical/ Auto & Truck Dealerships
ADBE/ Adobe Inc/ Technology/ Software - Infrastructure
ADC/ Agree Realty Corp./ Real Estate/ REIT - Retail
ADEA/ Adeia Inc/ Technology/ Software - Application
ADI/ Analog Devices Inc./ Technology/ Semiconductors
ADM/ Archer Daniels Midland Co./ Consumer Defensive/ Farm Products
ADMA/ Adma Biologics Inc/ Healthcare/ Biotechnology
ADNT/ Adient plc/ Consumer Cyclical/ Auto Parts
ADP/ Automatic Data Processing Inc./ Industrials/ Staffing & Employment Services
ADSK/ Autodesk Inc./ Technology/ Software - Application
ADT/ ADT Inc/ Industrials/ Security & Protection Services
ADUS/ Addus HomeCare Corporation/ Healthcare/ Medical Care Facilities
ADV/ Advantage Solutions Inc./ Communication Services/ Advertising Agencies
AEE/ Ameren Corp./ Utilities/ Utilities - Regulated Electric
AEG/ Aegon Ltd./ Financial/ Insurance - Diversified
AEIS/ Advanced Energy Industries Inc./ Industrials/ Electrical Equipment & Parts
AEL/ American Equity Investment Life Holding Co/ Financial/ Insurance - Life
AEM/ Agnico Eagle Mines Ltd/ Basic Materials/ Gold
AEO/ American Eagle Outfitters Inc./ Consumer Cyclical/ Apparel Retail
AEP/ American Electric Power Company Inc./ Utilities/ Utilities - Regulated Electric
AER/ Aercap Holdings N.V./ Industrials/ Rental & Leasing Services
AES/ AES Corp./ Utilities/ Utilities - Diversified
AFG/ American Financial Group Inc/ Financial/ Insurance - Property & Casualty
AFL/ Aflac Inc./ Financial/ Insurance - Life
AFRM/ Affirm Holdings Inc/ Technology/ Software - Infrastructure
AG/ First Majestic Silver Corporation/ Basic Materials/ Silver
AGCO/ AGCO Corp./ Industrials/ Farm & Heavy Construction Machinery
AGI/ Alamos Gold Inc./ Basic Materials/ Gold
AGIO/ Agios Pharmaceuticals Inc/ Healthcare/ Biotechnology
AGL/ Agilon Health Inc/ Healthcare/ Medical Care Facilities
AGM/ Federal Agricultural Mortgage Corp./ Financial/ Credit Services
AGNC/ AGNC Investment Corp/ Real Estate/ REIT - Mortgage
AGR/ Avangrid Inc/ Utilities/ Utilities - Regulated Electric
AGRO/ Adecoagro S.A./ Consumer Defensive/ Farm Products
AGTI/ Agiliti Inc/ Healthcare/ Health Information Services
AGYS/ Agilysys/ / 
AHH/ Armada Hoffler Properties Inc/ Real Estate/ REIT - Diversified
AI/ C3.ai Inc/ Technology/ Software - Application
AIG/ American International Group Inc/ Financial/ Insurance - Diversified
AIN/ Albany International Corp./ Consumer Cyclical/ Textile Manufacturing
AIR/ AAR Corp./ Industrials/ Aerospace & Defense
AIRC/ Apartment Income REIT Corp/ Real Estate/ REIT - Residential
AIT/ Applied Industrial Technologies Inc./ Industrials/ Industrial Distribution
AIV/ Apartment Investment & Management Co./ Real Estate/ REIT - Residential
AIZ/ Assurant Inc/ Financial/ Insurance - Specialty
AJG/ Arthur J. Gallagher & Co./ Financial/ Insurance Brokers
AKAM/ Akamai Technologies Inc/ Technology/ Software - Infrastructure
AKR/ Acadia Realty Trust/ Real Estate/ REIT - Retail
AKRO/ Akero Therapeutics Inc/ Healthcare/ Biotechnology
AL/ Air Lease Corp/ Industrials/ Rental & Leasing Services
ALB/ Albemarle Corp./ Basic Materials/ Specialty Chemicals
ALC/ Alcon Inc./ Healthcare/ Medical Instruments & Supplies
ALE/ Allete/ / 
ALEX/ Alexander & Baldwin Inc./ Real Estate/ REIT - Retail
ALG/ Alamo Group Inc./ Industrials/ Farm & Heavy Construction Machinery
ALGM/ Allegro Microsystems Inc./ Technology/ Semiconductors
ALGN/ Align Technology/ / 
ALGT/ Allegiant Travel/ Industrials/ Airlines
ALHC/ Alignment Healthcare Inc/ Healthcare/ Healthcare Plans
ALIT/ Alight Inc./ Technology/ Software - Application
ALK/ Alaska Air Group Inc./ Industrials/ Airlines
ALKS/ Alkermes plc/ Healthcare/ Drug Manufacturers - Specialty & Generic
ALKT/ Alkami Technology Inc/ Technology/ Software - Application
ALL/ Allstate Corp/ Financial/ Insurance - Property & Casualty
ALLE/ Allegion plc/ Industrials/ Security & Protection Services
ALLY/ Ally Financial Inc/ Financial/ Credit Services
ALNY/ Alnylam Pharmaceuticals Inc/ Healthcare/ Biotechnology
ALPN/ Alpine Immune Sciences Inc/ Healthcare/ Biotechnology
ALRM/ Alarm.com Holdings Inc/ Technology/ Software - Application
ALSN/ Allison Transmission Holdings Inc/ Consumer Cyclical/ Auto Parts
ALTR/ Altair Engineering Inc/ Technology/ Software - Infrastructure
ALV/ Autoliv Inc./ Consumer Cyclical/ Auto Parts
ALVO/ Alvotech/ Healthcare/ Drug Manufacturers - Specialty & Generic
ALX/ Alexander's Inc./ Real Estate/ REIT - Retail
AM/ Antero Midstream Corp/ Energy/ Oil & Gas Midstream
AMAM/ Ambrx Biopharma Inc./ Healthcare/ Biotechnology
AMAT/ Applied Materials Inc./ Technology/ Semiconductor Equipment & Materials
AMBA/ Ambarella Inc/ Technology/ Semiconductor Equipment & Materials
AMBP/ Ardagh Metal Packaging S.A./ Consumer Cyclical/ Packaging & Containers
AMC/ AMC Entertainment Holdings Inc/ Communication Services/ Entertainment
AMCR/ Amcor Plc/ Consumer Cyclical/ Packaging & Containers
AMD/ Advanced Micro Devices Inc./ Technology/ Semiconductors
AME/ Ametek Inc/ Industrials/ Specialty Industrial Machinery
AMED/ Amedisys Inc./ Healthcare/ Medical Care Facilities
AMEH/ Apollo Medical Holdings Inc/ Healthcare/ Medical Care Facilities
AMG/ Affiliated Managers Group Inc./ Financial/ Asset Management
AMGN/ AMGEN Inc./ Healthcare/ Drug Manufacturers - General
AMH/ American Homes 4 Rent/ Real Estate/ REIT - Residential
AMK/ Assetmark Financial Holdings Inc/ Financial/ Asset Management
AMKR/ AMKOR Technology Inc./ Technology/ Semiconductor Equipment & Materials
AMLX/ Amylyx Pharmaceuticals Inc/ Healthcare/ Biotechnology
AMN/ AMN Healthcare Services Inc./ Healthcare/ Medical Care Facilities
AMP/ Ameriprise Financial Inc/ Financial/ Asset Management
AMPH/ Amphastar Pharmaceuticals Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
AMPL/ Amplitude Inc/ Technology/ Software - Application
AMR/ Alpha Metallurgical Resources Inc/ Basic Materials/ Coking Coal
AMRC/ Ameresco Inc./ Industrials/ Engineering & Construction
AMRX/ Amneal Pharmaceuticals Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
AMT/ American Tower Corp./ Real Estate/ REIT - Specialty
AMWD/ American Woodmark Corp./ Consumer Cyclical/ Furnishings
AMZN/ Amazon.com Inc./ Consumer Cyclical/ Internet Retail
AN/ Autonation Inc./ Consumer Cyclical/ Auto & Truck Dealerships
ANDE/ Andersons Inc./ Consumer Defensive/ Food Distribution
ANET/ Arista Networks Inc/ Technology/ Computer Hardware
ANF/ Abercrombie & Fitch Co./ Consumer Cyclical/ Apparel Retail
ANGI/ Angi Inc/ Communication Services/ Internet Content & Information
ANIP/ ANI Pharmaceuticals Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
ANSS/ Ansys Inc./ Technology/ Software - Application
AON/ Aon plc./ Financial/ Insurance Brokers
AOS/ A.O. Smith Corp./ Industrials/ Specialty Industrial Machinery
APA/ APA Corporation/ Energy/ Oil & Gas E&P
APAM/ Artisan Partners Asset Management Inc/ Financial/ Asset Management
APD/ Air Products & Chemicals Inc./ Basic Materials/ Specialty Chemicals
APG/ APi Group Corporation/ Industrials/ Engineering & Construction
APGE/ Apogee Therapeutics Inc./ Healthcare/ Biotechnology
APH/ Amphenol Corp./ Technology/ Electronic Components
APLE/ Apple Hospitality REIT Inc/ Real Estate/ REIT - Hotel & Motel
APLS/ Apellis Pharmaceuticals Inc/ Healthcare/ Biotechnology
APO/ Apollo Global Management Inc/ Financial/ Asset Management
APOG/ Apogee Enterprises Inc./ Industrials/ Building Products & Equipment
APP/ Applovin Corp/ Technology/ Software - Application
APPF/ Appfolio Inc/ Technology/ Software - Application
APPN/ Appian Corp/ Technology/ Software - Infrastructure
APTV/ Aptiv PLC/ Consumer Cyclical/ Auto Parts
AQN/ Algonquin Power & Utilities Corp/ Utilities/ Utilities - Renewable
AQNU/ Algonquin Power & Utilities Corp/ Utilities/ Utilities - Renewable
AR/ Antero Resources Corp/ Energy/ Oil & Gas E&P
ARCB/ ArcBest Corp/ Industrials/ Trucking
ARCC/ Ares Capital Corporation/ Financial/ Asset Management
ARCH/ Arch Resources Inc/ Basic Materials/ Coking Coal
ARCO/ Arcos Dorados Holdings Inc/ Consumer Cyclical/ Restaurants
ARDX/ Ardelyx Inc/ Healthcare/ Biotechnology
ARE/ Alexandria Real Estate Equities Inc./ Real Estate/ REIT - Office
ARES/ Ares Management Corp/ Financial/ Asset Management
ARGX/ Argen X SE ADR/ Healthcare/ Biotechnology
ARHS/ Arhaus Inc/ Consumer Cyclical/ Home Improvement Retail
ARI/ Apollo Commercial Real Estate Finance Inc/ Real Estate/ REIT - Mortgage
ARLP/ Alliance Resource Partners/ / 
ARM/ Arm Holdings plc. ADR/ Technology/ Semiconductors
ARMK/ Aramark/ Industrials/ Specialty Business Services
AROC/ Archrock Inc/ Energy/ Oil & Gas Equipment & Services
ARRY/ Array Technologies Inc/ Technology/ Solar
ARVN/ Arvinas Inc/ Healthcare/ Biotechnology
ARW/ Arrow Electronics Inc./ Technology/ Electronics & Computer Distribution
ARWR/ Arrowhead Pharmaceuticals Inc./ Healthcare/ Biotechnology
ASAN/ Asana Inc/ Technology/ Software - Application
ASB/ Associated Banc-Corp./ Financial/ Banks - Regional
ASGN/ ASGN Inc/ Technology/ Information Technology Services
ASH/ Ashland Inc/ Basic Materials/ Specialty Chemicals
ASML/ ASML Holding NV/ Technology/ Semiconductor Equipment & Materials
ASND/ Ascendis Pharma A/S ADR/ Healthcare/ Biotechnology
ASO/ Academy Sports and Outdoors Inc/ Consumer Cyclical/ Specialty Retail
ASPN/ Aspen Aerogels Inc./ Industrials/ Building Products & Equipment
ATEC/ Alphatec Holdings Inc/ Healthcare/ Medical Devices
ATGE/ Adtalem Global Education Inc/ Consumer Defensive/ Education & Training Services
ATI/ ATI Inc/ Industrials/ Metal Fabrication
ATKR/ Atkore Inc/ Industrials/ Electrical Equipment & Parts
ATMU/ Atmus Filtration Technologies Inc/ Industrials/ Pollution & Treatment Controls
ATO/ Atmos Energy Corp./ Utilities/ Utilities - Regulated Gas
ATR/ Aptargroup Inc./ Healthcare/ Medical Instruments & Supplies
ATRC/ Atricure Inc/ Healthcare/ Medical Instruments & Supplies
ATS/ ATS Corporation./ Industrials/ Specialty Industrial Machinery
ATSG/ Air Transport Services Group Inc/ Industrials/ Airlines
ATUS/ Altice USA Inc/ Communication Services/ Telecom Services
AU/ AngloGold Ashanti Plc./ Basic Materials/ Gold
AUB/ Atlantic Union Bankshares Corp/ Financial/ Banks - Regional
AUPH/ Aurinia Pharmaceuticals Inc/ Healthcare/ Biotechnology
AUR/ Aurora Innovation Inc/ Technology/ Information Technology Services
AUTL/ Autolus Therapeutics plc ADR/ Healthcare/ Biotechnology
AVA/ Avista Corp./ Utilities/ Utilities - Diversified
AVAV/ AeroVironment Inc./ Industrials/ Aerospace & Defense
AVB/ Avalonbay Communities Inc./ Real Estate/ REIT - Residential
AVDL/ Avadel Pharmaceuticals plc ADR/ Healthcare/ Drug Manufacturers - Specialty & Generic
AVDX/ AvidXchange Holdings Inc/ Technology/ Software - Infrastructure
AVGO/ Broadcom Inc/ Technology/ Semiconductors
AVNT/ Avient Corp/ Basic Materials/ Specialty Chemicals
AVPT/ AvePoint Inc/ Technology/ Software - Infrastructure
AVT/ Avnet Inc./ Technology/ Electronics & Computer Distribution
AVTR/ Avantor Inc./ Basic Materials/ Specialty Chemicals
AVY/ Avery Dennison Corp./ Consumer Cyclical/ Packaging & Containers
AWI/ Armstrong World Industries Inc./ Industrials/ Building Products & Equipment
AWK/ American Water Works Co. Inc./ Utilities/ Utilities - Regulated Water
AWR/ American States Water Co./ Utilities/ Utilities - Regulated Water
AX/ Axos Financial Inc./ Financial/ Banks - Regional
AXNX/ Axonics Inc/ Healthcare/ Medical Devices
AXON/ Axon Enterprise Inc/ Industrials/ Aerospace & Defense
AXP/ American Express Co./ Financial/ Credit Services
AXSM/ Axsome Therapeutics Inc/ Healthcare/ Biotechnology
AXTA/ Axalta Coating Systems Ltd/ Basic Materials/ Specialty Chemicals
AY/ Atlantica Sustainable Infrastructure Plc/ Utilities/ Utilities - Renewable
AYI/ Acuity Brands/ / 
AYX/ Alteryx Inc/ Technology/ Software - Application
AZEK/ AZEK Company Inc/ Industrials/ Building Products & Equipment
AZN/ Astrazeneca plc ADR/ Healthcare/ Drug Manufacturers - General
AZO/ Autozone Inc./ Consumer Cyclical/ Specialty Retail
AZPN/ Aspen Technology Inc/ Technology/ Software - Application
AZTA/ Azenta Inc/ Healthcare/ Medical Instruments & Supplies
AZZ/ AZZ Inc/ Industrials/ Specialty Business Services
B/ Barnes Group Inc./ Industrials/ Specialty Industrial Machinery
BA/ Boeing Co./ Industrials/ Aerospace & Defense
BAC/ Bank Of America Corp./ Financial/ Banks - Diversified
BAH/ Booz Allen Hamilton Holding Corp/ Industrials/ Consulting Services
BALL/ Ball Corp./ Consumer Cyclical/ Packaging & Containers
BAM/ Brookfield Asset Management Ltd/ Financial/ Asset Management
BANC/ Banc of California Inc/ Financial/ Banks - Regional
BANF/ Bancfirst Corp./ Financial/ Banks - Regional
BANR/ Banner Corp./ Financial/ Banks - Regional
BASE/ Couchbase Inc/ Technology/ Software - Infrastructure
BATRA/ Atlanta Braves Holdings Inc/ Communication Services/ Entertainment
BATRK/ Atlanta Braves Holdings Inc/ Communication Services/ Entertainment
BAX/ Baxter International Inc./ Healthcare/ Medical Instruments & Supplies
BB/ BlackBerry Ltd/ Technology/ Software - Infrastructure
BBIO/ BridgeBio Pharma Inc/ Healthcare/ Biotechnology
BBU/ Brookfield Business Partners L.P./ Industrials/ Conglomerates
BBUC/ Brookfield Business Corp/ Financial/ Asset Management
BBVA/ Banco Bilbao Vizcaya Argentaria. ADR/ Financial/ Banks - Diversified
BBWI/ Bath & Body Works Inc/ Consumer Cyclical/ Specialty Retail
BBY/ Best Buy Co. Inc./ Consumer Cyclical/ Specialty Retail
BC/ Brunswick Corp./ Consumer Cyclical/ Recreational Vehicles
BCC/ Boise Cascade Co/ Basic Materials/ Building Materials
BCE/ BCE Inc/ Communication Services/ Telecom Services
BCO/ Brink's Co./ Industrials/ Security & Protection Services
BCPC/ Balchem Corp./ Basic Materials/ Specialty Chemicals
BCRX/ Biocryst Pharmaceuticals Inc./ Healthcare/ Biotechnology
BCS/ Barclays plc ADR/ Financial/ Banks - Diversified
BCSF/ Bain Capital Specialty Finance Inc/ Financial/ Asset Management
BDC/ Belden Inc/ Technology/ Communication Equipment
BDX/ Becton Dickinson & Co./ Healthcare/ Medical Instruments & Supplies
BE/ Bloom Energy Corp/ Industrials/ Electrical Equipment & Parts
BEAM/ Beam Therapeutics Inc/ Healthcare/ Biotechnology
BECN/ Beacon Roofing Supply Inc/ Industrials/ Industrial Distribution
BEN/ Franklin Resources/ / 
BEPC/ Brookfield Renewable Corporation/ Utilities/ Utilities - Renewable
BERY/ Berry Global Group Inc/ Consumer Cyclical/ Packaging & Containers
BF-A/ Brown-Forman Corp./ Consumer Defensive/ Beverages - Wineries & Distilleries
BF-B/ Brown-Forman Corp./ Consumer Defensive/ Beverages - Wineries & Distilleries
BFAM/ Bright Horizons Family Solutions/ / 
BFH/ Bread Financial Holdings Inc/ Financial/ Credit Services
BG/ Bunge Global SA/ Consumer Defensive/ Farm Products
BGC/ BGC Group Inc/ Financial/ Capital Markets
BHC/ Bausch Health Companies Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
BHF/ Brighthouse Financial Inc/ Financial/ Insurance - Life
BHLB/ Berkshire Hills Bancorp Inc./ Financial/ Banks - Regional
BHVN/ Biohaven Ltd/ Healthcare/ Biotechnology
BIIB/ Biogen Inc/ Healthcare/ Drug Manufacturers - General
BILL/ BILL Holdings Inc/ Technology/ Software - Application
BIO/ Bio-Rad Laboratories Inc./ Healthcare/ Medical Devices
BIPC/ Brookfield Infrastructure Corp/ Utilities/ Utilities - Regulated Gas
BIRK/ Birkenstock Holding Plc/ Consumer Cyclical/ Footwear & Accessories
BJ/ BJ's Wholesale Club Holdings Inc/ Consumer Defensive/ Discount Stores
BK/ Bank Of New York Mellon Corp/ Financial/ Asset Management
BKD/ Brookdale Senior Living Inc/ Healthcare/ Medical Care Facilities
BKE/ Buckle/ / 
BKH/ Black Hills Corporation/ Utilities/ Utilities - Diversified
BKNG/ Booking Holdings Inc/ Consumer Cyclical/ Travel Services
BKR/ Baker Hughes Co/ Energy/ Oil & Gas Equipment & Services
BKU/ BankUnited Inc/ Financial/ Banks - Regional
BL/ BlackLine Inc/ Technology/ Software - Application
BLCO/ Bausch + Lomb Corp/ Healthcare/ Medical Instruments & Supplies
BLD/ TopBuild Corp/ Industrials/ Engineering & Construction
BLDP/ Ballard Power Systems Inc./ Industrials/ Specialty Industrial Machinery
BLDR/ Builders Firstsource Inc/ Industrials/ Building Products & Equipment
BLK/ Blackrock Inc./ Financial/ Asset Management
BLKB/ Blackbaud Inc/ Technology/ Software - Application
BLMN/ Bloomin Brands Inc/ Consumer Cyclical/ Restaurants
BLTE/ Belite Bio Inc ADR/ Healthcare/ Biotechnology
BMBL/ Bumble Inc/ Technology/ Software - Application
BMI/ Badger Meter Inc./ Technology/ Scientific & Technical Instruments
BMO/ Bank of Montreal/ Financial/ Banks - Diversified
BMRN/ Biomarin Pharmaceutical Inc./ Healthcare/ Biotechnology
BMY/ Bristol-Myers Squibb Co./ Healthcare/ Drug Manufacturers - General
BN/ Brookfield Corporation/ Financial/ Asset Management
BNL/ Broadstone Net Lease Inc/ Real Estate/ REIT - Diversified
BNS/ Bank Of Nova Scotia/ Financial/ Banks - Diversified
BNTX/ BioNTech SE ADR/ Healthcare/ Biotechnology
BODY/ Beachbody Company Inc/ Communication Services/ Internet Content & Information
BOH/ Bank of Hawaii Corp./ Financial/ Banks - Regional
BOKF/ BOK Financial Corp./ Financial/ Banks - Regional
BOOT/ Boot Barn Holdings Inc/ Consumer Cyclical/ Apparel Retail
BOWL/ Bowlero Corp/ Consumer Cyclical/ Leisure
BOX/ Box Inc/ Technology/ Software - Infrastructure
BP/ BP plc ADR/ Energy/ Oil & Gas Integrated
BPMC/ Blueprint Medicines Corp/ Healthcare/ Biotechnology
BPOP/ Popular Inc./ Financial/ Banks - Regional
BR/ Broadridge Financial Solutions/ / 
BRBR/ Bellring Brands Inc/ Consumer Defensive/ Packaged Foods
BRC/ Brady Corp./ Industrials/ Security & Protection Services
BRK-A/ Berkshire Hathaway Inc./ Financial/ Insurance - Diversified
BRK-B/ Berkshire Hathaway Inc./ Financial/ Insurance - Diversified
BRKR/ Bruker Corp/ Healthcare/ Medical Devices
BRO/ Brown & Brown/ / 
BROS/ Dutch Bros Inc/ Consumer Cyclical/ Restaurants
BRP/ BRP Group Inc/ Financial/ Insurance Brokers
BRX/ Brixmor Property Group Inc/ Real Estate/ REIT - Retail
BRZE/ Braze Inc/ Technology/ Software - Application
BSM/ Black Stone Minerals/ / 
BSX/ Boston Scientific Corp./ Healthcare/ Medical Devices
BSY/ Bentley Systems Inc/ Technology/ Software - Application
BTE/ Baytex Energy Corp/ Energy/ Oil & Gas E&P
BTG/ B2gold Corp/ Basic Materials/ Gold
BTI/ British American Tobacco Plc ADR/ Consumer Defensive/ Tobacco
BTU/ Peabody Energy Corp./ Energy/ Thermal Coal
BUD/ Anheuser-Busch InBev SA/NV ADR/ Consumer Defensive/ Beverages - Brewers
BUR/ Burford Capital Limited/ Financial/ Asset Management
BURL/ Burlington Stores Inc/ Consumer Cyclical/ Apparel Retail
BUSE/ First Busey Corp./ Financial/ Banks - Regional
BVH/ Bluegreen Vacations Holding Corporation/ Consumer Cyclical/ Resorts & Casinos
BWA/ BorgWarner Inc/ Consumer Cyclical/ Auto Parts
BWXT/ BWX Technologies Inc/ Industrials/ Aerospace & Defense
BX/ Blackstone Inc/ Financial/ Asset Management
BXMT/ Blackstone Mortgage Trust Inc/ Real Estate/ REIT - Mortgage
BXP/ Boston Properties/ / 
BXSL/ Blackstone Secured Lending Fund/ Financial/ Asset Management
BYD/ Boyd Gaming Corp./ Consumer Cyclical/ Resorts & Casinos
BYON/ Beyond Inc/ Consumer Cyclical/ Internet Retail
C/ Citigroup Inc/ Financial/ Banks - Diversified
CAAP/ Corporacion America Airports S.A./ Industrials/ Airports & Air Services
CABA/ Cabaletta Bio Inc/ Healthcare/ Biotechnology
CABO/ Cable One Inc/ Communication Services/ Telecom Services
CACC/ Credit Acceptance Corp./ Financial/ Credit Services
CACI/ Caci International Inc./ Technology/ Information Technology Services
CADE/ Cadence Bank/ Financial/ Banks - Regional
CAE/ Cae Inc./ Industrials/ Aerospace & Defense
CAG/ Conagra Brands Inc/ Consumer Defensive/ Packaged Foods
CAH/ Cardinal Health/ / 
CAKE/ Cheesecake Factory Inc./ Consumer Cyclical/ Restaurants
CAL/ Caleres Inc/ Consumer Cyclical/ Apparel Retail
CALM/ Cal-Maine Foods/ / 
CALX/ Calix Inc/ Technology/ Software - Application
CAR/ Avis Budget Group Inc/ Industrials/ Rental & Leasing Services
CARG/ CarGurus Inc/ Consumer Cyclical/ Auto & Truck Dealerships
CARR/ Carrier Global Corp/ Industrials/ Building Products & Equipment
CARS/ Cars.com/ Consumer Cyclical/ Auto & Truck Dealerships
CART/ Maplebear Inc./ Consumer Cyclical/ Internet Retail
CASH/ Pathward Financial Inc/ Financial/ Banks - Regional
CASY/ Casey's General Stores/ / 
CAT/ Caterpillar Inc./ Industrials/ Farm & Heavy Construction Machinery
CATY/ Cathay General Bancorp/ Financial/ Banks - Regional
CAVA/ Cava Group Inc/ Consumer Cyclical/ Restaurants
CB/ Chubb Limited/ Financial/ Insurance - Property & Casualty
CBAY/ Cymabay Therapeutics Inc/ Healthcare/ Biotechnology
CBOE/ Cboe Global Markets Inc./ Financial/ Financial Data & Stock Exchanges
CBRE/ CBRE Group Inc/ Real Estate/ Real Estate Services
CBRL/ Cracker Barrel Old Country Store Inc/ Consumer Cyclical/ Restaurants
CBSH/ Commerce Bancshares/ / 
CBT/ Cabot Corp./ Basic Materials/ Specialty Chemicals
CBU/ Community Bank System/ / 
CBZ/ Cbiz Inc/ Industrials/ Specialty Business Services
CC/ Chemours Company/ Basic Materials/ Specialty Chemicals
CCCS/ CCC Intelligent Solutions Holdings Inc/ Technology/ Software - Infrastructure
CCEP/ Coca-Cola Europacific Partners Plc/ Consumer Defensive/ Beverages - Non-Alcoholic
CCI/ Crown Castle Inc/ Real Estate/ REIT - Specialty
CCJ/ Cameco Corp./ Energy/ Uranium
CCK/ Crown Holdings/ / 
CCL/ Carnival Corp./ Consumer Cyclical/ Travel Services
CCOI/ Cogent Communications Holdings Inc/ Communication Services/ Telecom Services
CCS/ Century Communities Inc/ Consumer Cyclical/ Residential Construction
CDAY/ Ceridian HCM Holding Inc./ Technology/ Software - Application
CDE/ Coeur Mining Inc/ Basic Materials/ Gold
CDLR/ Cadeler AS ADR/ Industrials/ Marine Shipping
CDNS/ Cadence Design Systems/ / 
CDP/ COPT Defense Properties/ Real Estate/ REIT - Office
CDRE/ Cadre Holdings Inc/ Industrials/ Aerospace & Defense
CDW/ CDW Corp/ Technology/ Information Technology Services
CE/ Celanese Corp/ Basic Materials/ Chemicals
CEF/ Sprott Physical Gold and Silver Trust/ Financial/ Asset Management
CEG/ Constellation Energy Corporation/ Utilities/ Utilities - Renewable
CEIX/ Consol Energy Inc/ Energy/ Thermal Coal
CELH/ Celsius Holdings Inc/ Consumer Defensive/ Beverages - Non-Alcoholic
CENT/ Central Garden & Pet Co./ Consumer Defensive/ Packaged Foods
CENTA/ Central Garden & Pet Co./ Consumer Defensive/ Packaged Foods
CENX/ Century Aluminum Co./ Basic Materials/ Aluminum
CERE/ Cerevel Therapeutics Holdings Inc/ Healthcare/ Biotechnology
CERT/ Certara Inc/ Healthcare/ Health Information Services
CF/ CF Industries Holdings Inc/ Basic Materials/ Agricultural Inputs
CFG/ Citizens Financial Group Inc/ Financial/ Banks - Regional
CFLT/ Confluent Inc/ Technology/ Software - Infrastructure
CFR/ Cullen Frost Bankers Inc./ Financial/ Banks - Regional
CG/ Carlyle Group Inc/ Financial/ Asset Management
CGAU/ Centerra Gold Inc./ Basic Materials/ Gold
CGNX/ Cognex Corp./ Technology/ Scientific & Technical Instruments
CHCO/ City Holding Co./ Financial/ Banks - Regional
CHD/ Church & Dwight Co./ / 
CHDN/ Churchill Downs/ / 
CHE/ Chemed Corp./ Healthcare/ Medical Care Facilities
CHEF/ Chefs' Warehouse Inc/ Consumer Defensive/ Food Distribution
CHGG/ Chegg Inc/ Consumer Defensive/ Education & Training Services
CHH/ Choice Hotels International/ / 
CHK/ Chesapeake Energy Corp./ Energy/ Oil & Gas E&P
CHRD/ Chord Energy Corp/ Energy/ Oil & Gas E&P
CHRW/ C.H. Robinson Worldwide/ / 
CHTR/ Charter Communications Inc./ Communication Services/ Telecom Services
CHWY/ Chewy Inc/ Consumer Cyclical/ Internet Retail
CHX/ ChampionX Corp./ Energy/ Oil & Gas Equipment & Services
CI/ Cigna Group/ Healthcare/ Healthcare Plans
CIEN/ CIENA Corp./ Technology/ Communication Equipment
CIGI/ Colliers International Group Inc/ Real Estate/ Real Estate Services
CIM/ Chimera Investment Corp/ Real Estate/ REIT - Mortgage
CINF/ Cincinnati Financial Corp./ Financial/ Insurance - Property & Casualty
CIVI/ Civitas Resources Inc/ Energy/ Oil & Gas E&P
CL/ Colgate-Palmolive Co./ Consumer Defensive/ Household & Personal Products
CLBK/ Columbia Financial/ / 
CLDX/ Celldex Therapeutics Inc./ Healthcare/ Biotechnology
CLF/ Cleveland-Cliffs Inc/ Basic Materials/ Steel
CLH/ Clean Harbors/ / 
CLMT/ Calumet Specialty Products Partners L.P./ Energy/ Oil & Gas E&P
CLS/ Celestica/ / 
CLSK/ Cleanspark Inc/ Financial/ Capital Markets
CLVT/ Clarivate Plc/ Technology/ Information Technology Services
CLX/ Clorox Co./ Consumer Defensive/ Household & Personal Products
CM/ Canadian Imperial Bank Of Commerce/ Financial/ Banks - Diversified
CMA/ Comerica/ / 
CMC/ Commercial Metals Co./ Basic Materials/ Steel
CMCO/ Columbus Mckinnon Corp./ Industrials/ Farm & Heavy Construction Machinery
CMCSA/ Comcast Corp/ Communication Services/ Telecom Services
CME/ CME Group Inc/ Financial/ Financial Data & Stock Exchanges
CMG/ Chipotle Mexican Grill/ Consumer Cyclical/ Restaurants
CMI/ Cummins Inc./ Industrials/ Specialty Industrial Machinery
CMPR/ Cimpress plc/ Communication Services/ Advertising Agencies
CMS/ CMS Energy Corporation/ Utilities/ Utilities - Regulated Electric
CMTG/ Claros Mortgage Trust Inc/ Real Estate/ REIT - Mortgage
CNA/ CNA Financial Corp./ Financial/ Insurance - Property & Casualty
CNC/ Centene Corp./ Healthcare/ Healthcare Plans
CNHI/ CNH Industrial NV/ Industrials/ Farm & Heavy Construction Machinery
CNI/ Canadian National Railway Co./ Industrials/ Railroads
CNK/ Cinemark Holdings Inc/ Communication Services/ Entertainment
CNM/ Core & Main Inc/ Industrials/ Industrial Distribution
CNMD/ Conmed Corp./ Healthcare/ Medical Devices
CNNE/ Cannae Holdings Inc/ Consumer Cyclical/ Restaurants
CNO/ CNO Financial Group Inc/ Financial/ Insurance - Life
CNP/ Centerpoint Energy Inc./ Utilities/ Utilities - Regulated Electric
CNQ/ Canadian Natural Resources Ltd./ Energy/ Oil & Gas E&P
CNS/ Cohen & Steers Inc./ Financial/ Asset Management
CNX/ CNX Resources Corp/ Energy/ Oil & Gas E&P
CNXC/ Concentrix Corp./ Technology/ Information Technology Services
CNXN/ PC Connection/ / 
COCO/ Vita Coco Company Inc/ Consumer Defensive/ Beverages - Non-Alcoholic
CODI/ Compass Diversified Holdings/ Industrials/ Conglomerates
COF/ Capital One Financial Corp./ Financial/ Credit Services
COHR/ Coherent Corp/ Technology/ Scientific & Technical Instruments
COHU/ Cohu/ / 
COIN/ Coinbase Global Inc/ Financial/ Financial Data & Stock Exchanges
COKE/ Coca-Cola Consolidated Inc/ Consumer Defensive/ Beverages - Non-Alcoholic
COLB/ Columbia Banking System/ / 
COLD/ Americold Realty Trust Inc/ Real Estate/ REIT - Industrial
COLL/ Collegium Pharmaceutical Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
COLM/ Columbia Sportswear Co./ Consumer Cyclical/ Apparel Manufacturing
COMP/ Compass Inc/ Real Estate/ Real Estate Services
COO/ Cooper Companies/ / 
COOP/ Mr. Cooper Group Inc/ Financial/ Mortgage Finance
COP/ Conoco Phillips/ Energy/ Oil & Gas E&P
COR/ Cencora Inc./ Healthcare/ Medical Distribution
CORT/ Corcept Therapeutics Inc/ Healthcare/ Biotechnology
COST/ Costco Wholesale Corp/ Consumer Defensive/ Discount Stores
COTY/ Coty Inc/ Consumer Defensive/ Household & Personal Products
COUR/ Coursera Inc/ Consumer Defensive/ Education & Training Services
CP/ Canadian Pacific Kansas City Limited/ Industrials/ Railroads
CPB/ Campbell Soup Co./ Consumer Defensive/ Packaged Foods
CPE/ Callon Petroleum Co./ Energy/ Oil & Gas E&P
CPG/ Crescent Point Energy Corp/ Energy/ Oil & Gas E&P
CPK/ Chesapeake Utilities Corp/ Utilities/ Utilities - Regulated Gas
CPNG/ Coupang Inc/ Consumer Cyclical/ Internet Retail
CPRI/ Capri Holdings Ltd/ Consumer Cyclical/ Luxury Goods
CPRT/ Copart/ / 
CPRX/ Catalyst Pharmaceuticals Inc/ Healthcare/ Biotechnology
CPT/ Camden Property Trust/ Real Estate/ REIT - Residential
CQP/ Cheniere Energy Partners LP/ Energy/ Oil & Gas Midstream
CR/ Crane Co/ Industrials/ Specialty Industrial Machinery
CRBG/ Corebridge Financial Inc./ Financial/ Asset Management
CRC/ California Resources Corporation/ Energy/ Oil & Gas E&P
CRCT/ Cricut Inc/ Technology/ Computer Hardware
CRGY/ Crescent Energy Co./ Energy/ Oil & Gas E&P
CRH/ CRH Plc/ Basic Materials/ Building Materials
CRI/ Carters Inc/ Consumer Cyclical/ Apparel Retail
CRK/ Comstock Resources/ / 
CRL/ Charles River Laboratories International Inc./ Healthcare/ Diagnostics & Research
CRM/ Salesforce Inc/ Technology/ Software - Application
CRNX/ Crinetics Pharmaceuticals Inc/ Healthcare/ Biotechnology
CROX/ Crocs Inc/ Consumer Cyclical/ Footwear & Accessories
CRS/ Carpenter Technology Corp./ Industrials/ Metal Fabrication
CRSP/ CRISPR Therapeutics AG/ Healthcare/ Biotechnology
CRSR/ Corsair Gaming Inc/ Technology/ Computer Hardware
CRTO/ Criteo S.A ADR/ Communication Services/ Advertising Agencies
CRUS/ Cirrus Logic/ / 
CRVL/ Corvel Corp./ Financial/ Insurance Brokers
CRWD/ Crowdstrike Holdings Inc/ Technology/ Software - Infrastructure
CSCO/ Cisco Systems/ / 
CSGP/ Costar Group/ / 
CSGS/ CSG Systems International Inc./ Technology/ Software - Infrastructure
CSIQ/ Canadian Solar Inc/ Technology/ Solar
CSL/ Carlisle Companies Inc./ Industrials/ Building Products & Equipment
CSTM/ Constellium SE/ Basic Materials/ Aluminum
CSWC/ Capital Southwest Corp./ Financial/ Asset Management
CSWI/ CSW Industrials Inc/ Industrials/ Specialty Industrial Machinery
CSX/ CSX Corp./ Industrials/ Railroads
CTAS/ Cintas Corporation/ Industrials/ Specialty Business Services
CTKB/ Cytek BioSciences Inc/ Healthcare/ Medical Devices
CTLT/ Catalent Inc./ Healthcare/ Drug Manufacturers - Specialty & Generic
CTOS/ Custom Truck One Source Inc/ Industrials/ Rental & Leasing Services
CTRA/ Coterra Energy Inc/ Energy/ Oil & Gas E&P
CTRE/ CareTrust REIT Inc/ Real Estate/ REIT - Healthcare Facilities
CTS/ CTS Corp./ Technology/ Electronic Components
CTSH/ Cognizant Technology Solutions Corp./ Technology/ Information Technology Services
CTVA/ Corteva Inc/ Basic Materials/ Agricultural Inputs
CUBE/ CubeSmart/ Real Estate/ REIT - Industrial
CUBI/ Customers Bancorp Inc/ Financial/ Banks - Regional
CUK/ Carnival plc ADR/ Consumer Cyclical/ Travel Services
CUZ/ Cousins Properties Inc./ Real Estate/ REIT - Office
CVBF/ CVB Financial Corp./ Financial/ Banks - Regional
CVCO/ Cavco Industries Inc/ Consumer Cyclical/ Residential Construction
CVE/ Cenovus Energy Inc/ Energy/ Oil & Gas Integrated
CVI/ CVR Energy Inc/ Energy/ Oil & Gas Refining & Marketing
CVLT/ Commvault Systems Inc/ Technology/ Software - Application
CVNA/ Carvana Co./ Consumer Cyclical/ Auto & Truck Dealerships
CVS/ CVS Health Corp/ Healthcare/ Healthcare Plans
CVX/ Chevron Corp./ Energy/ Oil & Gas Integrated
CW/ Curtiss-Wright Corp./ Industrials/ Aerospace & Defense
CWAN/ Clearwater Analytics Holdings Inc/ Technology/ Software - Application
CWEN/ Clearway Energy Inc/ Utilities/ Utilities - Renewable
CWEN-A/ Clearway Energy Inc/ Utilities/ Utilities - Renewable
CWH/ Camping World Holdings Inc/ Consumer Cyclical/ Auto & Truck Dealerships
CWK/ Cushman & Wakefield plc/ Real Estate/ Real Estate Services
CWST/ Casella Waste Systems/ / 
CWT/ California Water Service Group/ Utilities/ Utilities - Regulated Water
CXM/ Sprinklr Inc/ Technology/ Software - Application
CXT/ Crane NXT Co/ Industrials/ Specialty Industrial Machinery
CXW/ CoreCivic Inc/ Industrials/ Security & Protection Services
CYTK/ Cytokinetics Inc/ Healthcare/ Biotechnology
CZR/ Caesars Entertainment Inc/ Consumer Cyclical/ Resorts & Casinos
D/ Dominion Energy Inc/ Utilities/ Utilities - Regulated Electric
DAC/ Danaos Corporation/ Industrials/ Marine Shipping
DAL/ Delta Air Lines/ / 
DAN/ Dana Inc/ Consumer Cyclical/ Auto Parts
DAR/ Darling Ingredients Inc/ Consumer Defensive/ Packaged Foods
DASH/ DoorDash Inc/ Communication Services/ Internet Content & Information
DAVA/ Endava plc ADR/ Technology/ Software - Infrastructure
DAWN/ Day One Biopharmaceuticals Inc/ Healthcare/ Biotechnology
DB/ Deutsche Bank AG/ Financial/ Banks - Regional
DBD/ Diebold Nixdorf Inc/ Technology/ Software - Application
DBRG/ DigitalBridge Group Inc/ Real Estate/ Real Estate Services
DBX/ Dropbox Inc/ Technology/ Software - Infrastructure
DCBO/ Docebo Inc/ Technology/ Software - Application
DCI/ Donaldson Co. Inc./ Industrials/ Specialty Industrial Machinery
DCPH/ Deciphera Pharmaceuticals Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
DD/ DuPont de Nemours Inc/ Basic Materials/ Specialty Chemicals
DDOG/ Datadog Inc/ Technology/ Software - Application
DDS/ Dillard's Inc./ Consumer Cyclical/ Department Stores
DE/ Deere & Co./ Industrials/ Farm & Heavy Construction Machinery
DEA/ Easterly Government Properties Inc/ Real Estate/ REIT - Office
DECK/ Deckers Outdoor Corp./ Consumer Cyclical/ Footwear & Accessories
DEI/ Douglas Emmett Inc/ Real Estate/ REIT - Office
DELL/ Dell Technologies Inc/ Technology/ Computer Hardware
DEO/ Diageo plc ADR/ Consumer Defensive/ Beverages - Wineries & Distilleries
DFH/ Dream Finders Homes Inc/ Consumer Cyclical/ Residential Construction
DFIN/ Donnelley Financial Solutions Inc/ Financial/ Capital Markets
DFS/ Discover Financial Services/ Financial/ Credit Services
DG/ Dollar General Corp./ Consumer Defensive/ Discount Stores
DGX/ Quest Diagnostics/ / 
DH/ Definitive Healthcare Corp/ Healthcare/ Health Information Services
DHI/ D.R. Horton Inc./ Consumer Cyclical/ Residential Construction
DHR/ Danaher Corp./ Healthcare/ Diagnostics & Research
DINO/ HF Sinclair Corp./ Energy/ Oil & Gas Refining & Marketing
DIOD/ Diodes/ / 
DIS/ Walt Disney Co/ Communication Services/ Entertainment
DK/ Delek US Holdings Inc/ Energy/ Oil & Gas Refining & Marketing
DKL/ Delek Logistics Partners LP/ Energy/ Oil & Gas Refining & Marketing
DKNG/ DraftKings Inc./ Consumer Cyclical/ Gambling
DKS/ Dicks Sporting Goods/ / 
DLB/ Dolby Laboratories Inc/ Industrials/ Specialty Business Services
DLO/ DLocal Limited/ Technology/ Software - Infrastructure
DLR/ Digital Realty Trust Inc/ Real Estate/ REIT - Specialty
DLTR/ Dollar Tree Inc/ Consumer Defensive/ Discount Stores
DMLP/ Dorchester Minerals/ / 
DNA/ Ginkgo Bioworks Holdings Inc/ Healthcare/ Biotechnology
DNB/ Dun & Bradstreet Holdings Inc/ Financial/ Financial Data & Stock Exchanges
DNLI/ Denali Therapeutics Inc/ Healthcare/ Biotechnology
DNN/ Denison Mines Corp/ Energy/ Uranium
DNOW/ NOW Inc/ Energy/ Oil & Gas Equipment & Services
DNUT/ Krispy Kreme Inc/ Consumer Defensive/ Grocery Stores
DO/ Diamond Offshore Drilling/ / 
DOC/ Physicians Realty Trust/ Real Estate/ REIT - Healthcare Facilities
DOCN/ DigitalOcean Holdings Inc/ Technology/ Software - Infrastructure
DOCS/ Doximity Inc/ Healthcare/ Health Information Services
DOCU/ DocuSign Inc/ Technology/ Software - Application
DOLE/ Dole plc/ Consumer Defensive/ Farm Products
DOOO/ BRP Inc/ Consumer Cyclical/ Recreational Vehicles
DOOR/ Masonite International Corp/ Industrials/ Building Products & Equipment
DORM/ Dorman Products Inc/ Consumer Cyclical/ Auto Parts
DOV/ Dover Corp./ Industrials/ Specialty Industrial Machinery
DOW/ Dow Inc/ Basic Materials/ Chemicals
DOX/ Amdocs Ltd/ Technology/ Software - Infrastructure
DPZ/ Dominos Pizza Inc/ Consumer Cyclical/ Restaurants
DRH/ Diamondrock Hospitality Co./ Real Estate/ REIT - Hotel & Motel
DRI/ Darden Restaurants/ / 
DRS/ Leonardo DRS Inc./ Industrials/ Aerospace & Defense
DRVN/ Driven Brands Holdings Inc/ Consumer Cyclical/ Auto & Truck Dealerships
DSGR/ Distribution Solutions Group Inc/ Industrials/ Industrial Distribution
DSGX/ Descartes Systems Group Inc/ Technology/ Software - Application
DT/ Dynatrace Inc/ Technology/ Software - Application
DTE/ DTE Energy Co./ Utilities/ Utilities - Regulated Electric
DTM/ DT Midstream Inc/ Energy/ Oil & Gas Midstream
DUK/ Duke Energy Corp./ Utilities/ Utilities - Regulated Electric
DUOL/ Duolingo Inc/ Technology/ Software - Application
DV/ DoubleVerify Holdings Inc/ Technology/ Software - Application
DVA/ DaVita Inc/ Healthcare/ Medical Care Facilities
DVAX/ Dynavax Technologies Corp./ Healthcare/ Drug Manufacturers - Specialty & Generic
DVN/ Devon Energy Corp./ Energy/ Oil & Gas E&P
DXC/ DXC Technology Co/ Technology/ Information Technology Services
DXCM/ Dexcom Inc/ Healthcare/ Medical Devices
DY/ Dycom Industries/ / 
DYN/ Dyne Therapeutics Inc/ Healthcare/ Biotechnology
E/ Eni Spa ADR/ Energy/ Oil & Gas Integrated
EA/ Electronic Arts/ / 
EAT/ Brinker International/ / 
EBAY/ EBay Inc./ Consumer Cyclical/ Internet Retail
EBC/ Eastern Bankshares Inc./ Financial/ Banks - Regional
ECL/ Ecolab/ / 
ECPG/ Encore Capital Group/ / 
ECVT/ Ecovyst Inc/ Basic Materials/ Specialty Chemicals
ED/ Consolidated Edison/ / 
EDR/ Endeavor Group Holdings Inc/ Communication Services/ Entertainment
EE/ Excelerate Energy Inc/ Energy/ Oil & Gas Midstream
EEFT/ Euronet Worldwide Inc/ Technology/ Software - Infrastructure
EFSC/ Enterprise Financial Services Corp./ Financial/ Banks - Regional
EFX/ Equifax/ / 
EGO/ Eldorado Gold Corp./ Basic Materials/ Gold
EGP/ Eastgroup Properties/ / 
EHC/ Encompass Health Corp/ Healthcare/ Medical Care Facilities
EIX/ Edison International/ Utilities/ Utilities - Regulated Electric
EL/ Estee Lauder Cos./ / 
ELAN/ Elanco Animal Health Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
ELF/ e.l.f. Beauty Inc/ Consumer Defensive/ Household & Personal Products
ELME/ Elme Communities/ Real Estate/ REIT - Residential
ELS/ Equity Lifestyle Properties Inc./ Real Estate/ REIT - Residential
ELV/ Elevance Health Inc/ Healthcare/ Healthcare Plans
EMBC/ Embecta Corp/ Healthcare/ Medical Instruments & Supplies
EME/ Emcor Group/ / 
EMN/ Eastman Chemical Co/ Basic Materials/ Specialty Chemicals
EMR/ Emerson Electric Co./ Industrials/ Specialty Industrial Machinery
ENB/ Enbridge Inc/ Energy/ Oil & Gas Midstream
ENLC/ Enlink Midstream LLC/ Energy/ Oil & Gas Midstream
ENOV/ Enovis Corp/ Industrials/ Specialty Industrial Machinery
ENPH/ Enphase Energy Inc/ Technology/ Solar
ENR/ Energizer Holdings Inc/ Industrials/ Electrical Equipment & Parts
ENS/ Enersys/ Industrials/ Electrical Equipment & Parts
ENSG/ Ensign Group Inc/ Healthcare/ Medical Care Facilities
ENTG/ Entegris Inc/ Technology/ Semiconductor Equipment & Materials
ENV/ Envestnet Inc./ Technology/ Software - Application
ENVA/ Enova International Inc./ Financial/ Credit Services
ENVX/ Enovix Corporation/ Industrials/ Electrical Equipment & Parts
EOG/ EOG Resources/ / 
EPAC/ Enerpac Tool Group Corp/ Industrials/ Specialty Industrial Machinery
EPAM/ EPAM Systems Inc/ Technology/ Information Technology Services
EPC/ Edgewell Personal Care Co/ Consumer Defensive/ Household & Personal Products
EPD/ Enterprise Products Partners L P/ Energy/ Oil & Gas Midstream
EPR/ EPR Properties/ Real Estate/ REIT - Specialty
EPRT/ Essential Properties Realty Trust Inc/ Real Estate/ REIT - Diversified
EQC/ Equity Commonwealth/ Real Estate/ REIT - Office
EQH/ Equitable Holdings Inc/ Financial/ Insurance - Diversified
EQIX/ Equinix Inc/ Real Estate/ REIT - Specialty
EQNR/ Equinor ASA ADR/ Energy/ Oil & Gas Integrated
EQR/ Equity Residential Properties Trust/ Real Estate/ REIT - Residential
EQT/ EQT Corp/ Energy/ Oil & Gas E&P
EQX/ Equinox Gold Corp/ Basic Materials/ Gold
ERF/ Enerplus Corporation/ Energy/ Oil & Gas E&P
ERIC/ Telefonaktiebolaget L M Ericsson ADR/ Technology/ Communication Equipment
ERIE/ Erie Indemnity Co./ Financial/ Insurance Brokers
ERO/ Ero Copper Corp/ Basic Materials/ Copper
ES/ Eversource Energy/ Utilities/ Utilities - Regulated Electric
ESAB/ ESAB Corp/ Industrials/ Metal Fabrication
ESBA/ Empire State Realty OP LP/ Real Estate/ REIT - Office
ESE/ Esco Technologies/ / 
ESI/ Element Solutions Inc/ Basic Materials/ Specialty Chemicals
ESMT/ Engagesmart Inc/ Technology/ Software - Infrastructure
ESRT/ Empire State Realty Trust Inc/ Real Estate/ REIT - Diversified
ESS/ Essex Property Trust/ / 
ESTC/ Elastic N.V/ Technology/ Software - Application
ET/ Energy Transfer LP/ Energy/ Oil & Gas Midstream
ETN/ Eaton Corporation plc/ Industrials/ Specialty Industrial Machinery
ETNB/ 89bio Inc/ Healthcare/ Biotechnology
ETR/ Entergy Corp./ Utilities/ Utilities - Regulated Electric
ETRN/ Equitrans Midstream Corporation/ Energy/ Oil & Gas Midstream
ETSY/ Etsy Inc/ Consumer Cyclical/ Internet Retail
ETWO/ E2open Parent Holdings Inc/ Technology/ Software - Application
EURN/ Euronav NV/ Energy/ Oil & Gas Midstream
EVCM/ EverCommerce Inc/ Technology/ Software - Infrastructure
EVEX/ Eve Holding Inc/ Industrials/ Aerospace & Defense
EVH/ Evolent Health Inc/ Healthcare/ Health Information Services
EVO/ Evotec SE ADR/ Healthcare/ Drug Manufacturers - Specialty & Generic
EVR/ Evercore Inc/ Financial/ Capital Markets
EVRG/ Evergy Inc/ Utilities/ Utilities - Regulated Electric
EVTC/ Evertec Inc/ Technology/ Software - Infrastructure
EW/ Edwards Lifesciences Corp/ Healthcare/ Medical Devices
EWBC/ East West Bancorp/ / 
EXAS/ Exact Sciences Corp./ Healthcare/ Diagnostics & Research
EXC/ Exelon Corp./ Utilities/ Utilities - Regulated Electric
EXEL/ Exelixis Inc/ Healthcare/ Biotechnology
EXLS/ ExlService Holdings Inc/ Technology/ Information Technology Services
EXP/ Eagle Materials Inc./ Basic Materials/ Building Materials
EXPD/ Expeditors International Of Washington/ / 
EXPE/ Expedia Group Inc/ Consumer Cyclical/ Travel Services
EXPI/ eXp World Holdings Inc/ Real Estate/ Real Estate Services
EXPO/ Exponent Inc./ Industrials/ Engineering & Construction
EXR/ Extra Space Storage Inc./ Real Estate/ REIT - Industrial
EXTR/ Extreme Networks Inc./ Technology/ Communication Equipment
EYE/ National Vision Holdings Inc/ Consumer Cyclical/ Specialty Retail
F/ Ford Motor Co./ Consumer Cyclical/ Auto Manufacturers
FA/ First Advantage Corp./ Industrials/ Specialty Business Services
FAF/ First American Financial Corp/ Financial/ Insurance - Specialty
FANG/ Diamondback Energy Inc/ Energy/ Oil & Gas E&P
FAST/ Fastenal Co./ Industrials/ Industrial Distribution
FBIN/ Fortune Brands Innovations Inc/ Industrials/ Building Products & Equipment
FBK/ FB Financial Corp/ Financial/ Banks - Regional
FBNC/ First Bancorp/ Financial/ Banks - Regional
FBP/ First Bancorp PR/ Financial/ Banks - Regional
FBRT/ Franklin BSP Realty Trust Inc./ Real Estate/ REIT - Mortgage
FCF/ First Commonwealth Financial Corp./ Financial/ Banks - Regional
FCFS/ FirstCash Holdings Inc/ Financial/ Credit Services
FCN/ FTI Consulting Inc./ Industrials/ Consulting Services
FCNCA/ First Citizens Bancshares/ / 
FCPT/ Four Corners Property Trust Inc/ Real Estate/ REIT - Retail
FCX/ Freeport-McMoRan Inc/ Basic Materials/ Copper
FDP/ Fresh Del Monte Produce Inc/ Consumer Defensive/ Farm Products
FDS/ Factset Research Systems Inc./ Financial/ Financial Data & Stock Exchanges
FDX/ Fedex Corp/ Industrials/ Integrated Freight & Logistics
FE/ Firstenergy Corp./ Utilities/ Utilities - Regulated Electric
FELE/ Franklin Electric Co./ / 
FERG/ Ferguson Plc./ Industrials/ Industrial Distribution
FFBC/ First Financial Bancorp/ Financial/ Banks - Regional
FFIN/ First Financial Bankshares/ / 
FFIV/ F5 Inc/ Technology/ Software - Infrastructure
FG/ F&G Annuities & Life Inc/ Financial/ Insurance - Life
FHB/ First Hawaiian INC/ Financial/ Banks - Regional
FHI/ Federated Hermes Inc/ Financial/ Asset Management
FHN/ First Horizon Corporation/ Financial/ Banks - Regional
FI/ Fiserv/ / 
FIBK/ First Interstate BancSystem Inc./ Financial/ Banks - Regional
FICO/ Fair/ / 
FIGS/ Figs Inc/ Consumer Cyclical/ Apparel Manufacturing
FIS/ Fidelity National Information Services/ / 
FITB/ Fifth Third Bancorp/ Financial/ Banks - Regional
FIVE/ Five Below Inc/ Consumer Cyclical/ Specialty Retail
FIVN/ Five9 Inc/ Technology/ Software - Infrastructure
FIX/ Comfort Systems USA/ / 
FIZZ/ National Beverage Corp./ Consumer Defensive/ Beverages - Non-Alcoholic
FL/ Foot Locker Inc/ Consumer Cyclical/ Apparel Retail
FLEX/ Flex Ltd/ Technology/ Electronic Components
FLNC/ Fluence Energy Inc/ Utilities/ Utilities - Renewable
FLO/ Flowers Foods/ / 
FLR/ Fluor Corporation/ Industrials/ Engineering & Construction
FLS/ Flowserve Corp./ Industrials/ Specialty Industrial Machinery
FLT/ Fleetcor Technologies Inc/ Technology/ Software - Infrastructure
FLYW/ Flywire Corp/ Technology/ Software - Infrastructure
FMC/ FMC Corp./ Basic Materials/ Agricultural Inputs
FMS/ Fresenius Medical Care AG ADR/ Healthcare/ Medical Care Facilities
FNB/ F.N.B. Corp./ Financial/ Banks - Regional
FND/ Floor & Decor Holdings Inc/ Consumer Cyclical/ Home Improvement Retail
FNF/ Fidelity National Financial Inc/ Financial/ Insurance - Specialty
FNV/ Franco-Nevada Corporation/ Basic Materials/ Gold
FOLD/ Amicus Therapeutics Inc/ Healthcare/ Biotechnology
FOR/ Forestar Group Inc/ Real Estate/ Real Estate - Development
FORM/ FormFactor Inc./ Technology/ Semiconductors
FOUR/ Shift4 Payments Inc/ Technology/ Software - Infrastructure
FOX/ Fox Corporation/ Communication Services/ Entertainment
FOXA/ Fox Corporation/ Communication Services/ Entertainment
FOXF/ Fox Factory Holding Corp/ Consumer Cyclical/ Auto Parts
FR/ First Industrial Realty Trust/ / 
FRME/ First Merchants Corp./ Financial/ Banks - Regional
FROG/ JFrog Ltd/ Technology/ Software - Application
FRPT/ Freshpet Inc/ Consumer Defensive/ Packaged Foods
FRSH/ Freshworks Inc/ Technology/ Software - Application
FRT/ Federal Realty Investment Trust./ Real Estate/ REIT - Retail
FSK/ FS KKR Capital Corp./ Financial/ Asset Management
FSLR/ First Solar Inc/ Technology/ Solar
FSLY/ Fastly Inc/ Technology/ Software - Application
FSM/ Fortuna Silver Mines Inc./ Basic Materials/ Gold
FSS/ Federal Signal Corp./ Industrials/ Pollution & Treatment Controls
FSV/ FirstService Corp/ Real Estate/ Real Estate Services
FTAI/ FTAI Aviation Ltd/ Industrials/ Rental & Leasing Services
FTDR/ Frontdoor Inc./ Consumer Cyclical/ Personal Services
FTI/ TechnipFMC plc/ Energy/ Oil & Gas Equipment & Services
FTNT/ Fortinet Inc/ Technology/ Software - Infrastructure
FTRE/ Fortrea Holdings Inc/ Healthcare/ Biotechnology
FTS/ Fortis Inc./ Utilities/ Utilities - Regulated Electric
FTV/ Fortive Corp/ Technology/ Scientific & Technical Instruments
FUL/ H.B. Fuller Company/ Basic Materials/ Specialty Chemicals
FULT/ Fulton Financial Corp./ Financial/ Banks - Regional
FUN/ Cedar Fair L.P./ Consumer Cyclical/ Leisure
FWONA/ Liberty Media Corp./ Communication Services/ Entertainment
FWONK/ Liberty Media Corp./ Communication Services/ Entertainment
FWRD/ Forward Air Corp./ Industrials/ Integrated Freight & Logistics
FWRG/ First Watch Restaurant Group Inc/ Consumer Cyclical/ Restaurants
FYBR/ Frontier Communications Parent Inc/ Communication Services/ Telecom Services
GATX/ GATX Corp./ Industrials/ Rental & Leasing Services
GBCI/ Glacier Bancorp/ / 
GBDC/ Golub Capital BDC/ / 
GBTG/ Global Business Travel Group Inc/ Technology/ Software - Application
GBX/ Greenbrier Cos./ / 
GD/ General Dynamics Corp./ Industrials/ Aerospace & Defense
GDDY/ Godaddy Inc/ Technology/ Software - Infrastructure
GDEN/ Golden Entertainment Inc/ Consumer Cyclical/ Resorts & Casinos
GDRX/ GoodRx Holdings Inc/ Healthcare/ Health Information Services
GE/ General Electric Co./ Industrials/ Specialty Industrial Machinery
GEF/ Greif Inc/ Consumer Cyclical/ Packaging & Containers
GEF-B/ Greif Inc/ Consumer Cyclical/ Packaging & Containers
GEHC/ GE HealthCare Technologies Inc/ Healthcare/ Health Information Services
GEL/ Genesis Energy L.P./ Energy/ Oil & Gas Midstream
GEN/ Gen Digital Inc/ Technology/ Software - Infrastructure
GENI/ Genius Sports Limited/ Communication Services/ Internet Content & Information
GEO/ Geo Group/ / 
GERN/ Geron Corp./ Healthcare/ Biotechnology
GES/ Guess Inc./ Consumer Cyclical/ Apparel Retail
GETY/ Getty Images Holdings Inc/ Communication Services/ Internet Content & Information
GFF/ Griffon Corp./ Industrials/ Conglomerates
GFL/ GFL Environmental Inc./ Industrials/ Waste Management
GFS/ GlobalFoundries Inc/ Technology/ Semiconductors
GGG/ Graco Inc./ Industrials/ Specialty Industrial Machinery
GH/ Guardant Health Inc/ Healthcare/ Diagnostics & Research
GHC/ Graham Holdings Co./ Consumer Defensive/ Education & Training Services
GIB/ CGI Inc/ Technology/ Information Technology Services
GIC/ Global Industrial Co/ Industrials/ Industrial Distribution
GIII/ G-III Apparel Group Ltd./ Consumer Cyclical/ Apparel Manufacturing
GIL/ Gildan Activewear Inc/ Consumer Cyclical/ Apparel Manufacturing
GILD/ Gilead Sciences/ / 
GIS/ General Mills/ / 
GKOS/ Glaukos Corporation/ Healthcare/ Medical Devices
GL/ Globe Life Inc/ Financial/ Insurance - Life
GLOB/ Globant S.A./ Technology/ Information Technology Services
GLP/ Global Partners LP/ Energy/ Oil & Gas Midstream
GLPG/ Galapagos NV ADR/ Healthcare/ Biotechnology
GLPI/ Gaming and Leisure Properties Inc/ Real Estate/ REIT - Specialty
GLW/ Corning/ / 
GM/ General Motors Company/ Consumer Cyclical/ Auto Manufacturers
GMAB/ Genmab ADR/ Healthcare/ Biotechnology
GME/ Gamestop Corporation/ Consumer Cyclical/ Specialty Retail
GMED/ Globus Medical Inc/ Healthcare/ Medical Devices
GMS/ GMS Inc/ Industrials/ Building Products & Equipment
GNL/ Global Net Lease Inc/ Real Estate/ REIT - Diversified
GNRC/ Generac Holdings Inc/ Industrials/ Specialty Industrial Machinery
GNTX/ Gentex Corp./ Consumer Cyclical/ Auto Parts
GNW/ Genworth Financial Inc/ Financial/ Insurance - Life
GO/ Grocery Outlet Holding Corp/ Consumer Defensive/ Grocery Stores
GOGO/ Gogo Inc/ Communication Services/ Telecom Services
GOLD/ Barrick Gold Corp./ Basic Materials/ Gold
GOLF/ Acushnet Holdings Corp/ Consumer Cyclical/ Leisure
GOOG/ Alphabet Inc/ Communication Services/ Internet Content & Information
GOOGL/ Alphabet Inc/ Communication Services/ Internet Content & Information
GOOS/ Canada Goose Holdings Inc/ Consumer Cyclical/ Apparel Manufacturing
GPC/ Genuine Parts Co./ Consumer Cyclical/ Specialty Retail
GPCR/ Structure Therapeutics Inc ADR/ Healthcare/ Biotechnology
GPI/ Group 1 Automotive/ / 
GPK/ Graphic Packaging Holding Co/ Consumer Cyclical/ Packaging & Containers
GPN/ Global Payments/ / 
GPOR/ Gulfport Energy Corp./ Energy/ Oil & Gas E&P
GPRE/ Green Plains Inc/ Basic Materials/ Chemicals
GPS/ Gap/ / 
GRBK/ Green Brick Partners Inc/ Consumer Cyclical/ Residential Construction
GRFS/ Grifols SA ADR/ Healthcare/ Drug Manufacturers - General
GRMN/ Garmin Ltd/ Technology/ Scientific & Technical Instruments
GRND/ Grindr Inc/ Technology/ Software - Application
GS/ The Goldman Sachs Group/ / 
GSAT/ Globalstar Inc./ Communication Services/ Telecom Services
GSBD/ Goldman Sachs BDC/ / 
GSHD/ Goosehead Insurance Inc/ Financial/ Insurance - Diversified
GSK/ GSK Plc ADR/ Healthcare/ Drug Manufacturers - General
GSM/ Ferroglobe Plc/ Basic Materials/ Other Industrial Metals & Mining
GT/ Goodyear Tire & Rubber Co./ Consumer Cyclical/ Auto Parts
GTES/ Gates Industrial Corporation plc/ Industrials/ Specialty Industrial Machinery
GTLB/ Gitlab Inc/ Technology/ Software - Application
GTLS/ Chart Industries Inc/ Industrials/ Specialty Industrial Machinery
GTX/ Garrett Motion Inc/ Consumer Cyclical/ Auto Parts
GTY/ Getty Realty Corp./ Real Estate/ REIT - Retail
GVA/ Granite Construction Inc./ Industrials/ Engineering & Construction
GWRE/ Guidewire Software Inc/ Technology/ Software - Application
GWW/ W.W. Grainger Inc./ Industrials/ Industrial Distribution
GXO/ GXO Logistics Inc/ Industrials/ Integrated Freight & Logistics
GYRE/ Gyre Therapeutics Inc/ Healthcare/ Biotechnology
H/ Hyatt Hotels Corporation/ Consumer Cyclical/ Lodging
HAE/ Haemonetics Corp./ Healthcare/ Medical Instruments & Supplies
HAL/ Halliburton Co./ Energy/ Oil & Gas Equipment & Services
HALO/ Halozyme Therapeutics Inc./ Healthcare/ Biotechnology
HAS/ Hasbro/ / 
HASI/ Hannon Armstrong Sustainable Infrastructure capital Inc/ Real Estate/ REIT - Specialty
HAYW/ Hayward Holdings Inc/ Industrials/ Electrical Equipment & Parts
HBAN/ Huntington Bancshares/ / 
HBI/ Hanesbrands Inc/ Consumer Cyclical/ Apparel Manufacturing
HBM/ Hudbay Minerals Inc./ Basic Materials/ Copper
HCA/ HCA Healthcare Inc/ Healthcare/ Medical Care Facilities
HCC/ Warrior Met Coal Inc/ Basic Materials/ Coking Coal
HCP/ HashiCorp Inc/ Technology/ Software - Infrastructure
HD/ Home Depot/ / 
HE/ Hawaiian Electric Industries/ / 
HEES/ H&E Equipment Services Inc/ Industrials/ Rental & Leasing Services
HEI/ Heico Corp./ Industrials/ Aerospace & Defense
HEI-A/ Heico Corp./ Industrials/ Aerospace & Defense
HES/ Hess Corporation/ Energy/ Oil & Gas E&P
HESM/ Hess Midstream LP/ Energy/ Oil & Gas Midstream
HGV/ Hilton Grand Vacations Inc/ Consumer Cyclical/ Resorts & Casinos
HHH/ Howard Hughes Holdings Inc/ Real Estate/ Real Estate - Diversified
HI/ Hillenbrand Inc/ Industrials/ Specialty Industrial Machinery
HIG/ Hartford Financial Services Group Inc./ Financial/ Insurance - Property & Casualty
HII/ Huntington Ingalls Industries Inc/ Industrials/ Aerospace & Defense
HIMS/ Hims & Hers Health Inc/ Consumer Defensive/ Household & Personal Products
HIW/ Highwoods Properties/ / 
HL/ Hecla Mining Co./ Basic Materials/ Other Precious Metals & Mining
HLF/ Herbalife Ltd/ Consumer Defensive/ Packaged Foods
HLI/ Houlihan Lokey Inc/ Financial/ Capital Markets
HLIO/ Helios Technologies Inc/ Industrials/ Specialty Industrial Machinery
HLIT/ Harmonic/ / 
HLMN/ Hillman Solutions Corp/ Industrials/ Tools & Accessories
HLN/ Haleon plc ADR/ Healthcare/ Drug Manufacturers - Specialty & Generic
HLNE/ Hamilton Lane Inc/ Financial/ Asset Management
HLT/ Hilton Worldwide Holdings Inc/ Consumer Cyclical/ Lodging
HLX/ Helix Energy Solutions Group Inc/ Energy/ Oil & Gas Equipment & Services
HMN/ Horace Mann Educators Corp./ Financial/ Insurance - Property & Casualty
HNI/ HNI Corp./ Industrials/ Business Equipment & Supplies
HOG/ Harley-Davidson/ / 
HOLX/ Hologic/ / 
HOMB/ Home Bancshares Inc/ Financial/ Banks - Regional
HON/ Honeywell International Inc/ Industrials/ Conglomerates
HOOD/ Robinhood Markets Inc/ Financial/ Capital Markets
HOPE/ Hope Bancorp Inc/ Financial/ Banks - Regional
HP/ Helmerich & Payne/ / 
HPE/ Hewlett Packard Enterprise Co/ Technology/ Communication Equipment
HPK/ HighPeak Energy Inc/ Energy/ Oil & Gas E&P
HPP/ Hudson Pacific Properties Inc/ Real Estate/ REIT - Office
HPQ/ HP Inc/ Technology/ Computer Hardware
HQY/ Healthequity Inc/ Healthcare/ Health Information Services
HR/ Healthcare Realty Trust Inc/ Real Estate/ REIT - Healthcare Facilities
HRB/ H&R Block Inc./ Consumer Cyclical/ Personal Services
HRI/ Herc Holdings Inc/ Industrials/ Rental & Leasing Services
HRL/ Hormel Foods Corp./ Consumer Defensive/ Packaged Foods
HRMY/ Harmony Biosciences Holdings Inc/ Healthcare/ Biotechnology
HSBC/ HSBC Holdings plc ADR/ Financial/ Banks - Diversified
HSIC/ Henry Schein Inc./ Healthcare/ Medical Distribution
HST/ Host Hotels & Resorts Inc/ Real Estate/ REIT - Hotel & Motel
HSY/ Hershey Company/ Consumer Defensive/ Confectioners
HTGC/ Hercules Capital Inc/ Financial/ Asset Management
HTH/ Hilltop Holdings Inc/ Financial/ Banks - Regional
HTLD/ Heartland Express/ / 
HTLF/ Heartland Financial USA/ / 
HTZ/ Hertz Global Holdings Inc./ Industrials/ Rental & Leasing Services
HUBB/ Hubbell Inc./ Industrials/ Electrical Equipment & Parts
HUBG/ Hub Group/ / 
HUBS/ HubSpot Inc/ Technology/ Software - Application
HUM/ Humana Inc./ Healthcare/ Healthcare Plans
HUN/ Huntsman Corp/ Basic Materials/ Chemicals
HURN/ Huron Consulting Group Inc/ Industrials/ Consulting Services
HUT/ Hut 8 Corp/ Financial/ Capital Markets
HWC/ Hancock Whitney Corp./ Financial/ Banks - Regional
HWKN/ Hawkins Inc/ Basic Materials/ Specialty Chemicals
HWM/ Howmet Aerospace Inc/ Industrials/ Aerospace & Defense
HXL/ Hexcel Corp./ Industrials/ Aerospace & Defense
HY/ Hyster-Yale Materials Handling Inc/ Industrials/ Farm & Heavy Construction Machinery
IAC/ IAC Inc/ Communication Services/ Internet Content & Information
IAG/ Iamgold Corp./ Basic Materials/ Gold
IART/ Integra Lifesciences Holdings Corp/ Healthcare/ Medical Devices
IAS/ Integral Ad Science Holding Corp/ Communication Services/ Advertising Agencies
IBKR/ Interactive Brokers Group Inc/ Financial/ Capital Markets
IBM/ International Business Machines Corp./ Technology/ Information Technology Services
IBOC/ International Bancshares Corp./ Financial/ Banks - Regional
IBP/ Installed Building Products Inc/ Consumer Cyclical/ Residential Construction
IBRX/ ImmunityBio Inc/ Healthcare/ Biotechnology
IBTX/ Independent Bank Group Inc/ Financial/ Banks - Regional
ICE/ Intercontinental Exchange Inc/ Financial/ Financial Data & Stock Exchanges
ICFI/ ICF International/ / 
ICLR/ Icon Plc/ Healthcare/ Diagnostics & Research
ICUI/ ICU Medical/ / 
IDA/ Idacorp/ / 
IDCC/ Interdigital Inc/ Technology/ Software - Application
IDXX/ Idexx Laboratories/ / 
IDYA/ Ideaya Biosciences Inc/ Healthcare/ Biotechnology
IE/ Ivanhoe Electric Inc/ Basic Materials/ Copper
IEP/ Icahn Enterprises L P/ Energy/ Oil & Gas Refining & Marketing
IESC/ IES Holdings Inc/ Industrials/ Engineering & Construction
IEX/ Idex Corporation/ Industrials/ Specialty Industrial Machinery
IFF/ International Flavors & Fragrances Inc./ Basic Materials/ Specialty Chemicals
IGT/ International Game Technology PLC/ Consumer Cyclical/ Gambling
IHG/ Intercontinental Hotels Group ADR/ Consumer Cyclical/ Lodging
IHS/ IHS Holding Ltd/ Communication Services/ Telecom Services
IIPR/ Innovative Industrial Properties Inc/ Real Estate/ REIT - Industrial
ILMN/ Illumina Inc/ Healthcare/ Diagnostics & Research
IMCR/ Immunocore Holdings plc ADR/ Healthcare/ Biotechnology
IMGN/ Immunogen/ / 
IMKTA/ Ingles Markets/ / 
IMO/ Imperial Oil Ltd./ Energy/ Oil & Gas Integrated
IMVT/ Immunovant Inc/ Healthcare/ Biotechnology
INBX/ Inhibrx Inc/ Healthcare/ Biotechnology
INCY/ Incyte Corp./ Healthcare/ Biotechnology
INDB/ Independent Bank Corp./ Financial/ Banks - Regional
INDI/ Indie Semiconductor Inc/ Technology/ Semiconductor Equipment & Materials
INDV/ Indivior Plc/ Healthcare/ Drug Manufacturers - Specialty & Generic
INFA/ Informatica Inc/ Technology/ Software - Infrastructure
INFN/ Infinera Corp./ Technology/ Communication Equipment
ING/ ING Groep N.V. ADR/ Financial/ Banks - Diversified
INGR/ Ingredion Inc/ Consumer Defensive/ Packaged Foods
INSM/ Insmed Inc/ Healthcare/ Biotechnology
INSP/ Inspire Medical Systems Inc/ Healthcare/ Medical Devices
INST/ Instructure Holdings Inc/ Technology/ Software - Application
INSW/ International Seaways Inc/ Energy/ Oil & Gas Midstream
INTA/ Intapp Inc/ Technology/ Software - Application
INTC/ Intel Corp./ Technology/ Semiconductors
INTU/ Intuit Inc/ Technology/ Software - Application
INVA/ Innoviva Inc/ Healthcare/ Biotechnology
INVH/ Invitation Homes Inc/ Real Estate/ REIT - Residential
IONQ/ IonQ Inc/ Technology/ Computer Hardware
IONS/ Ionis Pharmaceuticals Inc/ Healthcare/ Biotechnology
IOSP/ Innospec Inc/ Basic Materials/ Specialty Chemicals
IOT/ Samsara Inc/ Technology/ Software - Infrastructure
IOVA/ Iovance Biotherapeutics Inc/ Healthcare/ Biotechnology
IP/ International Paper Co./ Consumer Cyclical/ Packaging & Containers
IPAR/ Inter Parfums/ / 
IPG/ Interpublic Group Of Cos./ / 
IPGP/ IPG Photonics Corp/ Technology/ Semiconductor Equipment & Materials
IQV/ IQVIA Holdings Inc/ Healthcare/ Diagnostics & Research
IR/ Ingersoll-Rand Inc/ Industrials/ Specialty Industrial Machinery
IRBT/ Irobot Corp/ Consumer Cyclical/ Furnishings
IRDM/ Iridium Communications Inc/ Communication Services/ Telecom Services
IRM/ Iron Mountain Inc./ Real Estate/ REIT - Specialty
IRON/ Disc Medicine Inc/ Healthcare/ Biotechnology
IRT/ Independence Realty Trust Inc/ Real Estate/ REIT - Residential
IRTC/ iRhythm Technologies Inc/ Healthcare/ Medical Devices
IRWD/ Ironwood Pharmaceuticals Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
ISRG/ Intuitive Surgical Inc/ Healthcare/ Medical Instruments & Supplies
IT/ Gartner/ / 
ITCI/ Intra-Cellular Therapies Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
ITGR/ Integer Holdings Corp/ Healthcare/ Medical Devices
ITRI/ Itron Inc./ Technology/ Scientific & Technical Instruments
ITT/ ITT Inc/ Industrials/ Specialty Industrial Machinery
ITW/ Illinois Tool Works/ / 
IVT/ InvenTrust Properties Corp/ Real Estate/ REIT - Retail
IVZ/ Invesco Ltd/ Financial/ Asset Management
IXHL/ Incannex Healthcare Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
J/ Jacobs Solutions Inc/ Industrials/ Engineering & Construction
JACK/ Jack In The Box/ / 
JAMF/ Jamf Holding Corp/ Technology/ Software - Application
JAZZ/ Jazz Pharmaceuticals plc/ Healthcare/ Biotechnology
JBGS/ JBG SMITH Properties/ Real Estate/ REIT - Office
JBHT/ J.B. Hunt Transport Services/ / 
JBI/ Janus International Group Inc/ Industrials/ Building Products & Equipment
JBL/ Jabil Inc/ Technology/ Electronic Components
JBLU/ Jetblue Airways Corp/ Industrials/ Airlines
JBSS/ Sanfilippo (John B.) & Son/ / 
JBT/ John Bean Technologies Corp/ Industrials/ Specialty Industrial Machinery
JCI/ Johnson Controls International plc/ Industrials/ Building Products & Equipment
JEF/ Jefferies Financial Group Inc/ Financial/ Capital Markets
JELD/ JELD-WEN Holding Inc./ Industrials/ Building Products & Equipment
JHG/ Janus Henderson Group plc/ Financial/ Asset Management
JHX/ James Hardie Industries plc ADR/ Basic Materials/ Building Materials
JJSF/ J&J Snack Foods Corp./ Consumer Defensive/ Packaged Foods
JKHY/ Jack Henry & Associates/ / 
JLL/ Jones Lang Lasalle Inc./ Real Estate/ Real Estate Services
JNJ/ Johnson & Johnson/ Healthcare/ Drug Manufacturers - General
JNPR/ Juniper Networks Inc/ Technology/ Communication Equipment
JOBY/ Joby Aviation Inc/ Industrials/ Airports & Air Services
JOE/ St. Joe Co./ Real Estate/ Real Estate - Diversified
JPM/ JPMorgan Chase & Co./ Financial/ Banks - Diversified
JWN/ Nordstrom/ / 
JXN/ Jackson Financial Inc/ Financial/ Insurance - Life
K/ Kellanova Co/ Consumer Defensive/ Packaged Foods
KAI/ Kadant/ / 
KALU/ Kaiser Aluminum Corp/ Basic Materials/ Aluminum
KAR/ Openlane Inc./ Consumer Cyclical/ Auto & Truck Dealerships
KBH/ KB Home/ Consumer Cyclical/ Residential Construction
KBR/ KBR Inc/ Industrials/ Engineering & Construction
KD/ Kyndryl Holdings Inc/ Technology/ Information Technology Services
KDP/ Keurig Dr Pepper Inc/ Consumer Defensive/ Beverages - Non-Alcoholic
KEX/ Kirby Corp./ Industrials/ Marine Shipping
KEY/ Keycorp/ Financial/ Banks - Regional
KEYS/ Keysight Technologies Inc/ Technology/ Scientific & Technical Instruments
KFRC/ Kforce Inc./ Industrials/ Staffing & Employment Services
KFY/ Korn Ferry/ Industrials/ Staffing & Employment Services
KGC/ Kinross Gold Corp./ Basic Materials/ Gold
KGS/ Kodiak Gas Services Inc/ Energy/ Oil & Gas Equipment & Services
KHC/ Kraft Heinz Co/ Consumer Defensive/ Packaged Foods
KIM/ Kimco Realty Corporation/ Real Estate/ REIT - Retail
KKR/ KKR & Co. Inc/ Financial/ Asset Management
KLAC/ KLA Corp./ Technology/ Semiconductor Equipment & Materials
KLG/ WK Kellogg Co/ Consumer Defensive/ Packaged Foods
KLIC/ Kulicke & Soffa Industries/ / 
KMB/ Kimberly-Clark Corp./ Consumer Defensive/ Household & Personal Products
KMI/ Kinder Morgan Inc/ Energy/ Oil & Gas Midstream
KMPR/ Kemper Corporation/ Financial/ Insurance - Property & Casualty
KMT/ Kennametal Inc./ Industrials/ Tools & Accessories
KMX/ Carmax Inc/ Consumer Cyclical/ Auto & Truck Dealerships
KN/ Knowles Corp/ Technology/ Communication Equipment
KNF/ Knife River Corp/ Basic Materials/ Building Materials
KNSA/ Kiniksa Pharmaceuticals Ltd/ Healthcare/ Biotechnology
KNSL/ Kinsale Capital Group Inc/ Financial/ Insurance - Property & Casualty
KNTK/ Kinetik Holdings Inc/ Energy/ Oil & Gas Midstream
KNX/ Knight-Swift Transportation Holdings Inc/ Industrials/ Trucking
KO/ Coca-Cola Co/ Consumer Defensive/ Beverages - Non-Alcoholic
KOS/ Kosmos Energy Ltd/ Energy/ Oil & Gas E&P
KR/ Kroger Co./ Consumer Defensive/ Grocery Stores
KRC/ Kilroy Realty Corp./ Real Estate/ REIT - Office
KRG/ Kite Realty Group Trust/ Real Estate/ REIT - Retail
KRO/ Kronos Worldwide/ / 
KROS/ Keros Therapeutics Inc/ Healthcare/ Biotechnology
KRP/ Kimbell Royalty Partners/ / 
KRTX/ Karuna Therapeutics Inc/ Healthcare/ Biotechnology
KRUS/ Kura Sushi USA Inc/ Consumer Cyclical/ Restaurants
KRYS/ Krystal Biotech Inc/ Healthcare/ Biotechnology
KSS/ Kohl's Corp./ Consumer Cyclical/ Department Stores
KTB/ Kontoor Brands Inc/ Consumer Cyclical/ Apparel Manufacturing
KTOS/ Kratos Defense & Security Solutions Inc/ Industrials/ Aerospace & Defense
KURA/ Kura Oncology Inc/ Healthcare/ Biotechnology
KVUE/ Kenvue Inc/ Consumer Defensive/ Household & Personal Products
KVYO/ Klaviyo Inc/ Technology/ Software - Infrastructure
KW/ Kennedy-Wilson Holdings Inc/ Real Estate/ Real Estate Services
KWR/ Quaker Houghton/ Basic Materials/ Specialty Chemicals
KYMR/ Kymera Therapeutics Inc/ Healthcare/ Biotechnology
L/ Loews Corp./ Financial/ Insurance - Property & Casualty
LAD/ Lithia Motors/ / 
LADR/ Ladder Capital Corp/ Real Estate/ REIT - Mortgage
LAMR/ Lamar Advertising Co/ Real Estate/ REIT - Specialty
LANC/ Lancaster Colony Corp./ Consumer Defensive/ Packaged Foods
LAUR/ Laureate Education Inc/ Consumer Defensive/ Education & Training Services
LAZ/ Lazard Inc./ Financial/ Capital Markets
LAZR/ Luminar Technologies Inc/ Consumer Cyclical/ Auto Parts
LBRDA/ Liberty Broadband Corp/ Communication Services/ Telecom Services
LBRDK/ Liberty Broadband Corp/ Communication Services/ Telecom Services
LBRT/ Liberty Energy Inc/ Energy/ Oil & Gas Equipment & Services
LCID/ Lucid Group Inc/ Consumer Cyclical/ Auto Manufacturers
LCII/ LCI Industries/ Consumer Cyclical/ Recreational Vehicles
LDOS/ Leidos Holdings Inc/ Technology/ Information Technology Services
LEA/ Lear Corp./ Consumer Cyclical/ Auto Parts
LECO/ Lincoln Electric Holdings/ / 
LEG/ Leggett & Platt/ / 
LEGN/ Legend Biotech Corp ADR/ Healthcare/ Biotechnology
LEN/ Lennar Corp./ Consumer Cyclical/ Residential Construction
LEN-B/ Lennar Corp./ Consumer Cyclical/ Residential Construction
LESL/ Leslies Inc/ Consumer Cyclical/ Specialty Retail
LEVI/ Levi Strauss & Co./ Consumer Cyclical/ Apparel Manufacturing
LFST/ LifeStance Health Group Inc/ Healthcare/ Medical Care Facilities
LFUS/ Littelfuse/ / 
LGF-A/ Lions Gate Entertainment Corp./ Communication Services/ Entertainment
LGF-B/ Lions Gate Entertainment Corp./ Communication Services/ Entertainment
LGIH/ LGI Homes Inc/ Consumer Cyclical/ Residential Construction
LGND/ Ligand Pharmaceuticals/ / 
LH/ Laboratory Corp. Of America Holdings/ Healthcare/ Diagnostics & Research
LHX/ L3Harris Technologies Inc/ Industrials/ Aerospace & Defense
LII/ Lennox International Inc/ Industrials/ Building Products & Equipment
LILA/ Liberty Latin America Ltd/ Communication Services/ Telecom Services
LILAK/ Liberty Latin America Ltd/ Communication Services/ Telecom Services
LIN/ Linde Plc./ Basic Materials/ Specialty Chemicals
LITE/ Lumentum Holdings Inc/ Technology/ Communication Equipment
LIVN/ LivaNova PLC/ Healthcare/ Medical Devices
LKFN/ Lakeland Financial Corp./ Financial/ Banks - Regional
LKQ/ LKQ Corp/ Consumer Cyclical/ Auto Parts
LLY/ Lilly(Eli) & Co/ Healthcare/ Drug Manufacturers - General
LLYVA/ Liberty Media Corp./ Communication Services/ Entertainment
LLYVK/ Liberty Media Corp./ Communication Services/ Entertainment
LMAT/ Lemaitre Vascular Inc/ Healthcare/ Medical Instruments & Supplies
LMND/ Lemonade Inc/ Financial/ Insurance - Property & Casualty
LMT/ Lockheed Martin Corp./ Industrials/ Aerospace & Defense
LNC/ Lincoln National Corp./ Financial/ Insurance - Life
LNG/ Cheniere Energy Inc./ Energy/ Oil & Gas Midstream
LNN/ Lindsay Corporation/ Industrials/ Farm & Heavy Construction Machinery
LNT/ Alliant Energy Corp./ Utilities/ Utilities - Regulated Electric
LNTH/ Lantheus Holdings Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
LNW/ Light & Wonder Inc/ Consumer Cyclical/ Gambling
LOB/ Live Oak Bancshares Inc/ Financial/ Banks - Regional
LOGI/ Logitech International S.A./ Technology/ Computer Hardware
LOPE/ Grand Canyon Education Inc/ Consumer Defensive/ Education & Training Services
LOW/ Lowe's Cos./ / 
LPG/ Dorian LPG Ltd/ Energy/ Oil & Gas Midstream
LPLA/ LPL Financial Holdings Inc/ Financial/ Capital Markets
LPX/ Louisiana-Pacific Corp./ Industrials/ Building Products & Equipment
LRCX/ Lam Research Corp./ Technology/ Semiconductor Equipment & Materials
LRN/ Stride Inc/ Consumer Defensive/ Education & Training Services
LSCC/ Lattice Semiconductor Corp./ Technology/ Semiconductors
LSPD/ Lightspeed Commerce Inc/ Technology/ Software - Application
LSTR/ Landstar System/ / 
LSXMA/ Liberty Media Corp./ Communication Services/ Entertainment
LSXMK/ Liberty Media Corp./ Communication Services/ Entertainment
LTC/ LTC Properties/ / 
LTH/ Life Time Group Holdings Inc/ Consumer Cyclical/ Leisure
LTHM/ Arcadium Lithium plc/ Basic Materials/ Specialty Chemicals
LULU/ Lululemon Athletica inc./ Consumer Cyclical/ Apparel Retail
LUMN/ Lumen Technologies Inc/ Communication Services/ Telecom Services
LUV/ Southwest Airlines Co/ Industrials/ Airlines
LVS/ Las Vegas Sands Corp/ Consumer Cyclical/ Resorts & Casinos
LVWR/ LiveWire Group Inc/ Consumer Cyclical/ Auto Manufacturers
LW/ Lamb Weston Holdings Inc/ Consumer Defensive/ Packaged Foods
LXP/ LXP Industrial Trust/ Real Estate/ REIT - Industrial
LYB/ LyondellBasell Industries NV/ Basic Materials/ Specialty Chemicals
LYFT/ Lyft Inc/ Technology/ Software - Application
LYG/ Lloyds Banking Group plc ADR/ Financial/ Banks - Regional
LYV/ Live Nation Entertainment Inc/ Communication Services/ Entertainment
LZ/ LegalZoom.com Inc./ Industrials/ Specialty Business Services
LZB/ La-Z-Boy Inc./ Consumer Cyclical/ Furnishings
M/ Macy's Inc/ Consumer Cyclical/ Department Stores
MA/ Mastercard Incorporated/ Financial/ Credit Services
MAA/ Mid-America Apartment Communities/ / 
MAC/ Macerich Co./ Real Estate/ REIT - Retail
MAG/ MAG Silver Corp./ Basic Materials/ Silver
MAIN/ Main Street Capital Corporation/ Financial/ Asset Management
MAN/ ManpowerGroup/ Industrials/ Staffing & Employment Services
MANH/ Manhattan Associates/ / 
MANU/ Manchester United Plc./ Communication Services/ Entertainment
MAR/ Marriott International/ / 
MARA/ Marathon Digital Holdings Inc/ Financial/ Capital Markets
MAS/ Masco Corp./ Industrials/ Building Products & Equipment
MASI/ Masimo Corp/ Healthcare/ Medical Devices
MAT/ Mattel/ / 
MATW/ Matthews International Corp./ Industrials/ Conglomerates
MATX/ Matson Inc/ Industrials/ Marine Shipping
MBC/ MasterBrand Inc/ Consumer Cyclical/ Furnishings
MBIN/ Merchants Bancorp/ Financial/ Banks - Regional
MBUU/ Malibu Boats Inc/ Consumer Cyclical/ Recreational Vehicles
MC/ Moelis & Co/ Financial/ Capital Markets
MCD/ McDonald's Corp/ Consumer Cyclical/ Restaurants
MCHP/ Microchip Technology/ / 
MCK/ Mckesson Corporation/ Healthcare/ Medical Distribution
MCO/ Moody's Corp./ Financial/ Financial Data & Stock Exchanges
MCRI/ Monarch Casino & Resort/ / 
MCW/ Mister Car Wash Inc/ Consumer Cyclical/ Personal Services
MCY/ Mercury General Corp./ Financial/ Insurance - Property & Casualty
MDB/ MongoDB Inc/ Technology/ Software - Infrastructure
MDC/ M.D.C. Holdings/ / 
MDGL/ Madrigal Pharmaceuticals Inc/ Healthcare/ Biotechnology
MDLZ/ Mondelez International Inc./ Consumer Defensive/ Confectioners
MDRX/ Veradigm Inc/ Healthcare/ Health Information Services
MDT/ Medtronic Plc/ Healthcare/ Medical Devices
MDU/ MDU Resources Group Inc/ Industrials/ Conglomerates
MEDP/ Medpace Holdings Inc/ Healthcare/ Diagnostics & Research
MELI/ MercadoLibre Inc/ Consumer Cyclical/ Internet Retail
MEOH/ Methanex Corp./ Basic Materials/ Chemicals
MET/ Metlife Inc/ Financial/ Insurance - Life
META/ Meta Platforms Inc/ Communication Services/ Internet Content & Information
METC/ Ramaco Resources Inc/ Basic Materials/ Coking Coal
MFA/ MFA Financial Inc/ Real Estate/ REIT - Mortgage
MFC/ Manulife Financial Corp./ Financial/ Insurance - Life
MGA/ Magna International Inc./ Consumer Cyclical/ Auto Parts
MGEE/ MGE Energy/ / 
MGM/ MGM Resorts International/ Consumer Cyclical/ Resorts & Casinos
MGNI/ Magnite Inc/ Communication Services/ Advertising Agencies
MGPI/ MGP Ingredients/ / 
MGRC/ McGrath Rentcorp/ Industrials/ Rental & Leasing Services
MGY/ Magnolia Oil & Gas Corp/ Energy/ Oil & Gas E&P
MHK/ Mohawk Industries/ / 
MHO/ MI Homes Inc./ Consumer Cyclical/ Residential Construction
MIDD/ Middleby Corp./ Industrials/ Specialty Industrial Machinery
MIR/ Mirion Technologies Inc./ Industrials/ Specialty Industrial Machinery
MIRM/ Mirum Pharmaceuticals Inc/ Healthcare/ Biotechnology
MKC/ McCormick & Co./ / 
MKL/ Markel Group Inc/ Financial/ Insurance - Property & Casualty
MKSI/ MKS Instruments/ / 
MKTX/ MarketAxess Holdings Inc./ Financial/ Capital Markets
MLI/ Mueller Industries/ / 
MLKN/ MillerKnoll Inc/ Consumer Cyclical/ Furnishings
MLM/ Martin Marietta Materials/ / 
MLNK/ MeridianLink Inc/ Technology/ Software - Application
MLTX/ MoonLake Immunotherapeutics/ Healthcare/ Biotechnology
MMC/ Marsh & McLennan Cos./ / 
MMI/ Marcus & Millichap Inc/ Real Estate/ Real Estate Services
MMM/ 3M Co./ Industrials/ Conglomerates
MMS/ Maximus Inc./ Industrials/ Specialty Business Services
MMSI/ Merit Medical Systems/ / 
MNR/ Mach Natural Resources LP/ Energy/ Oil & Gas E&P
MNST/ Monster Beverage Corp./ Consumer Defensive/ Beverages - Non-Alcoholic
MNTK/ Montauk Renewables Inc/ Utilities/ Utilities - Diversified
MO/ Altria Group Inc./ Consumer Defensive/ Tobacco
MOD/ Modine Manufacturing Co./ Consumer Cyclical/ Auto Parts
MODG/ Topgolf Callaway Brands Corp/ Consumer Cyclical/ Leisure
MODN/ Model N Inc/ Technology/ Software - Application
MOG-A/ Moog/ / 
MOH/ Molina Healthcare Inc/ Healthcare/ Healthcare Plans
MOR/ Morphosys AG ADR/ Healthcare/ Biotechnology
MORF/ Morphic Holding Inc/ Healthcare/ Biotechnology
MORN/ Morningstar Inc/ Financial/ Financial Data & Stock Exchanges
MOS/ Mosaic Company/ Basic Materials/ Agricultural Inputs
MP/ MP Materials Corporation/ Basic Materials/ Other Industrial Metals & Mining
MPC/ Marathon Petroleum Corp/ Energy/ Oil & Gas Refining & Marketing
MPLX/ MPLX LP/ Energy/ Oil & Gas Midstream
MPW/ Medical Properties Trust Inc/ Real Estate/ REIT - Healthcare Facilities
MPWR/ Monolithic Power System Inc/ Technology/ Semiconductors
MQ/ Marqeta Inc/ Technology/ Software - Infrastructure
MRCY/ Mercury Systems Inc/ Industrials/ Aerospace & Defense
MRK/ Merck & Co Inc/ Healthcare/ Drug Manufacturers - General
MRNA/ Moderna Inc/ Healthcare/ Biotechnology
MRO/ Marathon Oil Corporation/ Energy/ Oil & Gas E&P
MRTN/ Marten Transport/ / 
MRTX/ Mirati Therapeutics Inc/ Healthcare/ Biotechnology
MRUS/ Merus N.V/ Healthcare/ Biotechnology
MRVL/ Marvell Technology Inc/ Technology/ Semiconductors
MS/ Morgan Stanley/ Financial/ Capital Markets
MSA/ MSA Safety Inc/ Industrials/ Security & Protection Services
MSCI/ MSCI Inc/ Financial/ Financial Data & Stock Exchanges
MSEX/ Middlesex Water Co./ Utilities/ Utilities - Regulated Water
MSFT/ Microsoft Corporation/ Technology/ Software - Infrastructure
MSGE/ Madison Square Garden Entertainment Corp./ Consumer Cyclical/ Leisure
MSGS/ Madison Square Garden Sports Corp/ Communication Services/ Entertainment
MSI/ Motorola Solutions Inc/ Technology/ Communication Equipment
MSM/ MSC Industrial Direct Co./ / 
MSTR/ Microstrategy Inc./ Technology/ Software - Application
MT/ ArcelorMittal/ Basic Materials/ Steel
MTB/ M & T Bank Corp/ Financial/ Banks - Regional
MTCH/ Match Group Inc./ Communication Services/ Internet Content & Information
MTD/ Mettler-Toledo International/ / 
MTDR/ Matador Resources Co/ Energy/ Oil & Gas E&P
MTG/ MGIC Investment Corp/ Financial/ Insurance - Specialty
MTH/ Meritage Homes Corp./ Consumer Cyclical/ Residential Construction
MTN/ Vail Resorts Inc./ Consumer Cyclical/ Resorts & Casinos
MTRN/ Materion Corp/ Basic Materials/ Other Industrial Metals & Mining
MTSI/ MACOM Technology Solutions Holdings Inc/ Technology/ Semiconductors
MTX/ Minerals Technologies/ / 
MTZ/ Mastec Inc./ Industrials/ Engineering & Construction
MU/ Micron Technology Inc./ Technology/ Semiconductors
MUR/ Murphy Oil Corp./ Energy/ Oil & Gas E&P
MUSA/ Murphy USA Inc/ Consumer Cyclical/ Specialty Retail
MWA/ Mueller Water Products Inc/ Industrials/ Specialty Industrial Machinery
MXL/ MaxLinear Inc/ Technology/ Semiconductors
MYGN/ Myriad Genetics/ / 
MYRG/ MYR Group Inc/ Industrials/ Engineering & Construction
NABL/ N-able Inc/ Technology/ Information Technology Services
NAMS/ NewAmsterdam Pharma Company NV/ Healthcare/ Biotechnology
NAPA/ Duckhorn Portfolio Inc/ Consumer Defensive/ Beverages - Wineries & Distilleries
NARI/ Inari Medical Inc/ Healthcare/ Medical Devices
NATL/ NCR Atleos Corp/ Technology/ Software - Application
NAVI/ Navient Corp/ Financial/ Credit Services
NBHC/ National Bank Holdings Corp/ Financial/ Banks - Regional
NBIX/ Neurocrine Biosciences/ / 
NBTB/ NBT Bancorp. Inc./ Financial/ Banks - Regional
NCLH/ Norwegian Cruise Line Holdings Ltd/ Consumer Cyclical/ Travel Services
NCNO/ Ncino Inc./ Technology/ Software - Application
NDAQ/ Nasdaq Inc/ Financial/ Financial Data & Stock Exchanges
NDSN/ Nordson Corp./ Industrials/ Specialty Industrial Machinery
NE/ Noble Corp Plc/ Energy/ Oil & Gas Drilling
NEE/ NextEra Energy Inc/ Utilities/ Utilities - Regulated Electric
NEM/ Newmont Corp/ Basic Materials/ Gold
NEO/ Neogenomics Inc./ Healthcare/ Diagnostics & Research
NEOG/ Neogen Corp./ Healthcare/ Diagnostics & Research
NEP/ NextEra Energy Partners LP/ Utilities/ Utilities - Renewable
NET/ Cloudflare Inc/ Technology/ Software - Infrastructure
NEU/ NewMarket Corp./ Basic Materials/ Specialty Chemicals
NEXT/ NextDecade Corporation/ Energy/ Oil & Gas E&P
NFE/ New Fortress Energy Inc/ Utilities/ Utilities - Regulated Gas
NFG/ National Fuel Gas Co./ Energy/ Oil & Gas Integrated
NFLX/ Netflix Inc./ Communication Services/ Entertainment
NG/ Novagold Resources Inc./ Basic Materials/ Gold
NGG/ National Grid Plc ADR/ Utilities/ Utilities - Regulated Electric
NGVT/ Ingevity Corp/ Basic Materials/ Specialty Chemicals
NHC/ National Healthcare Corp./ Healthcare/ Medical Care Facilities
NHI/ National Health Investors/ / 
NI/ NiSource Inc/ Utilities/ Utilities - Regulated Gas
NIC/ Nicolet Bankshares Inc./ Financial/ Banks - Regional
NJR/ New Jersey Resources Corporation/ Utilities/ Utilities - Regulated Gas
NKE/ Nike/ / 
NLY/ Annaly Capital Management Inc/ Real Estate/ REIT - Mortgage
NMFC/ New Mountain Finance Corporation/ Financial/ Asset Management
NMIH/ NMI Holdings Inc/ Financial/ Insurance - Specialty
NMRA/ Neumora Therapeutics Inc./ Healthcare/ Biotechnology
NMRK/ Newmark Group Inc/ Real Estate/ Real Estate Services
NNI/ Nelnet Inc/ Financial/ Credit Services
NNN/ NNN REIT Inc/ Real Estate/ REIT - Retail
NOC/ Northrop Grumman Corp./ Industrials/ Aerospace & Defense
NOG/ Northern Oil and Gas Inc./ Energy/ Oil & Gas E&P
NOK/ Nokia Corp ADR/ Technology/ Communication Equipment
NOMD/ Nomad Foods Limited/ Consumer Defensive/ Packaged Foods
NOV/ NOV Inc/ Energy/ Oil & Gas Equipment & Services
NOVA/ Sunnova Energy International Inc/ Technology/ Solar
NOVT/ Novanta Inc/ Technology/ Scientific & Technical Instruments
NOW/ ServiceNow Inc/ Technology/ Software - Application
NPO/ Enpro Inc/ Industrials/ Specialty Industrial Machinery
NRDS/ Nerdwallet Inc/ Communication Services/ Internet Content & Information
NRG/ NRG Energy Inc./ Utilities/ Utilities - Independent Power Producers
NRP/ Natural Resource Partners LP/ Energy/ Thermal Coal
NS/ Nustar Energy L P/ Energy/ Oil & Gas Midstream
NSA/ National Storage Affiliates Trust/ Real Estate/ REIT - Industrial
NSC/ Norfolk Southern Corp./ Industrials/ Railroads
NSIT/ Insight Enterprises Inc./ Technology/ Electronics & Computer Distribution
NSP/ Insperity Inc/ Industrials/ Staffing & Employment Services
NSSC/ NAPCO Security Technologies Inc/ Industrials/ Security & Protection Services
NTAP/ Netapp Inc/ Technology/ Computer Hardware
NTCT/ Netscout Systems Inc/ Technology/ Software - Infrastructure
NTLA/ Intellia Therapeutics Inc/ Healthcare/ Biotechnology
NTNX/ Nutanix Inc/ Technology/ Software - Infrastructure
NTR/ Nutrien Ltd/ Basic Materials/ Agricultural Inputs
NTRA/ Natera Inc/ Healthcare/ Diagnostics & Research
NTRS/ Northern Trust Corp./ Financial/ Asset Management
NTRSO/ Northern Trust Corporation/ Financial/ Asset Management
NTST/ Netstreit Corp/ Real Estate/ REIT - Retail
NUE/ Nucor Corp./ Basic Materials/ Steel
NUVL/ Nuvalent Inc/ Healthcare/ Biotechnology
NVCR/ NovoCure Ltd/ Healthcare/ Medical Devices
NVDA/ NVIDIA Corp/ Technology/ Semiconductors
NVEE/ NV5 Global Inc/ Industrials/ Engineering & Construction
NVEI/ Nuvei Corporation/ Technology/ Software - Infrastructure
NVGS/ Navigator Holdings Ltd/ Energy/ Oil & Gas Midstream
NVO/ Novo Nordisk ADR/ Healthcare/ Biotechnology
NVR/ NVR Inc./ Consumer Cyclical/ Residential Construction
NVS/ Novartis AG ADR/ Healthcare/ Drug Manufacturers - General
NVST/ Envista Holdings Corp/ Healthcare/ Medical Instruments & Supplies
NVT/ nVent Electric plc/ Industrials/ Electrical Equipment & Parts
NVTS/ Navitas Semiconductor Corp/ Technology/ Semiconductors
NWBI/ Northwest Bancshares Inc/ Financial/ Banks - Regional
NWE/ NorthWestern Energy Group Inc/ Utilities/ Utilities - Diversified
NWG/ NatWest Group Plc ADR/ Financial/ Banks - Regional
NWL/ Newell Brands Inc/ Consumer Defensive/ Household & Personal Products
NWLI/ National Western Life Group Inc/ Financial/ Insurance - Life
NWN/ Northwest Natural Holding Co/ Utilities/ Utilities - Regulated Gas
NWS/ News Corp/ Communication Services/ Entertainment
NWSA/ News Corp/ Communication Services/ Entertainment
NXE/ NexGen Energy Ltd/ Energy/ Uranium
NXPI/ NXP Semiconductors NV/ Technology/ Semiconductors
NXST/ Nexstar Media Group Inc/ Communication Services/ Entertainment
NXT/ Nextracker Inc/ Technology/ Solar
NYCB/ New York Community Bancorp Inc./ Financial/ Banks - Regional
NYT/ New York Times Co./ Communication Services/ Publishing
O/ Realty Income Corp./ Real Estate/ REIT - Retail
OBDC/ Blue Owl Capital Corp/ Financial/ Credit Services
OBK/ Origin Bancorp Inc/ Financial/ Banks - Regional
OC/ Owens Corning/ Industrials/ Building Products & Equipment
OCFC/ OceanFirst Financial Corp./ Financial/ Banks - Regional
OCSL/ Oaktree Specialty Lending Corporation/ Financial/ Credit Services
ODFL/ Old Dominion Freight Line/ / 
ODP/ ODP Corporation/ Consumer Cyclical/ Specialty Retail
OEC/ Orion S.A/ Basic Materials/ Specialty Chemicals
OFG/ OFG Bancorp/ Financial/ Banks - Regional
OGE/ Oge Energy Corp./ Utilities/ Utilities - Regulated Electric
OGN/ Organon & Co./ Healthcare/ Drug Manufacturers - General
OGS/ ONE Gas Inc/ Utilities/ Utilities - Regulated Gas
OHI/ Omega Healthcare Investors/ / 
OI/ O-I Glass Inc/ Consumer Cyclical/ Packaging & Containers
OII/ Oceaneering International/ / 
OKE/ Oneok Inc./ Energy/ Oil & Gas Midstream
OKTA/ Okta Inc/ Technology/ Software - Infrastructure
OLED/ Universal Display Corp./ Technology/ Electronic Components
OLK/ Olink Holding AB (publ) ADR/ Healthcare/ Diagnostics & Research
OLLI/ Ollies Bargain Outlet Holdings Inc/ Consumer Defensive/ Discount Stores
OLN/ Olin Corp./ Basic Materials/ Specialty Chemicals
OLPX/ Olaplex Holdings Inc/ Consumer Cyclical/ Specialty Retail
OMC/ Omnicom Group/ / 
OMCL/ Omnicell/ / 
OMF/ OneMain Holdings Inc/ Financial/ Credit Services
OMI/ Owens & Minor/ / 
ON/ ON Semiconductor Corp./ Technology/ Semiconductors
ONB/ Old National Bancorp/ Financial/ Banks - Regional
ONON/ On Holding AG/ Consumer Cyclical/ Footwear & Accessories
ONTO/ Onto Innovation Inc./ Technology/ Semiconductor Equipment & Materials
OPCH/ Option Care Health Inc./ Healthcare/ Medical Care Facilities
OPEN/ Opendoor Technologies Inc/ Real Estate/ Real Estate Services
OPRA/ Opera Ltd ADR/ Communication Services/ Internet Content & Information
OR/ Osisko Gold Royalties Ltd/ Basic Materials/ Gold
ORA/ Ormat Technologies Inc/ Utilities/ Utilities - Renewable
ORAN/ Orange. ADR/ Communication Services/ Telecom Services
ORCL/ Oracle Corp./ Technology/ Software - Infrastructure
ORI/ Old Republic International Corp./ Financial/ Insurance - Diversified
ORLY/ O'Reilly Automotive/ / 
OSCR/ Oscar Health Inc/ Healthcare/ Healthcare Plans
OSIS/ OSI Systems/ / 
OSK/ Oshkosh Corp/ Industrials/ Farm & Heavy Construction Machinery
OTEX/ Open Text Corp/ Technology/ Software - Application
OTIS/ Otis Worldwide Corp/ Industrials/ Specialty Industrial Machinery
OTTR/ Otter Tail Corporation/ Utilities/ Utilities - Diversified
OUT/ Outfront Media Inc/ Real Estate/ REIT - Specialty
OVV/ Ovintiv Inc/ Energy/ Oil & Gas E&P
OWL/ Blue Owl Capital Inc/ Financial/ Asset Management
OXM/ Oxford Industries/ / 
OXY/ Occidental Petroleum Corp./ Energy/ Oil & Gas E&P
OZK/ Bank OZK/ Financial/ Banks - Regional
PAA/ Plains All American Pipeline LP/ Energy/ Oil & Gas Midstream
PAAS/ Pan American Silver Corp/ Basic Materials/ Gold
PACB/ Pacific Biosciences of California Inc/ Healthcare/ Medical Devices
PAG/ Penske Automotive Group Inc/ Consumer Cyclical/ Auto & Truck Dealerships
PAGP/ Plains GP Holdings LP/ Energy/ Oil & Gas Midstream
PANW/ Palo Alto Networks Inc/ Technology/ Software - Infrastructure
PAR/ Par Technology Corp./ Technology/ Software - Application
PARA/ Paramount Global/ Communication Services/ Entertainment
PARR/ Par Pacific Holdings Inc/ Energy/ Oil & Gas Refining & Marketing
PATH/ UiPath Inc/ Technology/ Software - Infrastructure
PATK/ Patrick Industries/ / 
PAY/ Paymentus Holdings Inc/ Technology/ Software - Infrastructure
PAYC/ Paycom Software Inc/ Technology/ Software - Application
PAYO/ Payoneer Global Inc/ Technology/ Software - Infrastructure
PAYX/ Paychex Inc./ Industrials/ Staffing & Employment Services
PB/ Prosperity Bancshares Inc./ Financial/ Banks - Regional
PBA/ Pembina Pipeline Corporation/ Energy/ Oil & Gas Midstream
PBF/ PBF Energy Inc/ Energy/ Oil & Gas Refining & Marketing
PBH/ Prestige Consumer Healthcare Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
PCAR/ Paccar Inc./ Industrials/ Farm & Heavy Construction Machinery
PCG/ PG&E Corp./ Utilities/ Utilities - Regulated Electric
PCH/ PotlatchDeltic Corp/ Real Estate/ REIT - Specialty
PCOR/ Procore Technologies Inc/ Technology/ Software - Application
PCRX/ Pacira BioSciences Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
PCTY/ Paylocity Holding Corp/ Technology/ Software - Application
PCVX/ Vaxcyte Inc/ Healthcare/ Biotechnology
PD/ Pagerduty Inc/ Technology/ Software - Application
PDCO/ Patterson Companies Inc./ Healthcare/ Medical Distribution
PDFS/ PDF Solutions Inc./ Technology/ Software - Application
PEAK/ Healthpeak Properties Inc./ Real Estate/ REIT - Healthcare Facilities
PEB/ Pebblebrook Hotel Trust/ Real Estate/ REIT - Hotel & Motel
PEBO/ Peoples Bancorp/ / 
PECO/ Phillips Edison & Company Inc/ Real Estate/ REIT - Retail
PEG/ Public Service Enterprise Group Inc./ Utilities/ Utilities - Regulated Electric
PEGA/ Pegasystems Inc./ Technology/ Software - Application
PEN/ Penumbra Inc/ Healthcare/ Medical Devices
PENN/ PENN Entertainment Inc/ Consumer Cyclical/ Resorts & Casinos
PEP/ PepsiCo Inc/ Consumer Defensive/ Beverages - Non-Alcoholic
PFBC/ Preferred Bank (Los Angeles/ / 
PFE/ Pfizer Inc./ Healthcare/ Drug Manufacturers - General
PFG/ Principal Financial Group Inc/ Financial/ Asset Management
PFGC/ Performance Food Group Company/ Consumer Defensive/ Food Distribution
PFS/ Provident Financial Services Inc/ Financial/ Banks - Regional
PFSI/ PennyMac Financial Services Inc./ Financial/ Mortgage Finance
PG/ Procter & Gamble Co./ Consumer Defensive/ Household & Personal Products
PGNY/ Progyny Inc/ Healthcare/ Health Information Services
PGR/ Progressive Corp./ Financial/ Insurance - Property & Casualty
PGRE/ Paramount Group Inc/ Real Estate/ REIT - Office
PGTI/ PGT Innovations Inc/ Industrials/ Building Products & Equipment
PH/ Parker-Hannifin Corp./ Industrials/ Specialty Industrial Machinery
PHG/ Koninklijke Philips N.V. ADR/ Healthcare/ Medical Devices
PHIN/ PHINIA Inc/ Consumer Cyclical/ Auto Parts
PHM/ PulteGroup Inc/ Consumer Cyclical/ Residential Construction
PHR/ Phreesia Inc/ Healthcare/ Health Information Services
PHVS/ Pharvaris NV/ Healthcare/ Biotechnology
PHYS/ Sprott Physical Gold Trust/ Financial/ Asset Management
PI/ Impinj Inc/ Technology/ Communication Equipment
PII/ Polaris Inc/ Consumer Cyclical/ Recreational Vehicles
PINC/ Premier Inc/ Healthcare/ Health Information Services
PINS/ Pinterest Inc/ Communication Services/ Internet Content & Information
PIPR/ Piper Sandler Co's/ Financial/ Capital Markets
PJT/ PJT Partners Inc/ Financial/ Capital Markets
PK/ Park Hotels & Resorts Inc/ Real Estate/ REIT - Hotel & Motel
PKG/ Packaging Corp Of America/ Consumer Cyclical/ Packaging & Containers
PLAB/ Photronics/ / 
PLAY/ Dave & Buster's Entertainment Inc/ Communication Services/ Entertainment
PLD/ Prologis Inc/ Real Estate/ REIT - Industrial
PLMR/ Palomar Holdings Inc/ Financial/ Insurance - Property & Casualty
PLNT/ Planet Fitness Inc/ Consumer Cyclical/ Leisure
PLRX/ Pliant Therapeutics Inc/ Healthcare/ Biotechnology
PLTR/ Palantir Technologies Inc/ Technology/ Software - Infrastructure
PLUG/ Plug Power Inc/ Industrials/ Electrical Equipment & Parts
PLUS/ ePlus Inc/ Technology/ Software - Application
PLXS/ Plexus Corp./ Technology/ Electronic Components
PLYA/ Playa Hotels & Resorts N.V./ Consumer Cyclical/ Resorts & Casinos
PLYM/ Plymouth Industrial Reit Inc/ Real Estate/ REIT - Industrial
PM/ Philip Morris International Inc/ Consumer Defensive/ Tobacco
PMT/ Pennymac Mortgage Investment Trust/ Real Estate/ REIT - Mortgage
PNC/ PNC Financial Services Group Inc/ Financial/ Banks - Regional
PNFP/ Pinnacle Financial Partners Inc./ Financial/ Banks - Regional
PNM/ PNM Resources Inc/ Utilities/ Utilities - Regulated Electric
PNR/ Pentair plc/ Industrials/ Specialty Industrial Machinery
PNW/ Pinnacle West Capital Corp./ Utilities/ Utilities - Regulated Electric
PODD/ Insulet Corporation/ Healthcare/ Medical Devices
POOL/ Pool Corporation/ Industrials/ Industrial Distribution
POR/ Portland General Electric Co/ Utilities/ Utilities - Regulated Electric
POST/ Post Holdings Inc/ Consumer Defensive/ Packaged Foods
POWI/ Power Integrations Inc./ Technology/ Semiconductors
PPBI/ Pacific Premier Bancorp/ / 
PPC/ Pilgrim's Pride Corp./ Consumer Defensive/ Packaged Foods
PPG/ PPG Industries/ / 
PPL/ PPL Corp/ Utilities/ Utilities - Regulated Electric
PR/ Permian Resources Corp/ Energy/ Oil & Gas E&P
PRCT/ Procept BioRobotics Corp/ Healthcare/ Medical Devices
PRDO/ Perdoceo Education Corporation/ Consumer Defensive/ Education & Training Services
PRFT/ Perficient Inc./ Technology/ Information Technology Services
PRG/ PROG Holdings Inc/ Industrials/ Rental & Leasing Services
PRGO/ Perrigo Company plc/ Healthcare/ Drug Manufacturers - Specialty & Generic
PRGS/ Progress Software Corp./ Technology/ Software - Application
PRI/ Primerica Inc/ Financial/ Insurance - Life
PRIM/ Primoris Services Corp/ Industrials/ Engineering & Construction
PRK/ Park National Corp./ Financial/ Banks - Regional
PRMW/ Primo Water Corporation/ Consumer Defensive/ Beverages - Non-Alcoholic
PRO/ Pros Holdings Inc/ Technology/ Software - Application
PRTA/ Prothena Corporation plc/ Healthcare/ Biotechnology
PRU/ Prudential Financial Inc./ Financial/ Insurance - Life
PRVA/ Privia Health Group Inc/ Healthcare/ Health Information Services
PSA/ Public Storage./ Real Estate/ REIT - Industrial
PSEC/ Prospect Capital Corporation/ Financial/ Asset Management
PSLV/ Sprott Physical Silver Trust/ Financial/ Asset Management
PSMT/ Pricesmart Inc./ Consumer Defensive/ Discount Stores
PSN/ Parsons Corp/ Technology/ Information Technology Services
PSO/ Pearson plc ADR/ Communication Services/ Publishing
PSTG/ Pure Storage Inc/ Technology/ Computer Hardware
PSX/ Phillips 66/ Energy/ Oil & Gas Refining & Marketing
PTC/ PTC Inc/ Technology/ Software - Application
PTCT/ PTC Therapeutics Inc/ Healthcare/ Biotechnology
PTEN/ Patterson-UTI Energy Inc/ Energy/ Oil & Gas Drilling
PTGX/ Protagonist Therapeutics Inc/ Healthcare/ Biotechnology
PTON/ Peloton Interactive Inc/ Consumer Cyclical/ Leisure
PTVE/ Pactiv Evergreen Inc/ Consumer Cyclical/ Packaging & Containers
PUK/ Prudential plc ADR/ Financial/ Insurance - Life
PVH/ PVH Corp/ Consumer Cyclical/ Apparel Manufacturing
PWR/ Quanta Services/ / 
PWSC/ PowerSchool Holdings Inc/ Technology/ Software - Application
PX/ P10 Inc/ Financial/ Asset Management
PXD/ Pioneer Natural Resources Co./ Energy/ Oil & Gas E&P
PYCR/ Paycor HCM Inc/ Technology/ Software - Application
PYPL/ PayPal Holdings Inc/ Financial/ Credit Services
PZZA/ Papa John's International/ / 
QCOM/ Qualcomm/ / 
QDEL/ QuidelOrtho Corporation/ Healthcare/ Medical Devices
QGEN/ Qiagen NV/ Healthcare/ Diagnostics & Research
QLYS/ Qualys Inc/ Technology/ Software - Infrastructure
QRTEB/ Qurate Retail Inc/ Consumer Cyclical/ Internet Retail
QRVO/ Qorvo Inc/ Technology/ Semiconductors
QS/ QuantumScape Corp/ Consumer Cyclical/ Auto Parts
QSR/ Restaurant Brands International Inc/ Consumer Cyclical/ Restaurants
QTRX/ Quanterix Corp/ Healthcare/ Medical Devices
QTWO/ Q2 Holdings Inc/ Technology/ Software - Application
R/ Ryder System/ / 
RACE/ Ferrari N.V./ Consumer Cyclical/ Auto Manufacturers
RAMP/ LiveRamp Holdings Inc/ Technology/ Software - Infrastructure
RARE/ Ultragenyx Pharmaceutical Inc./ Healthcare/ Biotechnology
RBA/ RB Global Inc/ Industrials/ Specialty Business Services
RBC/ RBC Bearings Inc./ Industrials/ Tools & Accessories
RBCAA/ Republic Bancorp/ / 
RBLX/ Roblox Corporation/ Communication Services/ Electronic Gaming & Multimedia
RC/ Ready Capital Corp/ Real Estate/ REIT - Mortgage
RCI/ Rogers Communications Inc./ Communication Services/ Telecom Services
RCKT/ Rocket Pharmaceuticals Inc/ Healthcare/ Biotechnology
RCL/ Royal Caribbean Group/ Consumer Cyclical/ Travel Services
RCM/ R1 RCM Inc./ Healthcare/ Health Information Services
RCUS/ Arcus Biosciences Inc/ Healthcare/ Biotechnology
RDFN/ Redfin Corp/ Real Estate/ Real Estate Services
RDN/ Radian Group/ / 
RDNT/ Radnet Inc/ Healthcare/ Diagnostics & Research
REG/ Regency Centers Corporation/ Real Estate/ REIT - Retail
REGN/ Regeneron Pharmaceuticals/ / 
RELX/ RELX Plc ADR/ Industrials/ Specialty Business Services
RELY/ Remitly Global Inc/ Technology/ Software - Infrastructure
RES/ RPC/ / 
REVG/ REV Group Inc/ Industrials/ Farm & Heavy Construction Machinery
REXR/ Rexford Industrial Realty Inc/ Real Estate/ REIT - Industrial
REYN/ Reynolds Consumer Products Inc/ Consumer Cyclical/ Packaging & Containers
REZI/ Resideo Technologies Inc/ Industrials/ Security & Protection Services
RF/ Regions Financial Corp./ Financial/ Banks - Regional
RGA/ Reinsurance Group Of America/ / 
RGEN/ Repligen Corp./ Healthcare/ Medical Instruments & Supplies
RGLD/ Royal Gold/ / 
RH/ RH/ Consumer Cyclical/ Specialty Retail
RHI/ Robert Half Inc/ Industrials/ Staffing & Employment Services
RHP/ Ryman Hospitality Properties Inc/ Real Estate/ REIT - Hotel & Motel
RIG/ Transocean Ltd/ Energy/ Oil & Gas Drilling
RIO/ Rio Tinto plc ADR/ Basic Materials/ Other Industrial Metals & Mining
RIOT/ Riot Platforms Inc/ Financial/ Capital Markets
RITM/ Rithm Capital Corporation/ Real Estate/ REIT - Mortgage
RIVN/ Rivian Automotive Inc/ Consumer Cyclical/ Auto Manufacturers
RJF/ Raymond James Financial/ / 
RKLB/ Rocket Lab USA Inc/ Industrials/ Aerospace & Defense
RKT/ Rocket Companies Inc/ Financial/ Mortgage Finance
RL/ Ralph Lauren Corp/ Consumer Cyclical/ Apparel Manufacturing
RLAY/ Relay Therapeutics Inc/ Healthcare/ Biotechnology
RLI/ RLI Corp./ Financial/ Insurance - Property & Casualty
RLJ/ RLJ Lodging Trust/ Real Estate/ REIT - Hotel & Motel
RMBS/ Rambus Inc./ Technology/ Semiconductors
RMD/ Resmed Inc./ Healthcare/ Medical Instruments & Supplies
RNG/ RingCentral Inc./ Technology/ Software - Application
RNST/ Renasant Corp./ Financial/ Banks - Regional
ROAD/ Construction Partners Inc/ Industrials/ Engineering & Construction
ROCK/ Gibraltar Industries Inc./ Industrials/ Building Products & Equipment
ROG/ Rogers Corp./ Technology/ Electronic Components
ROIC/ Retail Opportunity Investments Corp/ Real Estate/ REIT - Retail
ROIV/ Roivant Sciences Ltd/ Healthcare/ Biotechnology
ROK/ Rockwell Automation Inc/ Industrials/ Specialty Industrial Machinery
ROKU/ Roku Inc/ Communication Services/ Entertainment
ROL/ Rollins/ / 
ROP/ Roper Technologies Inc/ Technology/ Software - Application
ROST/ Ross Stores/ / 
ROVR/ Rover Group Inc/ Communication Services/ Internet Content & Information
RPD/ Rapid7 Inc/ Technology/ Software - Infrastructure
RPM/ RPM International/ / 
RPRX/ Royalty Pharma plc/ Healthcare/ Biotechnology
RRC/ Range Resources Corp/ Energy/ Oil & Gas E&P
RRR/ Red Rock Resorts Inc/ Consumer Cyclical/ Resorts & Casinos
RRX/ Regal Rexnord Corp/ Industrials/ Specialty Industrial Machinery
RS/ Reliance Steel & Aluminum Co./ Basic Materials/ Steel
RSG/ Republic Services/ / 
RTO/ Rentokil Initial Plc. ADR/ Industrials/ Specialty Business Services
RTX/ RTX Corp/ Industrials/ Aerospace & Defense
RUM/ Rumble Inc/ Technology/ Software - Application
RUN/ Sunrun Inc/ Technology/ Solar
RUSHA/ Rush Enterprises Inc/ Consumer Cyclical/ Auto & Truck Dealerships
RUSHB/ Rush Enterprises Inc/ Consumer Cyclical/ Auto & Truck Dealerships
RVLV/ Revolve Group Inc/ Consumer Cyclical/ Internet Retail
RVMD/ Revolution Medicines Inc/ Healthcare/ Biotechnology
RVTY/ Revvity Inc./ Healthcare/ Diagnostics & Research
RXO/ RXO Inc/ Industrials/ Trucking
RXRX/ Recursion Pharmaceuticals Inc/ Healthcare/ Biotechnology
RXST/ RxSight Inc/ Healthcare/ Medical Devices
RY/ Royal Bank Of Canada/ Financial/ Banks - Diversified
RYAAY/ Ryanair Holdings Plc ADR/ Industrials/ Airlines
RYAN/ Ryan Specialty Holdings Inc/ Financial/ Insurance - Specialty
RYI/ Ryerson Holding Corp./ Industrials/ Metal Fabrication
RYN/ Rayonier Inc./ Real Estate/ REIT - Specialty
RYTM/ Rhythm Pharmaceuticals Inc./ Healthcare/ Biotechnology
RYZB/ RayzeBio Inc./ Healthcare/ Biotechnology
S/ SentinelOne Inc/ Technology/ Software - Infrastructure
SABR/ Sabre Corp/ Consumer Cyclical/ Travel Services
SAFE/ Safehold Inc./ Real Estate/ REIT - Diversified
SAFT/ Safety Insurance Group/ / 
SAGE/ Sage Therapeutics Inc/ Healthcare/ Biotechnology
SAH/ Sonic Automotive/ / 
SAIA/ Saia Inc./ Industrials/ Trucking
SAIC/ Science Applications International Corp./ Technology/ Information Technology Services
SAM/ Boston Beer Co./ / 
SAN/ Banco Santander S.A. ADR/ Financial/ Banks - Diversified
SANA/ Sana Biotechnology Inc/ Healthcare/ Biotechnology
SAND/ Sandstorm Gold Ltd/ Basic Materials/ Gold
SANM/ Sanmina Corp/ Technology/ Electronic Components
SAP/ Sap SE ADR/ Technology/ Software - Application
SASR/ Sandy Spring Bancorp/ Financial/ Banks - Regional
SATS/ EchoStar Corp/ Technology/ Communication Equipment
SAVA/ Cassava Sciences Inc/ Healthcare/ Biotechnology
SAVE/ Spirit Airlines Inc/ Industrials/ Airlines
SBAC/ SBA Communications Corp/ Real Estate/ REIT - Specialty
SBCF/ Seacoast Banking Corp. Of Florida/ Financial/ Banks - Regional
SBH/ Sally Beauty Holdings Inc/ Consumer Cyclical/ Specialty Retail
SBLK/ Star Bulk Carriers Corp/ Industrials/ Marine Shipping
SBR/ Sabine Royalty Trust/ Energy/ Oil & Gas E&P
SBRA/ Sabra Healthcare REIT Inc/ Real Estate/ REIT - Healthcare Facilities
SBUX/ Starbucks Corp./ Consumer Cyclical/ Restaurants
SCCO/ Southern Copper Corporation/ Basic Materials/ Copper
SCHL/ Scholastic Corp./ Communication Services/ Publishing
SCHW/ Charles Schwab Corp./ Financial/ Capital Markets
SCI/ Service Corp. International/ Consumer Cyclical/ Personal Services
SCL/ Stepan Co./ Basic Materials/ Specialty Chemicals
SCS/ Steelcase/ / 
SDGR/ Schrodinger Inc/ Healthcare/ Health Information Services
SEAS/ SeaWorld Entertainment Inc/ Consumer Cyclical/ Leisure
SEB/ Seaboard Corp./ Industrials/ Conglomerates
SEE/ Sealed Air Corp./ Consumer Cyclical/ Packaging & Containers
SEIC/ SEI Investments Co./ Financial/ Asset Management
SEM/ Select Medical Holdings Corporation/ Healthcare/ Medical Care Facilities
SEMR/ SEMrush Holdings Inc/ Technology/ Software - Application
SF/ Stifel Financial Corp./ Financial/ Capital Markets
SFBS/ ServisFirst Bancshares Inc/ Financial/ Banks - Regional
SFM/ Sprouts Farmers Market Inc/ Consumer Defensive/ Grocery Stores
SFNC/ Simmons First National Corp./ Financial/ Banks - Regional
SG/ Sweetgreen Inc/ Consumer Cyclical/ Restaurants
SGHC/ Super Group (SGHC) Limited/ Consumer Cyclical/ Gambling
SGRY/ Surgery Partners Inc/ Healthcare/ Medical Care Facilities
SHAK/ Shake Shack Inc/ Consumer Cyclical/ Restaurants
SHC/ Sotera Health Co/ Healthcare/ Diagnostics & Research
SHCO/ Soho House & Co Inc/ Consumer Cyclical/ Lodging
SHEL/ Shell Plc ADR/ Energy/ Oil & Gas Integrated
SHEN/ Shenandoah Telecommunications Co./ Communication Services/ Telecom Services
SHLS/ Shoals Technologies Group Inc/ Technology/ Solar
SHO/ Sunstone Hotel Investors Inc/ Real Estate/ REIT - Hotel & Motel
SHOO/ Steven Madden Ltd./ Consumer Cyclical/ Footwear & Accessories
SHOP/ Shopify Inc/ Technology/ Software - Application
SHW/ Sherwin-Williams Co./ Basic Materials/ Specialty Chemicals
SIDU/ Sidus Space Inc/ Industrials/ Aerospace & Defense
SIGI/ Selective Insurance Group Inc./ Financial/ Insurance - Property & Casualty
SIRI/ Sirius XM Holdings Inc/ Communication Services/ Entertainment
SITC/ SITE Centers Corp/ Real Estate/ REIT - Retail
SITE/ SiteOne Landscape Supply Inc/ Industrials/ Industrial Distribution
SITM/ SiTime Corp/ Technology/ Semiconductors
SIX/ Six Flags Entertainment Corp/ Consumer Cyclical/ Leisure
SJM/ J.M. Smucker Co./ Consumer Defensive/ Packaged Foods
SJW/ SJW Group/ Utilities/ Utilities - Regulated Water
SKT/ Tanger Inc./ Real Estate/ REIT - Retail
SKWD/ Skyward Specialty Insurance Group Inc/ Financial/ Insurance - Property & Casualty
SKX/ Skechers U S A/ / 
SKY/ Skyline Champion Corp/ Consumer Cyclical/ Residential Construction
SKYW/ Skywest Inc./ Industrials/ Airlines
SLAB/ Silicon Laboratories Inc/ Technology/ Semiconductors
SLB/ Schlumberger Ltd./ Energy/ Oil & Gas Equipment & Services
SLF/ Sun Life Financial/ / 
SLG/ SL Green Realty Corp./ Real Estate/ REIT - Office
SLGN/ Silgan Holdings Inc./ Consumer Cyclical/ Packaging & Containers
SLM/ SLM Corp./ Financial/ Credit Services
SLNO/ Soleno Therapeutics Inc/ Healthcare/ Biotechnology
SLVM/ Sylvamo Corp/ Basic Materials/ Paper & Paper Products
SM/ SM Energy Co/ Energy/ Oil & Gas E&P
SMAR/ Smartsheet Inc/ Technology/ Software - Application
SMCI/ Super Micro Computer Inc/ Technology/ Computer Hardware
SMG/ Scotts Miracle-Gro Company/ Basic Materials/ Agricultural Inputs
SMMT/ Summit Therapeutics Inc/ Healthcare/ Biotechnology
SMPL/ Simply Good Foods Co/ Consumer Defensive/ Packaged Foods
SMTC/ Semtech Corp./ Technology/ Semiconductors
SN/ SharkNinja Inc./ Consumer Cyclical/ Furnishings
SNA/ Snap-on/ / 
SNAP/ Snap Inc/ Communication Services/ Internet Content & Information
SNDR/ Schneider National Inc/ Industrials/ Trucking
SNDX/ Syndax Pharmaceuticals Inc/ Healthcare/ Biotechnology
SNEX/ StoneX Group Inc/ Financial/ Capital Markets
SNN/ Smith & Nephew plc ADR/ Healthcare/ Medical Devices
SNOW/ Snowflake Inc/ Technology/ Software - Application
SNPS/ Synopsys/ / 
SNV/ Synovus Financial Corp./ Financial/ Banks - Regional
SNX/ TD Synnex Corp/ Technology/ Electronics & Computer Distribution
SNY/ Sanofi ADR/ Healthcare/ Drug Manufacturers - General
SO/ Southern Company/ Utilities/ Utilities - Regulated Electric
SOFI/ SoFi Technologies Inc/ Financial/ Credit Services
SON/ Sonoco Products Co./ Consumer Cyclical/ Packaging & Containers
SONO/ Sonos Inc/ Technology/ Consumer Electronics
SOVO/ Sovos Brands Inc/ Consumer Defensive/ Packaged Foods
SP/ SP Plus Corp/ Industrials/ Specialty Business Services
SPB/ Spectrum Brands Holdings Inc./ Consumer Defensive/ Household & Personal Products
SPG/ Simon Property Group/ / 
SPGI/ S&P Global Inc/ Financial/ Financial Data & Stock Exchanges
SPH/ Suburban Propane Partners LP/ Utilities/ Utilities - Regulated Gas
SPHR/ Sphere Entertainment Co/ Communication Services/ Entertainment
SPLK/ Splunk Inc/ Technology/ Software - Infrastructure
SPOT/ Spotify Technology S.A./ Communication Services/ Internet Content & Information
SPR/ Spirit Aerosystems Holdings Inc/ Industrials/ Aerospace & Defense
SPSC/ SPS Commerce Inc./ Technology/ Software - Infrastructure
SPT/ Sprout Social Inc/ Technology/ Software - Application
SPXC/ SPX Technologies Inc/ Industrials/ Building Products & Equipment
SQ/ Block Inc/ Technology/ Software - Infrastructure
SQSP/ Squarespace Inc/ Technology/ Software - Infrastructure
SR/ Spire Inc./ Utilities/ Utilities - Regulated Gas
SRAD/ Sportradar Group AG/ Technology/ Software - Application
SRC/ Spirit Realty Capital Inc/ Real Estate/ REIT - Diversified
SRCE/ 1st Source Corp./ Financial/ Banks - Regional
SRCL/ Stericycle Inc./ Industrials/ Waste Management
SRE/ Sempra/ Utilities/ Utilities - Diversified
SRPT/ Sarepta Therapeutics Inc/ Healthcare/ Biotechnology
SRRK/ Scholar Rock Holding Corp/ Healthcare/ Biotechnology
SSB/ SouthState Corporation/ Financial/ Banks - Regional
SSD/ Simpson Manufacturing Co./ / 
SSNC/ SS&C Technologies Holdings Inc/ Technology/ Software - Application
SSRM/ SSR Mining Inc/ Basic Materials/ Gold
SSTK/ Shutterstock Inc/ Communication Services/ Internet Content & Information
ST/ Sensata Technologies Holding Plc/ Technology/ Scientific & Technical Instruments
STAA/ Staar Surgical Co./ Healthcare/ Medical Instruments & Supplies
STAG/ STAG Industrial Inc/ Real Estate/ REIT - Industrial
STBA/ S & T Bancorp/ / 
STC/ Stewart Information Services Corp./ Financial/ Insurance - Property & Casualty
STE/ Steris Plc/ Healthcare/ Medical Devices
STEL/ Stellar Bancorp Inc/ Financial/ Banks - Regional
STEP/ StepStone Group Inc/ Financial/ Asset Management
STER/ Sterling Check Corp/ Technology/ Software - Infrastructure
STLA/ Stellantis N.V/ Consumer Cyclical/ Auto Manufacturers
STLD/ Steel Dynamics Inc./ Basic Materials/ Steel
STM/ ST Microelectronics/ Technology/ Semiconductors
STN/ Stantec Inc/ Industrials/ Engineering & Construction
STR/ Sitio Royalties Corp./ Energy/ Oil & Gas E&P
STRA/ Strategic Education Inc/ Consumer Defensive/ Education & Training Services
STRL/ Sterling Infrastructure Inc/ Industrials/ Engineering & Construction
STT/ State Street Corp./ Financial/ Asset Management
STVN/ Stevanato Group Spa/ Healthcare/ Medical Instruments & Supplies
STWD/ Starwood Property Trust Inc/ Real Estate/ REIT - Mortgage
STX/ Seagate Technology Holdings Plc/ Technology/ Computer Hardware
STZ/ Constellation Brands Inc/ Consumer Defensive/ Beverages - Wineries & Distilleries
SU/ Suncor Energy/ / 
SUI/ Sun Communities/ / 
SUM/ Summit Materials Inc/ Basic Materials/ Building Materials
SUN/ Sunoco LP/ Energy/ Oil & Gas Refining & Marketing
SUPN/ Supernus Pharmaceuticals Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
SVC/ Service Properties Trust/ Real Estate/ REIT - Hotel & Motel
SVV/ Savers Value Village Inc/ Consumer Cyclical/ Specialty Retail
SWAV/ ShockWave Medical Inc/ Healthcare/ Medical Devices
SWI/ SolarWinds Corp/ Technology/ Software - Infrastructure
SWK/ Stanley Black & Decker Inc/ Industrials/ Tools & Accessories
SWKS/ Skyworks Solutions/ / 
SWN/ Southwestern Energy Company/ Energy/ Oil & Gas E&P
SWTX/ SpringWorks Therapeutics Inc/ Healthcare/ Biotechnology
SWX/ Southwest Gas Holdings Inc/ Utilities/ Utilities - Regulated Gas
SXI/ Standex International Corp./ Industrials/ Specialty Industrial Machinery
SXT/ Sensient Technologies Corp./ Basic Materials/ Specialty Chemicals
SYBT/ Stock Yards Bancorp Inc/ Financial/ Banks - Regional
SYF/ Synchrony Financial/ Financial/ Credit Services
SYK/ Stryker Corp./ Healthcare/ Medical Devices
SYM/ Symbotic Inc/ Industrials/ Specialty Industrial Machinery
SYNA/ Synaptics Inc/ Technology/ Semiconductors
SYY/ Sysco Corp./ Consumer Defensive/ Food Distribution
T/ AT&T/ / 
TAC/ Transalta Corp./ Utilities/ Utilities - Independent Power Producers
TALO/ Talos Energy Inc/ Energy/ Oil & Gas E&P
TAP/ Molson Coors Beverage Company/ Consumer Defensive/ Beverages - Brewers
TASK/ TaskUs Inc/ Technology/ Information Technology Services
TBBK/ Bancorp Inc./ Financial/ Banks - Regional
TBLA/ Taboola.com Ltd/ Communication Services/ Internet Content & Information
TCBI/ Texas Capital Bancshares/ / 
TCBK/ Trico Bancshares/ Financial/ Banks - Regional
TCN/ Tricon Residential Inc/ Real Estate/ Real Estate Services
TD/ Toronto Dominion Bank/ Financial/ Banks - Diversified
TDC/ Teradata Corp/ Technology/ Software - Infrastructure
TDG/ Transdigm Group Incorporated/ Industrials/ Aerospace & Defense
TDOC/ Teladoc Health Inc/ Healthcare/ Health Information Services
TDS/ Telephone And Data Systems/ / 
TDW/ Tidewater Inc./ Energy/ Oil & Gas Equipment & Services
TDY/ Teledyne Technologies Inc/ Technology/ Scientific & Technical Instruments
TEAM/ Atlassian Corporation/ Technology/ Software - Application
TECH/ Bio-Techne Corp/ Healthcare/ Biotechnology
TECK/ Teck Resources Ltd/ Basic Materials/ Other Industrial Metals & Mining
TEF/ Telefonica S.A ADR/ Communication Services/ Telecom Services
TEL/ TE Connectivity Ltd/ Technology/ Electronic Components
TENB/ Tenable Holdings Inc/ Technology/ Software - Infrastructure
TER/ Teradyne/ / 
TEX/ Terex Corp./ Industrials/ Farm & Heavy Construction Machinery
TFC/ Truist Financial Corporation/ Financial/ Banks - Regional
TFII/ TFI International Inc/ Industrials/ Trucking
TFIN/ Triumph Financial Inc/ Financial/ Banks - Regional
TFPM/ Triple Flag Precious Metals Corp/ Basic Materials/ Other Precious Metals & Mining
TFSL/ TFS Financial Corporation/ Financial/ Banks - Regional
TFX/ Teleflex Incorporated/ Healthcare/ Medical Instruments & Supplies
TGI/ Triumph Group Inc./ Industrials/ Aerospace & Defense
TGLS/ Tecnoglass Inc/ Basic Materials/ Building Materials
TGNA/ TEGNA Inc/ Communication Services/ Broadcasting
TGT/ Target Corp/ Consumer Defensive/ Discount Stores
TGTX/ TG Therapeutics Inc/ Healthcare/ Biotechnology
THC/ Tenet Healthcare Corp./ Healthcare/ Medical Care Facilities
THG/ Hanover Insurance Group Inc/ Financial/ Insurance - Property & Casualty
THO/ Thor Industries/ / 
THR/ Thermon Group Holdings Inc/ Industrials/ Specialty Industrial Machinery
THRM/ Gentherm Inc/ Consumer Cyclical/ Auto Parts
THS/ Treehouse Foods Inc/ Consumer Defensive/ Packaged Foods
TIGO/ Millicom International Cellular S.A./ Communication Services/ Telecom Services
TIXT/ TELUS International (Cda) Inc/ Technology/ Software - Infrastructure
TJX/ TJX Companies/ / 
TKC/ Turkcell Iletisim Hizmetleri A.S. ADR/ Communication Services/ Telecom Services
TKO/ TKO Group Holdings Inc/ Communication Services/ Entertainment
TKR/ Timken Co./ Industrials/ Tools & Accessories
TLRY/ Tilray Brands Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
TMDX/ Transmedics Group Inc/ Healthcare/ Medical Devices
TMHC/ Taylor Morrison Home Corp./ Consumer Cyclical/ Residential Construction
TMO/ Thermo Fisher Scientific Inc./ Healthcare/ Diagnostics & Research
TMUS/ T-Mobile US Inc/ Communication Services/ Telecom Services
TNC/ Tennant Co./ Industrials/ Specialty Industrial Machinery
TNDM/ Tandem Diabetes Care Inc/ Healthcare/ Medical Devices
TNET/ TriNet Group Inc/ Industrials/ Staffing & Employment Services
TNL/ Travel+Leisure Co/ Consumer Cyclical/ Travel Services
TOL/ Toll Brothers Inc./ Consumer Cyclical/ Residential Construction
TOST/ Toast Inc/ Technology/ Software - Infrastructure
TOWN/ Townebank Portsmouth VA/ Financial/ Banks - Regional
TPG/ TPG Inc/ Financial/ Asset Management
TPH/ Tri Pointe Homes Inc./ Consumer Cyclical/ Residential Construction
TPL/ Texas Pacific Land Corporation/ Energy/ Oil & Gas E&P
TPR/ Tapestry Inc/ Consumer Cyclical/ Luxury Goods
TPX/ Tempur Sealy International Inc/ Consumer Cyclical/ Furnishings
TR/ Tootsie Roll Industries/ / 
TREX/ TREX Co./ / 
TRGP/ Targa Resources Corp/ Energy/ Oil & Gas Midstream
TRI/ Thomson-Reuters Corp/ Industrials/ Specialty Business Services
TRIP/ TripAdvisor Inc./ Consumer Cyclical/ Travel Services
TRMB/ Trimble Inc/ Technology/ Scientific & Technical Instruments
TRMD/ Torm Plc/ Energy/ Oil & Gas Midstream
TRMK/ Trustmark Corp./ Financial/ Banks - Regional
TRN/ Trinity Industries/ / 
TRNO/ Terreno Realty Corp/ Real Estate/ REIT - Industrial
TROW/ T. Rowe Price Group Inc./ Financial/ Asset Management
TROX/ Tronox Holdings plc/ Basic Materials/ Chemicals
TRP/ TC Energy Corporation/ Energy/ Oil & Gas Midstream
TRS/ Trimas Corporation/ Consumer Cyclical/ Packaging & Containers
TRU/ TransUnion/ Industrials/ Consulting Services
TRUP/ Trupanion Inc/ Financial/ Insurance - Specialty
TRV/ Travelers Companies Inc./ Financial/ Insurance - Property & Casualty
TS/ Tenaris S.A. ADR/ Energy/ Oil & Gas Equipment & Services
TSCO/ Tractor Supply Co./ Consumer Cyclical/ Specialty Retail
TSLA/ Tesla Inc/ Consumer Cyclical/ Auto Manufacturers
TSLX/ Sixth Street Specialty Lending/ / 
TSN/ Tyson Foods/ / 
TT/ Trane Technologies plc/ Industrials/ Building Products & Equipment
TTC/ Toro Co./ Industrials/ Tools & Accessories
TTD/ Trade Desk Inc/ Technology/ Software - Application
TTE/ TotalEnergies SE ADR/ Energy/ Oil & Gas Integrated
TTEK/ Tetra Tech/ / 
TTMI/ TTM Technologies Inc/ Technology/ Electronic Components
TTWO/ Take-Two Interactive Software/ / 
TU/ Telus Corp./ Communication Services/ Telecom Services
TW/ Tradeweb Markets Inc/ Financial/ Capital Markets
TWKS/ Thoughtworks Holding Inc/ Technology/ Information Technology Services
TWLO/ Twilio Inc/ Communication Services/ Internet Content & Information
TWO/ Two Harbors Investment Corp/ Real Estate/ REIT - Mortgage
TWST/ Twist Bioscience Corp/ Healthcare/ Diagnostics & Research
TX/ Ternium S.A. ADR/ Basic Materials/ Steel
TXG/ 10x Genomics Inc/ Healthcare/ Health Information Services
TXN/ Texas Instruments Inc./ Technology/ Semiconductors
TXRH/ Texas Roadhouse Inc/ Consumer Cyclical/ Restaurants
TXT/ Textron Inc./ Industrials/ Aerospace & Defense
TYL/ Tyler Technologies/ / 
U/ Unity Software Inc/ Technology/ Software - Application
UA/ Under Armour Inc/ Consumer Cyclical/ Apparel Manufacturing
UAA/ Under Armour Inc/ Consumer Cyclical/ Apparel Manufacturing
UAL/ United Airlines Holdings Inc/ Industrials/ Airlines
UBER/ Uber Technologies Inc/ Technology/ Software - Application
UBS/ UBS Group AG/ Financial/ Banks - Diversified
UBSI/ United Bankshares/ / 
UCBI/ United Community Banks Inc/ Financial/ Banks - Regional
UCTT/ Ultra Clean Hldgs Inc/ Technology/ Semiconductor Equipment & Materials
UDMY/ Udemy Inc/ Consumer Defensive/ Education & Training Services
UDR/ UDR Inc/ Real Estate/ REIT - Residential
UE/ Urban Edge Properties/ Real Estate/ REIT - Retail
UEC/ Uranium Energy Corp/ Energy/ Uranium
UFPI/ UFP Industries Inc/ Basic Materials/ Lumber & Wood Production
UFPT/ UFP Technologies Inc./ Healthcare/ Medical Devices
UGI/ UGI Corp./ Utilities/ Utilities - Regulated Gas
UHAL/ U-Haul Holding Company/ Industrials/ Rental & Leasing Services
UHAL-B/ U-Haul Holding Company/ Industrials/ Rental & Leasing Services
UHS/ Universal Health Services/ / 
UI/ Ubiquiti Inc/ Technology/ Communication Equipment
UL/ Unilever plc ADR/ Consumer Defensive/ Household & Personal Products
ULCC/ Frontier Group Holdings Inc/ Industrials/ Airlines
ULTA/ Ulta Beauty Inc/ Consumer Cyclical/ Specialty Retail
UMBF/ UMB Financial Corp./ Financial/ Banks - Regional
UMH/ UMH Properties Inc/ Real Estate/ REIT - Residential
UNF/ Unifirst Corp./ Industrials/ Specialty Business Services
UNH/ Unitedhealth Group Inc/ Healthcare/ Healthcare Plans
UNIT/ Uniti Group Inc/ Real Estate/ REIT - Specialty
UNM/ Unum Group/ Financial/ Insurance - Life
UNP/ Union Pacific Corp./ Industrials/ Railroads
UP/ Wheels Up Experience Inc/ Industrials/ Airports & Air Services
UPBD/ Upbound Group Inc/ Technology/ Software - Application
UPS/ United Parcel Service/ / 
UPST/ Upstart Holdings Inc/ Financial/ Credit Services
UPWK/ Upwork Inc/ Industrials/ Staffing & Employment Services
URBN/ Urban Outfitters/ / 
URI/ United Rentals/ / 
USAC/ USA Compression Partners LP/ Energy/ Oil & Gas Equipment & Services
USB/ U.S. Bancorp./ Financial/ Banks - Regional
USFD/ US Foods Holding Corp/ Consumer Defensive/ Food Distribution
USLM/ United States Lime & Minerals Inc./ Basic Materials/ Building Materials
USM/ United States Cellular Corporation/ Communication Services/ Telecom Services
USPH/ U.S. Physical Therapy/ / 
UTHR/ United Therapeutics Corp/ Healthcare/ Biotechnology
UTZ/ Utz Brands Inc/ Consumer Defensive/ Packaged Foods
UUUU/ Energy Fuels Inc/ Energy/ Uranium
UVV/ Universal Corp./ Consumer Defensive/ Tobacco
V/ Visa Inc/ Financial/ Credit Services
VAC/ Marriott Vacations Worldwide Corp/ Consumer Cyclical/ Resorts & Casinos
VBTX/ Veritex Holdings Inc/ Financial/ Banks - Regional
VC/ Visteon Corp./ Consumer Cyclical/ Auto Parts
VCEL/ Vericel Corp/ Healthcare/ Biotechnology
VCTR/ Victory Capital Holdings Inc/ Financial/ Asset Management
VCYT/ Veracyte Inc/ Healthcare/ Biotechnology
VECO/ Veeco Instruments Inc/ Technology/ Semiconductor Equipment & Materials
VEEV/ Veeva Systems Inc/ Healthcare/ Health Information Services
VEON/ VEON Ltd ADR/ Communication Services/ Telecom Services
VERV/ Verve Therapeutics Inc/ Healthcare/ Biotechnology
VERX/ Vertex Inc/ Technology/ Software - Application
VET/ Vermilion Energy Inc/ Energy/ Oil & Gas E&P
VFC/ VF Corp./ Consumer Cyclical/ Apparel Manufacturing
VFS/ VinFast Auto Ltd./ Consumer Cyclical/ Auto Manufacturers
VGR/ Vector Group Ltd/ Consumer Defensive/ Tobacco
VIAV/ Viavi Solutions Inc/ Technology/ Communication Equipment
VICI/ VICI Properties Inc/ Real Estate/ REIT - Diversified
VICR/ Vicor Corp./ Technology/ Electronic Components
VIR/ Vir Biotechnology Inc/ Healthcare/ Biotechnology
VIRT/ Virtu Financial Inc/ Financial/ Capital Markets
VKTX/ Viking Therapeutics Inc/ Healthcare/ Biotechnology
VLO/ Valero Energy Corp./ Energy/ Oil & Gas Refining & Marketing
VLTO/ Veralto Corp/ Industrials/ Pollution & Treatment Controls
VLY/ Valley National Bancorp/ Financial/ Banks - Regional
VMC/ Vulcan Materials Co/ Basic Materials/ Building Materials
VMI/ Valmont Industries/ / 
VNO/ Vornado Realty Trust/ Real Estate/ REIT - Office
VNOM/ Viper Energy Inc/ Energy/ Oil & Gas Midstream
VNT/ Vontier Corporation/ Technology/ Scientific & Technical Instruments
VOD/ Vodafone Group plc ADR/ Communication Services/ Telecom Services
VOYA/ Voya Financial Inc/ Financial/ Financial Conglomerates
VRDN/ Viridian Therapeutics Inc/ Healthcare/ Biotechnology
VRE/ Veris Residential Inc/ Real Estate/ REIT - Residential
VRNA/ Verona Pharma Plc ADR/ Healthcare/ Biotechnology
VRNS/ Varonis Systems Inc/ Technology/ Software - Infrastructure
VRNT/ Verint Systems/ / 
VRRM/ Verra Mobility Corp/ Industrials/ Infrastructure Operations
VRSK/ Verisk Analytics Inc/ Industrials/ Consulting Services
VRSN/ Verisign Inc./ Technology/ Software - Infrastructure
VRT/ Vertiv Holdings Co/ Industrials/ Electrical Equipment & Parts
VRTS/ Virtus Investment Partners Inc/ Financial/ Asset Management
VRTX/ Vertex Pharmaceuticals/ / 
VSAT/ Viasat/ / 
VSCO/ Victoria's Secret & Co/ Consumer Cyclical/ Apparel Retail
VSH/ Vishay Intertechnology/ / 
VST/ Vistra Corp/ Utilities/ Utilities - Independent Power Producers
VSTO/ Vista Outdoor Inc/ Consumer Cyclical/ Leisure
VSTS/ Vestis Corp/ Industrials/ Rental & Leasing Services
VTEX/ Vtex/ Technology/ Software - Application
VTLE/ Vital Energy Inc./ Energy/ Oil & Gas E&P
VTR/ Ventas Inc/ Real Estate/ REIT - Healthcare Facilities
VTRS/ Viatris Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
VVV/ Valvoline Inc/ Energy/ Oil & Gas Refining & Marketing
VVX/ V2X Inc/ Industrials/ Aerospace & Defense
VYX/ NCR Voyix Corp/ Technology/ Information Technology Services
VZ/ Verizon Communications Inc/ Communication Services/ Telecom Services
VZIO/ VIZIO Holding Corp/ Technology/ Consumer Electronics
W/ Wayfair Inc/ Consumer Cyclical/ Internet Retail
WAB/ Westinghouse Air Brake Technologies Corp/ Industrials/ Railroads
WABC/ Westamerica Bancorporation/ Financial/ Banks - Regional
WAFD/ WaFd Inc/ Financial/ Banks - Regional
WAL/ Western Alliance Bancorp/ Financial/ Banks - Regional
WALD/ Waldencast plc/ Technology/ Software - Application
WAT/ Waters Corp./ Healthcare/ Diagnostics & Research
WBA/ Walgreens Boots Alliance Inc/ Healthcare/ Pharmaceutical Retailers
WBD/ Warner Bros. Discovery Inc/ Communication Services/ Entertainment
WBS/ Webster Financial Corp./ Financial/ Banks - Regional
WCC/ Wesco International/ / 
WCN/ Waste Connections Inc/ Industrials/ Waste Management
WD/ Walker & Dunlop Inc/ Financial/ Mortgage Finance
WDAY/ Workday Inc/ Technology/ Software - Application
WDC/ Western Digital Corp./ Technology/ Computer Hardware
WDFC/ WD-40 Co./ Basic Materials/ Specialty Chemicals
WEC/ WEC Energy Group Inc/ Utilities/ Utilities - Regulated Electric
WELL/ Welltower Inc./ Real Estate/ REIT - Healthcare Facilities
WEN/ Wendy's Co/ Consumer Cyclical/ Restaurants
WERN/ Werner Enterprises/ / 
WES/ Western Midstream Partners LP/ Energy/ Oil & Gas Midstream
WEX/ WEX Inc/ Technology/ Software - Infrastructure
WFC/ Wells Fargo & Co./ Financial/ Banks - Diversified
WFG/ West Fraser Timber Co./ / 
WFRD/ Weatherford International plc/ Energy/ Oil & Gas Equipment & Services
WGO/ Winnebago Industries/ / 
WH/ Wyndham Hotels & Resorts Inc/ Consumer Cyclical/ Lodging
WHD/ Cactus Inc/ Energy/ Oil & Gas Equipment & Services
WHR/ Whirlpool Corp./ Consumer Cyclical/ Furnishings
WINA/ Winmark Corporation/ Consumer Cyclical/ Specialty Retail
WING/ Wingstop Inc/ Consumer Cyclical/ Restaurants
WIRE/ Encore Wire Corp./ Industrials/ Electrical Equipment & Parts
WK/ Workiva Inc/ Technology/ Software - Application
WKC/ World Kinect Corp/ Energy/ Oil & Gas Refining & Marketing
WLK/ Westlake Corporation/ Basic Materials/ Specialty Chemicals
WLY/ John Wiley & Sons Inc./ Communication Services/ Publishing
WM/ Waste Management/ / 
WMB/ Williams Cos Inc/ Energy/ Oil & Gas Midstream
WMG/ Warner Music Group Corp/ Communication Services/ Entertainment
WMK/ Weis Markets/ / 
WMS/ Advanced Drainage Systems Inc/ Industrials/ Building Products & Equipment
WMT/ Walmart Inc/ Consumer Defensive/ Discount Stores
WNC/ Wabash National Corp./ Industrials/ Farm & Heavy Construction Machinery
WOLF/ Wolfspeed Inc/ Technology/ Semiconductors
WOR/ Worthington Enterprises Inc./ Industrials/ Metal Fabrication
WPC/ W. P. Carey Inc/ Real Estate/ REIT - Diversified
WPM/ Wheaton Precious Metals Corp/ Basic Materials/ Gold
WPP/ WPP Plc. ADR/ Communication Services/ Advertising Agencies
WRB/ W.R. Berkley Corp./ Financial/ Insurance - Property & Casualty
WRBY/ Warby Parker Inc/ Healthcare/ Medical Instruments & Supplies
WRK/ WestRock Co/ Consumer Cyclical/ Packaging & Containers
WSBC/ Wesbanco/ / 
WSC/ WillScot Mobile Mini Holdings Corp/ Industrials/ Rental & Leasing Services
WSFS/ WSFS Financial Corp./ Financial/ Banks - Regional
WSM/ Williams-Sonoma/ / 
WSO/ Watsco Inc./ Industrials/ Industrial Distribution
WST/ West Pharmaceutical Services/ / 
WT/ WisdomTree/ / 
WTFC/ Wintrust Financial Corp./ Financial/ Banks - Regional
WTM/ White Mountains Insurance Group/ / 
WTRG/ Essential Utilities Inc/ Utilities/ Utilities - Regulated Water
WTS/ Watts Water Technologies/ / 
WTW/ Willis Towers Watson Public Limited Co/ Financial/ Insurance Brokers
WU/ Western Union Company/ Financial/ Credit Services
WWD/ Woodward Inc/ Industrials/ Aerospace & Defense
WY/ Weyerhaeuser Co./ Real Estate/ REIT - Specialty
WYNN/ Wynn Resorts Ltd./ Consumer Cyclical/ Resorts & Casinos
X/ United States Steel Corp./ Basic Materials/ Steel
XEL/ Xcel Energy/ / 
XENE/ Xenon Pharmaceuticals Inc/ Healthcare/ Biotechnology
XHR/ Xenia Hotels & Resorts Inc/ Real Estate/ REIT - Hotel & Motel
XMTR/ Xometry Inc/ Industrials/ Specialty Industrial Machinery
XNCR/ Xencor Inc/ Healthcare/ Biotechnology
XOM/ Exxon Mobil Corp./ Energy/ Oil & Gas Integrated
XPEL/ XPEL Inc/ Consumer Cyclical/ Auto Parts
XPO/ XPO Inc/ Industrials/ Trucking
XPRO/ Expro Group Holdings N.V./ Energy/ Oil & Gas Equipment & Services
XRAY/ DENTSPLY Sirona Inc/ Healthcare/ Medical Instruments & Supplies
XRX/ Xerox Holdings Corp/ Technology/ Information Technology Services
XYL/ Xylem Inc/ Industrials/ Specialty Industrial Machinery
YELP/ Yelp Inc/ Communication Services/ Internet Content & Information
YETI/ YETI Holdings Inc/ Consumer Cyclical/ Leisure
YOU/ Clear Secure Inc/ Technology/ Software - Application
YUM/ Yum Brands Inc./ Consumer Cyclical/ Restaurants
Z/ Zillow Group Inc/ Communication Services/ Internet Content & Information
ZBH/ Zimmer Biomet Holdings Inc/ Healthcare/ Medical Devices
ZBRA/ Zebra Technologies Corp./ Technology/ Communication Equipment
ZD/ Ziff Davis Inc/ Communication Services/ Advertising Agencies
ZETA/ Zeta Global Holdings Corp/ Technology/ Software - Application
ZG/ Zillow Group Inc/ Communication Services/ Internet Content & Information
ZGN/ Ermenegildo Zegna N.V./ Consumer Cyclical/ Apparel Manufacturing
ZI/ ZoomInfo Technologies Inc./ Technology/ Software - Application
ZION/ Zions Bancorporation N.A/ Financial/ Banks - Regional
ZIP/ ZipRecruiter Inc/ Industrials/ Staffing & Employment Services
ZM/ Zoom Video Communications Inc/ Technology/ Software - Application
ZNTL/ Zentalis Pharmaceuticals Inc/ Healthcare/ Biotechnology
ZS/ Zscaler Inc/ Technology/ Software - Infrastructure
ZTS/ Zoetis Inc/ Healthcare/ Drug Manufacturers - Specialty & Generic
ZUO/ Zuora Inc/ Technology/ Software - Infrastructure
ZWS/ Zurn Elkay Water Solutions Corp/ Industrials/ Pollution & Treatment Controls
"""

    # Split the data into lines and then into individual records
    records = data.strip().split("\n")

    # Create an empty dictionary to store stocks
    stocks_dict = {}

    # Iterate through the records
    for record in records:
        # Split the record into ticker, name, industry, and sub-industry
        ticker, name, industry, sub_industry = record.split("/ ")
        # Create a dictionary for the current stock
        stock_info = {
            "ticker": ticker.strip(),
            "name": name.strip(),
            "industry": industry.strip(),
            "sub_industry": sub_industry.strip()
        }
        # Add the stock to the stocks dictionary with the ticker as the key
        stocks_dict[ticker.strip()] = stock_info

    # Print the dictionary of stocks
    for ticker, stock_info in stocks_dict.items():
        print(ticker, ":", stock_info)

    return stocks_dict