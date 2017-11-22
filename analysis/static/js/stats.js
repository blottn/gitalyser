repos = repos.reverse();

var node = [];
var width = 750;
var height = 500;

for (i = 0 ; i < repos.length ; i++) {
	node[i] = {'time':Date.parse(repos[i].created_at),'count':i+1};
}

var delta = node[node.length - 1].time - node[0].time;
var offset = node[0].time;

for (i = 0 ; i < node.length ; i++) {
    node[i].time = node[i].time - offset;
    node[i].time = node[i].time / delta;
    node[i].time = node[i].time * width;
}

console.log("delta: " + delta);
for (i = 0 ; i < node.length ; i++) {
    console.log(node[i].time);
}


var svg = d3.select("#repos")
            .append("svg");

svg.attr("width",width)
   .attr("height",height);

var timeline = d3.line(node)
	.x(function(d) {return d.time;})
	.y(function(d) {return height - d.count;});


var graph = svg.append("path")
    //.interpolate("step-before")
	.attr("d", timeline(node))
	.attr("stroke","blue")
	.attr("stroke-width",2)
	.attr("fill","none");


function graph(id, data, fx, fy) {

}
