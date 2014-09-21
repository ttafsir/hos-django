function initmap() {

	
	//jquery gets used!, so you need it!
    var loc = $("#location");
    var facilities = $("#facilities");
	
	//need somehow for user to input location and distance to query
	
    var getLocation = function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(handlePosition);
            } else {
                loc.html("GeoLocation not supported");
            } 
        }
        
    
    var handlePosition = function(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        console.log('lat : ' + lat);
        console.log('lon : ' + lon);
        $.get(url, {"lat": lat,
                    "lon": lon },
                    function(data) {
                        facilities.empty();
                        $.each(data.features, function(index, val) {
                            var name = val.properties.name;
                            var description = val.properties.description;
                            facilities.append(name);
                            facilities.append(description);
                            makeMap(val, lon, lat);
                        });
                    }); 
        }

	
    var featurePopup = function(feature, layer) {
            var popupContent = feature.properties.name;

            if (feature.properties && feature.properties.popupContent) {
                popupContent += feature.properties.popupContent;
            }

            layer.bindPopup(popupContent);
        }



    var makeMap = function(feature, lon, lat) {
        var map = L.map('map').setView([lat, lon], 13);
        
        //Location selected to query
        var unit = L.geoJson(feature, {
            onEachFeature: featurePopup
        }).addTo(map);
        
        //need something else to add all locations to the map, along with making them have pop-ups with attribute info!

        //OSM layer
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Marker
        L.marker([lat, lon]).addTo(map)
            .bindPopup(feature.properties.name)
            .openPopup();
    }

    getLocation();
    
  	//var map = L.map('map').setView([51.505, -0.09], 13);
  	
    
}

initmap();