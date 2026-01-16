[out:json][timeout:240];
// fetch area “göteborg” to search in
{{geocodeArea:göteborg}}->.searchArea;
// schools in area
nwr(area.searchArea)["amenity"="school"]->.schools;
// Find traffic signs with Swedish codes and inscriptions referencing time or "Skola"
(
  node(area.searchArea)["traffic_sign"~"SE:C31|SE:A13"];     // speed limit or children warning
)->.signs; 
// print results
out geom;
