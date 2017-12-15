var width = 960;
var height = 960;

data = {}
data.name = "Leaches"
data.children = contribs;


var root = d3.hierarchy(data);

root.sum(function(d) {return d.value;});
var pack = d3.pack().size([width,height]).padding([3]);
pack(root);

var svg = d3.select("#graph")
			.append("svg")
			.attr("width",width)
			.attr("height",height)
			.attr("class","bubble");

var node = svg.selectAll(".node")
			.data(root.children)
			.enter()
			.append("g")
			.attr("transform", function(d) {return "translate("+ d.x + ", " + d.y + ")";});

node.append("circle")
	.attr("r",function(d) {return d.r})
	.style("fill","#FF5555");

node.append("text")
	.attr("dy",".3em")
	.style("text-anchor", "middle")
	.text(function(d) { return d.data.name;});
