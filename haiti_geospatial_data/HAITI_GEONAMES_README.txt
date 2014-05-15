HAITI PLACENAMES

>>>>>13 Jan 2010


SOURCE:  GEONAMES.org


URL:  http://download.geonames.org/export/dump/



Following fields were preserved:

geoid = geonameid        : integer id of record in geonames database
asciinm  =  asciiname    : name of geographical point in plain ascii characters, varchar(200)
altnm =  alternatenames  : alternatenames, comma separated varchar(5000)
lat =  latitude          : latitude in decimal degrees (wgs84)
long =  longitude        : longitude in decimal degrees (wgs84)
class =  feature class   : see http://www.geonames.org/export/codes.html, char(1)
code = feature code      : see http://www.geonames.org/export/codes.html, varchar(10)





Following fields were stripped from data:


country code      : ISO-3166 2-letter country code, 2 characters
cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 60 characters
admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80) 
admin3 code       : code for third level administrative division, varchar(20)
admin4 code       : code for fourth level administrative division, varchar(20)
population        : bigint (4 byte int) 
elevation         : in meters, integer
gtopo30           : average elevation of 30'x30' (ca 900mx900m) area in meters, integer
timezone          : the timezone id (see file timeZone.txt)
modification date : date of last modification in yyyy-MM-dd format
