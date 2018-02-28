var dataDir = "./backend/data/";
// URLS:
var countryEmigration = dataDir + "emigration_country_result.json";
var countryImmigration = dataDir + "immigration_country_result.json";
var regionEmigration = dataDir + "emigration_region_result.json";
var regionImmigration = dataDir + "immigration_region_result.json";

/*
 * function to get the files from each of those directories
 * url - one of the urls above
 * callback - function to accept the data. example below
 */
var getData = function (url, callback) {
    console.log(url);
    $.ajax({
        dataType: "json",
        url: url,
        success: callback,
        error: function(err) {
            console.log(err);
        }
    });
};

/*
 * Example usage:
 * getData(countryEmigration, function(data){
 *  // use the function to display the data
 * });
 *
 */