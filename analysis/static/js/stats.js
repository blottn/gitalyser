repos = repos.reverse();

var node = [];
var com_list = [];

var width = 750;
var height = 500;

var time_week = 604800; //time in a week

for (i = 0 ; i < repos.length ; i++) {
	node[i] = {'time':Date.parse(repos[i].created_at),'count':i+1};
}

for (i = 0 ; i < commits.length ; i++) {
	com_list[i] = {'time':commits[i],'count':i+1};
}


var delta = node[node.length - 1].time - node[0].time;
var offset = node[0].time;

for (i = 0 ; i < node.length ; i++) {
    node[i].time = node[i].time - offset;
    node[i].time = node[i].time / delta;
    node[i].time = node[i].time * width;
}

var com_delta = com_list[com_list.length - 1].time - com_list[0].time;
var com_offset = com_list[0].time;

for (i = 0 ; i < com_list.length ; i++) {
	com_list[i].time = com_list[i].time - com_offset;
	com_list[i].time = com_list[i].time / com_delta;
	com_list[i].time = com_list[i].time * width;
}

graph("#repos", width, height, node, function(d) {return d.time;},function(d) {
    return (height - (height * (d.count / node[node.length-1].count) / 2));
});

graph("#commits", width, height, com_list, function(d) {return d.time;}, function(d) {
    return (height - (height * (d.count / com_list[com_list.length-1].count) / 2));
});

function graph(id, w, h,  data, fx, fy) {

    var svg = d3.select(id)
            .append("svg");

    var timeline = d3.line(node)
	    .x(fx)
	    .y(fy);

    svg.attr("width",w)
        .attr("height",h);
   
    var graph = svg.append("path")
	    .attr("d", timeline(data))
	    .attr("stroke","green")
	    .attr("stroke-width",2)
	    .attr("fill","none");

}
