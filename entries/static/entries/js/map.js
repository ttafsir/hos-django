function initmap() {

	
	//jquery gets used!, so you need it!
    var loc = $("#location");
    var facilities = $("#facilities");
	
	//need somehow for user to input location and distance to query
	 /* 
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
*/
	var loadFacilities = function(position) {
        //var lat = position.coords.latitude;
        //var lon = position.coords.longitude;
        //console.log('lat : ' + lat);
        //console.log('lon : ' + lon);
        $.get(url_all,
                    function(data) {
                        facilities.empty();
                        
                        console.log('hi');
                        
                        console.log(data.features);
                        
                        var justData = data.features;
                        
                        console.log(justData.length);
                        
                        var markerArray = new Array(justData.length);
                        
                        
                        //$.each(justData.length, function(index, val) {
                        for (var i = 0; i < justData.length; i++){
                        	//var record = data[i];
                        	
                        	/*
                            var name = val.properties.provider_name;
                            var description = val.properties.provider_name;
                            var lat = val.properties.latitude;
        					var lon = val.properties.longitude;
        					
                            facilities.append(name);
                            facilities.append(description);
                            facilities.append(lat);
                            facilities.append(lon);
                            */
                            
                            var record = justData[i];
                            
                            var lat = record.properties.latitude;
        					var lon = record.properties.longitude;
        					
        					
                            
                            
                            /*
                            for (var i = 0; i < justData.length; i++){
								var record = justData[i];
								//popupBindTxt = record.FEATURE_CLASS + " = " + record.FEATURE_NAME;
								markerArray[i] = L.marker([record.properties.latitude, record.properties.longitude]);
								//console.log(record)

							}
							*/
                            
                            if (lat) {
                            	if (lon) {
                            		markerArray[i] = L.marker([lat,lon]).addTo(map);
                            		console.log(lon);
                            		console.log(markerArray[i]);
                            	}
                            }
                        
                        }
                        makeMap(markerArray);
                    }); 
        }
        
    var featurePopup = function(feature, layer) {
            var popupContent = feature.properties.name;

            if (feature.properties && feature.properties.popupContent) {
                popupContent += feature.properties.popupContent;
            }

            layer.bindPopup(popupContent);
        }



    var makeMap = function(markerArray) {
        //var map = L.map('map').setView([lat, lon], 13);
        
        //Location selected to query
        /*
        var unit = L.geoJson(feature, {
            onEachFeature: featurePopup
        }).addTo(map);
        */
        console.log('now to make map!');
        //need something else to add all locations to the map, along with making them have pop-ups with attribute info!
		markerLayerGroup = L.layerGroup(markerArray).addTo(map);
		
		console.log(markerArray[2]);
		
        //OSM layer
        /*
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
		*/
		
        // Marker
        /*
        L.marker([lat, lon]).addTo(map)
            .bindPopup(feature.properties.name)
            .openPopup();
        */
    }

    //getLocation();
    

    //Add a layer group to hold the pins
    //var markerLayerGroup = L.layerGroup().addTo(map);

    //initialize the map with OSM tiles
    var map = L.map('map').setView([18.57, -72.292], 9);

	//Add a layer group to hold the pins
    var markerLayerGroup = L.layerGroup().addTo(map);

	L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);
    
    loadFacilities();
    
  	//var map = L.map('map').setView([51.505, -0.09], 13);
  	
    
}

initmap();