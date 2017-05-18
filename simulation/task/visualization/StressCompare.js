var StressCompare = function(canvas_width, canvas_height) {
    // Create the tag:
    var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
    canvas_tag += "style='border:1px dotted'></canvas>";
    // Append it to body:
    var canvas = $(canvas_tag)[0];
    $("body").append(canvas);
    // Create the context and the drawing controller:
    var context = canvas.getContext("2d");

    // Prep the chart properties and series:

    // Add a zero value for each bin
    //for (var i in bins)
    //    datasets[0].data.push(0);

    var data = {
      labels: [],
      datasets: [
    		{
    			label: "My First dataset",
    			fillColor: "rgba(220,220,220,0.2)",
    			strokeColor: "rgba(220,220,220,1)",
    			pointColor: "rgba(220,220,220,1)",
    			pointStrokeColor: "#fff",
    			pointHighlightFill: "#fff",
    			pointHighlightStroke: "rgba(220,220,220,1)",
    			data: []
    		},
        {
    			label: "My Second dataset",
    			fillColor: "rgba(80,220,220,0.2)",
    			strokeColor: "rgba(80,220,220,1)",
    			pointColor: "rgba(80,220,220,1)",
    			pointStrokeColor: "#fff",
    			pointHighlightFill: "#fff",
    			pointHighlightStroke: "rgba(80,220,220,1)",
    			data: []
    		}
    	]
    }

    var options = {
        spanGaps: true
    };

    // Create the chart object
    var lineChart = new Chart(context).Line(data, options);

    // ...Everything from above...
    this.render = function(data) {
        //for (var i in data)
        //    chart.datasets[0].bars[i].value = data[i];
        if(data == -1) return;
        lineChart.addData([data[0]], data[1]);
        //lineChart.data.labels = "Hola";
        //lineChart.config.data.labels.push("A label2");
        //lineChart.config.data.datasets[0].data.push(data);
        //lineChart.datasets[0].labels.push("hola");
        //lineChart.datasets[0].data = data;
        lineChart.update();
    };

    this.reset = function() {
        lineChart.destroy();
        // Create the chart object
        var lineChart = new Chart(ctx, {
            type: 'line',
            data: data,
            options: options
        });
    };
};
