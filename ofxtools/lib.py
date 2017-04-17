# coding: utf-8

OFXv1 = ('102', '103')
OFXv2 = ('200', '203', '211')

APPIDS = ('QWIN', # Quicken for Windows
            'QMOFX', # Quicken for Mac
            'QBW', # QuickBooks for Windows
            'QBM', # QuickBooks for Mac
            'Money', # MSFT Money
            'Money Plus', # MSFT Money Plus
            'PyOFX', # Custom
)

APPVERS = ('1500', # Quicken 2006/ Money 2006
            '1600', # Quicken 2007/ Money 2007/ QuickBooks 2006
            '1700', # Quicken 2008/ Money Plus/ QuickBooks 2007
            '1800', # Quicken 2009/ QuickBooks 2008
            '1900', # Quicken 2010/ QuickBooks 2009
            '2000', # QuickBooks 2010
            '9999', # Custom
)


# 2-letter country codes for numbering agencies (used to construct ISINs)
# Swiped from
# http://code.activestate.com/recipes/498277-isin-validator/
NUMBERING_AGENCIES = \
        {'BE': ('Euronext - Brussels', 'Belgium'),
         'FR': ('Euroclear France', 'France'),
         'BG': ('Central Depository of Bulgaria', 'Bulgaria'),
         'VE': ('Bolsa de Valores de Caracas, C.A.', 'Venezuela'),
         'DK': ('VP Securities Services', 'Denmark'),
         'HR': ('SDA - Central Depository Agency of Croatia', 'Croatia'),
         'DE': ('Wertpapier-Mitteilungen', 'Germany'),
         'JP': ('Tokyo Stock Exchange', 'Japan'),
         'H': ('KELER', 'Hungary'),
         'HK': ('Hong Kong Exchanges and Clearing Ltd', 'Hong Kong'),
         'JO': ('Securities Depository Center of Jordan', 'Jordan'),
         'BR': ('Bolsa de Valores de Sao Paulo - BOVESPA', 'Brazil'),
         'XS': ('Clearstream Banking', 'Clearstream'),
         'FI': ('Finnish Central Securities Depository Ltd', 'Finland'),
         'GR': ('Central Securities Depository S.A.', 'Greece'),
         'IS': ('Icelandic Securities Depository', 'Iceland'),
         'R': ('The National Depository Center, Russia', 'Russia'),
         'LB': ('Midclear S.A.L.', 'Lebanon'),
         'PT': ('Interbolsa - Sociedade Gestora de Sistemas de Liquidação e Sistemas Centralizados de Valores', 'Portugal'),
         'NO': ('Verdipapirsentralen (VPS) ASA', 'Norway'),
         'TW': ('Taiwan Stock Exchange Corporation', 'Taiwan, Province of China'),
         'UA': ('National Depository of Ukraine', 'Ukraine'),
         'TR': ('Takasbank', 'Turkey'),
         'LK': ('Colombo Stock Exchange', 'Sri Lanka'),
         'LV': ('OMX - Latvian Central Depository', 'Latvia'),
         'L': ('Clearstream Banking', 'Luxembourg'),
         'TH': ('Thailand Securities Depository Co., Ltd', 'Thailand'),
         'NL': ('Euronext Netherlands', 'Netherlands'),
         'PK': ('Central Depository Company of Pakistan Ltd', 'Pakistan'),
         'PH': ('Philippine Stock Exchange, Inc.', 'Philippines'),
         'RO': ('The National Securities Clearing Settlement and Depository Corporation', 'Romania'),
         'EG': ('Misr for Central Clearing, Depository and Registry (MCDR)', 'Egypt'),
         'PL': ('National Depository for Securities', 'Poland'),
         'AA': ('ANNA Secretariat', 'ANNAland'),
         'CH': ('Telekurs Financial Ltd.', 'Switzerland'),
         'CN': ('China Securities Regulatory Commission', 'China'),
         'CL': ('Deposito Central de Valores', 'Chile'),
         'EE': ('Estonian Central Depository for Securities', 'Estonia'),
         'CA': ('The Canadian Depository for Securities Ltd', 'Canada'),
         'IR': ('Tehran Stock Exchange Services Company', 'Iran'),
         'IT': ('Ufficio Italiano dei Cambi', 'Italy'),
         'ZA': ('JSE Securities Exchange of South Africa', 'South Africa'),
         'CZ': ('Czech National Bank', 'Czech Republic'),
         'CY': ('Cyprus Stock Exchange', 'Cyprus'),
         'AR': ('Caja de Valores S.A.', 'Argentina'),
         'A': ('Australian Stock Exchange Limited', 'Australia'),
         'AT': ('Oesterreichische Kontrollbank AG', 'Austria'),
         'IN': ('Securities and Exchange Board of India', 'India'),
         'CS': ('Central Securities Depository A.D. Beograd', 'Serbia & Montenegro'),
         'CR': ('Central de Valores - CEVAL', 'Costa Rica'),
         'IE': ('The Irish Stock Exchange', 'Ireland'),
         'ID': ('PT. Kustodian Sentral Efek Indonesia (Indonesian Central Securities Depository (ICSD))', 'Indonesia'),
         'ES': ('Comision Nacional del Mercado de Valores (CNMV)', 'Spain'),
         'PE': ('Bolsa de Valores de Lima', 'Per'),
         'TN': ('Sticodevam', 'Tunisia'),
         'PA': ('Bolsa de Valores de Panama S.A.', 'Panama'),
         'SG': ('Singapore Exchange Limited', 'Singapore'),
         'IL': ('The Tel Aviv Stock Exchange', 'Israel'),
         'US': ("Standard & Poor's - CUSIP Service Bureau", 'USA'),
         'MX': ('S.D. Indeval SA de CV', 'Mexico'),
         'SK': ('Central Securities Depository SR, Inc.', 'Slovakia'),
         'KR': ('Korea Exchange - KRX', 'Korea'),
         'SI': ('KDD Central Securities Clearing Corporation', 'Slovenia'),
         'KW': ('Kuwait Clearing Company', 'Kuwait'),
         'MY': ('Bursa Malaysia', 'Malaysia'),
         'MO': ('MAROCLEAR S.A.', 'Morocco'),
         'SE': ('VPC AB', 'Sweden'),
         'GB': ('London Stock Exchange', 'United Kingdom'),
         }
