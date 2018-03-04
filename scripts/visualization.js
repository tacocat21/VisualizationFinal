    google.load('visualization', '1', {
        'packages': ['geochart', 'table']
    });
    google.setOnLoadCallback(drawRegionsMap);
    var currentRegion;

    function drawRegionsMap() {
        var data = google.visualization.arrayToDataTable([

        ['Country', 'Net Immigration To: (thousands)'],
            ['Germany', 720],
            ['United States', 340],
            ['Brazil', 43],
            ['Canada', 571],
            ['France', 967],
            ['Russia', 054],
            ['Finland', 58],
            ['Kyrgyzstan', 7],
            ['Iran', 534],
            ['South Africa', 75],
            ['Australia', 734],
            ['Sudan', 534],
            ['Burma', 754],
            ['South Korea', 534],
            ['Chile', 574]

        ]);

        var view = new google.visualization.DataView(data)
        view.setColumns([0, 1])



        var chart = new google.visualization.GeoChart(
        document.getElementById('chart_div'));
        chart.draw(data, options);

        var geochart = new google.visualization.GeoChart(
        document.getElementById('chart_div'));
        var options = {
            width: 1440,
            height: 480,
            colorAxis: {
                colors: ['#acb2b9', '#2f3f4f']
            } // Map Colors
        };

        google.visualization.events.addListener(geochart, 'regionClick', function (eventData) {
            // maybe you want to change the data table here...
            currentRegion = eventData.region;
            options['region'] = eventData.region;
            options['resolution'] = 'provinces';

            // Add Results for Individual State
            // Format needs to match what is below so that it locates the correct position
            // Additional information can be added to array
            // Uses first value in 2nd column to determine scale for markers
            if (currentRegion == 'US') {
                //If it is a US State
                var data = google.visualization.arrayToDataTable([
                    ['State', 'Net Immigration To'],
                    ['California', 750],
                    ['North Carolina', 387],
                    ['Illinois', 446],
                    ['Texas',475 ]])


            } else if (currentRegion.substring(0, 3) == "US-") {
                // If it is a US city
                options['displayMode'] = 'markers';
                var data = google.visualization.arrayToDataTable([
                // Add Results for Individual State
                // Format needs to match what is below so that it locates the correct position
                // Additional information can be added to array
                // Uses first value in 2nd column to determine scale for markers
                ['State', 'Migrants to (Thousands)', ],
                    ['Illinois', 300],
                    ['New York', 400],
                    ['California', 400],
                    ['Maryland', 400],
                    ['Texas', 100],
                    ['Washington', 300], ]);

            } else {
                //If it is a foreign city
                options['displayMode'] = 'markers';
                var data = google.visualization.arrayToDataTable([
                    ['Destination', 'Migrants'],
                    ['United States', 423],
                    ['Canada', 434],
                    ['Germany', 276],
                    ['France', 500],
                    ['Iraq', 500],
                    ['Libya', 300], ]);
            }
            geochart.draw(data, options);
            var table = new google.visualization.Table(document.getElementById('table'));
            table.draw(data, null);
        });
        geochart.draw(data, options);


    }
